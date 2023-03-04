content = True
i = 0
with open(f"File I/Sample.txt") as f:
    while content:
        i += 1
        content = f.readline()

        if 'python' in content.lower():
            print(f"Yes,python is present in line number is {i}")
