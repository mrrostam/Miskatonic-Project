import json
import os
from collections import OrderedDict

import chaosbag
from deck import *
import constant
import scenarios


class Player:
    def __init__(self, name="Player", investigator="Roland Banks", deck="1"):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, constant.INV_DB)
        with open(abs_file_path, "r") as read_file:
            inv_list = json.load(read_file)
        for inv in inv_list:
            if inv['name'] == investigator:
                self.investigator = inv
                break
        abs_file_path = os.path.join(script_dir, f"db/deck/{deck}.json")
        with open(abs_file_path, "r") as read_file:
            deck = json.load(read_file)

        self.deck = Deck()
        self.resource = constant.INIT_RES
        self.Exhausted = False
        self.hand = []
        for i in range(constant.INIT_HAND):
            self.draw()

    def showHand(self):
        print(self.hand)

    def getData(self, s='name'):
        return self.investigator[s]

    def draw(self):
        self.hand.append(self.deck.drawCard())

    def gainResource(self):
        self.resource += 1
        return self.resource

    def engage(self):
        pass

    def investigate(self):
        pass

    def move(self):
        pass

    def play(self):
        pass

    def evade(self):
        pass

    def fight(self):
        pass

    def skillTest(self, test_type, difficulty, chaos_bag):
        token = str(chaos_bag.get_token()[0])
        if (token == "Skull"):
            modified_skill_value = self.investigator[test_type] + 0
        elif (token == "Cultist"):
            modified_skill_value = self.investigator[test_type] + 0
        elif (token == "Elder Thing"):
            modified_skill_value = self.investigator[test_type] + 0
        elif (token == "Tablet"):
            modified_skill_value = self.investigator[test_type] + 0
        elif (token == "Tentacles"):
            modified_skill_value = 0
        elif (token == "Elder Sign"):
            modified_skill_value = self.investigator[test_type]
        else:
            modified_skill_value = self.investigator[test_type] + int(token)
        if modified_skill_value >= difficulty:
            return token, 0
        else:
            return token, -1

    @property
    def location(self):
        return self.location


if __name__ == '__main__':
    player1 = Player()
    chaos = chaosbag.ChaosBag()
    print(player1.getData())
    player1.showHand()
    print(player1.gainResource())
    print(player1.skillTest("skill_intellect", 3, chaos))