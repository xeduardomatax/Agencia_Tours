"""E13. Repositorios SQLite con SQL explícito y mapeo de filas.

Referencias: jerarquia06.py (contrato abstracto), elemento.py
(reconstrucción polimórfica con ``Tour.crear``).
"""

import sqlite3
from abc import ABC, abstractmethod
from datetime import date

from ..modelo.actor import Nivel, Viajero
from ..modelo.elemento import Tour
from ..modelo.transaccion import Reserva
from .conexion import transaccion


class Repositorio[T](ABC):
    """Contrato genérico de repositorio (la anotación ``[T]`` es sólo de tipos)."""

    def __init__(self, con: sqlite3.Connection) -> None:
        self._con = con

    @abstractmethod
    def guardar(self, objeto: T) -> None:
        """Inserta o actualiza (upsert)."""

    @abstractmethod
    def obtener(self, clave: str) -> T | None:
        """Busca por clave."""

    @abstractmethod
    def todos(self) -> list[T]:
        """Recupera todos."""

    @abstractmethod
    def _mapear(self, fila: sqlite3.Row) -> T:
        """Convierte una fila en objeto."""


class RepositorioTour(Repositorio[Tour]):
    """Persistencia de tours (los tres subtipos en una tabla)."""

    _UPSERT = (
        "INSERT INTO tours (clave, tipo, nombre, precio_base, atributo) "
        "VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(clave) DO UPDATE SET nombre = excluded.nombre, "
        "precio_base = excluded.precio_base, atributo = excluded.atributo"
    )

    @staticmethod
    def _parametros(e: Tour) -> tuple[str, str, str, float, int]:
        return (e.clave, e.tipo, e.nombre, e.precio_base, e.valor_atributo())

    def guardar(self, objeto: Tour) -> None:
        # TODO E13: implementar `RepositorioTour.guardar`
        raise NotImplementedError

    def guardar_varios(self, objetos: list[Tour]) -> None:
        """Inserción masiva con ``executemany``."""
        # TODO E13: implementar `RepositorioTour.guardar_varios`
        raise NotImplementedError

    def obtener(self, clave: str) -> Tour | None:
        # TODO E13: implementar `RepositorioTour.obtener`
        raise NotImplementedError

    def todos(self) -> list[Tour]:
        # TODO E13: implementar `RepositorioTour.todos`
        raise NotImplementedError

    def _mapear(self, fila: sqlite3.Row) -> Tour:
        """Reconstrucción polimórfica por la columna ``tipo``."""
        # TODO E13: implementar `RepositorioTour._mapear`
        raise NotImplementedError


class RepositorioViajero(Repositorio[Viajero]):
    """Persistencia de viajeros."""

    def guardar(self, objeto: Viajero) -> None:
        # TODO E13: implementar `RepositorioViajero.guardar`
        raise NotImplementedError

    def obtener(self, clave: str) -> Viajero | None:
        # TODO E13: implementar `RepositorioViajero.obtener`
        raise NotImplementedError

    def todos(self) -> list[Viajero]:
        # TODO E13: implementar `RepositorioViajero.todos`
        raise NotImplementedError

    def _mapear(self, fila: sqlite3.Row) -> Viajero:
        # TODO E13: implementar `RepositorioViajero._mapear`
        raise NotImplementedError


class RepositorioReserva(Repositorio[Reserva]):
    """Persistencia de reservas y sus líneas (composición)."""

    def __init__(
        self,
        con: sqlite3.Connection,
        repo_tours: RepositorioTour,
        repo_viajeros: RepositorioViajero,
    ) -> None:
        super().__init__(con)
        self._repo_tours = repo_tours
        self._repo_viajeros = repo_viajeros

    def guardar(self, objeto: Reserva) -> None:
        """Upsert de la transacción y reemplazo de sus líneas en UNA transacción."""
        # TODO E13: implementar `RepositorioReserva.guardar`
        raise NotImplementedError

    def obtener(self, clave: str) -> Reserva | None:
        # TODO E13: implementar `RepositorioReserva.obtener`
        raise NotImplementedError

    def todos(self) -> list[Reserva]:
        # TODO E13: implementar `RepositorioReserva.todos`
        raise NotImplementedError

    def _mapear(self, fila: sqlite3.Row) -> Reserva:
        """Reconstruye la transacción, su viajero y sus líneas."""
        # TODO E13: implementar `RepositorioReserva._mapear`
        raise NotImplementedError
