import random

def roll_dice():
    return random.randint(1, 6)

def create_board():
    board = {}

    # Snakes
    board[16] = 6
    board[47] = 26
    board[49] = 11
    board[56] = 53
    board[62] = 19
    board[64] = 60
    board[87] = 24
    board[93] = 73
    board[95] = 75
    board[98] = 78

    # Ladders
    board[1] = 38
    board[4] = 14
    board[9] = 31
    board[21] = 42
    board[28] = 84
    board[36] = 44
    board[51] = 67
    board[71] = 91
    board[80] = 100

    return board

# --- Player class ---
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps, board):
        if self.position + steps <= 100:
            self.position += steps
            if self.position in board:
                new_position = board[self.position]
                if new_position > self.position:
                    print(f" {self.name} climbed a ladder to {new_position}!")
                else:
                    print(f" {self.name} got bitten by a snake and slid to {new_position}!")
                self.position = new_position


def play_game():
    board = create_board()
    players = [Player("Player 1"), Player("Player 2")]
    winner = None

    print(" Welcome to Snakes and Ladders \n")

    while not winner:
        for player in players:
            input(f"{player.name}, press Enter to roll the dice...")
            dice = roll_dice()
            print(f"{player.name} rolled a {dice}!")

            player.move(dice, board)
            print(f"{player.name} is now on {player.position}")

            if player.position == 100:
                winner = player
                print(f" {player.name} wins!")
                break
            print("")


if __name__ == "__main__":
    play_game()
