""" CSE210 W03 - High/Low """

from game.playing_cards import DeckofCards

# TODO: 
# 1) [COMPLETE] Create a deck of cards, 4 suits of 13 cards each. Might be best to create a seperate file and import later.
# 2) Draw the first card for the user to see, which will then ask if the following card is Higher/Lower.
# 3) Make sure get_inputs(self) method works.
# 4) Update the game's score if the user guesses Higher/Lower than the drawn card value.
# 5) Display the score to the user after each round, ask if they want to keep playing, end the game if they decide to quit.

class Director:
    """ A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes: (To be created)
        deck_cards (List[Cards]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The accumulated score for the entire game.
    """

    def __init__(self):
        """ Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        print("--------------------")

        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        #self.start_game()
        self.get_card_from_deck()

    def start_game(self):
        """ Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs() # Get user input.
            self.do_updates() # Update the game based after checking user input.
            self.do_outputs() # Display user output.
        

    def get_inputs(self):
        """ Ask the user if they guess that the next card will be higher or lower in value.

        Args:
            self (Director): An instance of Director.
        """
        higher_lower = input("Higher or Lower? [h/l] ")
        self.is_playing = (higher_lower == "h" or higher_lower == "l") # If user types 'h' or 'l', they are considered actively playing.

    def do_updates(self):
        """ Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        pass 
        # To be updated later, will need to update the player score if they are still playing.

    def do_outputs(self):
        """ Displays the card that was drawn as well as the score. Also asks the player if they want to keep playing. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        drawn_card = ""
        # To be update later, will need to somehow draw a card from a deck.

        print(f"Next card was: {drawn_card}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

    def get_card_from_deck(self):
        """ Create a deck of 52 cards using the 'DeckofCards' class in 'playing_cards.py'.
        The deck is generated using the '.create_deck' method and is stored within a list.
        An individual card can be accessed from the list by calling its index. (ex. 'deck[0]')
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
            .draw_card()        draws a card from the Deck.
            .shuffle_deck()     Re-orders the list of objects in the Deck.
            .count_deck()       Returns the amount of cards in the Deck.
            .view_top_card()    Prints the card name in position [0] of the Deck list.
            .view_deck()        Prints each card name within the Deck list.
            .view_deck_list()   Prints each card along with it's attributes within the Deck list. 
        """

        # The deck list will fill with cards with the create_deck() method.
        # Methods/functions will need to pass through the deck list as an attribute.
        deck = []
        # Access the DeckofCards() class and store the generated deck in an object. 
        deck_obj = DeckofCards()
        deck_obj.create_deck(deck)
        deck_obj.view_top_card(deck)
        deck_obj.shuffle_deck(deck)
        

