# TODO — Agencia de tours

Total: **146** tareas en 16 grupos.

| Grupo | Tema | Tareas | Semana |
|---|---|---|---|
| E01 | Configuración del proyecto | 3 | 1 |
| E02 | Contrato raíz (abstracción) | 4 | 1 |
| E03 | Clave (identidad) | 3 | 1 |
| E04 | Clase base abstracta | 7 | 1 |
| E05 | Subtipos y capacidades (herencia múltiple) | 30 | 2 |
| E06 | Actor y niveles (Singleton) | 15 | 2 |
| E07 | Transacción, estados y composición | 16 | 2 |
| E08 | Totales | 4 | 2 |
| E09 | Catálogo (agregación) | 8 | 3 |
| E10 | Tipos anidados y locales | 1 | 3 |
| E11 | Programación funcional | 8 | 3 |
| E12 | Concurrencia y monitor | 8 | 3 |
| E13 | Persistencia SQLite | 15 | 4 |
| E14 | Respaldo pickle | 5 | 4 |
| E15 | Servicio y eventos | 15 | 4 |
| E16 | Reportes | 4 | 4 |

## Detalle

| Grupo | Archivo | Línea | Tarea |
|---|---|---|---|
| E01 | `agencia_tours/__init__.py` | 13 | implementar `info` |
| E01 | `pyproject.toml` | 6 | escribe tu nombre y correo institucional |
| E01 | `pyproject.toml` | 11 | conserva sólo la tecnología de UI que elijas (tkinter viene con Python) |
| E02 | `agencia_tours/modelo/contrato.py` | 25 | implementar `Tarifable.cotizar` |
| E02 | `agencia_tours/modelo/contrato.py` | 30 | implementar `Tarifable.cotizar_con_iva` |
| E02 | `agencia_tours/modelo/contrato.py` | 40 | implementar `Tarifable.redondear` |
| E02 | `agencia_tours/modelo/contrato.py` | 46 | implementar `Tarifable.moneda` |
| E03 | `agencia_tours/modelo/clave.py` | 20 | implementar `Clave.es_valida` |
| E03 | `agencia_tours/modelo/clave.py` | 30 | implementar `Clave.siguiente` |
| E03 | `agencia_tours/modelo/clave.py` | 36 | implementar `Clave.registrar` |
| E04 | `agencia_tours/modelo/elemento.py` | 23 | implementar `Tour.__init__` |
| E04 | `agencia_tours/modelo/elemento.py` | 29 | implementar `Tour.clave` |
| E04 | `agencia_tours/modelo/elemento.py` | 35 | implementar `Tour.nombre` |
| E04 | `agencia_tours/modelo/elemento.py` | 40 | implementar `Tour.nombre` |
| E04 | `agencia_tours/modelo/elemento.py` | 46 | implementar `Tour.precio_base` |
| E04 | `agencia_tours/modelo/elemento.py` | 51 | implementar `Tour.precio_base` |
| E04 | `agencia_tours/modelo/elemento.py` | 73 | implementar `Tour._calcular` |
| E05 | `agencia_tours/modelo/elemento.py` | 78 | implementar `Tour.copiar` |
| E05 | `agencia_tours/modelo/elemento.py` | 88 | implementar `Tour.crear` |
| E05 | `agencia_tours/modelo/elemento.py` | 110 | valor por deducir de los ejemplos (§6) |
| E05 | `agencia_tours/modelo/elemento.py` | 113 | implementar `ConTransporte.recargo` |
| E05 | `agencia_tours/modelo/elemento.py` | 117 | implementar `ConTransporte.etiquetas` |
| E05 | `agencia_tours/modelo/elemento.py` | 124 | valor por deducir de los ejemplos (§6) |
| E05 | `agencia_tours/modelo/elemento.py` | 127 | implementar `ConGuia.recargo` |
| E05 | `agencia_tours/modelo/elemento.py` | 131 | implementar `ConGuia.etiquetas` |
| E05 | `agencia_tours/modelo/elemento.py` | 138 | declarar las capacidades que hereda y su orden (§6 y prueba 05) |
| E05 | `agencia_tours/modelo/elemento.py` | 143 | valor por deducir de los ejemplos (§6) |
| E05 | `agencia_tours/modelo/elemento.py` | 146 | implementar `Cultural.__init__` |
| E05 | `agencia_tours/modelo/elemento.py` | 152 | implementar `Cultural.sitios` |
| E05 | `agencia_tours/modelo/elemento.py` | 157 | implementar `Cultural.sitios` |
| E05 | `agencia_tours/modelo/elemento.py` | 162 | implementar `Cultural.factor` |
| E05 | `agencia_tours/modelo/elemento.py` | 166 | implementar `Cultural.valor_atributo` |
| E05 | `agencia_tours/modelo/elemento.py` | 173 | declarar las capacidades que hereda y su orden (§6 y prueba 05) |
| E05 | `agencia_tours/modelo/elemento.py` | 178 | valor por deducir de los ejemplos (§6) |
| E05 | `agencia_tours/modelo/elemento.py` | 181 | implementar `Aventura.__init__` |
| E05 | `agencia_tours/modelo/elemento.py` | 187 | implementar `Aventura.dificultad` |
| E05 | `agencia_tours/modelo/elemento.py` | 192 | implementar `Aventura.dificultad` |
| E05 | `agencia_tours/modelo/elemento.py` | 197 | implementar `Aventura.factor` |
| E05 | `agencia_tours/modelo/elemento.py` | 201 | implementar `Aventura.valor_atributo` |
| E05 | `agencia_tours/modelo/elemento.py` | 208 | declarar las capacidades que hereda y su orden (§6 y prueba 05) |
| E05 | `agencia_tours/modelo/elemento.py` | 213 | valor por deducir de los ejemplos (§6) |
| E05 | `agencia_tours/modelo/elemento.py` | 216 | implementar `Gastronomico.__init__` |
| E05 | `agencia_tours/modelo/elemento.py` | 222 | implementar `Gastronomico.degustaciones` |
| E05 | `agencia_tours/modelo/elemento.py` | 227 | implementar `Gastronomico.degustaciones` |
| E05 | `agencia_tours/modelo/elemento.py` | 232 | implementar `Gastronomico.factor` |
| E05 | `agencia_tours/modelo/elemento.py` | 236 | implementar `Gastronomico.valor_atributo` |
| E05 | `agencia_tours/modelo/elemento.py` | 241 | implementar `Gastronomico.recargo` |
| E06 | `agencia_tours/modelo/actor.py` | 22 | implementar `Nivel.__new__` |
| E06 | `agencia_tours/modelo/actor.py` | 32 | implementar `Nivel.desde_nombre` |
| E06 | `agencia_tours/modelo/actor.py` | 46 | implementar `Basico.descuento` |
| E06 | `agencia_tours/modelo/actor.py` | 57 | implementar `Plata.descuento` |
| E06 | `agencia_tours/modelo/actor.py` | 68 | implementar `Oro.descuento` |
| E06 | `agencia_tours/modelo/actor.py` | 81 | implementar `Viajero.__init__` |
| E06 | `agencia_tours/modelo/actor.py` | 87 | implementar `Viajero.desde_texto` |
| E06 | `agencia_tours/modelo/actor.py` | 92 | implementar `Viajero.clave` |
| E06 | `agencia_tours/modelo/actor.py` | 97 | implementar `Viajero.nombre` |
| E06 | `agencia_tours/modelo/actor.py` | 102 | implementar `Viajero.nombre` |
| E06 | `agencia_tours/modelo/actor.py` | 107 | implementar `Viajero.correo` |
| E06 | `agencia_tours/modelo/actor.py` | 112 | implementar `Viajero.correo` |
| E06 | `agencia_tours/modelo/actor.py` | 117 | implementar `Viajero.nivel` |
| E06 | `agencia_tours/modelo/actor.py` | 122 | implementar `Viajero.nivel` |
| E06 | `agencia_tours/modelo/actor.py` | 127 | implementar `Viajero.descuento` |
| E07 | `agencia_tours/modelo/transaccion.py` | 26 | traducir el diagrama de estados (§6) a una tabla de transiciones |
| E07 | `agencia_tours/modelo/transaccion.py` | 33 | implementar `Reserva.Linea.__init__` |
| E07 | `agencia_tours/modelo/transaccion.py` | 39 | implementar `Reserva.Linea.contenedora` |
| E07 | `agencia_tours/modelo/transaccion.py` | 44 | implementar `Reserva.Linea.tour` |
| E07 | `agencia_tours/modelo/transaccion.py` | 49 | implementar `Reserva.Linea.dias` |
| E07 | `agencia_tours/modelo/transaccion.py` | 65 | implementar `Reserva.__init__` |
| E07 | `agencia_tours/modelo/transaccion.py` | 70 | implementar `Reserva.clave` |
| E07 | `agencia_tours/modelo/transaccion.py` | 75 | implementar `Reserva.viajero` |
| E07 | `agencia_tours/modelo/transaccion.py` | 80 | implementar `Reserva.fecha` |
| E07 | `agencia_tours/modelo/transaccion.py` | 85 | implementar `Reserva.estado` |
| E07 | `agencia_tours/modelo/transaccion.py` | 91 | implementar `Reserva.lineas` |
| E07 | `agencia_tours/modelo/transaccion.py` | 96 | implementar `Reserva.agregar` |
| E07 | `agencia_tours/modelo/transaccion.py` | 101 | implementar `Reserva._restaurar_linea` |
| E07 | `agencia_tours/modelo/transaccion.py` | 110 | implementar `Reserva.cambiar_estado` |
| E07 | `agencia_tours/modelo/transaccion.py` | 115 | implementar `Reserva.antiguedad` |
| E07 | `agencia_tours/modelo/transaccion.py` | 144 | implementar `Reserva.__str__` |
| E08 | `agencia_tours/modelo/transaccion.py` | 54 | implementar `Reserva.Linea.importe` |
| E08 | `agencia_tours/modelo/transaccion.py` | 120 | implementar `Reserva.subtotal` |
| E08 | `agencia_tours/modelo/transaccion.py` | 125 | implementar `Reserva.descuento` |
| E08 | `agencia_tours/modelo/transaccion.py` | 130 | implementar `Reserva.total` |
| E09 | `agencia_tours/modelo/catalogo.py` | 15 | implementar `Folleto.__init__` |
| E09 | `agencia_tours/modelo/catalogo.py` | 20 | implementar `Folleto.agregar` |
| E09 | `agencia_tours/modelo/catalogo.py` | 25 | implementar `Folleto.obtener` |
| E09 | `agencia_tours/modelo/catalogo.py` | 29 | implementar `Folleto.quitar` |
| E09 | `agencia_tours/modelo/catalogo.py` | 34 | implementar `Folleto.todos` |
| E09 | `agencia_tours/modelo/catalogo.py` | 38 | implementar `Folleto.__len__` |
| E09 | `agencia_tours/modelo/catalogo.py` | 47 | implementar `Folleto.buscar` |
| E09 | `agencia_tours/modelo/catalogo.py` | 52 | implementar `Folleto.ordenados` |
| E10 | `agencia_tours/modelo/catalogo.py` | 67 | implementar `Folleto.resumen_por_tipo` |
| E11 | `agencia_tours/funcional/reglas.py` | 23 | implementar `Regla.__call__` |
| E11 | `agencia_tours/funcional/reglas.py` | 28 | implementar `Regla.y` |
| E11 | `agencia_tours/funcional/reglas.py` | 33 | implementar `Regla.o` |
| E11 | `agencia_tours/funcional/reglas.py` | 38 | implementar `Regla.negar` |
| E11 | `agencia_tours/funcional/reglas.py` | 47 | implementar `precio_maximo` |
| E11 | `agencia_tours/funcional/reglas.py` | 53 | implementar `de_tipo` |
| E11 | `agencia_tours/funcional/reglas.py` | 59 | implementar `filtrar` |
| E11 | `agencia_tours/funcional/reglas.py` | 65 | implementar `aplicar` |
| E12 | `agencia_tours/concurrencia/tarea.py` | 15 | implementar `TareaPeriodica.__init__` |
| E12 | `agencia_tours/concurrencia/tarea.py` | 20 | implementar `TareaPeriodica.run` |
| E12 | `agencia_tours/concurrencia/tarea.py` | 25 | implementar `TareaPeriodica.detener` |
| E12 | `agencia_tours/servicio/servicio.py` | 39 | implementar `ServicioTours.Monitor.__init__` |
| E12 | `agencia_tours/servicio/servicio.py` | 43 | implementar `ServicioTours.Monitor.ejecutar` |
| E12 | `agencia_tours/servicio/servicio.py` | 125 | implementar `ServicioTours.revisar` |
| E12 | `agencia_tours/servicio/servicio.py` | 129 | implementar `ServicioTours.iniciar_monitor` |
| E12 | `agencia_tours/servicio/servicio.py` | 133 | implementar `ServicioTours.detener_monitor` |
| E13 | `agencia_tours/persistencia/conexion.py` | 42 | implementar `abrir` |
| E13 | `agencia_tours/persistencia/conexion.py` | 49 | implementar `transaccion` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 55 | implementar `RepositorioTour.guardar` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 60 | implementar `RepositorioTour.guardar_varios` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 64 | implementar `RepositorioTour.obtener` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 68 | implementar `RepositorioTour.todos` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 73 | implementar `RepositorioTour._mapear` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 81 | implementar `RepositorioViajero.guardar` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 85 | implementar `RepositorioViajero.obtener` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 89 | implementar `RepositorioViajero.todos` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 93 | implementar `RepositorioViajero._mapear` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 112 | implementar `RepositorioReserva.guardar` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 116 | implementar `RepositorioReserva.obtener` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 120 | implementar `RepositorioReserva.todos` |
| E13 | `agencia_tours/persistencia/repositorios.py` | 125 | implementar `RepositorioReserva._mapear` |
| E14 | `agencia_tours/modelo/transaccion.py` | 135 | implementar `Reserva.__getstate__` |
| E14 | `agencia_tours/modelo/transaccion.py` | 140 | implementar `Reserva.__setstate__` |
| E14 | `agencia_tours/persistencia/respaldo.py` | 16 | implementar `respaldar` |
| E14 | `agencia_tours/persistencia/respaldo.py` | 26 | implementar `restaurar` |
| E14 | `agencia_tours/servicio/servicio.py` | 142 | implementar `ServicioTours.respaldar` |
| E15 | `agencia_tours/eventos/oyentes.py` | 26 | implementar `OyenteMemoria.notificar` |
| E15 | `agencia_tours/eventos/oyentes.py` | 37 | implementar `OyenteCola.notificar` |
| E15 | `agencia_tours/eventos/oyentes.py` | 42 | implementar `OyenteCola.pendientes` |
| E15 | `agencia_tours/servicio/servicio.py` | 61 | implementar `ServicioTours.__enter__` |
| E15 | `agencia_tours/servicio/servicio.py` | 70 | implementar `ServicioTours.__exit__` |
| E15 | `agencia_tours/servicio/servicio.py` | 75 | implementar `ServicioTours.suscribir` |
| E15 | `agencia_tours/servicio/servicio.py` | 79 | implementar `ServicioTours._emitir` |
| E15 | `agencia_tours/servicio/servicio.py` | 84 | implementar `ServicioTours.registrar_tour` |
| E15 | `agencia_tours/servicio/servicio.py` | 88 | implementar `ServicioTours.registrar_viajero` |
| E15 | `agencia_tours/servicio/servicio.py` | 92 | implementar `ServicioTours.viajeros` |
| E15 | `agencia_tours/servicio/servicio.py` | 97 | implementar `ServicioTours.abrir` |
| E15 | `agencia_tours/servicio/servicio.py` | 101 | implementar `ServicioTours.agregar_linea` |
| E15 | `agencia_tours/servicio/servicio.py` | 105 | implementar `ServicioTours.cambiar_estado` |
| E15 | `agencia_tours/servicio/servicio.py` | 110 | implementar `ServicioTours.reservas` |
| E15 | `agencia_tours/servicio/servicio.py` | 114 | implementar `ServicioTours._requerir` |
| E16 | `agencia_tours/servicio/servicio.py` | 148 | implementar `ServicioTours.conteo_por_estado` |
| E16 | `agencia_tours/servicio/servicio.py` | 153 | implementar `ServicioTours.ingresos_por_tipo` |
| E16 | `agencia_tours/servicio/servicio.py` | 158 | implementar `ServicioTours.top_tours` |
| E16 | `agencia_tours/servicio/servicio.py` | 163 | implementar `ServicioTours.ticket_promedio` |
