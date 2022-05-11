""" CSE210 W03 - High/Low """

import random

class DeckofCards:
    """Creates a list of 52 unique card objects which will act as the Deck.

    Attributes: 
        create_deck | Builds the Deck of cards using a list of objects.
        shuffle_deck | Re-orders the list of objects in the Deck.
        count_deck | Returns the amount of cards in the Deck.
        draw_card | draws a card from the Deck, places card in Hand.
        discard_hand | Discards all cards from hand.
        merge_discarded | Combines discarded cards back into the Deck.
        view_top_card | Prints the card name in position [0] of a list.
        view_list | Prints all card names in a list.
        view_all_lists | Prints the Deck, Hand, and Discard lists.
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

    def shuffle_deck(self, deck):
        # Re-orders the list of objects.
        random.shuffle(deck)

    def count_deck(self, deck):
        # Count the number of cards in the deck.
        total_cards = len(deck)
        if total_cards < 52:
            print(f"There are {total_cards} cards left in the deck.")
        else:
            print(f"There are {total_cards} cards in the deck.")
    
    # ========================================================================= #

    def view_top_card(self, object_list):
        # Print the card in position [0] of the list.
        if len(object_list) > 0:
            top_card = object_list[0].name
            print(f"Top card in list: {top_card}")
        else:
            print("No cards in list.")

    def view_list(self, object_list): # (self, deck/hand/discard)
        # Print the name of each card in the object list along with their position.
        place_counter = 0 
        if len(object_list) > 0:
            for card_object in object_list:
                place_counter += 1
                name = card_object.name
                print(f"{place_counter}) {name}")
            print()
        else:
            print("No cards in list.")

    def view_all_lists(self, deck, hand, discard):
        # Loop through each list, store the name of each item in a different list for display purposes.
        deck_display = []
        hand_display = []
        discard_display = []
        # Count the amount of items in each list.
        deck_counter = 0
        hand_counter = 0
        discard_counter = 0
        # Append the name of each item into the display lists.
        if len(deck) > 0:
            for card_object in deck:
                deck_counter += 1
                nickname = card_object.shortcut
                deck_display.append(nickname)
        if len(hand) > 0:
            for card_object in hand:
                hand_counter += 1
                nickname = card_object.shortcut
                hand_display.append(nickname)
        if len(discard) > 0:
            for card_object in discard:
                discard_counter += 1
                nickname = card_object.shortcut
                discard_display.append(nickname)
        # Prints total items in each list along with the list's items.
        print(f"Deck - {deck_counter} items: \n{deck_display}\n")
        print(f"Hand - {hand_counter} items: \n: {hand_display}\n") 
        print(f"Discard - {discard_counter} items: \n: {discard_display}\n") 
                
    # ========================================================================= #

    def draw_card(self, deck, hand): # DECK -> HAND
        # Draw a card from the deck list, move the drawn card to the hand list.
        if len(deck) > 0:
            top_card = deck.pop(0)
            # TEST: print(f"You draw a '{top_card.name}' ({top_card.value}).")
            hand.append(top_card)
        else:
            print("No cards left in the deck to draw from.")

    def discard_hand(self, hand, discard): # HAND -> DISCARD
        # Discard all cards from your hand list, move the cards into the discard list.
        if len(hand) > 0:
            for card in hand:
                discarded_card = hand.pop(0)
                discard.insert(0, discarded_card)
        else:
            print("No cards in the hand to discard.")
    
    def discard_card(self, hand, discard): # HAND -> DISCARD
        # Discard the first card from your hand list, move the card into the discard list.
        if len(hand) > 0:
            discarded_card = hand.pop(0)
            discard.insert(0, discarded_card)
        else:
            print("No cards in the hand to discard.")

    def merge_discarded(self, discard, deck): # DISCARD -> DECK
        # Combine cards in the discard list back into the deck list.
        if len(discard) > 0:
            for card in discard:
                returned_card = discard.pop(card)
                deck.append(returned_card)
        else:
            print("No cards in the discard pile to merge into the deck.")

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


