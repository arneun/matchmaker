from structure import Player, Match
from contest import Contest
from utils import messages
from random import shuffle

class Tournament(Contest):

    def __init__(self, player_names):
        self.players = []
        self.matches = []
        for name in player_names:
            self.players.append(Player(name))

        shuffle(self.players)
        stack_players = []
        
        for player in self.players:
            stack_players.append(player)
            if(len(stack_players) is 2):
                    self.matches.append(Match(stack_players.pop(), stack_players.pop()))

    def get_round(self):
        return self.matches

    def next_round(self):
        new_match_table = [] 
        winners = []
        for match in self.matches:
            if(not match.ended):
                players = match.get_players()
                raise Not_Finished_Error("Match between " + players[0] + ", and " + players[1] + "is not ended" )
            else:
                winners.append(match.get_winner())
                if(len(winners) is 2):
                    new_match_table.append(Match(winners.pop(),winners.pop()))
        self.matches = new_match_table
        return True


           

