""" CSE210 W03 - High/Low """

from game.playing_cards import DeckofCards

# TODO: 
# 1) Compare card value with user input
# 2) Make score update if player guesses correctly or incorrectly.
# 3) Any other fun additions to the game.

class Director:
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

        # Create the deck and set up the game.
        self.deck = [] # Holds a list of individual card objects.
        self.hand = [] # Temporarily holds any cards that are drawn from the deck list.
        self.discard = [] # Will contain any cards that are discarded from the hand list.

        # Store deck data in an object called 'hilo' created from the class 'DeckofCards'.
        self.hilo = DeckofCards()
        self.hilo.create_deck(self.deck)

        # Start the game.
        self.game_setup()
        self.start_game()

    def game_setup(self):
        # Print the game name and initial message.
        print("-----------------------")
        print("       HiLo Game       ")
        print("- - - - - - - - - - - -")
        print("Instructions:")
        print("Try to guess if the next card will be of higher or lower value than the previous.")
        print("-----------------------\n")

    def start_game(self):
        """ Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.everything()
            # self.get_inputs() # Get user input.
            # self.do_updates() # Update the game after checking user input.
            # self.do_outputs() # Display user output.

    def get_inputs(self):
        """ Draw a card from the Deck.
            Ask the user if they guess that the next card will be higher or lower in value.

        Args:
            self (Director): An instance of Director.
        """
        #self.hilo.view_all_lists(self.deck, self.hand, self.discard)
        # Draw a card. Store the card's attributes in variables.
        self.hilo.draw_card(self.deck, self.hand)
        card_value = self.hand[0].value
        # Ask user if the next card will be in higher value.
        higher_lower = input("Higher or Lower? [h/l] ")
        self.is_playing = (higher_lower == "h" or higher_lower == "l") # If user types 'h' or 'l', they are considered actively playing.

    def do_updates(self):
        """ Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        # TODO: Compare the user input with the card's value.

        # TEST: self.hilo.view_all_lists(self.deck, self.hand, self.discard)
        drawn_card = self.hand[0].value
        self.hilo.discard_card(self.hand, self.discard)
        last_card = self.discard[0].value
        print(drawn_card)
        print(last_card)

    def do_outputs(self):
        """ Displays Score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        drawn_card = ""
        # TODO: Update the user score.

        print(f"Next card was: {drawn_card}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

    def everything(self):
        self.hilo.draw_card(self.deck, self.hand)
        last_card = self.hand[0].shortcut
        higher_lower = input("Higher or Lower? [h/l] ")
        self.is_playing = (higher_lower == "h" or higher_lower == "l")
        self.hilo.discard_card(self.hand, self.discard)
       
        self.hilo.draw_card(self.deck, self.hand)
        # self.hilo.view_all_lists(self.deck, self.hand, self.discard)
        next_card = self.hand[0].shortcut   
        
        print(f"last card {last_card}")
        print(f"next card {next_card}")
        # 
        self.hilo.discard_card(self.hand, self.discard)
        
        # print(f"first card {drawn_card}")
        # print(f"last card {last_card}")