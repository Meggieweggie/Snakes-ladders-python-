import sqlite3
from datetime import datetime

class GameDatabase:
    def __init__(self, db_name="snakes_ladders.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Create tables if they don't exist"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                winner TEXT NOT NULL,
                total_moves INTEGER,
                game_date TEXT,
                duration_seconds INTEGER
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                games_played INTEGER DEFAULT 0,
                games_won INTEGER DEFAULT 0
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_game(self, winner, total_moves, duration):
        """Save completed game"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO games (winner, total_moves, game_date, duration_seconds)
            VALUES (?, ?, ?, ?)
        ''', (winner, total_moves, datetime.now().isoformat(), duration))
        
        conn.commit()
        conn.close()
    
    def update_player_stats(self, player_name, won=False):
        """Update player statistics"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM players WHERE name = ?', (player_name,))
        player = cursor.fetchone()
        
        if player:
            games_played = player[2] + 1
            games_won = player[3] + (1 if won else 0)
            cursor.execute('''
                UPDATE players SET games_played = ?, games_won = ?
                WHERE name = ?
            ''', (games_played, games_won, player_name))
        else:
            cursor.execute('''
                INSERT INTO players (name, games_played, games_won)
                VALUES (?, 1, ?)
            ''', (player_name, 1 if won else 0))
        
        conn.commit()
        conn.close()
    
    def get_player_stats(self, player_name):
        """Get player statistics"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM players WHERE name = ?', (player_name,))
        result = cursor.fetchone()
        conn.close()
        
        return result
    
    def get_game_history(self, limit=10):
        """Get recent game history"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT winner, total_moves, game_date, duration_seconds
            FROM games ORDER BY id DESC LIMIT ?
        ''', (limit,))
        
        results = cursor.fetchall()
        conn.close()
        
        return results