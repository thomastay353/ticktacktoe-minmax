# Tic Tac Toe AI Implementations

This repository contains two different AI implementations for playing Tic Tac Toe against a human player:

1. **app_random.py** - Computer makes random moves
2. **app_minmax.py** - Computer uses the Minimax algorithm (unbeatable)

## Files

- `app.py` - Original 2-player version (human vs human)
- `app_random.py` - 1-player vs computer with random AI
- `app_minmax.py` - 1-player vs computer with minimax AI

## Minimax Algorithm Explanation

### What is Minimax?

Minimax is a recursive decision-making algorithm used in game theory. It evaluates all possible future game states to find the **optimal move**. The algorithm works by:

1. **Exploring the entire game tree** - All possible moves and resulting positions
2. **Scoring leaf nodes** - Terminal positions (win/loss/draw)
3. **Propagating scores upward** - Working backwards to evaluate positions

### How It Works

The algorithm alternates between two perspectives:

- **Maximizing Layer (Computer/O)**: Chooses moves that maximize the score
  - Wants to win: score = +1
  - Wants to force a draw: score = 0
  - Wants to avoid loss: score = -1

- **Minimizing Layer (Human/X)**: Chooses moves that minimize the score
  - Wants opponent (human) to lose: low scores are good
  - Prevents computer from winning: seeks the best defense

### Scoring System

```
+1  : Computer wins
-1  : Human wins
 0  : Draw (no one wins)
```

### Example Game Tree (Simplified)

```
        [Board State]
       /      |      \
    Move1   Move2   Move3
    /         |         \
  -1         1          0
  
Best Move: Move2 (score = 1, guaranteed win)
```

### Pseudocode

```
function minimax(board, isMaximizing):
    if board is terminal (win/loss/draw):
        return score
    
    if isMaximizing (Computer's turn):
        bestScore = -infinity
        for each empty square:
            place O
            score = minimax(board, false)
            undo move
            bestScore = max(score, bestScore)
        return bestScore
    else (Human's turn):
        bestScore = +infinity
        for each empty square:
            place X
            score = minimax(board, true)
            undo move
            bestScore = min(score, bestScore)
        return bestScore
```

### Why Computer Wins/Draws

- **Maximizing layer**: Computer evaluates all possible moves and picks the one with the highest score
- **Minimizing layer**: Assumes human plays optimally (worst case for computer)
- **Result**: Computer either wins or forces a draw - **unbeatable!**

### Complexity

- **Time Complexity**: O(9!) ≈ 362,880 for empty board (but cached in practice)
- **Space Complexity**: O(depth of tree) ≈ O(9)
- **Performance**: Very fast for Tic Tac Toe (small game space)

## Running the Games

```bash
# Random AI (easier - computer makes random moves)
python app_random.py

# Minimax AI (unbeatable - computer plays optimally)
python app_minmax.py

# Original 2-player
python app.py
```

## Key Differences

| Feature | Random | Minimax |
|---------|--------|---------|
| AI Strategy | Random selection | Optimal play |
| Difficulty | Easy | Unbeatable |
| Algorithm | None | Minimax search tree |
| Can Human Win? | Yes | No (only draw) |
