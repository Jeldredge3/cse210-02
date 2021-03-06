""" CSE210 W03 - High/Low """

from genericpath import samefile
from game.playing_cards import DeckofCards
from game.hilo_game import GameRules

# TODO: 
# 1) Compare card value with user input
# 2) Make score update if player guesses correctly or incorrectly.
# 3) Any other fun additions to the game.

class Director: # This runs '__init__(self)' the moment it is called.
    """ The person who directs the game. Controls the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The accumulated score for the entire game.
    """

    def __init__(self):
        """ Create a deck of 52 cards using the 'DeckofCards' class in 'playing_cards.py'.
        The deck is generated using the '.create_deck' method and is stored within a list.
        An individual card can be accessed from the list by calling its index. (ex. 'self.deck[0]')
        The unique card object will not be readable unless one of its attributes are called.
        See below for a list of attributes.

        Attributes: 
            .suit               "Clubs, Diamonds, Hearts, Spades" 
            .rank               "Ace, Jack, Queen, King, etc."
            .value              the card's value in integer form (1-13)
            .name               the full name of a card (ex. "Ace of Spades")
            .shortcut           the abbreviated name of a card (ex. "S1")

        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        The deck of cards can also be accessed and modified using the below methods.
        The deck will need to be passed through these methods as a parameter.

        Methods: 
            .create_deck()      Builds the Deck of cards using a list of objects.
            .shuffle_deck()     Re-orders the list of objects in the Deck.
            .count_deck()       Returns the amount of cards in the Deck.
            .draw_card()        Draws a card from the Deck.                         (Parameters: Deck, Hand)
            .discard_hand()     Discards all cards in Hand.                         (Parameters: Hand, Discard)
            .merge_discarded()  Combines all discarded cards back into the Deck.    (Parameters: Discard, Deck)
            .view_top_card()    Prints the card name in position [0] of a list.
            .view_list()        Prints each card name within a list.
            .view_all_lists()   Prints each list.                                   (Parameters: Deck, Hand, Discard)
        """
        # Establish whether the game is being played. Set variables for the score.
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        # Create empty lists to be populated later.
        self.deck = [] # Holds a list of individual card objects.
        self.hand = [] # Temporarily holds any cards that are drawn from the deck list.
        self.discard = [] # Will contain any cards that are discarded from the hand list.

        # Store deck data in an object called 'cards' created from the class 'DeckofCards' in 'playing_cards.py'.
        self.cards = DeckofCards()
        # Pass through 'self.deck' into the '.create_deck()' method which will fill the empty list with 52 card objects.
        self.cards.create_deck(self.deck)
        # Shuffle the deck list.
        self.cards.shuffle_deck(self.deck)

        # Store game rules data in an object called 'hilo' created from the class 'GameRules' in 'hilo_game.py'.
        self.hilo = GameRules()
        # Print the game name and initial message.
        self.hilo.print_game_intro()

        # Start the game. Run the method/function below.
        self.start_game()

    def start_game(self):
        """ Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            # Run the '.everything()' method at the bottom of the file's code.
            # Will loop until 'self.is_playing' == False.
            if self.is_playing == True:
                self.everything()

    # =============================================================================== #

    def everything(self):
        """ Steps:
                (1) Begin the first round.
                (2) Draw the first card, place it in the discard pile.
                (3) Create a loop.
                    (a) Before begining the round, check if user's score is > 0.
                    (b) Ask user if the next card will be higher/lower.
                    (c) Check if the deck is empty. If deck is empty: refill it from the discard pile.
                    (d) Draw the next card.
                    (e) Compare the last card with the next card. Update the user's score based on their guess.
                    (f) Begin the next round, repeat the loop.
                (4) Display the final score.
                (5) Ask the user if they want to keep playing.

            Objects:
                self.hilo  | see 'hilo_game.py' file
                self.cards | see 'playing_cards.py' file
        """
        

        # (1) Start the first round.
        self.turn = 1
        loop_game = True
        self.score = 300
        print("-----------------------")
        print(f"Turn: {self.turn}    Score: {self.score}")
        print("- - - - - - - - - - - -\n")

        # (2) Draw the first card from the deck. If no cards, exit game.
        self.cards.draw_card(self.deck, self.hand)
        old_card = self.hand[0].value_and_suit
        old_card_value = self.hand[0].value

        # (3) Discard the first card.
        self.cards.discard_card(self.hand, self.discard)

        while loop_game == True:
            # (a) If the user has below 0 points, end the game.
            if self.score <= 0: 
                loop_game = False
                break

            # (b) Print the last card that was discarded. Ask user if the next card will be higher or lower in value.
            print(old_card)
            self.hilo.ask_higher_or_lower()
            # Get the returned value in 'self.hilo.guess' ("higher", "lower").
            guess = self.hilo.guess
            # Create a variable to hold a integer value that is higher or lower than the last card.
            if guess == "higher":
                guess_number = old_card_value + 1
            elif guess == "lower":
                guess_number = old_card_value - 1 
            elif guess == "same":
                guess_number = old_card_value 
            else:
                loop_game = False
                break

            # (c) Check if deck is empty. If near empty, repopulate the deck. Shuffle deck.
            if len(self.deck) == 0:
                self.cards.merge_discarded(self.discard, self.deck)
                self.cards.shuffle_deck(self.deck)

            # (d) Draw the next card from the deck.
            self.cards.draw_card(self.deck, self.hand)
            new_card = self.hand[0].value_and_suit
            new_card_value = self.hand[0].value
            print(f"{new_card}")

            # (e) Update the player's score depending on the user's guess.
            if new_card_value > old_card_value and guess_number > old_card_value:
                print("You guessed right!")
                self.score += 100
            elif new_card_value < old_card_value and guess_number < old_card_value:
                print("You guessed right!")
                self.score += 100
            elif new_card_value == old_card_value and guess_number == old_card_value:
                print("ahoy!!! you guess the same")
                self.score += 200
            else:
                print("Your guess was wrong.")
                self.score -= 75

            # Discard the most recent card, redefine it as the 'old_card'.
            self.cards.discard_card(self.hand, self.discard)
            old_card = self.discard[0].value_and_suit
            old_card_value = self.discard[0].value

            # (f) Begin the next round.
            self.turn += 1
            print("-----------------------")
            print(f"Turn: {self.turn}    Score: {self.score}")
            print("- - - - - - - - - - - -\n")
        
        # (4) When loop_game = False:
        self.hilo.print_game_over(self.turn, self.score)
            
        # (5) Ask the user if they want to continue playing.
        keep_playing = input("Keep playing? [y/n] ")

        if keep_playing.lower() == "y" or keep_playing.lower() == "yes":
            # If "yes", reset the turns and score.
            self.turn = 1
            self.score = 300
            # Combine the used cards back into the deck. Shuffle the deck.
            self.cards.merge_discarded(self.discard, self.deck)
            self.cards.shuffle_deck(self.deck)

        elif keep_playing.lower() == "n" or keep_playing.lower() == "no":
            # If "no", exit program.
            print("Exiting...")
            self.is_playing = False
