""" CSE210 W03 - High/Low """

import random

class DeckofCards:
    """Creates a list of 52 unique card objects which will act as the Deck.

    Attributes: 
        create_deck | Builds the Deck of cards using a list of objects.
        draw_card | draws a card from the Deck.
        shuffle_deck | Re-orders the list of objects in the Deck.
        count_deck | Returns the amount of cards in the Deck.
        view_top_card | Prints the card name in position [0] of the Deck list.
        view_deck | Prints each card name within the Deck list.
        view_deck_list | Prints each card along with it's attributes within the Deck list. 
    """

    def __init__(self):
        """ Runs automatically when DeckofCards class is called.
        Creates the deck of cards to be used in the High/Low game.

        Lists:
            deck_list | Contains card objects from when the Deck was created.
            discard_list | Will hold any discard cards that are removed from the Deck.
        """
        # deck_list = []
        # discard_list = []

        # self.create_deck(deck_list)

    def create_deck(self, deck):
        # Constructs a Deck using by appending Card objects to a list.
        card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        card_suits_abbr = ['C', 'D', 'H', 'S']
        card_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        # Loops through each suit.
        for SUIT_INDEX in range(0, 4):
            # For each suit in the list, loop through the 13 ranks/values.
            for RANK_INDEX in range(0, 13):
                suit = card_suits[SUIT_INDEX]
                rank = card_ranks[RANK_INDEX]
                value = RANK_INDEX + 1
                name = f"{rank} of {suit}"
                shortcut = card_suits_abbr[SUIT_INDEX] + str(value)
                # Create a unique card object which will hold the cards name, suit, and value.
                card_obj = CardObject()
                card_obj.suit = suit
                card_obj.rank = rank
                card_obj.value = value
                card_obj.name = name
                card_obj.shortcut = shortcut
                # Append the unique card object to the Deck list.
                deck.append(card_obj)
        
    def draw_card(self, deck):
        pass
    
    def shuffle_deck(self, deck):
        # Re-orders the list of objects.
        random.shuffle(deck)

    def count_deck(self, deck):
        # Count the number of cards in the deck.
        total_cards = len(deck)
        print(f"There are {total_cards} in the Deck.")
    
    def view_top_card(self, deck):
        # Print the card in position [0] of the Deck list.
        first_card = deck[0].name
        print(f"First Card: {first_card}")

    def view_deck(self, deck):
        # Print the name of each card in the Deck along with their position.
        place_counter = 0 
        for card_object in deck:
            place_counter += 1
            name = card_object.name
            print(f"{place_counter}) {name}")
        print()

    def view_deck_list(self, deck):
        # Print each card's attributes listed within the deck.
        for card_object in deck:
            suit = card_object.suit
            rank = card_object.rank
            value = card_object.value
            name = card_object.name
            shortcut = card_object.shortcut
            print(f"'{shortcut}', {rank}, {suit}, {name}, {value}")
        print()

class CardObject():
    """ Creates a unique card object and stores each attribute within the object.

    Attributes: 
        suit | "Clubs, Diamonds, Hearts, Spades" 
        rank | "Ace, Jack, Queen, King, etc."
        value | the card's value in integer form (1-13)
        name | the full name of a card (ex. "Ace of Spades")
        shortcut | the abbreviated name of a card (ex. "S1")
    """
    def __init__(self):
        # Constructs a new instance to create and object and store its attributes.
        self.suit = ""
        self.rank = ""
        self.value = ""
        self.name = ""
        self.shortcut = ""

    def print_attributes(self):
        # Call this method to print out the object's attributes.
        print(f"'{self.shortcut}', {self.rank}, {self.suit}, {self.value}, '{self.name}'")

# Called with: deck_obj = DeckofCards()


