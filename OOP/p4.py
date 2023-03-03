class Calculator:
    def __init__(self,num):
        self.number =num
    
    @staticmethod
    def Greet():
        print("*****Hello welcome to my calculator*****")
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} square is {self.number**3}")

a=Calculator(9)
a.Greet()
a.square()
a.squareRoot()
a.cube()
