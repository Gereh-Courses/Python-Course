# پروژه پایتون محافل گره
# 2048 Game in Python with Pygame

## Project Overview

This project is a Python implementation of the popular puzzle game, 2048, using the Pygame library. The game operates on a 4x4 grid where the player combines tiles with the same numbers to form larger numbers, aiming to reach the 2048 tile. The game ends when the grid is full and no more moves are possible.

## Features

- **Dynamic Grid Generation**: A 4x4 grid where tiles with numbers appear randomly.
- **Smooth Tile Movement**: Utilizes Pygame to animate tile movements and merges.
- **Score Tracking**: Keeps track of the current score and the best score across sessions.
- **Game Over Detection**: Determines when no further moves are possible and ends the game.
- **Reset Functionality**: Allows players to restart the game at any time by pressing a reset button.
- **Color-Coded Tiles**: Each tile number has a distinct color for better visual differentiation.

## How to Play

- Use the arrow keys (↑, ↓, ←, →) to move the tiles across the grid.
- Tiles with the same number merge into one when they touch, adding up their values.
- After every move, a new tile (either 2 or 4) appears in a random empty spot on the grid.
- The game continues until there are no more moves left, and the grid is full.
- Press the "Reset" button on the screen to start a new game at any point.

## Requirements

- Python 3.x
- Pygame library

To install Pygame, run:

```
pip install pygame numpy

```



## Running the Game

To start the game, navigate to the directory containing the game files and run:

```
python code.py
```

## Future Enhancements

- Saving and loading game state.
- Adding animations for merging tiles.
- Implementing an undo move feature.
- High score leaderboard.

## License

This project is open-source and available under the MIT License. Feel free to fork, modify, and use it in your own projects.

---

Remember to adjust the content based on the specifics of your implementation and any additional features you might have added. This template provides a structured way to present your project on GitHub, making it accessible and understandable for other developers and users interested in your work.
