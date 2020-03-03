import json
import os

import constant


class Card:
    def __init__(self, info, parentDeck=None):
        self.info = info
        self.parentDeck = parentDeck

    def __str__(self):
        return self.info['name']

    def __repr__(self):
        return self.info['name']


if __name__ == '__main__':
    script_dir = os.path.dirname('..')
    abs_file_path = os.path.join(script_dir, constant.CARD_DB)
    with open(abs_file_path, "r") as read_file:
        card_raw = json.load(read_file)

    my_card = Card(card_raw[13])
    print(my_card)
