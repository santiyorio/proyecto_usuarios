from usuario import Usuario
import database
import api


def main():

    database.crear_db()

    lista = []

    while True:

        print("1 - Agregar usuario")
        print("2 - Mostrar DB")
        print("3 - Guardar JSON")
        print("4 - Leer JSON")
        print("5 - Salir")

        op = input("Opcion: ")

        if op == "1":

            nombre = input("Nombre: ")
            edad = int(input("Edad: "))

            u = Usuario(nombre, edad)

            lista.append({
                "nombre": nombre,
                "edad": edad
            })

            database.insertar(nombre, edad)

        elif op == "2":

            database.mostrar()

        elif op == "3":

            api.guardar_json(lista)

        elif op == "4":

            print(api.leer_json())

        elif op == "5":
            break


if __name__ == "__main__":
    main()