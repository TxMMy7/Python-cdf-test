import threading
import time
class tamat:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.hambre = 0
        self.felicidad = 50
        self.humor = "indiferente"
        self.vivo = True
    def morir(self):
        if self.energia <= 0 or self.hambre >= 100 or self.felicidad <= 0:
            self.vivo = False
            print("El Tamagotchi ha muerto!")
    def mostrar_estado(self):
        #Muestra en consola el nombre del Tamagotchi y sus niveles actuales de energía, hambre y estado de humor.
        print(f"mi nombre es {self.nombre} y mi energia es: {self.energia} mi hambre es: {self.hambre} y mi humor es: {self.humor}")
    def alimentar(self):
        #Disminuye el nivel de hambre en 10 y disminuye el nivel de energía en 15.
        self.hambre -= 10
        self.energia -= 15
        self.morir()
    def jugar(self):
        #Aumenta el nivel de felicidad en 20, disminuye el nivel de energía en 18 y aumenta el nivel de hambre en 10.
        self.felicidad += 20
        self.energia -= 18
        self.hambre += 10
        self.morir()
    def dormir(self):
        #Aumenta el nivel de energía en 40 y aumenta el nivel de hambre en 5
        self.energia += 40
        self.hambre += 5
        self.morir()
    def tiempo(self, condicion):
        while not condicion.is_set() and self.vivo:
            self.hambre += 20
            self.humor = "triste"
            self.energia -= 20
            self.morir()
            time.sleep(60)
    def verificar_estado(self):
        if not self.vivo:
            self.morir()
        elif self.hambre >= 20:
            self.energia -= 20
            self.felicidad -= 30
            print("El Tamagotchi está hambriento.")
        else:
            print("El Tamagotchi está vivo y feliz.")


condicion = threading.Event()


nombre = input("Nombre del tamatgochi:")
tamatgochi = tamat(nombre)

hilo = threading.Thread(target=tamatgochi.tiempo, args=(condicion,))
hilo.start()

while tamatgochi.vivo:
    print("""
        1) estado
        2) alimentar
        3) jugar
        4) dormir
        5) salir
    """)
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        tamatgochi.mostrar_estado()
    if opcion == "2":
        tamatgochi.alimentar()
        tamatgochi.verificar_estado()
        tamatgochi.mostrar_estado()
    if opcion == "3":
        tamatgochi.jugar()
        tamatgochi.verificar_estado()
    if opcion == "4":
        tamatgochi.dormir()
        tamatgochi.verificar_estado()
    if opcion == "5":
        print("has salido!")
        condicion.set()
        hilo.join()
        break

