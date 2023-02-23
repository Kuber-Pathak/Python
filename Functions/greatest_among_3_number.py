def greatest(a, b, c):
    if (a > b):
        if (b > c):
            return a
        else:
            return c
    else:
        if (b > c):
            return b
        else:
            return c


m = greatest(2, 33, 43)
print("The greatest value is " + str(m))
