import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(person_score, comp_score):
    """to compare the computer score and person score"""
    if person_score == comp_score:
        return "EQUAL"
    elif comp_score == 0:
        return "you lose, opponent win"
    elif person_score == 0:
        return "You Win"
    elif person_score > 21:
        return "you crossed the total, you lose."
    elif comp_score > 21:
        return "opposite player won"
    elif person_score > comp_score:
        return "you win"
    else:
        return "you lose"


def play_again():
    global comp_score, person_score
    person_cards = []
    computer_cards = []
    game_ends = False

    for _ in range(2):
        new_card = deal_card()
        person_cards.append(new_card)
        computer_cards.append(new_card)

    while not game_ends:

        person_score = calculate_score(person_cards)
        print(f"person cards{person_cards}, person_score{person_score}")
        comp_score = calculate_score(computer_cards)
        print(f"computer cards {computer_cards [0]}")

        if person_score == 0 or comp_score == 0 or person_score > 21:
            game_ends = True
        else:
            person_draw_card = input("do you want another card y or no?").lower()
            if person_draw_card == "y":
                person_cards.append(deal_card())
            else:
                game_ends = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f" person final card{person_cards}, final score{person_score}")
    print(f" computer final card{computer_cards}, final score{comp_score}")
    print(compare(person_score, comp_score))
