def sum_recursion(n):
    if (n == 1):
        return 1
    if (n == 0):
        return 0
    return n+sum_recursion(n-1)


num = 3
sum = sum_recursion(num)
print("The sum of first", num, "natural number is "+str(sum))
