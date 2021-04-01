from art import logo, vs
from game_data import data
import random
import clear


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description},from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
continue_game = True
person_b = random.choice(data)

while continue_game:
    person_a = person_b
    person_b = random.choice(data)

    while person_a == person_b:
        person_b = random.choice(data)

    print(f"compare A: {format_data(person_a)}.")
    print(vs)
    print(f"compare B: {format_data(person_b)}.")

    guess = input("who has more follower? Type 'A' or 'B':").lower()
    a_follower_count = person_a["follower_count"]
    b_follower_count = person_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear

    if is_correct:
        score += 1
        print(f"its right. current score: {score}.")
    else:
        print(f"its wrong. final score: {score}.")
