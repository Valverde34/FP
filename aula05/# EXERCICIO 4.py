# EXERCICIO 4 

def is_isbn(isbn):
    if '-' in isbn:
        isbn = ''.join(isbn.split('-'))
    
    if (len(isbn) > 10) or (not isbn.isdigit() and (isbn[-1].upper() != 'X')):
        return False
        
    totalMult = 0
    for x in range(10, 0 , -1):
        if (x == 1) and (isbn[-1].upper() == 'X'):
            totalMult += 10
            continue
        totalMult += x * isbn[-x]
    
    return totalMult % 11 == 0