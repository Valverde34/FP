import sys

dic = {}
def count(fname):
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        for line in f.read():
            for ch in line:
                if ch.isalpha():
                    ch = ch.islower()
                    if ch not in dic:
                        dic[ch] = 0
                    dic[ch] += 1

for c in sorted(dic.items()):
    print(c, dic[c])

count(sys.argv[1]) 

