#basic dictionary / key assignment
players = {
    "SS": "Correa",
    "2B": "Altuve",
    "3B": "Bregman",
    "DH": "Grattis",
    "OF": "Springer"
}

print(players)

second_base = players['2B']
designated_hitter = players['DH']

print(second_base)
print(designated_hitter)

# Dictionary object views
# print(players.items())
# player_names = list(players.copy().values()) => copies the list created from dict obj view 
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(list(players.items())[2])

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

print(len(team_groupings))


print(list(team_groupings)[1][1][0]) # =Trout