player1_pos = 0
player2_pos = 0
turn = 1
WINNING_POSITION = 100

while True:
    if turn == 1:
        dice = int(input("Player 1, enter your dice roll: "))
        player1_pos += dice
        print("Player 1 is now at:", player1_pos)
        if player1_pos >= WINNING_POSITION:
            print(" Player 1 wins!")
            break
        turn = 2
    else:
        dice = int(input("Player 2, enter your dice roll: "))
        player2_pos += dice
        print("Player 2 is now at:", player2_pos)
        if player2_pos >= WINNING_POSITION:
            print(" Player 2 wins!")
            break
        turn = 1