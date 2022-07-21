# In this code we will calculate a square aproximation of a number

def aproximation():
    objetivo = int(input("Escoje un numero: "))
    epsilon = 0.01
    paso =  epsilon ** 2
    respuesta = 0.0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    print(f"La raiz cuadrada aproximada de {objetivo} es {respuesta}")

    
def run():
    aproximation()


if __name__ == "__main__":
    run()
    


