class Number:
    def __init__(self, num):
        self.num = num
    
    def __str__(self):     #str dunder method
        return f"Decimal Number: {self.num}"
    
    def __len__(self):       #len dunder method
        return 1
    
n1 = Number(2)
print(n1)
print(len(n1))
