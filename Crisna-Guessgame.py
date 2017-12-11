import random

print(random.randint(1,50))
number = (random.randint(1,50))
guess = "0"
guesses = 0

while int(guess) != number and guesses < 5:
    guess = input("What is your guess?")
    if guess == str(number):
        print("Correct.")
    elif(int(guess) >= number):
        print("Lower.")
    elif(int(guess) >= number):
        print("Higher")
        guesses += 1
if guesses >= 5:
        print("Goodbye.")


# 1) generate a number
# 2)get a number (input) from the user
# 3)compare number to input
# 4)add "Higher" or "lower"
# 5)add 5 guesses

