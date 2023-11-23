import random
while True:
    usuario = input("Escriba su jugada entre piedra, papel o tijera: ")
    opciones = ["piedra", "papel", "tijera"]
    maquina = random.choice(opciones)
    if usuario == maquina:
        print("Has Empatado contra",maquina)
    elif usuario == "piedra" and maquina == "tijera" or usuario == "tijera" and maquina == "papel" or usuario  == "papel" and maquina == "piedra":
        print("Has ganado contra",maquina)
    else:
        print("Has perdido contra",maquina)
    volver_a_jugar = input("¿Deseas volver a jugar? s/n: ")
    if 's' in volver_a_jugar:
        continue
    else:
        break 
