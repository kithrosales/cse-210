from game.jumper import Jumper
import random


class Director:
    def __init__(self):
        self.words = [
            "witch",
            "gaffe",
            "rally",
            "grace",
            "chain",
            "claim",
            "lodge",
            "range",
            "belly",
            "rumor",
        ]
        self.word = random.choice(self.words)
        self.running = True
        self.jumper = Jumper()
        self.jumper.init_parachute()
        self.letters = ["_"]  * len(self.word)
    
    def start_game(self):
        while self.running:
            self.draw()
            self.do_inputs()
            self.check_game_status()

    def draw(self):
        """ draw the game"""
        self.display_letters()
        self.jumper.draw_parachute()
        print("\n\n^^^^^^^^")
    
    def display_letters(self):
        """ Prints the letters whos corrected """
        for letter in self.letters:
            print(letter, end=" ")
        print("\n")
    
    def do_inputs(self):
        """ Getting the letter of your guess"""
        guess = input("Guess a letter [a-z]: ")
        self.check_guess(guess)
    
    def check_guess(self, guess):
        """ Check if a guess is in the word's letters"""
        if guess in self.word:
            self.letters[self.word.index(guess)] = guess
        else:
            self.jumper.cut_line()
    
    def check_game_status(self):
        """ Check if the game is over or not"""
        self.display_letters()
        self.draw()
        if "".join(self.letters) == self.word:
            self.running = False
            print("Successfully completed!")

        if len(self.jumper.parachute) <= 3:
            self.running = False
            print("Game over")
        
        