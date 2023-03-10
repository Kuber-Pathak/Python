class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self,n2):
        print("Lets add")
        return self.num + n2.num

    def __mul__(self,n2):
        print("Lets add")
        return self.num * n2.num
    
n1 = Number(2)
n2 = Number(3)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
