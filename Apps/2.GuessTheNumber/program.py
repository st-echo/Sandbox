import random
from typing import Any, Union

print('-----------------------------------------------------------------')
print('                    Guess The Number')
print('-----------------------------------------------------------------')
print()

the_number: Union[int, Any] = random.randint(0, 100)
guess = -1

name = input("Please enter your name to get started: ")

while guess != the_number:
    guess = int(input("Guess a number between 0 and 100: "))  # This is useful

    if guess < the_number:
        print("Sorry {}, your entry of {} is TOO LOW. Guess again.".format(name, guess))
    elif guess > the_number:
        print("Sorry {}, your entry of {} is TOO HIGH. Try again.".format(name, guess))
    else:
        print("{} is CORRECT!".format(guess))

print("Wow {}, you guessed correctly!".format(name))
