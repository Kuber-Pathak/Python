class Complex:
    def __init__(self, a, b):
        self.real = a
        self.img = b

    def __add__(self,c):
        return Complex(self.real + c.real,self.img + c.img)
    
    def __mul__(self,c):
        mulreal = self.real*c.real - self.img*c.img 
        mulimg = self.real*c.img + self.img*c.real 
        return Complex(mulreal,mulimg)
    
    def __str__(self):
        return f"{self.real} + {self.img}i"
    
c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1+c2)
print(c1*c2)
