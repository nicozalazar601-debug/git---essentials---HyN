# Juego de Adivinar el Número

## Descripción

Este programa en Python consiste en un juego donde el usuario debe adivinar un número elegido aleatoriamente entre dos números ingresados previamente.

El jugador dispone de 10 vidas representadas gráficamente mediante corazones.

---

## Librería utilizada

```python
import random
```

La librería `random` se utiliza para seleccionar un número aleatorio de la lista.

---

## Funcionamiento del programa

### 1. Ingreso de números

El usuario ingresa dos números positivos:

```python
a = int(input("Ingrese un numero positivo: "))
b = int(input("Ingrese otro numero positivo: "))
```

---

### 2. Creación de lista

Los números se almacenan en una lista:

```python
lista = [a, b]
```

---

### 3. Sistema de vidas

El jugador comienza con 10 vidas:

```python
vidas = 10
```

Las vidas se representan con corazones:

```python
vidasgraf= [' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ',' ❤️ ']
```

---

### 4. Selección aleatoria

El programa selecciona uno de los números al azar:

```python
azar = random.choice(lista)
```

---

### 5. Inicio del juego

Se muestran las vidas disponibles:

```python
print("Tienes 10 vidas",(''.join(vidasgraf)))
```

---

### 6. Bucle principal

El juego se ejecuta dentro de un ciclo infinito:

```python
while True:
```

---

### 7. Verificación del número

El usuario ingresa un número y el programa verifica si coincide con el número aleatorio:

```python
if num == azar:
```

Si el número es correcto:
- El jugador gana.
- El programa finaliza utilizando `break`.

---

### 8. Sistema de errores

Si el usuario falla:
- Se resta una vida.
- Se elimina un corazón.
- Se muestran las vidas restantes.

```python
vidas -= 1
vidasgraf.pop()
```

---

### 9. Fin del juego

Cuando las vidas llegan a cero:

```python
if vidas == 0:
```

El programa muestra el mensaje de derrota y finaliza.

---

## Código completo

```python
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
```
