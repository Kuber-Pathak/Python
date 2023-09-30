import os
if (not os.path.exists("data")):
    os.mkdir("OS module/data")

for i in range(0, 100):
    os.mkdir(f"OS module/data/Day{i+1}")