"""
Criar um jogo de blackjack

as cartas k, q e j valem 10
o às pode valer 11 ou 1
"""

from random import choice


def deal_card(deck):
    card = choice(deck)
    deck.remove(card)
    return card


def calculate_score(hand: list):
    total_score = sum(hand)
    if len(hand) == 2 and total_score == 21:
        return 0
    else:
        return total_score


def start_again():
    print("Do you want to play again?")
    user_answer = input("(y)es or (n)o: ")
    if user_answer == "y":
        return play()
    else:
        exit(0)


def check_score(user_score, dealer_score):
    if user_score == 0 or user_score == 21:
        print("You win!")
        start_again()
    elif dealer_score == 0 or dealer_score == 21:
        print("Dealer wins!")
        start_again()
    elif user_score > 21:
        print("You lose!")
        start_again()
    elif dealer_score > 21:
        print("You win!")
        start_again()


def play():
    play_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = [deal_card(play_deck) for _ in range(2)]
    dealer_hand = [deal_card(play_deck) for _ in range(2)]
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Player: {user_hand}")
    print(f"Dealer: [{dealer_hand[0]}, X]")

    check_score(user_score, dealer_score)

    while user_score < 21:
        print("Do you want to draw another card?")
        user_choice = input("(y)es or (n)o: ")
        if user_choice == "y":
            user_hand.append(deal_card(play_deck))
            user_score = sum(user_hand)
            if 11 in user_hand:
                if user_score > 21:
                    user_hand.remove(11)
                    user_hand.append(1)
                    user_score = sum(user_hand)
            print(f"Player: {user_hand}")
            print(f"Dealer: {dealer_hand}\n")
        else:
            break

    check_score(user_score, dealer_score)

    while dealer_score < 17:
        dealer_hand.append(deal_card(play_deck))
        dealer_score = sum(dealer_hand)
        if 11 in dealer_hand:
            if dealer_score > 21:
                dealer_hand.remove(11)
                dealer_hand.append(1)
                dealer_score = sum(dealer_hand)
        print(f"Dealer: {dealer_hand}")

    print(f"Player: {user_hand}")
    print(f"Dealer: {dealer_hand}")

    check_score(user_score, dealer_score)

    if user_score > dealer_score:
        print("You win!")
        start_again()
    elif user_score < dealer_score:
        print("Dealer wins!")
        start_again()
    else:
        print("It's a draw!")
        start_again()


play()
