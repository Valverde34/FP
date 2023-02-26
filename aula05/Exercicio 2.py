def funcao(sub, lst):
    indexes = []
    for i in range(len(lst) - len(sub) + 1):
        if lst[i:i+len(sub)] == sub:
            indexes.append(i)
    return indexes
  
