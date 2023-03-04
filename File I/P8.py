with open(f"File I/Sample.txt") as f:
    content = f.read()

with open(f"File I/copy.txt", 'w') as f:
    f.write(content)