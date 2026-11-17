"""E04–E05. Clase base abstracta, capacidades (mixins) y subtipos.

Referencias: jerarquia05.py (especialización), jerarquia06.py (ABC),
jerarquia11.py y jerarquia12.py (herencia múltiple y colisión de métodos),
encapsulacion03.py (propiedad calculada), persona03.py (name mangling),
p10_match.py (``match``).
"""

from abc import abstractmethod
from typing import ClassVar

from .clave import Clave
from .contrato import Tarifable


class Tour(Tarifable):
    """Abstracción central: recorrido turístico."""

    PREFIJO: ClassVar[str] = ""

    def __init__(self, nombre: str, precio_base: float, clave: str | None = None) -> None:
        """Inicializa nombre, precio base y clave (se genera si es ``None``)."""
        # TODO E04: implementar `Tour.__init__`
        raise NotImplementedError

    @property
    def clave(self) -> str:
        """Identidad inmutable (solo lectura)."""
        # TODO E04: implementar `Tour.clave`
        raise NotImplementedError

    @property
    def nombre(self) -> str:
        """Nombre descriptivo, no vacío."""
        # TODO E04: implementar `Tour.nombre`
        raise NotImplementedError

    @nombre.setter
    def nombre(self, valor: str) -> None:
        # TODO E04: implementar `Tour.nombre`
        raise NotImplementedError

    @property
    def precio_base(self) -> float:
        """Precio base por día, estrictamente positivo."""
        # TODO E04: implementar `Tour.precio_base`
        raise NotImplementedError

    @precio_base.setter
    def precio_base(self, valor: float) -> None:
        # TODO E04: implementar `Tour.precio_base`
        raise NotImplementedError

    @property
    def tipo(self) -> str:
        """Prefijo del subtipo (propiedad calculada)."""
        return self.PREFIJO

    def recargo(self) -> float:
        """Recargo por capacidades; la base no tiene ninguno."""
        return 0.0

    @abstractmethod
    def factor(self) -> float:
        """Factor multiplicativo propio del subtipo."""

    @abstractmethod
    def valor_atributo(self) -> int:
        """Valor del atributo distintivo del subtipo (para persistencia)."""

    def _calcular(self, dias: int) -> float:
        """Tarifa del subtipo por ``dias`` (fórmula: §6 del DOCX, por deducir)."""
        # TODO E04: implementar `Tour._calcular`
        raise NotImplementedError

    def copiar(self) -> "Tour":
        """Crea un objeto equivalente con clave NUEVA (identidad distinta)."""
        # TODO E05: implementar `Tour.copiar`
        raise NotImplementedError

    @staticmethod
    def crear(prefijo: str, nombre: str, precio_base: float, valor: int, clave: str | None = None) -> "Tour":
        """Fábrica polimórfica: reconstruye el subtipo correcto según el prefijo.

        Raises:
            ValueError: si el prefijo no corresponde a ningún subtipo.
        """
        # TODO E05: implementar `Tour.crear`
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.clave} {self.nombre} (${self.precio_base:.2f}/día)"


class Capacidad:
    """Raíz de las capacidades: termina la cadena cooperativa de ``super()``."""

    def recargo(self) -> float:
        """Recargo neutro."""
        return 0.0

    def etiquetas(self) -> list[str]:
        """Etiquetas acumuladas por la cadena de ``super()``."""
        return []


class ConTransporte(Capacidad):
    """Capacidad: incluye transporte."""

    RECARGO: ClassVar[float]  # TODO E05: valor por deducir de los ejemplos (§6)

    def recargo(self) -> float:
        # TODO E05: implementar `ConTransporte.recargo`
        raise NotImplementedError

    def etiquetas(self) -> list[str]:
        # TODO E05: implementar `ConTransporte.etiquetas`
        raise NotImplementedError


class ConGuia(Capacidad):
    """Capacidad: incluye guía certificado."""

    RECARGO: ClassVar[float]  # TODO E05: valor por deducir de los ejemplos (§6)

    def recargo(self) -> float:
        # TODO E05: implementar `ConGuia.recargo`
        raise NotImplementedError

    def etiquetas(self) -> list[str]:
        # TODO E05: implementar `ConGuia.etiquetas`
        raise NotImplementedError


