# Pong Game

This repository contains a simple implementation of the classic Pong game using Python's Turtle graphics library. The game features multiple modes, including player vs. computer, player vs. player, and computer vs. computer, along with adjustable difficulty levels for the AI.

## Features

- **Game Modes**:
  - **Player 1 vs Computer**: Play against an AI opponent with adjustable difficulty levels (Easy, Medium, Impossible).
  - **Player 1 vs Player 2**: Compete against another player on the same keyboard.
  - **Computer vs Computer**: Watch two AI opponents compete against each other.

- **Difficulty Levels**:
  - **Easy**: The AI moves randomly, making it easier for players to score.
  - **Medium**: The AI follows the ball with a slight delay, providing a balanced challenge.
  - **Impossible**: The AI perfectly follows the ball, making it very difficult to win.

## Code Structure

- **Main Game Logic**: The main game loop handles user input, ball movement, collision detection, and scoring.
- **Classes**:
  - **Characters**: Represents the paddles for players and AI. Handles paddle movement and drawing.
  - **Ball**: Represents the ball, including its movement, bouncing off paddles, and resetting its position after scoring.
  - **Scoreboard**: Manages and displays the score for both players.
  - **Comp**: Inherits from `Characters` and implements AI behavior based on the selected difficulty level.

## Getting Started

### Prerequisites

- Python 3.x
- Turtle graphics library (included with standard Python installations)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/datnaijakid/pong-game.git
   cd pong-game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

### Controls

- **Player 1 (Left Paddle)**:
  - Move Up: `W`
  - Move Down: `S`

- **Player 2 (Right Paddle)**:
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`

- **Select Game Mode**: Press `1`, `2`, or `3` to choose the game mode.
- **Select Difficulty** (if applicable): Press `1`, `2`, or `3` to choose the difficulty level for the AI.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
