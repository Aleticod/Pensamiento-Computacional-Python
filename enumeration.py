# This code determinate if a number have a exact square 



def enumeration ():
    objetivo = int(input("Ingrese un numero entero: "))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene una raiz cudrada exacta")

def run():
    enumeration()


if __name__ == "__main__":
    run()
