def factorial(n: int) -> int:
    """
    Calcula el factorian de un numero n

    param n int, es un numero entero mayor que 0

    returns el factorial de numero n
    """

    # Primero se inicia con el caso base
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def run():
    numero = int(input("Ingrese un numero positivo: "))
    print(f'El factoria de {numero} es {factorial(numero)}')


if __name__ == '__main__':
    run()
