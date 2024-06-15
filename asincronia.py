import datetime
import asyncio

'''
Ejercicio
'''

async def task(name: str, duration: int):
    print(f"Tarea: {name}, Duration: {duration}s, inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(f"Tarea: {name}, fin: {datetime.datetime.now()}")

asyncio.run(task("2", 2))
asyncio.run(task("1", 1))

'''
Extra
'''
async def async_tasks():
    await asyncio.gather(task("C", 10), task("B", 7),task("A", 4))
    await task("D", 1)

asyncio.run(async_tasks())