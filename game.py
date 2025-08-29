from dice import roll_dice
from board import create_board
from player import Player
from database import GameDatabase
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class Game:
    def __init__(self, players):
        self.board = create_board()
        self.players = [Player(name) for name in players]
        self.winner = None
        self.db = GameDatabase()
        self.total_moves = 0
        self.start_time = None

    def play(self):
        console.print(Panel.fit("[bold blue] SNAKES AND LADDERS [/bold blue]", border_style="bright_blue"))
        console.print("[cyan]Race to square 100! Watch out for snakes and climb those ladders![/cyan]\n")
        
        self.start_time = time.time()

        while not self.winner:
            for player in self.players:
                console.print(f"\n[yellow]{player.name}[/yellow] - Position: [bold green]{player.position}[/bold green]")
                console.input("[dim]Press Enter to roll the dice...[/dim]")
                
                dice = roll_dice()
                console.print(f" [bold]{player.name}[/bold] rolled a [bold red]{dice}[/bold red]!")
                self.total_moves += 1

                old_position = player.position
                player.move(dice, self.board)
                
                if player.position != old_position + dice:
                    if player.position > old_position + dice:
                        console.print(f"[green] Ladder! Climbed to {player.position}[/green]")
                    else:
                        console.print(f"[red] Snake! Slid down to {player.position}[/red]")
                else:
                    console.print(f"[blue]Moved to position {player.position}[/blue]")

                if player.position == 100:
                    self.winner = player
                    console.print(Panel.fit(f"[bold gold1]{player.name} WINS![/bold gold1]", border_style="gold1"))
                    self.save_game_data()
                    break
                
                console.print("[dim]" + "─" * 40 + "[/dim]")
    
    def save_game_data(self):
        """Save game results to database"""
        duration = int(time.time() - self.start_time)
        self.db.save_game(self.winner.name, self.total_moves, duration)
        
        for player in self.players:
            won = player == self.winner
            self.db.update_player_stats(player.name, won)
        
        # Show game summary
        table = Table(title="Game Summary")
        table.add_column("Stat", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Winner", self.winner.name)
        table.add_row("Total Moves", str(self.total_moves))
        table.add_row("Duration", f"{duration}s")
        console.print(table)

if __name__ == "__main__":
    game1 = Game(["Player 1", "Player 2"])
    game1.play()