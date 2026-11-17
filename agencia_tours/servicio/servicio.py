"""E15–E16 y E12. Fachada única del dominio Agencia de tours.

Referencias: p23_contexto3.py (``__enter__``/``__exit__``), jerarquia13.py
(clase anidada ``Monitor``), thread07.py (hilo como clase), construccion09.py.
"""

import threading
from collections.abc import Callable
from datetime import date
from pathlib import Path
from types import TracebackType
from typing import ClassVar

from ..concurrencia.tarea import TareaPeriodica
from ..eventos.oyentes import Oyente
from ..modelo.actor import Viajero
from ..modelo.catalogo import Folleto
from ..modelo.elemento import Tour
from ..modelo.transaccion import Reserva
from ..persistencia import respaldo
from ..persistencia.conexion import abrir
from ..persistencia.repositorios import (
    RepositorioReserva,
    RepositorioTour,
    RepositorioViajero,
)


class ServicioTours:
    """Fachada: casos de uso, eventos, monitor y reportes."""

    PLAZO: ClassVar[int] = 5
    """Días máximos que una reserva puede permanecer EN_CURSO."""

    class Monitor(TareaPeriodica):
        """Hilo vigilante: clase anidada con referencia explícita a su servicio."""

        def __init__(self, servicio: "ServicioTours", periodo: float) -> None:
            # TODO E12: implementar `ServicioTours.Monitor.__init__`
            raise NotImplementedError

        def ejecutar(self) -> None:
            # TODO E12: implementar `ServicioTours.Monitor.ejecutar`
            raise NotImplementedError

    def __init__(
        self,
        ruta_bd: str = ":memory:",
        reloj: Callable[[], date] = date.today,
    ) -> None:
        """``reloj`` inyectable para pruebas deterministas."""
        self._ruta_bd = ruta_bd
        self._reloj = reloj
        self._oyentes: list[Oyente] = []
        self._candado = threading.Lock()
        self._monitor: ServicioTours.Monitor | None = None
        self.catalogo = Folleto()

    # ---------------------------------------------------------------- ciclo de vida
    def __enter__(self) -> "ServicioTours":
        # TODO E15: implementar `ServicioTours.__enter__`
        raise NotImplementedError

    def __exit__(
        self,
        tipo: type[BaseException] | None,
        valor: BaseException | None,
        traza: TracebackType | None,
    ) -> None:
        # TODO E15: implementar `ServicioTours.__exit__`
        raise NotImplementedError

    # ---------------------------------------------------------------- eventos
    def suscribir(self, oyente: Oyente) -> None:
        # TODO E15: implementar `ServicioTours.suscribir`
        raise NotImplementedError

    def _emitir(self, evento: str, detalle: str) -> None:
        # TODO E15: implementar `ServicioTours._emitir`
        raise NotImplementedError

    # ---------------------------------------------------------------- casos de uso
    def registrar_tour(self, tour: Tour) -> None:
        # TODO E15: implementar `ServicioTours.registrar_tour`
        raise NotImplementedError

    def registrar_viajero(self, viajero: Viajero) -> None:
        # TODO E15: implementar `ServicioTours.registrar_viajero`
        raise NotImplementedError

    def viajeros(self) -> list[Viajero]:
        # TODO E15: implementar `ServicioTours.viajeros`
        raise NotImplementedError

    def abrir(self, clave_viajero: str) -> Reserva:
        """Abre una reserva con la fecha del reloj inyectado."""
        # TODO E15: implementar `ServicioTours.abrir`
        raise NotImplementedError

    def agregar_linea(self, clave_reserva: str, clave_tour: str, dias: int) -> Reserva:
        # TODO E15: implementar `ServicioTours.agregar_linea`
        raise NotImplementedError

    def cambiar_estado(self, clave_reserva: str, nuevo: str) -> Reserva:
        # TODO E15: implementar `ServicioTours.cambiar_estado`
        raise NotImplementedError

    def reservas(self, estado: str | None = None) -> list[Reserva]:
        """Todas o sólo las del estado indicado."""
        # TODO E15: implementar `ServicioTours.reservas`
        raise NotImplementedError

    def _requerir(self, clave: str) -> Reserva:
        # TODO E15: implementar `ServicioTours._requerir`
        raise NotImplementedError

    # ---------------------------------------------------------------- monitor
    def revisar(self) -> tuple[int, int]:
        """Reglas del monitor; devuelve (canceladas, alertas emitidas).

        1. ABIERTA sin líneas con antigüedad >= 1 día → CANCELADA.
        2. EN_CURSO con antigüedad > PLAZO y sin alerta previa → alerta ÚNICA
           (el indicador ``alertada`` se persiste).
        """
        # TODO E12: implementar `ServicioTours.revisar`
        raise NotImplementedError

    def iniciar_monitor(self, periodo: float = 60.0) -> None:
        # TODO E12: implementar `ServicioTours.iniciar_monitor`
        raise NotImplementedError

    def detener_monitor(self) -> None:
        # TODO E12: implementar `ServicioTours.detener_monitor`
        raise NotImplementedError

    @property
    def monitor(self) -> "ServicioTours.Monitor | None":
        return self._monitor

    # ---------------------------------------------------------------- respaldo
    def respaldar(self, ruta: str | Path) -> int:
        # TODO E14: implementar `ServicioTours.respaldar`
        raise NotImplementedError

    # ---------------------------------------------------------------- reportes
    def conteo_por_estado(self) -> dict[str, int]:
        """Número de reservas por estado (los 4 estados siempre presentes)."""
        # TODO E16: implementar `ServicioTours.conteo_por_estado`
        raise NotImplementedError

    def ingresos_por_tipo(self) -> dict[str, float]:
        """Suma de importes de reservas CERRADAS agrupada por tipo de tour."""
        # TODO E16: implementar `ServicioTours.ingresos_por_tipo`
        raise NotImplementedError

    def top_tours(self, n: int = 3) -> list[tuple[str, int]]:
        """Los ``n`` tours más usados (clave, días acumulados), descendente."""
        # TODO E16: implementar `ServicioTours.top_tours`
        raise NotImplementedError

    def ticket_promedio(self) -> float:
        """Promedio del total de las reservas CERRADAS (0.0 si no hay)."""
        # TODO E16: implementar `ServicioTours.ticket_promedio`
        raise NotImplementedError
