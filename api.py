import json

def guardar_json(lista):

    with open("datos.json", "w") as f:
        json.dump(lista, f)


def leer_json():

    with open("datos.json", "r") as f:
        data = json.load(f)

    return data