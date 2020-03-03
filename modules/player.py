import json
import os
from collections import OrderedDict

import chaosbag
import mydeck
import constant
import scenarios


class Player:
    def __init__(self, name="Player", investigator="Roland Banks", deck="1", parentScenario=None):
        script_dir = os.path.dirname('..')
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
        self.parentScenario = parentScenario
        self.deck = mydeck.Deck()
        self.resource = constant.INIT_RES
        self.Exhausted = False
        self.hand = []
        for _ in range(constant.INIT_HAND):
            self.draw()

        self._damage = 0
        self._horror = 0

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
        scenario_token_list = ["Skull" , "Cultist" , "Elder Thing" , "Tablet"]
        print(token)
        if token in scenario_token_list:
            success, modified_skill_value = self.parentScenario.scenarioToken(self, token, test_type, difficulty)
        elif (token == "Tentacles"):
            success, modified_skill_value = -1, 0
        elif (token == "Elder Sign"):
            success, modified_skill_value = self.investigatorToken()
        else:
            modified_skill_value = self.investigator[test_type] + int(token)
            if modified_skill_value >= difficulty:
                success = 0
            else:
                success = -1
        return token, success

    def investigatorToken(self):
        return 1, 00

    def location(self):
        return self.location

    @property
    def horror(self):
        return self._horror

    @property
    def damage(self):
        return self._damage

    @horror.setter
    def horror(self, value):
        if value >= self.investigator["sanity"]:
            print("You are dead!")
            self._horror = value
        else:
            self._horror = value

    @damage.setter
    def damage(self, value):
        if value >= self.investigator["health"]:
            print("You are dead!")
            self._damage = value
        else:
            self._damage = value


if __name__ == '__main__':
    player1 = Player()
    chaos = chaosbag.ChaosBag()
    print(player1.getData())
    player1.showHand()
    print(player1.gainResource())
    print(player1.skillTest("skill_intellect", 3, chaos))
