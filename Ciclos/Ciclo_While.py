def suma_n (n):
    " Suma los numeros del 1 a n"
    result = 0
    x = n
    while x > 0:
        result += x
        x -= 1
    return result
suma_n (5)


def Ciclo_infinito():
    "Imprime el # 1 infinitas veces"
    i = 1
    while i <= 10:
        print(i, end = " ")

Ciclo_infinito()
    