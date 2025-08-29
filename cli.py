
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import board

console = Console()

def show_welcome():
    console.clear()
    console.print(Panel(
        "[bold magenta]Welcome to Snakes and Ladders![/bold magenta]\n"
        "[green]Climb ladders  and avoid snakes [/green]\n"
        "First to reach 100 wins!",
        title=" Let's Play!",
        border_style="bright_blue",
        expand=False
    ))
    console.print("\n[blue]Legend:[/blue]")
    console.print(" Player 1 |  Player 2 |  Snake |  Ladder")
    Prompt.ask("\nPress Enter to start")

def display_board(game):
    player_positions = {p.name: p.position for p in game.players}
    table = board.create_board_table(player_positions)
    console.print(table)

def show_turn(player):
    console.print(f"\n[bold {player.color}] {player.name}'s Turn[/bold {player.color}]")

def show_winner(game):
    console.clear()
    console.print(Panel(
        f"[bold gold1] {game.winner.name} Wins the Game![/bold gold1]\n"
        f"[italic]Congratulations! [/italic]",
        title=" Champion!",
        style="bold white on green",
        border_style="yellow",
        expand=False
    ))