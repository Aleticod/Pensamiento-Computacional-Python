def binary(binary_num: str) -> float:
    """
    Devuelve un numero decimal a partir de un numero decimal

    param binary_num string: un cadena de texto que contenga los numeros despues del punto flotante

    return suma float: el resultado de convertir un numero binario de punto flotante a decimal
    """

    suma = 0.0
    pos = 1

    for bit in binary_num:
        if bit == '1':
            suma += round(1 / (2 ** pos), 10)
        pos += 1
    return round(suma, 10)


def run():
    # Ingrese solo los bits despede del punto
    binary_num = input('Give me the binary num: ')

    result = binary(binary_num)
    print(f'{binary_num} es {result} en decimal')


if __name__ == '__main__':
    run()
