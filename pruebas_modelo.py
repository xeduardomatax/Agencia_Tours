"""Pruebas de aceptación (14) — Agencia de tours.

El docente ejecutará SU copia original de este archivo contra tu entrega:
    pytest -q pruebas_modelo.py
No lo modifiques.
"""

import hashlib
import pickle
import sqlite3
import time
from collections.abc import Iterator
from datetime import date, timedelta
from pathlib import Path

import pytest

from agencia_tours.eventos.oyentes import OyenteMemoria
from agencia_tours.funcional.reglas import Regla, aplicar, de_tipo, filtrar, precio_maximo
from agencia_tours.modelo.actor import Basico, Nivel, Oro, Plata, Viajero
from agencia_tours.modelo.catalogo import Folleto
from agencia_tours.modelo.clave import Clave
from agencia_tours.modelo.contrato import Tarifable
from agencia_tours.modelo.elemento import Aventura, ConGuia, ConTransporte, Cultural, Gastronomico, Tour
from agencia_tours.modelo.transaccion import Reserva
from agencia_tours.persistencia.conexion import abrir
from agencia_tours.persistencia.repositorios import (
    RepositorioReserva,
    RepositorioTour,
    RepositorioViajero,
)
from agencia_tours.servicio.servicio import ServicioTours

HOY = date(2026, 1, 15)


def _sello(*valores: float) -> str:
    """Oráculo sellado: huella SHA-256 de valores redondeados a 4 decimales.

    Las pruebas comparan huellas, no números: debes deducir las reglas de la
    especificación (§6 del DOCX) y comprobar tus hipótesis ejecutando pytest.
    """
    texto = ";".join(f"{v:.4f}" for v in valores)
    return hashlib.sha256(f"agencia_tours|{texto}".encode()).hexdigest()[:20]


@pytest.fixture(autouse=True)
def _claves_limpias() -> Iterator[None]:
    Clave.reiniciar()
    yield


def _trio() -> tuple[Cultural, Aventura, Gastronomico]:
    return (
        Cultural("Uno", 100.0, 4),
        Aventura("Dos", 200.0, 3),
        Gastronomico("Tres", 300.0, 6),
    )


def _actor(nivel: Nivel | None = None) -> Viajero:
    return Viajero("Ada Lovelace", "ada@ejemplo.mx", nivel)


def test_01_clave_formato_y_secuencia() -> None:
    assert Clave.es_valida("ABC-0001") and not Clave.es_valida("AB-0001")
    assert Clave.siguiente("XYZ") == "XYZ-0001"
    assert Clave.siguiente("XYZ") == "XYZ-0002"
    Clave.registrar("XYZ-0040")
    assert Clave.siguiente("XYZ") == "XYZ-0041"
    with pytest.raises(ValueError):
        Clave.siguiente("xy")


def test_02_contrato_abstracto_y_plantilla() -> None:
    with pytest.raises(TypeError):
        Tour("x", 1.0)  # type: ignore[abstract]
    e = Cultural("Uno", 100.0, 4)
    assert isinstance(e, Tarifable) and Tarifable.moneda() == "MXN"
    with pytest.raises(ValueError):
        e.cotizar(0)
    assert e.cotizar_con_iva(1) == round(e.cotizar(1) * 1.16, 2)


def test_03_encapsulacion_y_validacion() -> None:
    e = Cultural("  Uno  ", 100.0, 4)
    assert e.nombre == "Uno" and e.clave == "CUL-0001"
    with pytest.raises(ValueError):
        e.nombre = "   "
    with pytest.raises(ValueError):
        e.precio_base = 0
    with pytest.raises(ValueError):
        e.sitios = 10 + 1
    with pytest.raises(AttributeError):
        e.clave = "CUL-0009"  # type: ignore[misc]
    with pytest.raises(ValueError):
        Cultural("Otro", 10.0, 4, clave="AVE-0001")


def test_04_tarifas_polimorficas() -> None:
    a, b, c = _trio()
    assert _sello(a.cotizar(2)) == "96a009ce08d500b02314"
    assert _sello(b.cotizar(2)) == "0b0dde7f9658eaf0a859"
    assert _sello(c.cotizar(2)) == "ea0c615fe21064992f90"
    assert [x.tipo for x in (a, b, c)] == ["CUL", "AVE", "GAS"]


