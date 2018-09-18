from structure import Player, Match
from contest import Contest
from utils import messages
from random import shuffle

class Swiss(Contest):

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

    def win_match(self, number, winner):
        self.matches[number].finish(winner)

    def print_players(self):
        for player in self.players:
            print("{} {}".format(player.get_name(), player.get_points()) )

    def next_round(self):
        new_match_table = [] 
        winners = []
        for match in self.matches:
            if(not match.ended):
                players = match.get_players()
                raise Not_Finished_Error("Match between " + players[0] + ", and " + players[1] + "is not ended" )
            else:
                match.get_winner().winner()
        
        table = {}
        
        for player in self.players:
            if player.get_points() in table:
                table[player.get_points()].append(player)
            else: 
                table[player.get_points()] = [player]
        
        new_matches = []
        for key in sorted(table.keys()):
            new_matches = new_matches + table[key]

        new_match_table = []
        stack_players= []

        for player in new_matches:
            stack_players.append(player)
            if(len(stack_players) is 2):
                new_match_table.append(Match(stack_players.pop(), stack_players.pop()))

        if len(stack_players) is not 0:
            print("Lonely wolfs")
            for player in stack_players:
                print(player.get_name())

        self.matches = new_match_table
        
        
        return True

    def print_matches(self):
        for idx,match in enumerate(self.matches):
            print("[{}]".format(idx))
            for player in match.get_players():
                if match.ended and player.get_name() == match.get_winner().get_name():
                    print(player.get_name() + "(W)")
                else:
                    print(player.get_name())
            print("")





