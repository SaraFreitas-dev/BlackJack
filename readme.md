# Blackjack Game

This is a simple Blackjack game played in the terminal, coded in Python.

## Overview

- **Game**: Blackjack
- **Platform**: Terminal/Command Line
- **Language**: Python

## Files

- **`Instructions.py`**: Provides hints and guidance to help you understand and modify the code. It’s a resource if you want to attempt coding the game yourself or improve upon it.
  
- **`playBlackjack.bat`**: A batch file that you can run to execute and play the Blackjack game on Windows. Simply double-click the file to start the game.

- **`Blackjack.py`**: The main Python script that contains the game logic. This is where the core functionality of the game is implemented.

## Features

- Play a game of Blackjack directly in your terminal.
- Game logic is fully functional.
- Basic gameplay mechanics are implemented.

## To Do

- **ASCII Art**: Add ASCII art to enhance the visual appeal of the game.
- **Hide Opponent’s Card**: Implement functionality to hide the opponent's card until the end of the game.
- **Restart Option**: Implement a more refined restart option to allow users to start a new game seamlessly.

## BlackJack Rules

1. **Card Values**:
   - **2-10**: Face value
   - **Jack, Queen, King**: 10 points
   - **Ace**: 1 or 11 points

2. **Objective**: Get a hand value closer to 21 than the dealer without exceeding 21. A hand totaling exactly 21 is a "Blackjack" and wins automatically.

3. **Gameplay**:
   - Both player and dealer are dealt two cards. Player's cards are face up; the dealer has one card face up and one card face down.
   - The player can choose to "Hit" (take another card) or "Stand" (keep current hand).
   - The dealer reveals the hidden card when the player decides to stand.
   - The hand closest to 21 wins. If a hand exceeds 21, it results in an automatic loss (a bust). 
   - If the hand is 21, is an automatic win since the player got a BlackJack.

