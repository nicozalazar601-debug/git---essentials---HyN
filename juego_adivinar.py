#modificado por Nicolás Zalazar
print("=================================")
print("  Juego creado por: N. Zalazar y H. Hasi  ")
print("=================================")

import random

a = int(input("Ingrese un numero positivo: "))
b = int(input("Ingrese otro numero positivo: "))

lista = [a, b]

vidas = 10

vidasgraf= [' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ']

azar = random.choice(lista)

print("Tienes 10 vidas",(''.join(vidasgraf)))

while True:

    num = int(input("Ingrese un numero: "))

    if num == azar:
        print("\n")
        print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Adivinaste!!!!!!!!!!!!!!!!!!!")
        print("\n")
        break

    else:
        print("No adivinaste")
        vidas -= 1
        vidasgraf.pop()
        print(f"Te restan {vidas} vidas")
        print(''.join(vidasgraf))

        if vidas == 0:
            print("\n")
            print("PERDISTE")
            print("\n")
            break
