import json

class Libro:
    def __init__(self, nombre, autor, año, unidad):
        self.nombre = nombre
        self.autor = autor
        self.publicacion = año
        self.disponibilidad = True
        self.unidad = unidad
    def mostrar_libro(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"{self.nombre} / {self.autor} / {self.publicacion} / {estado}"
class Biblioteca:
    def __init__(self, nombre, archivo_json):
        self.nombre = nombre
        self.archivo_json = archivo_json
        self.libros = self.cargar_desde_json()
    def mostrar_libros(self):
        print(f"Libros en la biblioteca {self.nombre}:")
        for i, libro in enumerate(self.libros, start=1):
            print(f"{i}. {libro.mostrar_libro()}")
    def prestar_libro(self, num_libro):
        if 1 <= num_libro <= len(self.libros):
            libro = self.libros[num_libro - 1]
            if libro.disponibilidad:
                libro.disponibilidad = False
                print(f"Libro '{libro.nombre}' prestado con éxito.")
            else:
                print(f"Libro '{libro.nombre}' no disponible.")
        else:
            print("Número de libro no válido.")
    def devolver_libro(self, num_libro):
        if 1 <= num_libro <= len(self.libros):
            libro = self.libros[num_libro - 1]
            if not libro.disponibilidad:
                libro.disponibilidad = True
                print(f"Libro '{libro.nombre}' devuelto con éxito.")
            else:
                print(f"Libro '{libro.nombre}' ya disponible.")
        else:
            print("Número de libro no válido.")
    def agregar_libro(self, nuevo_libro):
        self.libros.append(nuevo_libro)
        self.guardar_en_json()
    def cargar_desde_json(self):
        try:
            with open(self.archivo_json, 'r') as file:
                libros_data = json.load(file)
                return [Libro(libro["name"], libro["author"], libro["year"], libro.get("unidad", 1)) for libro in libros_data]
        except FileNotFoundError:
            print(f"El archivo JSON '{self.archivo_json}' no existe. Se creará al guardar los cambios.")
            return []
    def guardar_en_json(self):
        with open(self.archivo_json, 'w') as file:
            libros_data = [
                {"name": libro.nombre, "author": libro.autor, "year": libro.publicacion, "unidad": libro.unidad}
                for libro in self.libros
            ]
            json.dump(libros_data, file, indent=2)
            print(f"Libro/s agregado/s al archivo JSON '{self.archivo_json}'.")
biblioteca_historia = Biblioteca("Historia", "historia.json")
biblioteca_biologia = Biblioteca("Biología", "biologia.json")
while True:
    print("""------- Menú Principal -------
1 - Acceder a Biblioteca de Historia
2 - Acceder a Biblioteca de Biología
3 - Salir""")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        while True:
            print("""------- Menú de historia -------")
1 - Mostrar libros
2 - Prestar libro
3 - Devolver libro
4 - Agregar libro
5 - Volver al menú principal""")
            accion = input("Seleccione una acción: ")
            if accion == "1":
                biblioteca_historia.mostrar_libros()
            elif accion == "2":
                num_libro = int(input("Seleccione el número del libro que desea prestar: "))
                biblioteca_historia.prestar_libro(num_libro)
            elif accion == "3":
                num_libro = int(input("Seleccione el número del libro que desea devolver: "))
                biblioteca_historia.devolver_libro(num_libro)
            elif accion == "4":
                nuevo_libro = Libro(
                    input("Ingrese el título del libro: "),
                    input("Ingrese el autor del libro: "),
                    input("Ingrese el año de publicación: "),
                    int(input("Ingrese la cantidad de unidades del libro: "))
                )
                biblioteca_historia.agregar_libro(nuevo_libro)
            elif accion == "5":
                break
            else:
                print("Opción no válida.")
    elif opcion == "2":
        while True:
            print("""-------Menú de Biologia-------")
1 - Mostrar libros
2 - Prestar libro
3 - Devolver libro
4 - Agregar libro
5 - Volver al menú principal""")
            accion = input("Seleccione una acción: ")
            if accion == "1":
                biblioteca_biologia.mostrar_libros()
            elif accion == "2":
                num_libro = int(input("Seleccione el número del libro que desea prestar: "))
                biblioteca_biologia.prestar_libro(num_libro)
            elif accion == "3":
                num_libro = int(input("Seleccione el número del libro que desea devolver: "))
                biblioteca_biologia.devolver_libro(num_libro)
            elif accion == "4":
                nuevo_libro = Libro(
                    input("Ingrese el título del libro: "),
                    input("Ingrese el autor del libro: "),
                    input("Ingrese el año de publicación: "),
                    int(input("Ingrese la cantidad de unidades del libro: "))
                )
                biblioteca_biologia.agregar_libro(nuevo_libro)
            elif accion == "5":
                break
            else:
                print("Opción no válida.")
    elif opcion == "3":
        print("Has salido!")
        break
    else:
        print("Opcion no válida.")