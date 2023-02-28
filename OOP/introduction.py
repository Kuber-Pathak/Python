class Number:
    def add(self):
        return self.a + self.b


num = Number()
num.a = 5
num.b = 6
s=num.add()
print(s)