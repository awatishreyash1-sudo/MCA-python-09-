correct = 50

while True:
    guess = int(input("Enter your guess: "))

    if guess > correct:
        print("Too High")
    elif guess < correct:
        print("Too Low")
    else:
        print("Correct Guess!")
        break