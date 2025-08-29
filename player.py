class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, steps, board):
        new_position = self.position + steps
        if new_position <= 100:
            self.position = new_position
            if self.position in board:
                self.position = board[self.position]
