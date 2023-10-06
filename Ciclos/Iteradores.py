lista = [1,2,3]
it = iter(lista)
it
next(it)
next(it)
next(it)
next(it)

class iterator:
    """
        Iterador que devuelve los elementos de 
        las posiciones pares de una lista
    """
    
    def __init__(self, data):
        self.data = data
        self.indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice >= len(self.data):
            raise StopIteration
        elem = self.data[self.indice]
        self.indice += 2
        return elem
    
it = iterator([])
for e in it:
    print(e)
    
it = iterator([1])
for e in it:
    print(e)
    
it = iterator([1,2])
for e in it:
    print(e)
    
it = iterator([1,2,3,4,5,6])
for e in it:
    print(e)



# EJERCICIO 1 SEMANA 5

class SumaDos:
    
    def __init__(self, datos):
        self.datos  = datos
    self.indice = 0
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self.indice == len(self.datos):
    raise StopIteration()
    elemento = self.datos[self.indice]+2
    self.indice += 1
    return elemento

SumaDos([1,2,3,4,5])