"""E07–E08 y E14. Transacción con estados, composición de líneas y totales.

Referencias: demo.py y jerarquia13.py (clase anidada), construccion13.py
(la parte la crea el todo), thread07.py (sección crítica), persistencia03.py
(pickle de objetos).
"""

import threading
from datetime import date
from typing import ClassVar

from .actor import Viajero
from .clave import Clave
from .contrato import Tarifable
from .elemento import Tour


class Reserva:
    """Transacción del dominio: reserva de tours."""

    PREFIJO: ClassVar[str] = "RSV"
    ABIERTA: ClassVar[str] = "ABIERTA"
    EN_CURSO: ClassVar[str] = "EN_CURSO"
    CERRADA: ClassVar[str] = "CERRADA"
    CANCELADA: ClassVar[str] = "CANCELADA"
    # TODO E07: traducir el diagrama de estados (§6) a una tabla de transiciones
    TRANSICIONES: ClassVar[dict[str, tuple[str, ...]]]

    class Linea:
        """Parte de la composición: sólo existe dentro de su transacción."""

        def __init__(self, contenedora: "Reserva", tour: Tour, dias: int) -> None:
            # TODO E07: implementar `Reserva.Linea.__init__`
            raise NotImplementedError

        @property
        def contenedora(self) -> "Reserva":
            """Referencia explícita al todo."""
            # TODO E07: implementar `Reserva.Linea.contenedora`
            raise NotImplementedError

        @property
        def tour(self) -> Tour:
            # TODO E07: implementar `Reserva.Linea.tour`
            raise NotImplementedError

        @property
        def dias(self) -> int:
            # TODO E07: implementar `Reserva.Linea.dias`
            raise NotImplementedError

        def importe(self) -> float:
            """Importe de la línea = cotización polimórfica del tour."""
            # TODO E08: implementar `Reserva.Linea.importe`
            raise NotImplementedError

    def __init__(
        self,
        viajero: Viajero,
        fecha: date,
        clave: str | None = None,
        estado: str = "ABIERTA",
        alertada: bool = False,
    ) -> None:
        # TODO E07: implementar `Reserva.__init__`
        raise NotImplementedError

    @property
    def clave(self) -> str:
        # TODO E07: implementar `Reserva.clave`
        raise NotImplementedError

    @property
    def viajero(self) -> Viajero:
        # TODO E07: implementar `Reserva.viajero`
        raise NotImplementedError

    @property
    def fecha(self) -> date:
        # TODO E07: implementar `Reserva.fecha`
        raise NotImplementedError

    @property
    def estado(self) -> str:
        # TODO E07: implementar `Reserva.estado`
        raise NotImplementedError

    @property
    def lineas(self) -> tuple["Reserva.Linea", ...]:
        """Vista inmutable de las líneas."""
        # TODO E07: implementar `Reserva.lineas`
        raise NotImplementedError

    def agregar(self, tour: Tour, dias: int) -> "Reserva.Linea":
        """Crea y posee una línea; sólo en estado ABIERTA. Sección crítica."""
        # TODO E07: implementar `Reserva.agregar`
        raise NotImplementedError

    def _restaurar_linea(self, tour: Tour, dias: int) -> None:
        """Uso exclusivo de persistencia: agrega sin validar el estado."""
        # TODO E07: implementar `Reserva._restaurar_linea`
        raise NotImplementedError

    def cambiar_estado(self, nuevo: str) -> None:
        """Aplica una transición válida de TRANSICIONES.

        Raises:
            ValueError: transición no permitida o EN_CURSO sin líneas.
        """
        # TODO E07: implementar `Reserva.cambiar_estado`
        raise NotImplementedError

    def antiguedad(self, hoy: date) -> int:
        """Días transcurridos desde la apertura."""
        # TODO E07: implementar `Reserva.antiguedad`
        raise NotImplementedError

    def subtotal(self) -> float:
        """Suma de importes de las líneas."""
        # TODO E08: implementar `Reserva.subtotal`
        raise NotImplementedError

    def descuento(self) -> float:
        """Monto de descuento según el nivel del viajero."""
        # TODO E08: implementar `Reserva.descuento`
        raise NotImplementedError

    def total(self) -> float:
        """Total = subtotal - descuento."""
        # TODO E08: implementar `Reserva.total`
        raise NotImplementedError

    def __getstate__(self) -> dict[str, object]:
        """Excluye el candado (no serializable), equivalente a ``transient``."""
        # TODO E14: implementar `Reserva.__getstate__`
        raise NotImplementedError

    def __setstate__(self, estado: dict[str, object]) -> None:
        """Restaura atributos y crea un candado nuevo."""
        # TODO E14: implementar `Reserva.__setstate__`
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO E07: implementar `Reserva.__str__`
        raise NotImplementedError
