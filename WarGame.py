import random

cards = []


def generate_deck(suits=4, cards_type=13):

    for suite in range(suits):
        for card_type in range(1, cards_type + 1):
            cards.append(card_type)
    random.shuffle(cards)
    print(cards)
    return cards


def war_game(deck):

    player1_cards = deck[0:int(len(deck)/2)]
    player2_cards = deck[int(len(deck)/2):]
    player1_stash = []
    player2_stash = []

    i = 1
    while player1_cards and player2_cards:
        player1_card = player1_cards.pop()
        player2_card = player2_cards.pop()

        if player1_card == player2_card:

            player1_stash.extend([player1_card] + player1_cards[-2:])
            player1_cards = player1_cards[:-2]
            player1_cards.append(player1_stash.pop())

            player2_stash.extend([player2_card] + player2_cards[-2:])
            player2_cards = player2_cards[:-2]
            player2_cards.append(player2_stash.pop())

        elif player1_card > player2_card:
            player1_cards = [player1_card, player2_card] + player1_stash + player2_stash + player1_cards
            player1_stash = []
            player2_stash = []
        elif player1_card < player2_card:
            player2_cards = [player2_card, player1_card] + player2_stash + player1_stash + player2_cards
            player1_stash = []
            player2_stash = []

        print(f" iteration :{i}\nPlayer 1 remaining cards:{len(player1_cards)}\n"
              f"Player 2 remaining cards:{len(player2_cards)}")

        i += 1

    if len(player1_cards) == 0:

        print("player 2 has won")

    else:
        print("player1 has won")


deck_cards = generate_deck()
war_game(deck_cards)
