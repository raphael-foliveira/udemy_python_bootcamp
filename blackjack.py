"""
Criar um jogo de blackjack

as cartas k, q e j valem 10
o às pode valer 11 ou 1
"""
from random import choice
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = choice(deck)
    return card


def calculate_initial_score(hand: list):
    total_score = sum(hand)
    if 11 in hand:
        if total_score == 21:
            return 0
    if 11 in hand:
        if total_score > 21:
            hand.remove(11)
            hand.append(1)
            total_score = sum(hand)
            return total_score
    return total_score


def start_again():
    print("Do you want to play again?")
    user_answer = input("(y)es or (n)o: ")
    if user_answer == "y":
        return play()
    else:
        exit(0)


def check_score(user_score, dealer_score):
    if user_score == 0:
        print("You win!")
        return start_again()
    elif dealer_score == 0:
        print("You lose!")
        return start_again()
    elif user_score == 21:
        print("You win!")
        return start_again()
    elif dealer_score == 21:
        print("You lose!")
        return start_again()
    elif user_score > 21:
        print("You lose!")
        return start_again()
    elif dealer_score > 21:
        print("You win!")
        return start_again()


def play():
    user_hand = [deal_card() for _ in range(2)]
    dealer_hand = [deal_card() for _ in range(2)]
    user_score = calculate_initial_score(user_hand)
    dealer_score = calculate_initial_score(dealer_hand)

    print(f"user_hand: {user_hand}")
    print(f"dealer_hand: {dealer_hand}")

    check_score(user_score, dealer_score)

    while user_score < 21:
        print("Do you want to draw another card?")
        user_choice = input("(y)es or (n)o: ")
        if user_choice == "y":
            user_hand.append(deal_card())
            user_score = sum(user_hand)
            if 11 in user_hand:
                if user_score > 21:
                    user_hand.remove(11)
                    user_hand.append(1)
                    user_score = sum(user_hand)
            print(f"Player: {user_hand}\n")
        else:
            break

    check_score(user_score, dealer_score)

    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = sum(dealer_hand)
        if 11 in dealer_hand:
            if dealer_score > 21:
                dealer_hand.remove(11)
                dealer_hand.append(1)
                dealer_score = sum(dealer_hand)
        print(f"Dealer: {dealer_hand}\n")

    print(f"Player: {user_hand}\n")
    print(f"Dealer: {dealer_hand}\n")

    check_score(user_score, dealer_score)

    if user_score > dealer_score:
        print("You win!")
        start_again()
    elif user_score < dealer_score:
        print("You lose!")
        start_again()
    else:
        print("It's a draw!")
        start_again()


play()




