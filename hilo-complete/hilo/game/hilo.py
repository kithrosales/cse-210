import random

# Application 
class Hilo:
    def __init__(self):
        self.current_card = random.randint(0, 13)
        self.next_card = random.randint(0, 13)
    
    def check_choice(self, choice):
        """
            * Check the choice if correct or not.

            @params:
                choice: str - High (h) or low (l)

            Return Type: bool

            * if correct return True else False
        """
        if self.current_card < self.next_card and choice == 'h':
            return True
        elif self.current_card > self.next_card and choice == 'l':
            return True
        else:
            return False
    
    def card_update(self):
        """ Change the value of the cards """
        self.current_card = random.randint(0, 13)
        self.next_card = random.randint(0, 13)
    
    