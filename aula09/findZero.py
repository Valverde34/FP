import math

def findZero(func, a, b, tol):
    if func(a) * func(b) > 0:
        print("Não existe uma raíz real no intervalo especificado!")
        return None
    if func(a) == 0:
        return a
    if func(b) == 0:
        return b
    while abs(b - a) > tol:
        c = (a + b) / 2
        if func(c) == 0:
            return c 
        if func(a) * func(c) > 0:
            a = c
        else:
            b = c
    return (a + b) / 2

def main():
    funct = lambda x: x + math.sin(10*x)
    print(findZero(funct, 0.2, 0.4, 0.001))

main()
