# Hilo
Hilo is short for High-Low, which is a card game where a card is drawn and the player has to guess whether the next card is higher or lower in value than the previous card. The player begins the game with 300 points which will increase if they guess right, or decrease if they guess wrong. Once the player reaches 0 points, the game is over. 
Hilo will use a standard playing card deck of 52 cards (without Jokers).

## Game Rules
---
* The player starts the game with 300 points.
* Individual cards are represented as a number from 1 to 13.
* The current card is displayed.
* The player guesses if the next one will be higher or lower.
* The the next card is displayed.
* The player earns 100 points if they guessed correctly.
* The player loses 75 points if they guessed incorrectly.
* If a player reaches 0 points the game is over.
* If a player has more than 0 points they decide if they want to keep playing.
* If a player decides not to play again the game is over.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 hilo
```

## Project Structure
---
The project files and folders are organized as follows:
```
cse210-02                   (project root folder)
+-- game                    (specific classes folder)
    +-- director.py         (contains a class and methods that define the program)
    +-- playing_cards.py    (contains classes that create a deck of cards)
+-- __main__.py             (runs the program by calling 'director.py')
+-- README.md               (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Herrera Axel
* Igor de Paula
* Jordan Eldredge - Says Hi.
* Jonathan Troche

