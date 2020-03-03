import json
import os
import random

from mycard import *
import constant


class Deck:
    def __init__(self, id="1"):
        script_dir = os.path.dirname('..')
        abs_file_path = os.path.join(script_dir, f"db/deck/{id}.json")
        with open(abs_file_path, "r") as read_file:
            deck_raw = json.load(read_file)
        abs_file_path = os.path.join(script_dir, constant.CARD_DB)
        with open(abs_file_path, "r") as read_file:
            card_raw = json.load(read_file)
        deck_cards = deck_raw["slots"]
        self.id = id
        self.cards = []
        for card_id, card_num in deck_cards.items():
            for card_info in card_raw:
                if card_id == card_info["code"]:
                    for i in range(card_num):
                        self.cards.append(Card(card_info, self))
        self.shuffle()
        self.numCards = len(self.cards)

    def __str__(self):
        s = ""
        for card in self.cards:
            s = s + str(card) + "\n"
        return s

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):  # Fisher–Yates shuffle
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        self.numCards -= 1
        return self.cards.pop()


if __name__ == '__main__':
    my_deck = Deck()
    print(my_deck)
    print(my_deck.drawCard())