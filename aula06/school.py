# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            data = line.split("\t")
            tuple = (int(data[0]), data[1], float(data[5]), float(data[6]), float(data[7]))
            lst.append(tuple)   
        
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    return sum(reg[2:]) / 3

# c) Crie a função printPauta aqui...
def printPauta(lst, filename=""):
    text = f'{"Numero":>6} {"Nome":^50} {"Nota":>4}\n'
    for data in lst:
        text += f"{data[0]:>6} {data[1]:^50} {notaFinal(data):>4.1f}\n"
    print(text)
    with open(filename, "w") as f:
        f.write(text)


# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    printPauta(lst, filename="schooldata.txt")


# Call main function
if __name__ == "__main__":
    main()
