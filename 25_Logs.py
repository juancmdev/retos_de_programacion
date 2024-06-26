"""
EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
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

"""
* DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
"""

class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, name: str, description: str ):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea añadida: {name}")
        else:
            logging.warning(f"Se ha intentado añadir una tarea que ya existe: {name}")


    def delete_task(self, name: str):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Se ha eliminado la tarea: {name}")
        else:
            logging.error(f"Se está intentando eliminar una tarea que no existe")

    def list_tasks(self):
        if self.tasks:
            logging.info(f"Se va a imprimir la lista de tareas")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        else:
            logging.info(f"No hay tareas para mostrar")

            
task_manager = TaskManager()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.add_task("Python", "Estudiar Python")
task_manager.list_tasks()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
