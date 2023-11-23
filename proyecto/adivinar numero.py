
import random
vida = 5
resto = vida
numero_aleatorio = random.randint(1, 10)
while True:
    if resto == 0:
        print("Te has quedado sin vidas, perdiste")
        break
    numero_usuario = int(input("Elija un numero del 1 al 10: "))
    if numero_aleatorio == numero_usuario:
        print("Has ganado! El numero es:",numero_aleatorio)
        break
    elif numero_aleatorio > numero_usuario:
        resto-=1
        print(f"El numero de la maquina es mayor, te quedan {resto} vidas")
    elif numero_aleatorio < numero_usuario:
        resto-=1
        print(f"El numero de la maquina es menor, te quedan {resto} vidas")
