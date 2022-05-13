""" CSE210 W03 - High/Low """

class GameRules:
    """ Creates a new object which contains the below attributes. The object will be accessible through the 'director.py' file.
    To call an attribute in a different file, you will need to type in the object name followed by a period and the attribute name.

    ex. object_name = GameRules() | Creates an object using this file.
        object_name.attribute     | Calls an attribute of an object.
        object_name.method()      | Calls a method of an object, will automatically pass 'self' as a parameter.

    Methods/Functions:
        print_game_intro    | Prints the first message that tells the user the rules of the game.
        print_game_over     | Prints the last message with the score and amount of turns taken. 
        ask_higher_or_lower | Asks the user for a string input "higher" or "lower".
    """

    def __init__(self):
        """ Runs the moment the 'GameRules' class is called. 
        Ignore for now.
        """

    def print_game_intro(self):
        # Display the first message of the game, establishes the rules.
        print("-----------------------")
        print("       HiLo Game       ")
        print("- - - - - - - - - - - -")
        print("Instructions:")
        print("Try to guess if the next card will be of higher or lower value than the previous.")
        print("You begin the game with 300 points. Correct guesses add 100 points, incorrect guesses minus 75 points.")
        print("Once you reach '0' points, the game is over.\n")

    def print_game_over(self, turn, score):
        # Display a message when the game ends.
        print("-----------------------")
        print("       Game Over       ")
        print("- - - - - - - - - - - -")
        print(f"Turns: {turn}")
        print(f"Score: {score}\n")
        print("-----------------------")

    def ask_higher_or_lower(self):
        # Ask user if the next card will be of higher or lower value.
        user_input = input("Higher or Lower? [h/l] ")
        input_lowercase = user_input.lower()
        # Create an attribute called '.guess' which can be accessed in another file through an object.
        if input_lowercase == "l" or input_lowercase == "lower":
            self.guess = "lower"
        elif input_lowercase == "h" or input_lowercase == "higher":
            self.guess = "higher"
        elif input_lowercase == "s" or input_lowercase == "same":
            self.guess = "same"    
        else:
            self.guess = None
    def add_more_score(self, score):
        score += 200
        print("+200")
    
    def add_score(self, score):
        score += 100
        print("+100 points")
    
    def subtract_score(self, score):
        score -= 75
        print("-75 points")