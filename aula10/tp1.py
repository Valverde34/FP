def unload(t, m, q):
    for stock in t[::-1]:
        if m == stock[0]:
            if q == stock[0]:
                t.remove(stock)
                return 0
                break
            elif q < stock[1]:
                s = stock[1] - q
                stock[1] -= q
            else:
                t.remove(stock)
                q -= stock[1]
    return q 