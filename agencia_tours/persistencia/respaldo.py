"""E14. Respaldo complementario con ``pickle``.

Referencias: persistencia02.py y persistencia03.py. Investigación del
estudiante: ``__getstate__``/``__setstate__`` (necesarios porque un
``threading.Lock`` no es serializable).
"""

import pickle
from pathlib import Path

from ..modelo.transaccion import Reserva


def respaldar(ruta: str | Path, reservas: list[Reserva]) -> int:
    """Serializa la lista completa; devuelve cuántas se guardaron."""
    # TODO E14: implementar `respaldar`
    raise NotImplementedError


def restaurar(ruta: str | Path) -> list[Reserva]:
    """Lee un respaldo previo.

    Raises:
        TypeError: si el contenido no es una lista de Reserva.
    """
    # TODO E14: implementar `restaurar`
    raise NotImplementedError
