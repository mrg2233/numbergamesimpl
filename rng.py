import random

i = random.randint(1,100)
guessed = False
guessc = 0

while not guessed:
    guess = int(input("Guess the number: "))
    guessc = guessc + 1
    if guess == i:
        guessed = True
        print(f'You did it in {guessc} tries!')
    elif guess > i:
        print("The number is less than", + guess)
    elif guess < i:
        print("The number is greater than", + guess)
