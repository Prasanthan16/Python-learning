from random import randint

easy = 10
hard = 5


def checking_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high number.")
        return attempts - 1
    elif guess < answer:
        print("Too low number")
        return attempts - 1
    else:
        print(f"answer is correct. answer is {answer}")


def difficulty():
    level = input("choose the difficulty? 'easy' r 'hard'? ")
    if level == "easy":
        return easy
    else:
        return hard


def game():
    print("Welcome to the number guessing game")
    print("I'm thinking of number from 1 to 100")
    answer = randint(1, 100)
        
    attempts = difficulty()
    guess = 0
    while guess != answer:
        print(f"{attempts} attempts left to find the answer correctly..")
        guess = int(input("Make a Guess? "))
        attempts = checking_answer(guess, answer, attempts)
        if attempts == 0:
            print("no more attempts left. you lose")
            return
        elif guess != attempts:
            print("Guess again")


game()
