words = ["donkey", "gadha"]
with open(f"File I/Donkey.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "******")
    with open(f"File I/Donkey.txt", 'w') as f:
        f.write(content)