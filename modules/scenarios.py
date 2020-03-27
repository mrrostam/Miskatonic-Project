import constant
import os
import json

import chaosbag

class Location():
    def __init__(self, info, parentScenario):
        self.info = info
        self.parentScenario = parentScenario
        self.shroud = info["shroud"]
        self.clues = info["clues"]*self.parentScenario.num_player

class Agenda():
    pass

class Act():
    pass


class Scenario():
    def __init__(self, name = "The Gathering", parentCampaign=None, num_player = 2, difficulty = "easy"):
        self.name = name
        self.parentCampaign = parentCampaign
        self.num_player = num_player
        self.difficulty = difficulty
        self.chaosbag = chaosbag.ChaosBag()
        self.scenario_card = None
        self.agenda = []
        self.act = []
        self.location = []
        script_dir = os.path.dirname(os.path.dirname(__file__))
        abs_file_path = os.path.join(script_dir, constant.SCENARIOS_DB)
        with open(abs_file_path, "r") as read_file:
            scenario_raw = json.load(read_file)
        for scenario_card in scenario_raw:
            if scenario_card["encounter_name"] == name:
                if scenario_card["type_name"] == "Scenario":
                    self.scenario_card = scenario_card
                elif scenario_card["type_name"] == "Agenda":
                    self.agenda.append(scenario_card)
                elif scenario_card["type_name"] == "Act":
                    self.act.append(scenario_card)
                elif scenario_card["type_name"] == "Location":
                    self.location.append(Location(scenario_card, self))
        self.setup()

    def setup(self):
        pass

    def scenarioToken(self, player, token , test_type, difficulty):
        enemy = 1
        X = enemy #player.location.enemy
        if (token == "Skull"):
            modified_skill_value = player.investigator[test_type] - X
            if modified_skill_value >= difficulty:
                success = 0
            else:
                success = -1
        elif (token == "Cultist"):
            modified_skill_value = player.investigator[test_type] - 1
            if modified_skill_value >= difficulty:
                success = 0
            else:
                success = -1
                player.horror += 1
        elif (token == "Tablet"):
            modified_skill_value = player.investigator[test_type] - 2
            if enemy != 0:
                player.damage += 1
            if modified_skill_value >= difficulty:
                success = 0
            else:
                success = -1
                player.horror += 1            
        return success, modified_skill_value
  
if __name__ == "__main__":
    mysenario = Scenario()
    print(mysenario.location[3].clues)