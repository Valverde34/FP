def primesUpTo(n):
    numbers = list(range(2, n+1))
    primes = set()                      #já faz parte da próxima matéria
    while len(numbers) > 0:
        p = numbers[0]
        primes.add(p)
        for i in range(p, n+1, p):
            if i in numbers:
                numbers.remove(i)
    return primes

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

