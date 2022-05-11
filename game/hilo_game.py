""" CSE210 W03 - High/Low """

class GameRules:
    """ Creates a new object which contains the below attributes. The object will be accessible through the 'director.py' file.
    To call an attribute in a different file, you will need to type in the object name followed by a period and the attribute name.

    ex. object_name = GameRules() | Creates an object using this file.
        object_name.attribute     | Calls an attribute of an object.
        object_name.method()      | Calls a method of an object, will automatically pass 'self' as a parameter.

    Methods/Functions:
        print_score | Prints the score.
    """

    def __init__(self):
        """ Runs the moment the 'GameRules' class is called. 
        Ignore for now.
        """

    def print_score(self, score):
        print(f"Your current score is: {score}")