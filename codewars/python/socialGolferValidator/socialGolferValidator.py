
#! this one i failed!
#! incomplete, missing a few cases

def valid(a):
    def check_games(day):  # for all days after first
        today = []  # a list to track players played today
        if len(day) != games_per_day:  # if nubmer of games changed
            return True
        for game in day:
            if check_if_played_together(game):
                return True
            if len(game) != players_per_game:  # amount of players in game stays same
                return True
            for player in game:
                if player in today:  # checking for a player playing twice
                    return True
                elif player not in players:  # checking for a new player who didn't play before
                    return True
                else:
                    today.append(player)

    def check_if_played_together(game):
        i = 0
        while i < len(game)-1:
            player = game[i]
            i += 1
            other_players = game[i:]
            played_games = list(filter(lambda x: player in x, all_games))
            for other in other_players:
                for played in played_games:
                    if other in played:  # check if player from this game played with the current player before
                        return True
        all_games.append(game)

    players = []  # a list to track all players
    all_games = []  # a list to track all combos of players (ordered)
    first_day = a[0]
    players_per_game = len(a[0][0])
    games_per_day = len(a[0])
    for game in first_day:  # making a player list from the first day
        if check_if_played_together(game):
            return False
        if len(game) != players_per_game:  # amount of players in game stays same
            return False
        for player in game:
            if player in players:  # checking for a player playing twice
                return False
            else:
                players.append(player)

    for day in a[1:]:
        if check_games(day):
            return False

    return True


'''
checks ->
amount of players in game is same ->
    game.len == first_game.len
playin once a day ->
    not playing twice -> keep a list of cur day
    not missing a day -> keep a list of 1st day, keeping ammount of games in day (if it stays the same and no new player THEN all players played that day)
playing new players ->
    not playing a player played before ->
        list of all all_games (ordered) ->
            for each player scan through all games that include said player ->
                check if other players in this current player's game are in said games
'''


s = [["ABC", "DEF"], ["ADE", "CBF"]]
print(valid(s))
