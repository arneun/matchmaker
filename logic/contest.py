

class Contest(object):
    def __init__(self, player_names):
        self.matches = []
        self.players = []
        
        register_players(player_names)
        

    def register_players(self, player_names):
        for name in player_names:
            self.players.append(Player(name))
    
    def get_round(self):
        pass

    def next_round(self):
        pass 

    def win_match(self, number, winner):
        self.matches[number].finish(winner)

    def end_round(self):
        for match in self.matches:
            if(not match.ended):
                players = match.get_players()
                raise Not_Finished_Error("Match between " + players[0] + ", and " + players[1] + "is not ended" )
            else:
                match.get_winner().winner()
        
    def print_players(self):
        for player in self.players:
            print("{} {}".format(player.get_name(), player.get_points()) )

    def check_finished_matches():
        for match in self.matches:
            if(not match.ended):
                players = match.get_players()
                raise Not_Finished_Error("Match between " + players[0] + ", and " + players[1] + "is not ended" )
            else:
                match.get_winner().winner()

    def print_matches(self):
        for idx,match in enumerate(self.matches):
            print("[{}]".format(idx))
            for player in match.get_players():
                if match.ended and player.get_name() == match.get_winner().get_name():
                    print(player.get_name() + "(W)")
                else:
                    print(player.get_name())
            print("")
    
    def assign_matches(self, players):
        stack_players= []
        new_match_table = []

        for player in players:
            stack_players.append(player)
            if(len(stack_players) is 2):
                new_match_table.append(Match(stack_players.pop(), stack_players.pop()))
        
        print_lonely(stack_players)
        return new_match_table
           
    def print_lonely(self, lonely)  
        if len(stack_players) is not 0:
            print("Lonely wolfs")
            for player in stack_players:
                print(player.get_name())
    


