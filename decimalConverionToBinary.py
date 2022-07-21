def decimal_convert(num_decimal: float) -> str:
    binary_num = '0.'
    for i in range(20):
        product = num_decimal * 2
        if product < 1.0:
            binary_num += '0'
            num_decimal = product
        else:
            binary_num += '1'
            num_decimal = product - 1.0
    return binary_num


def run():
    # Ingremos por consola un numero decimal flotante
    float_decimal = float(input('Ingrese un nuemro decimal: '))
    result = decimal_convert(float_decimal)
    print(f'El numero {float_decimal} en binario es {result}')


if __name__ == '__main__':
    run()
