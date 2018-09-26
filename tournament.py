from structure import Player, Match
from contest import Contest
from utils import messages
from random import shuffle

class Tournament(Contest):

    def __init__(self, player_names):
        super().__init__(player_names)

        shuffle(self.players)
        
        self.matches = assign_matches(players)

    def get_round(self):
        return self.matches

    def next_round(self):
        try:
            check_finished_matches()
        except Not_Finished_Error:
            return False
        
        self.matches = assign_matches(self.get_winners())
        
        return True
    
    def get_winners(self):
        winners = []
        for match in self.matches:
            winners.append(match.get_winner())
        return winners

