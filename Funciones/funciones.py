def peso (masa, gravedad=9.8):
    "Fórmula de peso"
    return masa*gravedad

# Parámetros opcionales

print ("Peso en la tierra: ", peso(10))
print ("peso en la luna: ", peso(10, 1.63))

# Parámetros con palabras claves ( o argumentos nombrados)
print ("Peso en la luna: ", peso(10, gravedad = 1.63))
print ("Peso en la luna: ", peso(masa=10, gravedad = 1.63))
print ("Peso en la luna: ", peso(gravedad = 1.63, masa=10))

# Lista de parámetros

def suma_numeros (*args):
    "Suma los numeros pasados por parámetros"
    return sum(args)

print("6 + 7 + 8 =", suma_numeros(*[6,7,8]))
print("6 + 7 + 8 =", suma_numeros(6,7,8))

# Diccionarion de parámetros 
def imprimir_ticket (*args, **kwargs):
    "imprime el ticket de una compra"
    print ("Detalle Ticket")    
    for item, precio in kwargs.items():
        print(item, ":", precio)