

##fib (n) = fib (n-1) + fib (n-2)

##fib(0)=0
##fib(1)=1


def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
print ("El resultado es: ",fib(35))

