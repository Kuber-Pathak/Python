class Employee:
    company_name= " visa "

class Freelancer:
    company = "Fiverr"

    def display(self):
        print(self.company)

class Programmer(Employee,Freelancer):
    name = "Ram"

p = Programmer()
print(p.company_name)
p.display()
