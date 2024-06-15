'''
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
'''

for i in range(0, 10):
    print(i + 1)


i = 0

while i <= 10:
    print(i)
    i += 1

print("\n\n")


def count_ten(i: int):
    if i <= 50:
        print(i)
        count_ten(i + 1)

count_ten(1)


'''
* DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
'''