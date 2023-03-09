class Employee:
    company = "Microsoft"
    salary = 2500
    bonus = 400
   #totalSalary

    @property
    def totalsalary(self):
        return self.salary + self.bonus
    
    @totalsalary.setter
    def totalsalary(self , val):
        self.bonus = val - self.salary

e = Employee()
print(e.totalsalary)
e.totalsalary = 3000
print(e.salary)
print(e.bonus)
