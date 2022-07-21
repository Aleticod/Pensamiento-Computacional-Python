def busqueda_binaria():
    objetivo = int(input("Escoge un numero entero: "))
    epsilon = 0.000000001
    limite_inferior = 0.0
    limite_superior = max(1.0, objetivo)
    respuesta = (limite_superior + limite_inferior) / 2
    while abs(respuesta ** 2 - objetivo) >= epsilon:
        if respuesta ** 2 < objetivo:
            limite_inferior = respuesta
        else:
            limite_superior = respuesta
        respuesta = (limite_superior + limite_inferior) / 2

    print(f"La raiz cuadrada aproximada es {respuesta}")


def run():
    busqueda_binaria()


if __name__ == '__main__':
    run()
