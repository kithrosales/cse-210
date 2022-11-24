from game.hilo import Hilo


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        cards (List[card]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.running = True
        self.score = 300
        self.hilo = Hilo()
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self.running:
            
            self.do_inputs()
            self.display_score()
            self.check_game_status()
            self.do_update()
            print("")


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
    
    def display_score(self):
        """ Display the score """
        print(f"Your score is: {self.score}")

    def do_inputs(self):
        print(f"The card is: {self.hilo.current_card}")
        choice = input("Higher or lower? [h/l] ")
        print(f"Next card was: {self.hilo.next_card}")
        self.check_choice(choice)

    def check_choice(self, choice):
        """ Check if correct gain 100 points else lose 75 points"""
        if self.hilo.check_choice(choice):
            self.score += 100
        else:
            self.score -= 75
    
    def do_update(self):
        """ the current_card and the next_card will be update """
        self.hilo.card_update()