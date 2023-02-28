class Employee:
    company = "Google"

    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
        print("Employee is created")
    def Getdata(self):
        print(f"The name of Employee is {self.name}. \nHis salary is {self.salary}.")


harry = Employee("sunima",10000)
harry.Getdata()