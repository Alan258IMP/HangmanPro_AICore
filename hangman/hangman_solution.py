#%%
# -*- coding: UTF-8 -*-
# Alan Li
# AICore 2022
# All rights reserved
'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

# This is a global variable
hangman_pictures = [
    '''
       +----+
       |    |
       |    
       |    
       | 
       |    
       |   
    =======
    ''', u'''
       +----+
       |    |
       |   \U0001f604
       |    
       | 
       |    
       |   
    =======
    ''', u'''
       +----+
       |    |
       |   \U0001F610
       |    |
       | 
       |     
       |   
    =======
    ''', u'''
       +----+
       |    |
       |   \U0001F628
       |   /|
       | 
       |     
       |   
    =======
    ''', u'''
       +----+
       |    |
       |   \U0001F62B
       |   /|\ 
       |   
       |     
       |   
    =======
    ''', u'''
       +----+
       |    |
       |   \U0001F607
       |   /|\ 
       |   / \ 
       |     
       |   
    =======
    '''
]

listof_word_lists = [
    open('hangman/mylist_110.txt').read().split(" "),
    [word for word in open('hangman/wordlist_10000.txt').read().split(" ") if len(word) >= 4],
    'apple banana orange pear strawberry watermelon'.split(" ")
]

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = ['_'] * self.num_letters
        self.num_lives = num_lives
        self.list_letters = []
        # Print messages upon initialization
        print("The mystery word has %.d characters" %(len(self.word)))
        print(self.word_guessed)
        pass

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A word can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        letter = letter.lower() # Convert this to lowercase, making the rest of the code case insensitive
        self.list_letters.append(letter)
        if letter in self.word:
            print('Nice! ' + letter + ' is in the word.')
            #Replace
            indices_to_replace = [i for i, l in enumerate(self.word) if l == letter]
            for i in indices_to_replace:
                self.word_guessed[i] = letter
            print(self.word_guessed)
        else:
            print('Sorry, ' + letter + ' is not in the word.')
            self.num_lives -= 1
            print('You have %d lives left.' %(self.num_lives))
            # Addition: print the hangman here
            # But not compatitable with Hangman classes of more than 5
            # As we only have five pictures in the hangman_pictures
            print(hangman_pictures[-(self.num_lives+1)])

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        letter = input('Please enter a letter')
        letter = letter.lower() 
        #if type(letter) != str:
        #    raise TypeError('Please, enter a letter') - this error handler already exist for input() function
        if len(letter) != 1:
            print('Please, enter just ONE character')
        elif letter in self.list_letters:
            print(letter + ' was already tried')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please, enter an English letter in the alphabet')
        else:
            self.check_letter(letter)
            self.list_letters.append(letter) # Add to the list of letters already tried

def play_game():
    # Select the word list (extra)
    print('Welcome to the game Hangman!')
    print('Please select the word list you wanna play with:')
    while True:
        word_list_choice = input('1: Custom 110-word list 2: 10000-word list from mit.edu 3: 6-word list for debugging')
        if word_list_choice in ['1','2','3']:
            word_list = listof_word_lists[int(word_list_choice) - 1]
            print(int(word_list_choice) - 1)
            break
        else:
            print('please input 1, 2 or 3')
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"
    num_lives_setting = game.num_lives
    print(hangman_pictures[0])
    while True:
        game.ask_letter()
        if game.num_lives == 0:
            print("You ran out of lives. The word was: " + game.word)
            break
        if game.word == ''.join(game.word_guessed):
            print("Congratulations, you won!! The word is " + game.word)
            break
    pass

if __name__ == '__main__':
    play_game()
# %%