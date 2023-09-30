from typing import Any


class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):  #to display name as module
        return f"the name of the employee is:{self.name} "

    def __repr__(self):  #to display name as module if there is not str
        return f" employee is:({self.name}) "

    def __call__(self, ):
        print("hey i am good")