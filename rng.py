import random

i = random.randint(1,100)
guessed = False
guessc = 0

while not guessed:
    guess = input("Guess the number:")
    guessc = guessc + 1
    if int(guess) == i:
        guessed = True
        print(f'You did it in {guessc} tries!')
    elif int(guess) > i:
        print(f'The number is less than {guess}.')
    elif int(guess) < i:
        print(f'The number is greater than {guess}.')
