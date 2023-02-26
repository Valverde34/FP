import bisect

def possible_suffixes(words, prefix):
    start_index = bisect.bisect_right(words, prefix)
    end_index = bisect.bisect_left(words, prefix + chr(127))
    suffixes = set()
    for i in range(start_index, end_index):
        suffixes.add(words[i][len(prefix):len(prefix)+1])
    return suffixes

def main():
    with open("wordlist.txt", "r") as f:
        words = f.read().split()

    prefix = ""
    while True:
        prefix += input(f"Current prefix: {'None' if prefix == '' else prefix}\nAdd to prefix: ")
        suffixes = possible_suffixes(words, prefix)
        if suffixes:
            print("Possible suffixes:", suffixes)
        else:
            print("No words found with the prefix:", prefix)

main()

