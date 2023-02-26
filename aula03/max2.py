def max2(x, y):
    if x > y: 
        return x
    else:
        return y

def max3(x, y, z):
    return max2(x, max(x,y))


def main():
    n1 = float(input("Valor para o primeiro número: "))
    n2 = float(input("Valor para o segundo número: "))

    print("O maior valor é: ", max2(n1, n2))

    n1 = float(input("Valor para o primeiro número: "))
    n2 = float(input("Valor para o segundo número: "))
    n3 = float(input("Valor para o terceiro número: "))

    print("O maior valor é: ", max3(n1, n2, n3))

main()

