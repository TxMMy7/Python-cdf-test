import threading
import time

def hola(bandera):
    while not bandera.is_set():
        print("ejecucion en segundo plano... ")
        time.sleep(3)

bandera = threading.Event()
hilo = threading.Thread(target=hola, args=(bandera,))
hilo.start()

while True:
    entrada = input("PRESIONE UNA TECLA PARA DETENER LA EJECUCIÓN")
    if entrada:
        bandera.set()
        hilo.join()
        break