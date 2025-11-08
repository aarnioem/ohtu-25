import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")

    finns = []

    for player in players:
        if player.nationality == "FIN":
            finns.append(player)
    
    sorted_finns = sorted(finns, key=lambda player: (player.points, player.goals), reverse=True)
    for player in sorted_finns:
        print(player)

main()