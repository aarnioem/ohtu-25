from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        country_players = []
        for player in self.players:
            if player.nationality == nationality:
                country_players.append(player)
        
        result = sorted(country_players, key=lambda player: (player.points, player.goals), reverse=True)
        return result