def lastName(fname):
    dic = {}
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.split()
            if line[-1] not in dic:
                dic[line[-1]] = line[0]
            else:
                dic[line[-1]] += " " + line[0]
    return dic

def main():
    print(lastName("names.txt")) 

if __name__ == "__main__":
    main()
