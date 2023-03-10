class Employee:
    salary = 1000
    increament = 1.5

    @property
    def SalaryAfterIncreament(self):
        return self.salary*self.increament
    
    @SalaryAfterIncreament.setter
    def SalaryAfterIncreament(self, sai):
        self.increament = sai/self.salary

e = Employee()
print(e.SalaryAfterIncreament)

print(e.increament)
e.SalaryAfterIncreament = 3000
print(e.increament)