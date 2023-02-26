def reverseDigits(value):
    return reverseAux(value, 0)

def reverseAux(value, acc):
    if value == 0:
        return acc
    else:
        return reverseAux(value // 10, acc * 10 + value % 10)

def main():
    print(reverseDigits(1234))
    print(reverseDigits(1234567890))

main()