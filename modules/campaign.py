import constant
import os
import json
import chaosbag
import scenarios

import player

class Campaign():
    def __init__(self, name = "Night of the Zealot", players_list = None, difficulty_level = "easy"):
        script_dir = os.path.dirname(os.path.dirname(__file__))
        abs_file_path = os.path.join(script_dir, constant.CAMPAIGN_DB)
        with open(abs_file_path, "r") as read_file:
            campaign_list = json.load(read_file)
        for campaign in campaign_list:
            if campaign['name'] == name:
                self.campaign = campaign
                break
        self.players = players_list
        self.difficulty_level = difficulty_level
        tokens = []
        for key, value in self.campaign['chaos_bag'][difficulty_level].items():
            tokens.append((key, value))
        self.chaos_bag = chaosbag.ChaosBag(tokens)
        
    def add_player(self):
        pass

if __name__ == "__main__":
    campaign_name = "Night of the Zealot"
    player1 = player.Player("player", "Roland Banks", 1, scenarios)
    players = [player1]
    my_campaign = Campaign(campaign_name, players, 'easy')
    print(my_campaign.chaos_bag)