print("Welcome To our guessing game")
guess = 0
while guess != 5:
    g = input("Guess the winning number: ")
    guess = int(g)
    if guess == 5:
        print('You win!')
    else:
        if guess > 5:
            print("Too high")
        else:
            print("Too Low")
print("Game Over")
