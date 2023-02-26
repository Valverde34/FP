def filter_list(l):
    'return a new list with the strings filtered out'
    lst = []
    for i in l:
        if type(i) == int:
            lst.append(i)
    return lst

print(filter_list([1, 2, "abc"]))