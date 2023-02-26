def countDown(N):
    while N > 0:
        N -= 1
        print(N)

def main():
    num = int(input("Insira um número positivo --> "))
    print(num)
    countDown(num)

main()

