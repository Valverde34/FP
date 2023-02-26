def mdc(a, b):
    r = a % b 
    if r == 0:
        return b
    else: 
        return mdc(b, r)

def main():
    print("Este programa calcula o máximo deivisor comum entre dois números inteiros.")
    n1 = int(input("Número 1 --> "))
    n2 = int(input("Número 2--> "))
    
    print("O Máximo Divisor Comum de {} e {} é:".format(n1, n2), mdc(n1, n2))

if __name__ == "__main__":
    main()