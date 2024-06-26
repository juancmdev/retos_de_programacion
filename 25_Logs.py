"""
EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s - handlers=[logging.StreemHandler()]")

# Niveles de severidad
logging.debug("Esto es un mensaje de DEBUG")
logging.info("Esto es un mensaje INFO") 
logging.warning("Esto es un mensaje de WARNING")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Este es un mensaje CRITICAL")

# Solo imprime por consola los mensajes de ERROR, WARNING y CRITICAL
# Es decir, aquellos que suponen un problema