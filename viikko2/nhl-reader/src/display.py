from rich.table import Table
from rich.console import Console

def print_player_table(player_list):
    console = Console()
    table = Table(title="Statistics")

    table.add_column("Name", justify="left", style="cyan")
    table.add_column("Teams", justify="left", style="magenta")
    table.add_column("Goals", justify="left", style="green")
    table.add_column("Assists", justify="left", style="green")
    table.add_column("Points", justify="left", style="green")
    
    for player in player_list:
        table.add_row(
            str(player.name),
            str(player.team),
            str(player.goals),
            str(player.assists),
            str(player.points)
        )
    
    console.print(table)