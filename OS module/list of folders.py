import os

folders = os.listdir("OS module/data")

for folder in folders:
    print(folder)
    print(os.listdir(f"OS module/data/{folder}"))
