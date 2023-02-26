def open_or_senior(data):
    lst = []
    for (age, handicap) in data:
        if age >= 55 and handicap > 7:
            return lst.append("Senior")
        else:
            return lst.append("Open")
    return lst

print(open_or_senior([(18,20), [55,9]]))