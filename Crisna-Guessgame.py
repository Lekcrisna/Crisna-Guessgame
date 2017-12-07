import random
# print("Guess a number between 1 and 50")
# response = ""
# while response != "50":
#     response = input("Say \"50\"")
print()

number = (random.randint(1, 50))
print(number)
guess = int(input("Guess a number between 1 and 50"))
if number == guess:
    print("You win")





# 1) generate a number
# 2)get a number (input) from the user
# 3)compare number to input
# 4)add "Higher" or "lower"
# 5)add 5 guesses

