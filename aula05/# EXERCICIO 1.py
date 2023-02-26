# EXERCICIO 1

notaT = float(input("notaT? "))
while (0 > notaT) or (notaT > 20):
    print("Tem de estar em [0, 20]!")
    notaT = float(input("notaT? "))
    
notaP = float(input("notaP? "))
while (0 > notaP) or (notaP > 20):
    print("Tem de estar em [0, 20]!")
    notaP = float(input("notaP? "))

notaF = (notaT + notaP) / 2

classificacao = "REP"
if notaF >= 13:
    classificacao = "BOM"
elif notaF >= 9.5:
    classificacao = "SUF"

print("Nota final: {} {}".format(notaF, classificacao))



