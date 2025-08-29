from database import GameDatabase

def show_stats():
    db = GameDatabase()
    
    print("=== GAME STATISTICS ===\n")
    
    # Recent games
    print("Recent Games:")
    games = db.get_game_history(5)
    if games:
        for game in games:
            winner, moves, date, duration = game
            print(f"  {winner} won in {moves} moves ({duration}s) - {date[:10]}")
    else:
        print("  No games played yet")
    
    print("\nPlayer Stats:")
    # This would need a method to get all players
    print("  Use db.get_player_stats('Player Name') to check individual stats")

if __name__ == "__main__":
    show_stats()