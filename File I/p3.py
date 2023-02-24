with open(f"File I/Donkey.txt") as f:
    content = f.read()

content = content.replace("donkey", "******")

with open(f"File I/Donkey.txt", 'w') as f:
    f.write(content)
