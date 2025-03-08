import random


def construct_deck():
    suits = ["H", "D", "C", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append({"suit": suit, "rank": rank})
    return deck


def shuffle_deck(deck: list):
    random.shuffle(deck)
    return deck
