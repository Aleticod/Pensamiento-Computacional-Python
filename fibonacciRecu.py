def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def run():
    numero = int(input('Ingrese un numero positivo: '))

    for i in range(numero + 1):
        print(f'Elemento {i} de la serie es {fibonacci(i)}')


if __name__ == '__main__':
    run()
