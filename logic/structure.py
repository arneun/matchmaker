from utils import messages


class Tree(object):
    def __init__(self): 
        self.matches = []
        self.trees = []

    def get_trees():
        return self.trees

    def get_players():
        players = []
    
        for match in self.matches:
            players.add(match.get_players())

        for tree in self.trees:
            players.add(tree.get_players())
        return players


class Player:
    
    def __init__(self, player_name=None):
        self.name = player_name
        self.points = 0 # should be used only in swiss system
                
    def winner(self):
        self.points = self.points + 1

    def get_points(self):
        return self.points

    def get_name(self):
        return self.name

class Match(object): 

    def __init__(self, player_one, player_two):
        self.players = (player_one, player_two)
        self.ended = False
        self.winner= Player()

    def finish(self, player_name):
        self.ended = True
        if( player_name == self.players[0].get_name()):
            self.winner = self.players[0]
        elif (player_name == self.players[1].get_name()):
            self.winner = self.players[1]
        else: 
            raise Not_Playing_Error(player_name + " is not a player in match")

    def get_winner(self):
        return self.winner

    def get_players(self):
        return self.players


    

    

