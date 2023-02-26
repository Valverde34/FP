def leibnizPi4(n):
    val = 0
    while n >= 0:
        val += ((-1)**n) / ((2*n) + 1)
        n -= 1
    return val

n = int(input("Quantidade de termos a somar: "))

print(leibnizPi4(n))
