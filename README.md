# Flappy Bird Clone

This project is a simple implementation of a Flappy Bird-like game using Python. The game features a bird that the player controls by making it flap its wings to avoid obstacles (pipes) and stay in the air.

## Project Structure

```
flappy_bird_clone
├── src
│   ├── main.py          # Entry point of the game
│   ├── game             # Contains game logic and classes
│   │   ├── __init__.py
│   │   ├── bird.py      # Bird class for game mechanics
│   │   ├── pipe.py      # Pipe class for obstacles
│   │   ├── base.py      # Base class for ground rendering
│   │   └── game_loop.py # Main game loop logic
│   └── assets           # Contains asset loading functionality
│       └── __init__.py
└── README.md            # Project documentation
```

## Running the Game

To start the game, run the following command in your terminal:

```
python src/main.py
```

## Controls

- Press the spacebar to make the bird flap and jump.
- Avoid the pipes to keep the game going.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add!
