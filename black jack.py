import random 

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose"
    elif user_score == 0:
        return "You win"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win"
    elif user_score > computer_score:
        return "You win"
    else: 
        return "You lose"


def start():
    state = True
    user_cards = []
    computer_cards = []
    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while state:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            state = False
        elif input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            user_cards.append(deal_card())
        else:
            state = False
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  start()