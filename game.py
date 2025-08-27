from dice import roll_dice
from board import create_board
from player import Player

class Game:
    def __init__(self, players):
        self.board = create_board()
        self.players = [Player(name) for name in players]
        self.winner = None

    def play(self):
        print("Welcome to Snakes and Ladders am done\n")

        while not self.winner:
            for player in self.players:
                input(f"{player.name}, press Enter to roll the dice...")
                dice = roll_dice()
                print(f"{player.name} rolled a {dice}!")

                player.move(dice, self.board)
                print(f"{player.name} is now on {player.position}")

                if player.position == 100:
                    self.winner = player
                    print(f"{player.name} wins!")
                    break
                print("")
