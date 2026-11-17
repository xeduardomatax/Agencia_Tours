"""Capa de aplicación: puerto único entre la UI y el servicio.

La UI (escritorio o web) SÓLO importa este módulo: recibe y entrega tipos
simples (``str``, ``int``, ``float``, ``dict``) y nunca toca ``sqlite3``.
"""

from datetime import date, timedelta

from ..eventos.oyentes import OyenteCola
from ..modelo.actor import Nivel, Viajero
from ..modelo.elemento import Tour
from ..servicio.servicio import ServicioTours

Fila = dict[str, str]

TIPOS: dict[str, str] = {
    "CUL": "Cultural (sitios)",
    "AVE": "Aventura (dificultad)",
    "GAS": "Gastronomico (degustaciones)",
}
ESTADOS: tuple[str, ...] = ("ABIERTA", "EN_CURSO", "CERRADA", "CANCELADA")


class Controlador:
    """Adaptador de la UI: traduce eventos de interfaz a casos de uso."""

    def __init__(self, servicio: ServicioTours) -> None:
        self._s = servicio
        self.eventos = OyenteCola()
        servicio.suscribir(self.eventos)

    def tours(self) -> list[Fila]:
        return [
            {
                "clave": e.clave,
                "tipo": e.tipo,
                "nombre": e.nombre,
                "precio": f"{e.precio_base:.2f}",
                "atributo": str(e.valor_atributo()),
            }
            for e in self._s.catalogo.ordenados("clave")
        ]

    def viajeros(self) -> list[Fila]:
        return [
            {"clave": a.clave, "nombre": a.nombre, "correo": a.correo, "nivel": str(a.nivel)}
            for a in self._s.viajeros()
        ]

    def reservas(self) -> list[Fila]:
        return [
            {
                "clave": t.clave,
                "viajero": t.viajero.nombre,
                "fecha": t.fecha.isoformat(),
                "estado": t.estado,
                "lineas": str(len(t.lineas)),
                "total": f"{t.total():.2f}",
            }
            for t in self._s.reservas()
        ]

    def alta_tour(self, tipo: str, nombre: str, precio: float, valor: int) -> str:
        e = Tour.crear(tipo, nombre, precio, valor)
        self._s.registrar_tour(e)
        return e.clave

    def alta_viajero(self, nombre: str, correo: str, nivel: str) -> str:
        a = Viajero(nombre, correo, Nivel.desde_nombre(nivel))
        self._s.registrar_viajero(a)
        return a.clave

    def abrir(self, clave_viajero: str) -> str:
        return self._s.abrir(clave_viajero).clave

    def agregar(self, clave_reserva: str, clave_tour: str, dias: int) -> None:
        self._s.agregar_linea(clave_reserva, clave_tour, dias)

    def cambiar(self, clave_reserva: str, estado: str) -> None:
        self._s.cambiar_estado(clave_reserva, estado)

    def revisar(self) -> tuple[int, int]:
        return self._s.revisar()

    def reportes(self) -> dict[str, str]:
        return {
            "Conteo por estado": str(self._s.conteo_por_estado()),
            "Ingresos por tipo": str(self._s.ingresos_por_tipo()),
            "Top tours": str(self._s.top_tours()),
            "Ticket promedio": f"{self._s.ticket_promedio():.2f}",
        }

    def pendientes(self) -> list[str]:
        """Eventos acumulados por otros hilos (se consumen en el hilo de la UI)."""
        return [f"{e}: {d}" for e, d in self.eventos.pendientes()]


def poblar_demo(servicio: ServicioTours) -> None:
    """Datos mínimos exigidos: 6 tours, 3 viajeros y 4 reservas (una por estado)."""
    if servicio.catalogo.todos():
        return
    ejemplos = [
        Tour.crear("CUL", "Centro histórico Orizaba", 350.0, 6),
        Tour.crear("CUL", "Ruta de los murales", 300.0, 4),
        Tour.crear("AVE", "Rápel en Cañón de la Carbonera", 900.0, 4),
        Tour.crear("AVE", "Ascenso al Cerro del Borrego", 400.0, 2),
        Tour.crear("GAS", "Ruta del café", 650.0, 5),
        Tour.crear("GAS", "Mercados y antojitos", 380.0, 8),
    ]
    for e in ejemplos:
        servicio.registrar_tour(e)
    actores = [
        Viajero.desde_texto("Carlos Méndez;carlos0@ejemplo.mx;BASICO"),
        Viajero.desde_texto("Familia Vázquez;familia1@ejemplo.mx;PLATA"),
        Viajero.desde_texto("Club Excursionista;club2@ejemplo.mx;ORO"),
    ]
    for a in actores:
        servicio.registrar_viajero(a)
    abierta = servicio.abrir(actores[0].clave)
    servicio.agregar_linea(abierta.clave, ejemplos[0].clave, 1)
    en_curso = servicio.abrir(actores[1].clave)
    servicio.agregar_linea(en_curso.clave, ejemplos[2].clave, 2)
    servicio.cambiar_estado(en_curso.clave, "EN_CURSO")
    cerrada = servicio.abrir(actores[2].clave)
    servicio.agregar_linea(cerrada.clave, ejemplos[4].clave, 3)
    servicio.agregar_linea(cerrada.clave, ejemplos[1].clave, 1)
    servicio.cambiar_estado(cerrada.clave, "EN_CURSO")
    servicio.cambiar_estado(cerrada.clave, "CERRADA")
    cancelada = servicio.abrir(actores[0].clave)
    servicio.cambiar_estado(cancelada.clave, "CANCELADA")


def reloj_demo() -> date:
    """Reloj de ejemplo desplazado; útil para observar el monitor en la UI."""
    return date.today() + timedelta(days=ServicioTours.PLAZO + 1)
