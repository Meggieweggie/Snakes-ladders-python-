#### Snakes and Ladders Game
# A simple two-player console game where players take turns rolling a dice
# to move from position 1 to 100, navigating snakes and ladders along the way


import random

# SNAKES: key is head, value is tail (you slide down)
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

# LADDERS: key is bottom, value is top (you climb up)
ladders = {
    3: 22,
    5: 8,
    11: 26,
    20: 29,
    27: 84,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94
}

def handle_player_turn(player_num, position, dice_roll):
    """Handle a player's turn and return new position and win status"""
    new_position = position + dice_roll
    
    # Check if move is valid (does not exceed 100)
    if new_position > 100:
        print(f"   Oh no! You rolled too high. You stay at {position}")
        return position, False
    
    position = new_position
    print(f"   Player {player_num} moves to {position}")
    
    # Check for snakes
    if position in snakes:
        print("    Oops! You hit a snake!", end="")
        position = snakes[position]
        print(f" Sliding down to {position}")
    
    # Check for ladders
    elif position in ladders:
        print(f"   {'🪜' if player_num == 1 else '   '} Wow! You found a ladder!", end="")
        position = ladders[position]
        print(f" Climbing up to {position}")
    
    # Check for win
    if position == 100:
        print(f"\nPlayer {player_num} WINS! Congratulations!")
        return position, True
    
    return position, False

#  Players start at position 1 to the last square (100)
player1_position = 1
player2_position = 1

#  Game loop starts here
print(" Welcome to Snakes and Ladders!")
print("First player to reach 100 wins!")
print("Press Enter to roll the dice.\n")

# We'll use a variable to track whose turn it is to roll the dice
# 1 = Player 1, 2 = Player 2
current_player = 1

# Main game loop with error handling
try:
    while True:
        # Show who's turn it is and their current position
        current_position = player1_position if current_player == 1 else player2_position
        print(f" Player {current_player} is at position {current_position}")
        input("   Press Enter to roll the dice... ")

        # Roll the dice (random number from 1 to 6)
        dice_roll = random.randint(1, 6)
        print(f"    You rolled a {dice_roll}!")

        # Handle player turn
        if current_player == 1:
            player1_position, won = handle_player_turn(1, player1_position, dice_roll)
        else:
            player2_position, won = handle_player_turn(2, player2_position, dice_roll)
        
        if won:
            break  # End the game

        # Print a separator for clarity between turns 
        print("-" * 40)

        # Switch turns using concise approach
        current_player = 3 - current_player

except KeyboardInterrupt:
    print("\n\nGame interrupted by user. Thanks for playing!")
    exit(0)

# Game ends here 