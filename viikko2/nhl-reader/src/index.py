from rich.prompt import Prompt
from player import Player
from player_reader import PlayerReader
from statistics_service import PlayerStats
from display import print_player_table

def main():
    season = Prompt.ask("Season", choices=["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"], default="2024-25")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    
    while True:
        nationality = Prompt.ask(
            "Nationality",
            choices=["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK",
                    "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]
            )
        players = stats.top_scorers_by_nationality(nationality)
        print_player_table(players)


main()