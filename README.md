# Hangman Project
This Python project is an implementation of a classic game called Hangman in which a player thinks of a word, and the other player tries to guess the word one letter at a time.

Only the [random](https://docs.python.org/3/library/random.html ) package and Python built-in functions are used.

> Yeah.

## Milestone 1: Creating the repo

Firstly I created a new repository using the existing [template](https://github.com/IvanYingX/Hangman_Test ). Then I created a copy of hangman_Template.py and renamed it hangman_solution.py, which is the main file we worked with.

The class Hangman encodes the game and the play_game() function runs the game.

## Milestone 2: ask_letter() method

I then created the ask_letter() method by requesting an input from the user.

The input character has to be one single English letter that has not yet been tried. Input with more than 1 characters or characters not in the English alphabet are not accepted. The user will be asked iteratively until a valid input is given. Note that uppercase letter input will be converted to lowercase.

## Milestone 3: Define the initializer

I filled in the __init__ method of the Hangman class according to the docstring already provided in the template. See the docstring for a description of the attributes.

## Milestone 4: check_letter() method

I then completed the check_letter() method. This method is called by the ask_letter() method after a valid input is given. The method then proceed to check if the letter is in the word.

If the letter is in the word, then it will replace all the blanks of the word_guessed list. I made the code more concise by using a list comprehension to identify the indices of the blanks to be replaced.

```python
indices_to_replace = [i for i, l in enumerate(self.word) if l == letter]
for i in indices_to_replace:
    self.word_guessed[i] = letter
```

If the letter is not in the word, the number of lives (self.num_lives) is reduced by 1.

## Milestone 5: Code the logic of the game

Finally, I coded the logic of the game in the play_game() function. This function creates an instance of the Hangman class called "game" and then iteratively calls the ask_letter() method with a while loop. The loop is broken if the word is correctly guessed or if the player run out of lives.

```python
while True:
    game.ask_letter()
    if game.num_lives == 0:
        print("You ran out of lives. The word was: " + game.word)
        break
    if game.word == ''.join(game.word_guessed):
        print("Congratulations, you won!! The word is " + game.word)
        break
```


## Extra

I added two things to make the code fancier. Firstly, I 


## Conclusion
> Through th


