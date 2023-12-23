import random

class Arma:
    def __init__(self, nombre, bonus):
        self.nombre = nombre
        self.bonus = bonus

    def atacar(self, enemigo):
        try:
            if self:
                daño = self.bonus - enemigo.defensa
            else:
                daño = -enemigo.defensa

            daño = max(daño, 0)
            enemigo.vida -= daño
        except AttributeError:
            print("Error")

class Machete(Arma):
    def __init__(self):
        super().__init__("Espada", bonus=20)

class Cuchillo(Arma):
    def __init__(self):
        super().__init__("Cuchillo", bonus=10)

class Arco(Arma):
    def __init__(self):
        super().__init__("Arco", bonus=10)

class Ballesta(Arma):
    def __init__(self):
        super().__init__("Ballesta", bonus=20)

class Vara(Arma):
    def __init__(self):
        super().__init__("Vara", bonus=15)

class Guantes(Arma):
    def __init__(self):
        super().__init__("Guantes", bonus=20)

class Espada(Arma):
    def __init__(self):
        super().__init__("Espada", bonus=10)

class Hacha(Arma):
    def __init__(self):
        super().__init__("Hacha", bonus=20)

class Personajes:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, armas=None):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.armas = armas

    def atacar(self, enemigo):
        try:
            if isinstance(self, (Guerrero, Mago, Arquero, Asesino)) and getattr(self, 'armas', None):
                daño = self.ataque + sum(arma.bonus for arma in self.armas) - enemigo.defensa
            else:
                daño = self.ataque - enemigo.defensa

            daño = max(daño, 0)
            enemigo.vida -= daño
            return daño
        except AttributeError:
            print("")

class Guerrero(Personajes):
    def __init__(self, nombre, armas=None):
        super().__init__(nombre, vida=100, ataque=100, defensa=50, inteligencia=20, agilidad=30, fuerza=30, armas=armas)

    def atacar(self, enemigo):
        super().atacar(enemigo)

class Mago(Personajes):
    def __init__(self, nombre, armas=None):
        super().__init__(nombre, vida=100, ataque=80, defensa=17, inteligencia=15, agilidad=12, fuerza=10, armas=armas)

    def atacar(self, enemigo):
        super().atacar(enemigo)

class Arquero(Personajes):
    def __init__(self, nombre, armas=None):
        super().__init__(nombre, vida=100, ataque=70, defensa=20, inteligencia=10, agilidad=10, fuerza=20, armas=armas)

    def atacar(self, enemigo):
        super().atacar(enemigo)

class Asesino(Personajes):
    def __init__(self, nombre, armas=None):
        super().__init__(nombre, vida=100, ataque=95, defensa=20, inteligencia=10, agilidad=10, fuerza=50, armas=armas)

    def atacar(self, enemigo):
        super().atacar(enemigo)

class Enemigo:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, arma=None):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.arma = arma

    def atacar(self, personaje):
        pass

class Bruja(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=100, ataque=25, defensa=15, inteligencia=10, agilidad=30, fuerza=20, arma=None)
        self.vuela = True

    def esquive(self):
        if self.vuela:
            return random.random() < 0.4

    def atacar(self, personaje):
        if not self.esquive():
            daño = self.ataque - personaje.defensa
            daño = max(daño, 0)
            personaje.vida -= daño
            print(f"{self.nombre} ataca a {personaje.nombre}.")
        else:
            print(f"{self.nombre} esquiva el ataque de {personaje.nombre}.")

class Ciclope(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=130, ataque=35, defensa=25, inteligencia=15, agilidad=10, fuerza=40, arma=None)

class Minotauro(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=150, ataque=40, defensa=30, inteligencia=10, agilidad=10, fuerza=50, arma=None)

class HombreDeCristal(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=200, ataque=25, defensa=40, inteligencia=5, agilidad=5, fuerza=40, arma=None)

def seleccionar_rival(jugadores, enemigos):
    print("""\n-----Encuentros-----")
1. Guerrero vs Bruja
2. Mago vs Ciclope
3. Arquero vs Minotauro
4. Asesino vs Hombre de Cristal""")

    opcion = input("Seleccione un nro de encuentro: ")

    if opcion == "1":
        return jugadores[0], enemigos[0]
    elif opcion == "2":
        return jugadores[1], enemigos[1]
    elif opcion == "3":
        return jugadores[2], enemigos[2]
    elif opcion == "4":
        return jugadores[3], enemigos[3]
    else:
        print("Opción no válida. Seleccionando encuentro predeterminado.")
        return jugadores[0], enemigos[0]

def mostrar_estado(turno, personaje):
    print(f"\n--- Ronda {turno}/1 ---")
    print(f"Turno {turno} - {personaje.nombre} ({type(personaje).__name__})")
    print(f"Vida: {personaje.vida}")

def sistema_turnos(jugadores, enemigos):
    for ronda in range(1, 2):
        personajes = jugadores + enemigos
        personajes.sort(key=lambda x: x.agilidad, reverse=True)

        for personaje in personajes:
            if isinstance(personaje, (Guerrero, Mago, Arquero, Asesino)):
                objetivo = random.choice(enemigos)
            else:
                objetivo = random.choice(jugadores)

            mostrar_estado(ronda, personaje)
            
            daño = personaje.atacar(objetivo)
            

            if hasattr(personaje, 'armas') and personaje.armas:
                print(f"{objetivo.nombre} tiene {objetivo.vida} de vida restante.")

    print("")


guerrero = Guerrero("Guerrero1", armas=[Espada(), Hacha()])
mago = Mago("Mago1", armas=[Vara(), Guantes()])
arquero = Arquero("Arquero1", armas=[Ballesta(), Arco()])
asesino = Asesino("Asesino1", armas=[Machete(), Cuchillo()])

bruja = Bruja("Bruja1")
ciclope = Ciclope("Ciclope1")
minotauro = Minotauro("Minotauro1")
hombre_cristal = HombreDeCristal("Hombre de Cristal1")

jugadores = [guerrero, mago, arquero, asesino]
enemigos = [bruja, ciclope, minotauro, hombre_cristal]

def sistema_encuentros(jugadores, enemigos):
    for encuentro in range(1, 5):
        input(f"\nPresiona Enter para comenzar el Encuentro {encuentro}")

        jugador, enemigo = seleccionar_rival(jugadores, enemigos)
        print(f"\n¡{jugador.nombre} vs {enemigo.nombre}!\n")

        sistema_turnos([jugador], [enemigo])

        if jugador.vida > 0:
            print(f"\n¡{jugador.nombre} ha ganado el Encuentro {encuentro}!\n")
        else:
            print(f"\n¡{jugador.nombre} ha sido derrotado por {enemigo.nombre} en el Encuentro {encuentro}!\n")
            break

sistema_encuentros(jugadores, enemigos)