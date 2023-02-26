# EXERCICIO 3 

def funcao(lst):
    max = []
    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i] > lst[i + 1]:
            max.append(i)
    return max