def test_05_herencia_multiple_y_colision() -> None:
    c = Gastronomico("Tres", 300.0, 6)
    mro = Gastronomico.__mro__
    assert mro.index(ConTransporte) < mro.index(ConGuia) < mro.index(Tour)
    assert _sello(round(c.recargo(), 4)) == "7aaf249b654001fd861d"
    assert c.etiquetas() == ["con_transporte", "con_guia"]
    assert Cultural("Uno", 1.0, 4).etiquetas() == ["con_transporte"]


def test_06_niveles_singleton() -> None:
    assert Basico() is Basico() and Oro() is Nivel.desde_nombre("oro")
    a = Viajero.desde_texto("Grace Hopper;grace@ejemplo.mx;PLATA")
    assert a.nivel is Plata() and a.clave == "VIA-0001"
    assert _sello(*(n.descuento() for n in (Basico(), Plata(), Oro()))) == "dffc22f94fa0d0b042ae"
    assert _sello(a.descuento()) == "1ddfad7e7f4a3fb22fdc"
    with pytest.raises(ValueError):
        _actor().correo = "sin-arroba"
    with pytest.raises(ValueError):
        Nivel.desde_nombre("DIAMANTE")


def test_07_estados_y_transiciones() -> None:
    t = Reserva(_actor(), HOY)
    assert t.estado == Reserva.ABIERTA
    with pytest.raises(ValueError):
        t.cambiar_estado(Reserva.EN_CURSO)
    t.agregar(_trio()[0], 1)
    t.cambiar_estado(Reserva.EN_CURSO)
    with pytest.raises(ValueError):
        t.agregar(_trio()[1], 1)
    t.cambiar_estado(Reserva.CERRADA)
    with pytest.raises(ValueError):
        t.cambiar_estado(Reserva.ABIERTA)


def test_08_totales_con_descuento() -> None:
    a, b, c = _trio()
    t = Reserva(_actor(Oro()), HOY)
    t.agregar(a, 1)
    t.agregar(b, 2)
    t.agregar(c, 3)
    esperado = round(a.cotizar(1) + b.cotizar(2) + c.cotizar(3), 2)
    assert t.subtotal() == esperado
    assert _sello(round(t.descuento() / esperado, 2)) == "cad8654b57f8d51eabb7"
    assert t.total() == round(t.subtotal() - t.descuento(), 2)


def test_09_catalogo_agregacion() -> None:
    a, b, c = _trio()
    cat = Folleto(a, b)
    assert cat.agregar(c) == 1 and len(cat) == 3
    with pytest.raises(ValueError):
        cat.agregar(a)
    assert cat.buscar(tipo="AVE") == [b]
    assert cat.buscar(precio_max=250, texto="o") == [a, b]
    assert [e.nombre for e in cat.ordenados("precio", descendente=True)] == ["Tres", "Dos", "Uno"]
    assert cat.resumen_por_tipo() == {"CUL": 1, "AVE": 1, "GAS": 1}
    with pytest.raises(KeyError):
        cat.obtener("ZZZ-0001")


def test_10_tipos_anidados_y_copia() -> None:
    a, _, _ = _trio()
    t = Reserva(_actor(), HOY)
    linea = t.agregar(a, 2)
    assert isinstance(linea, Reserva.Linea) and linea.contenedora is t
    assert t.lineas == (linea,) and isinstance(t.lineas, tuple)
    copia = a.copiar()
    assert type(copia) is Cultural and copia.clave != a.clave and copia.nombre == a.nombre
    assert type(Tour.crear("GAS", "x", 1.0, 6)) is Gastronomico


def test_11_reglas_funcionales() -> None:
    a, b, c = _trio()
    barata = precio_maximo(250)
    regla = barata.y(de_tipo("CUL").negar()).o(de_tipo("GAS"))
    assert isinstance(regla, Regla) and callable(regla)
    assert filtrar([a, b, c], regla) == [b, c]
    assert filtrar([a, b, c], lambda e: e.precio_base > 150) == [b, c]
    assert aplicar([a, b], lambda e: e.precio_base * 2) == [200.0, 400.0]


