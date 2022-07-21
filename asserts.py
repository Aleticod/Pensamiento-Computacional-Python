
def primeras_letras(lista_palabras):
    first_letters = []

    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es un string'
            assert len(palabra) > 0, 'No se permite strings vacios'
            
            first_letters.append(palabra[0])
        except AssertionError as e:
            print(e)

    return first_letters


def run():
    palabras = ['hola', 'que', 'estas', 'haciendo', '', 5]

    print(primeras_letras(palabras))


if __name__ == '__main__':
    run()