class Cultural(Tour):
    """Recorrido histórico. Atributo ``sitios`` (sitios visitados) entre 1 y 10."""

    # TODO E05: declarar las capacidades que hereda y su orden (§6 y prueba 05)

    PREFIJO: ClassVar[str] = "CUL"
    MINIMO: ClassVar[int] = 1
    MAXIMO: ClassVar[int] = 10
    ESCALA: ClassVar[int]  # TODO E05: valor por deducir de los ejemplos (§6)

    def __init__(self, nombre: str, precio_base: float, sitios: int, clave: str | None = None) -> None:
        # TODO E05: implementar `Cultural.__init__`
        raise NotImplementedError

    @property
    def sitios(self) -> int:
        """sitios visitados."""
        # TODO E05: implementar `Cultural.sitios`
        raise NotImplementedError

    @sitios.setter
    def sitios(self, valor: int) -> None:
        # TODO E05: implementar `Cultural.sitios`
        raise NotImplementedError

    def factor(self) -> float:
        """Factor propio del subtipo; depende de ``sitios`` y de ``ESCALA``."""
        # TODO E05: implementar `Cultural.factor`
        raise NotImplementedError

    def valor_atributo(self) -> int:
        # TODO E05: implementar `Cultural.valor_atributo`
        raise NotImplementedError


class Aventura(Tour):
    """Recorrido de aventura. Atributo ``dificultad`` (nivel 1–5) entre 1 y 5."""

    # TODO E05: declarar las capacidades que hereda y su orden (§6 y prueba 05)

    PREFIJO: ClassVar[str] = "AVE"
    MINIMO: ClassVar[int] = 1
    MAXIMO: ClassVar[int] = 5
    ESCALA: ClassVar[int]  # TODO E05: valor por deducir de los ejemplos (§6)

    def __init__(self, nombre: str, precio_base: float, dificultad: int, clave: str | None = None) -> None:
        # TODO E05: implementar `Aventura.__init__`
        raise NotImplementedError

    @property
    def dificultad(self) -> int:
        """nivel 1–5."""
        # TODO E05: implementar `Aventura.dificultad`
        raise NotImplementedError

    @dificultad.setter
    def dificultad(self, valor: int) -> None:
        # TODO E05: implementar `Aventura.dificultad`
        raise NotImplementedError

    def factor(self) -> float:
        """Factor propio del subtipo; depende de ``dificultad`` y de ``ESCALA``."""
        # TODO E05: implementar `Aventura.factor`
        raise NotImplementedError

    def valor_atributo(self) -> int:
        # TODO E05: implementar `Aventura.valor_atributo`
        raise NotImplementedError


class Gastronomico(Tour):
    """Ruta gastronómica. Atributo ``degustaciones`` (degustaciones) entre 1 y 12."""

    # TODO E05: declarar las capacidades que hereda y su orden (§6 y prueba 05)

    PREFIJO: ClassVar[str] = "GAS"
    MINIMO: ClassVar[int] = 1
    MAXIMO: ClassVar[int] = 12
    ESCALA: ClassVar[int]  # TODO E05: valor por deducir de los ejemplos (§6)

    def __init__(self, nombre: str, precio_base: float, degustaciones: int, clave: str | None = None) -> None:
        # TODO E05: implementar `Gastronomico.__init__`
        raise NotImplementedError

    @property
    def degustaciones(self) -> int:
        """degustaciones."""
        # TODO E05: implementar `Gastronomico.degustaciones`
        raise NotImplementedError

    @degustaciones.setter
    def degustaciones(self, valor: int) -> None:
        # TODO E05: implementar `Gastronomico.degustaciones`
        raise NotImplementedError

    def factor(self) -> float:
        """Factor propio del subtipo; depende de ``degustaciones`` y de ``ESCALA``."""
        # TODO E05: implementar `Gastronomico.factor`
        raise NotImplementedError

    def valor_atributo(self) -> int:
        # TODO E05: implementar `Gastronomico.valor_atributo`
        raise NotImplementedError

    def recargo(self) -> float:
        """Colisión: ambas capacidades definen recargo(); resuélvela de forma explícita (regla: §6)."""
        # TODO E05: implementar `Gastronomico.recargo`
        raise NotImplementedError
