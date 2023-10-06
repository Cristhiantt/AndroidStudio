import random

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    
    
    print(dado1)
    print(dado2)
    
    return input("¿Desea tirar los dados de nuevo? si/no: ").lower()

tirar_dados = "si"
while tirar_dados == "si":
    tirar_dados = dados()

print("Fin programa.")