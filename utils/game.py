# Import library
from typing import *
import random

# Initialize class
class Hangman (object):    
    """
    The Hangman game.
    This class is an object to perform a hangman game. There are somes variables to build the game.
    lives: int = 5
    turn_count: int = 0
    error_count: int = 0
    well_guessed_letter: str = ' '
    possible_words: List[st] = ['python', 'coding', 'dictionary', 'paper','apotheek','becode', 'learning', 'mathematics', 'sessions']
    word_to_find: List[str] = []
    correctly_guessed_letters : List[str] = []
    wrongly_guessed_letters: List[str] = []
    """

    # Constructor : create this object Hangman
    def _init_(self, word):
        """
        Function to initialize the game with a word to guess.
        : type word: str
        : param word: a word to guess        
        """
        super().__init__()
        self.word = word
        self.lives: int = 5
        self.letters = ""
        self.
        self.turn_count: int = 0
        self.error_count: int = 0
        self.well_guessed_letter: str = ' '
        self.possible_words: List[str] = ['python', 'coding', 'dictionary', 'paper','apotheek','becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: List[str] = []
        self.correctly_guessed_letters : List[str] = []
        self.wrongly_guessed_letters: List[str] = []


    # Function play()    
    def play(self) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        """
        This function ask a player to type in a character. It's only a character and not something else
        If is in condition then and this character in well_guessed_letter, ifnot ask again
        """
        while True:
            print(' Enter a single guessed letter please : ')
            char_letter = input()
            char_letter = char_letter.lower()
            if len(char_letter) != 1:
                print('Please enter a only one guess character : ')
            elif char_letter in seft.correctly_guessed_letter:
                print('This letter is already guessed')
            elif char_letter not in alphabet:
                print('please enter a alphabet letter : ')
            else:
                self.well_guessed_letter.append(char_latter)
                print(self.well_guessed_letter)
                #return char_letter      

    # Function game_over()
    def game_over(self)-> boolean:
        """
        This function return true if a game is end, ifnot return false.
        A game is end when a player win or lives is 0
        """


        return
    def well_played():
        return    
    def well_guessed_letters():
        return
    def bad_guessed_letters():
        return
    def life():
        return
    #def error_count():
        return
    #def turn_count():  
        return  
    def start_game():
        """
        This function is used to starting a hangman game.
        It's call all functions in the class Hangman.
        """
