
from tournament import Tournament


tournament = Tournament(["jeden", "dwa", "trzy", "cztery"])

for match in tournament.get_round():
    match.finish(match.get_players()[0].get_name())
 #   for player in match.get_players():
  #      print(player.get_name())
    
print(tournament.next_round())

print(tournament.get_round())

for match in tournament.get_round():
    print(match.get_players())
    for player in match.get_players():
        print(player.get_name())
 






