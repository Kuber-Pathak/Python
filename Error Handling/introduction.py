a = input("Enter a number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid input!")

print("Some imp lines of code")