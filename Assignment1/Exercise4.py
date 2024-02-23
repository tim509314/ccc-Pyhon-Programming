import random

min = 1
max = 20

intRandNum = random.randint(min, max)
intUserInput = 0
time = 0
""" print("The answer is: ", intRandNum) """

def guessNum():
    global intUserInput
    while True:
        try:
            intUserInput = int(input("Please type a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


while intUserInput != intRandNum:
    guessNum()
    if min <= intUserInput <= max:
        if intUserInput < intRandNum:
            print("The number is smaller than answer.")
        elif intUserInput > intRandNum:
            print("The number is larger than answer.")
        time += 1
    else:
        print("Please type a number between {min} and {max}.")
    
print("Good job! You guessed my number in {time} guesses!")