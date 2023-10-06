def buscar_numero_en(numero, lista):

# Busca el numero @numero en la lista @lista
# Si lo encuentra devuelve la posición en la que se encontró su primera aparición
# Si no lo encuentra devuelve -1 

indice = -1
for i, item in enumerate(lista):
    if item == numero:
        indice = i
        break 
return indice

buscar_numero_en(1, [2,1,3,4,5])
buscar_numero_en(1, [2,6,3,4,5])


## EJERCICO SEMANA 4

def es_primo(numero):
    resultado = True
    
    for divisor in range (2, numero):
        if(numero % divisor ) == 0:
            resultado = False
    Break
    
    return resultado


## cuestionario semana 4


s= 0

for n in range (1,10):
    if n%2 != 0:
    continue;
    s+=n
    
else:
    s+=5
    
    
    