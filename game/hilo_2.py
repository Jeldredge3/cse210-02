""" Programming with Classes - High/Low Game Example. """

import random

def main():
    
    rules = ChangeTheScore()
    
    keep_playing = True

    while keep_playing == True:
        print("---------------------")
        old_random_number = random.randint(1, 13)
        print(f"Random Number: {old_random_number}")

        guess = input("Higher or Lower? [h/l] ")
        print("- - - - - - - - - - -")
        if guess == "h":
            user_number = old_random_number + 1
        elif guess == "l":
            user_number = old_random_number - 1 
        else:
            break
            
        new_random_number = random.randint(1, 13)
        print(f"Random Number: {new_random_number}")
        
        if new_random_number > old_random_number and user_number > old_random_number:
            print("You guessed right!")
            rules.addscore()
        elif new_random_number < old_random_number and user_number < old_random_number:
            print("You guessed right!")
            rules.addscore()
        else:
            print("Your guess was wrong.")
            rules.minusscore()
        
        rules.print_score() # Calls a method within the object to print the score. The parameter it is passing is 'obj.score' which is an attribute of the object. # See line 49.
            
        if rules.score <= 0: 
            keep_playing == False
            print("Game Over.")
            break
    
class ChangeTheScore:
    def __init__(self):
        self.score = 300
    def addscore(self):
        self.score += 100
    def minusscore(self):
        self.score -= 75
    def print_score(self):
        print(f"Score: {self.score}")
    
# This starts the program by calling 'main()'

main()