def test_12_monitor_y_concurrencia() -> None:
    dia = [HOY]
    eventos = OyenteMemoria()
    with ServicioTours(reloj=lambda: dia[0]) as s:
        s.suscribir(eventos)
        a, b, _ = _trio()
        s.registrar_tour(a)
        s.registrar_viajero(_actor())
        vacia = s.abrir("VIA-0001")
        larga = s.abrir("VIA-0001")
        s.agregar_linea(larga.clave, a.clave, 1)
        s.cambiar_estado(larga.clave, Reserva.EN_CURSO)
        dia[0] = HOY + timedelta(days=ServicioTours.PLAZO + 1)
        assert s.revisar() == (1, 1)
        assert s.revisar() == (0, 0)
        assert [t.estado for t in s.reservas()] == [Reserva.CANCELADA, Reserva.EN_CURSO]
        assert ("CANCELACION", vacia.clave) in eventos.eventos
        assert sum(1 for e, _ in eventos.eventos if e == "ALERTA") == 1
        s.iniciar_monitor(periodo=0.02)
        monitor = s.monitor
        assert isinstance(monitor, ServicioTours.Monitor)
        limite = time.monotonic() + 3
        while monitor.ejecuciones < 2 and time.monotonic() < limite:
            time.sleep(0.01)
        s.detener_monitor()
        assert monitor.ejecuciones >= 2 and not monitor.is_alive()


def test_13_persistencia_sqlite_y_pickle(tmp_path: Path) -> None:
    con = abrir(str(tmp_path / "prueba.db"))
    assert con.execute("PRAGMA foreign_keys").fetchone()[0] == 1
    re = RepositorioTour(con)
    ra = RepositorioViajero(con)
    rt = RepositorioReserva(con, re, ra)
    a, b, c = _trio()
    re.guardar_varios([a, b, c])
    b.precio_base = 250.0
    re.guardar(b)
    assert sorted(type(x).__name__ for x in re.todos()) == sorted(["Cultural", "Aventura", "Gastronomico"])
    obtenido = re.obtener(b.clave)
    assert obtenido is not None and obtenido.precio_base == 250.0
    actor = _actor(Plata())
    ra.guardar(actor)
    t = Reserva(actor, HOY)
    t.agregar(c, 2)
    rt.guardar(t)
    leida = rt.obtener(t.clave)
    assert leida is not None and leida.total() == t.total() and leida.viajero.nivel is Plata()
    with pytest.raises(sqlite3.IntegrityError):
        con.execute("INSERT INTO lineas (reserva, tour, dias) VALUES ('NOP-0001', ?, 1)", (a.clave,))
    copia = pickle.loads(pickle.dumps(t))
    assert "_candado" not in t.__getstate__()
    assert copia.total() == t.total() and copia.lineas[0].contenedora is copia
    copia.agregar(a, 1)


def test_14_servicio_y_reportes(tmp_path: Path) -> None:
    with ServicioTours(str(tmp_path / "s.db"), reloj=lambda: HOY) as s:
        a, b, c = _trio()
        for e in (a, b, c):
            s.registrar_tour(e)
        s.registrar_viajero(_actor(Oro()))
        t1 = s.abrir("VIA-0001")
        s.agregar_linea(t1.clave, a.clave, 2)
        s.agregar_linea(t1.clave, c.clave, 1)
        s.cambiar_estado(t1.clave, Reserva.EN_CURSO)
        s.cambiar_estado(t1.clave, Reserva.CERRADA)
        t2 = s.abrir("VIA-0001")
        s.agregar_linea(t2.clave, a.clave, 5)
        conteo = s.conteo_por_estado()
        assert conteo == {"ABIERTA": 1, "EN_CURSO": 0, "CERRADA": 1, "CANCELADA": 0}
        ingresos = s.ingresos_por_tipo()
        assert "AVE" not in ingresos
        assert _sello(round(ingresos["CUL"] / a.cotizar(2), 2)) == "ef6890e8400d35bb2d05"
        assert s.top_tours(2) == [(a.clave, 7), (c.clave, 1)]
        cerrada = s.reservas(Reserva.CERRADA)[0]
        assert s.ticket_promedio() == cerrada.total()
        assert s.respaldar(tmp_path / "r.pkl") == 2
    with ServicioTours(str(tmp_path / "s.db")) as s2:
        assert len(s2.catalogo) == 3 and len(s2.reservas()) == 2
