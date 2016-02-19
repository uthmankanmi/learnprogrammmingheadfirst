from random import (randint)

print("Welcome To our guessing game")

guess = 0
secret = randint(1, 10)
while guess != secret:
    g = input("Guess the winning number: ")
    guess = int(g)
    if guess == secret:
        print('You win!')
    else:
        if guess > secret:
            print("Too high")
        else:
            print("Too Low")
print("Game Over")
