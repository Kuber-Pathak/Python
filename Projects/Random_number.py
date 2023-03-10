import random
randNumber = random.randint(1, 100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Guess the correct number: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("Projects/hi_score.txt","r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("Projects/hi_score.txt","w") as f:
        f.write(str(guesses))