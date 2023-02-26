import sys

def file_histogram(filename):
    histogram = []

    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            for character in line:
                if character.isalpha():
                    character = character.lower()
                    if character not in histogram:
                        histogram[character] = 1 
                    else: 
                        histogram[character] += 1
    return histogram

print(file_histogram(sys.argv[1]))