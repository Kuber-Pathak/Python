class Animals:
        animaltype = "Mammal"

class Pet(Animals):
        color = "Black"

class Dog(Pet):
    @staticmethod
    def Bark():
        print("Bow Bow!")

German = Dog()
German.Bark()
