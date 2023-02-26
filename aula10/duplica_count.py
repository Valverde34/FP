def duplicate_count(text):
    text = text.lower()
    digits = {}
    letters = {}
    for i in text:
        if i.isdigit():
            if i in digits:
                digits[i] += 1
            else:
                digits[i] = 1
        else:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    return len([i for i in digits if digits[i] > 1]) + len([i for i in letters if letters[i] > 1])
    