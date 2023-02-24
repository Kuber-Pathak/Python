with open(f"File I/Sample.txt") as f:
    content1 = f.read()

with open(f"File I/copy.txt", ) as f:
    content2 = f.read()

if content1 == content2:
    print("They are identical")
else:
    print("They are not identical")