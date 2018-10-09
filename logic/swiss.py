from structure import Player, Match
from contest import Contest
from utils import messages
from random import shuffle

class Swiss(Contest):

    def __init__(self, player_names):
        super().__init__(player_names)
        
        shuffle(self.players)
        
        matches = assign_matches(players)

    def get_round(self):
        return self.matches

    
    def next_round(self):
        try:
            check_finished_matches()
        except Not_Finished_Error:
            return False
        
        table = give_points()
        
        self.matches = assign_matches(table)
        return True

    
    
    
    def sort_players(self, table):
        players = []
        
        for key in sorted(table.keys()):
            players = players + table[key]
        
        return players


    def give_points(self):
        table = {}
        for player in self.players:
            if player.get_points() in table:
                table[player.get_points()].append(player)
            else: 
                table[player.get_points()] = [player]
        return sort_players(table)


   



