import constant
import os
import json

import chaosbag

class Scenario():
    def __init__(self, name = "The Gathering", parentCampaign=None, num_player = 1, difficulty = "easy"):
        self.name = name
        self.parentCampaign = parentCampaign
        self.num_player = num_player
        self.difficulty = difficulty
        self.chaosbag = chaosbag.ChaosBag()
        
        script_dir = os.path.dirname(os.path.dirname(__file__))
        abs_file_path = os.path.join(script_dir, constant.SCENARIOS_DB)
        with open(abs_file_path, "r") as read_file:
            scenario_raw = json.load(read_file)
        for loc in scenario_raw:
            if loc['name'] == name:
                self.location = loc
                break

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

class Location():
    def __init__(self, name = "Study"):
        pass
  
if __name__ == "__main__":
    mysenario = Scenario()