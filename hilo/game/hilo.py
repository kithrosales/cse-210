import random

# Application 
class Hilo:
    def __init__(self):
        self.current_card = random.randint(0, 13)
        self.next_card = random.randint(0, 13)
        self.running = True
        self.score = 300
    
    def run_game(self):
        """Run the game"""

        while self.running:
            
            self.do_inputs()
            self.display_score()
            self.check_game_status()
            self.change_card()
            print("")
            
    def check_card(self, hilo):
        """
            * Check the hilo if correct or not.
            * if you got correct your points will be added 100
            * if its not correct you will lose 75 points

            @params:
                hilo: str - High (h) or low (l)
        """
        if self.current_card < self.next_card and hilo == 'h':
            self.score += 100
        elif self.current_card > self.next_card and hilo == 'l':
            self.score += 100
        else:
            self.score -= 75
        
    
    def change_card(self):
        """ Change the value of the cards """
        self.current_card = random.randint(0, 13)
        self.next_card = random.randint(0, 13)

    def do_inputs(self):
        print(f"The card is: {self.current_card}")
        hilo = input("Higher or lower? [h/l] ")
        print(f"Next card was: {self.next_card}")
        self.check_card(hilo)
    
    def display_score(self):
        """ Display the score """
        print(f"Your score is: {self.score}")
    
    def check_game_status(self):
        """
            Check if the game is over unless the player's score is more than 0
            and if the player wanted to play again
        """
        if self.score <= 0:
            self.running = False
            return

        again = input("Play again? [y/n] ")
        if again == 'n' or again == 'N':
            self.running = False