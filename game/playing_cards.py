""" CSE210 W03 - High/Low """

import random

class DeckofCards:
    """Creates a list of 52 unique card objects which will act as the Deck.

    Attributes: 
        create_deck | Builds the Deck of cards using a list of objects.
        draw_card | draws a card from the Deck, places card in Hand.
        discard_hand | Discards all cards from hand.
        merge_deck | Combines discarded cards back into the Deck.
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
        
    def draw_card(self, deck, hand):
        # Draw a card from the deck list, move the drawn card to the hand list.
        if len(deck) > 0:
            top_card = deck.pop(0)
            print(f"Card drawn is: {top_card.name}.")
            hand.append(top_card)
        else:
            print("No cards left in the deck to draw from.")

    def discard_hand(self, hand, discard):
        # Discard a card from your hand list, move the card to the discard list.
        if len(hand) > 0:
            for card in hand:
                discarded_card = hand.pop(card)
                discard.append(discarded_card)
        else:
            print("No cards in the hand to discard.")

    def merge_deck(self, deck, discard):
        # Combine cards in the discard list back into the deck list.
        if len(discard) > 0:
            for card in discard:
                returned_card = discard.pop(card)
                deck.append(returned_card)
        else:
            print("No cards in the discard pile to merge into the deck.")

    def shuffle_deck(self, deck):
        # Re-orders the list of objects.
        random.shuffle(deck)

    def count_deck(self, deck):
        # Count the number of cards in the deck.
        total_cards = len(deck)
        print(f"There are {total_cards} in the deck.")
    
    def view_top_card(self, deck):
        # Print the card in position [0] of the Deck list.
        top_card = deck[0].name
        print(f"Top card in deck: {top_card}")

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


