# Snakes and Ladders CLI Game

A command-line Snakes and Ladders game built with Python and Rich library.

## Overview

Classic board game where 2 players race to reach square 100. Roll dice, climb ladders, slide down snakes.

## Requirements

```bash
python >= 3.8
rich >= 12.0.0
```

## Installation

```bash
git clone <repository-url>
cd Snakes-ladders-python-
pip install rich
python snakes_and_ladders.py
```

## How to Play

- Players start at position 1
- Press Enter to roll dice
- Land on ladders to climb up, snakes to slide down
- First to reach exactly 100 wins

## Game Elements

**Snakes:** 16→6, 47→26, 49→11, 56→53, 62→19, 64→60, 87→24, 93→73, 95→75, 98→78

**Ladders:** 3→22, 5→8, 11→26, 20→29, 27→84, 28→84, 36→44, 51→67, 71→91, 78→98, 87→94

## Team

| Member | Role |
|--------|------|
| Megan | Game Logic |
| Charles | Player Movement & State |
| Christian | Board Setup & Dice |
| Khalid | Win Conditions & Turns |