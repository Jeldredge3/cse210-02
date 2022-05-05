""" CSE210 W03 - High Low """

# TODO: 
# 1) Create a deck of cards, 4 suits of 13 cards each. Might be best to create a seperate file and import later.
# 2) Draw the first card for the user to see, which will then ask if the following card is Higher/Lower.
# 3) Make sure get_inputs(self) method works.
# 4) Update the game's score if the user guesses Higher/Lower than the drawn card value.
# 5) Display the score to the user after each round, ask if they want to keep playing, end the game if they decide to quit.

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes: (To be created)
        deck_cards (List[Cards]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The accumulated score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs() # Get user input.
            self.do_updates() # Update the game based after checking user input.
            self.do_outputs() # Display user output.
    
    def get_inputs(self):
        """Ask the user if they guess that the next card will be higher or lower in value.

        Args:
            self (Director): An instance of Director.
        """
        higher_lower = input("Higher or Lower? [h/l] ")
        self.is_playing = (higher_lower == "h" or higher_lower == "l") # If user types 'h' or 'l', they are considered actively playing.

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        pass 
        # To be updated later, will need to update the player score if they are still playing.

    def do_outputs(self):
        """Displays the card that was drawn as well as the score. Also asks the player if they want to keep playing. 

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