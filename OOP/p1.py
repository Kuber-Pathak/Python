class Programmer:
    comapny="Microsodft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfto(self):
        print(f"The name of programemr is {self.name} and the product is {self.product}")

harry = Programmer("Harry","skype")
alka=Programmer("Alka","Git")
harry.getInfto()
alka.getInfto()