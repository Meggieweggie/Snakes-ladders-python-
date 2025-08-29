class player:
    def __init__(self,name):
        self.name
        self.position =0

    def move(self,steps,board):
        if self.position + steps <=100:
            self.position += steps
            if self.position in board:
                self.position =board[self.position] 
