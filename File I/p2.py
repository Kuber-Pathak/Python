def game():
    return 88


score = game()
with open(f"File I/Hiscore.txt") as f:
    hiscoreStr = f.read()

if hiscoreStr == '':
    with open(f"File I/Hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiscoreStr) < score:
    with open("Hiscore.txt", "w") as f:
        f.write(str(score))