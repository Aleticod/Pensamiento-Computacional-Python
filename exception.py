
def division_list(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

def run():
    objeto = list(range(10))
    divisor = 0

    print(division_list(objeto, divisor))


if __name__ == '__main__':
    run()
