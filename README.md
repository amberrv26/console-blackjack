# Blackjack Game - Console Version

- A simple Blackjack (21) game written using Python 3
- Simulates a single-player blackjack game against the computer (the dealer) with an optional betting mode

## Features

- Fully functional blackjack game, using the console for interaction
- Optional betting mode with a starting balance
- Ace card logic (switches from 11 to 1 when needed)
- Dealer follows blackjack rules (twists until reaching 17)
- Clean Python code written using procedural programming

## Requirements

- Any version of Python 3
- Only imports 'random' and 'time' from the standard library - no external libraries needed

## How to Run

1. Clone or download this repo:
    ```bash
    git clone https://github.com/amberrv26/console-blackjack.git
    cd console-blackjack
    ```
2. Run the game:
    ```bash
    python blackjack.py
    ```
3. Follow the on-screen prompts to play!

## How to Play

- Choose whether you would like to enable betting mode. If you do, you must place a bet of at least £5
- When it's your turn, you can stick (stand) or twist (hit) - gain another card
- The dealer continues to draw until they reach 17 or higher. If they go over 21, they go bust!
- If your hand goes over 21, you go bust! 

## Planned Improvements

- Add GUI version with Tkinter or Pygame, including implementation of card graphics
- Add score tracking
- Add multiplayer mode (offline)

## License

- This project is open for personal or educational use, so please feel free to modify or contribute