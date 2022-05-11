""" CSE210 W03 - High/Low """

from game.playing_cards import DeckofCards

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

        # Store deck data in an object called 'hilo' created from the class 'DeckofCards'.
        self.hilo = DeckofCards()
        # Pass through 'self.deck' into the '.create_deck()' method which will fill the empty list with 52 card objects.
        self.hilo.create_deck(self.deck)
        # Shuffle the deck list.
        self.hilo.shuffle_deck(self.deck)

        # =========================================================================== #

        # Print the game name and initial message.
        print("-----------------------")
        print("       HiLo Game       ")
        print("- - - - - - - - - - - -")
        print("Instructions:")
        print("Try to guess if the next card will be of higher or lower value than the previous.")
        print("-----------------------\n")

        # Start the game. Runs the method/function below.
        self.start_game()

    def start_game(self):
        """ Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # Draw a card from the deck list to the hand list.
        self.hilo.draw_card(self.deck, self.hand)
        # Discard the card from the hand list to the discard list.
        self.hilo.discard_card(self.hand, self.discard)

        while self.is_playing:
            # Run the '.everything()' method at the bottom of the file's code.
            # Will loop until 'self.is_playing' == False.
            self.everything()

    # =============================================================================== #

    def everything(self):
        """ Steps:
                (1) Define the last drawn card.
                (2) Ask user if the next card will be higher/lower.
                (3) Define the next drawn card.
                (4) Compare the last card with the next card.
                (5) Check if user guessed correctly, update the score.
                (6) Display the current score each round.
                (7) End the game if player falls below '0' points.
        """
        if self.is_playing == True:

            # ================= (1) ================= #

            # Create a variable called 'last_card' which will be the card in position [0] of the discard list.
            last_card = self.discard[0].value

            # ================= (2) ================= #

            # Ask the user whether they think the next card is higher or lower in value.
            user_input = input("Higher or Lower? [h/l] ")
            input_lowercase = user_input.lower()
            user_guess = "" # Empty variable to define later.

            # If user guesses 'h' or 'higher'...
            if input_lowercase == "h" or input_lowercase == "higher":
                print("You guess higher.")

            # If user guesses 'l' or 'lower'... 
            elif input_lowercase == "l" or input_lowercase == "lower":
                print("You guess lower.")

            # EXTRA: If guesses 's' or 'same'...
            elif input_lowercase == "s" or input_lowercase == "same":
                pass

            # TESTING: If user types '?' or 'test'...
            elif input_lowercase == "?" or input_lowercase == "test":
                print("--------------------")
                self.hilo.view_all_lists(self.deck, self.hand, self.discard)
                print("--------------------\n")

            # QUIT: If user types 'q' or 'quit'...
            elif input_lowercase == "q" or input_lowercase == "quit":
                print("Exiting...")
                self.is_playing = False

            # If user types anything else...
            else:
                print(f"'{user_input}' is not a valid option. Type 'h' for higher or 'l' for lower.")
                print("Type 'q' to quit the program.\n")
                pass

            # ================= (3) ================= #

            # Draw the next card from the deck to the hand list.
            self.hilo.draw_card(self.deck, self.hand)
            # Create a variable called 'next_card' which will be the card that was just drawn.
            next_card = self.hand[0].value
            next_card_name = self.hand[0].shortcut 

            # ================= (4) ================= #
            # TODO: Compare 'last_card' with 'next_card'

            # ================= (5) ================= #
            # TODO: Check if user guessed correctly. Update the player's score.

            # ================= (6) ================= #
            # TODO: Display the current score after each round.

            # ================= (7) ================= #
            # TODO: End the game if player falls below '0' points.