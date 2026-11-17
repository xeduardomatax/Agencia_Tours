"""``python -m agencia_tours.app [ruta.db]``: crea/actualiza la base de demostración."""

import sys

from ..servicio.servicio import ServicioTours
from .controlador import Controlador, poblar_demo


def main() -> None:
    ruta = sys.argv[1] if len(sys.argv) > 1 else "datos.db"
    with ServicioTours(ruta) as servicio:
        poblar_demo(servicio)
        c = Controlador(servicio)
        print(f"{len(c.tours())} tours, {len(c.viajeros())} viajeros, {len(c.reservas())} reservas en {ruta}")
        for nombre, valor in c.reportes().items():
            print(f"{nombre}: {valor}")


if __name__ == "__main__":
    main()
