# 🐍🪜 Snakes and Ladders CLI Game

A beautiful command-line implementation of the classic Snakes and Ladders board game built with Python and Rich library for an enhanced visual experience.

##  Game Overview

Snakes and Ladders is a classic board game where 2 players race to reach square 100 first. Players take turns rolling a dice to move across the board, climbing ladders for shortcuts and sliding down snakes as setbacks.

## Features

- **Rich CLI Interface**: Beautiful tables, colors, and progress bars using the Rich library
- **Interactive Gameplay**: Clean input handling and visual feedback
- **Classic Rules**: Traditional 100-square board with snakes and ladders
- **Two-Player Mode**: Turn-based gameplay for two players
- **Visual Board**: Colorful board representation with player positions
- **Game Statistics**: Track moves, ladder climbs, and snake encounters

##  Technologies Used

- **Python 3.8+**: Core game logic and functionality
- **Rich Library**: Enhanced CLI interface with colors, tables, and styling
- **Random Module**: Dice rolling mechanics

##  Requirements

```bash
python >= 3.8
rich >= 12.0.0
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Snakes-ladders-python-
```

2. Install dependencies:
```bash
pip install rich
```

3. Run the game:
```bash
python snakes_and_ladders.py
```

##  How to Play

1. **Start**: Both players begin at position 1
2. **Turn**: Players take turns pressing Enter to roll the dice
3. **Move**: Move forward by the number shown on the dice
4. **Ladders**: Land on a ladder bottom to climb up instantly
5. **Snakes**: Land on a snake head to slide down to its tail
6. **Win**: First player to reach exactly square 100 wins
7. **Exact Landing**: Must roll exact number to land on 100

## 🎲 Game Elements

### Snakes (Head → Tail)
- 16 → 6, 47 → 26, 49 → 11, 56 → 53, 62 → 19
- 64 → 60, 87 → 24, 93 → 73, 95 → 75, 98 → 78

### Ladders (Bottom → Top)
- 3 → 22, 5 → 8, 11 → 26, 20 → 29, 27 → 84
- 28 → 84, 36 → 44, 51 → 67, 71 → 91, 78 → 98, 87 → 94

## 👥 Team & Contributions

This project was developed collaboratively with clear role divisions:

| Team Member | Role | Responsibilities |
|-------------|------|------------------|
| **Megan** | Game Logic | Core game mechanics, rule implementation, game flow control |
| **Charles** | Player Movement & State | Position tracking, movement validation, player state management |
| **Christian** | Board Setup & Dice | Board initialization, dice rolling mechanics, random number generation |
| **Khalid** | Win Conditions & Turns | Victory detection, turn management, game completion logic |

##  Project Structure

```
Snakes-ladders-python-/
├── snakes_and_ladders.py    # Main game file
├── README.md                # Project documentation
└── requirements.txt         # Dependencies (if created)
```

##  Rich Library Features Used

- **Colorful Output**: Enhanced visual feedback with colors
- **Tables**: Clean board representation and game statistics
- **Progress Indicators**: Visual progress tracking
- **Styled Text**: Beautiful formatting for game messages
- **Input Prompts**: Enhanced user interaction

##  Future Enhancements

- [ ] Animated dice rolling
- [ ] Sound effects
- [ ] Multiple board themes
- [ ] Save/load game functionality
- [ ] AI opponent option
- [ ] Multiplayer support (3-4 players)
- [ ] Game replay feature
- [ ] Statistics tracking

##  Known Issues

- None currently reported

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create a Pull Request





