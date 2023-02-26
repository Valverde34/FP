import bisect

def find_word(fname):
    with open(fname, "r") as f:
        words = f.read().split()
    Iea = bisect.bisect_right(words, "ea")
    Ieb = bisect.bisect_left(words, "eb")
    total = Ieb - Iea
    return total

print(find_word("wordlist.txt"))
