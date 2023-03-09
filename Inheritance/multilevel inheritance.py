class Person:
    country = "Nepal"

    def takebreak(self):
            print("i am on break..")
    

class Employee(Person):
    company = "Tesla"

    def getSalary(slef):
        print(f"salary is 5000")

class Programmer(Employee):
     company_name = "Fiver"

     def salary(self):
          print("No salary for programmer")


p = Programmer()
p.takebreak()
p.getSalary()
p.salary()