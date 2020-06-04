"""
File: word_guess.py
-------------------
When the user plays WordGuess, the computer first selects a secret word at random from
a list built into the program. The program then prints out a row of dashes—one for each
letter in the secret word and asks the user to guess a letter. If the user guesses a letter that
is in the word, the word is redisplayed with all instances of that letter shown in the correct
positions, along with any letters correctly guessed on previous turns. If the letter does not
appear in the word, the user is charged with an incorrect guess. The user keeps guessing
letters until either
(1) the user has correctly guessed all the letters in the word or
(2) the user has made eight incorrect guesses.
"""

import random
from termcolor import colored
from colorama import init
init(autoreset=True)

DEAD_COLOR = 'red'


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    guess_count = INITIAL_GUESSES                                                       #chances are predefined by 8
    word_shown = []                                                                     #create a list to show the word after each guess
    for i in range(len(secret_word)):                                                   #for the length of word
        word_shown.append('-')                                                          #append list with - for each letter in the secrect wprd
    show_word(secret_word, word_shown)
    incorrect = 0
    store=[INITIAL_GUESSES]

    while True:
        print(f"\nYou have {guess_count} guesses left")                                #print the guess chances left
        guess = input("Type a single letter here, then press enter: ").upper()         #user input i.e guess the letter and convert it to upper since all words are in uppercase in the file
        if(len(guess)>1):                                                              #if user input is not a single character
            print("Guess should only be a single character.")                          #print message accordingly
            show_word(secret_word, word_shown)
            print(f"\nYou have {guess_count} guesses left")                            #do not decrement the guess chance if the entered input is wrong ....showing the guess count did not update after incorrect user input
            guess = input("Type a single letter here, then press enter: ").upper()     #ask the user for input again


        position = 0

        if guess in secret_word:
            for char in secret_word:
                if guess in char:
                    position = secret_word.index(char, position)
                    word_shown[position] = guess
                    position += 1
            print("That guess is correct.")
        elif guess in store:
            pass
        else:
            guess_count -= 1                                                         #decrement the guess_count by 1 for each incorrect guess
            print(f"There are no {guess}'s in the word")                             #print appropriate message on which guess is incorrect
            incorrect += 1
            hangman_diagram(incorrect)
        store.append(guess)
        show_word(secret_word, word_shown)                                           #displays instance of word revealed
        end_message(guess_count,secret_word,word_shown)

def hangman_diagram(incorrect):
    if incorrect==1:
        print('\t\tO')
    elif incorrect==2:
        print('      O   ')
        print('      |   ')
        print('      |   ')
    elif incorrect == 3:
        print('      O   ')
        print('     /|   ')
        print('      |   ')
    elif incorrect == 4:
        print('      O   ')
        print('     /|\\ ')
        print('      |   ')
    elif incorrect ==5:
        print('      O   ')
        print('     /|\\ ')
        print('      |   ')
        print('     /    ')
    elif incorrect == 6:
        print('      O   ')
        print('     /|\\ ')
        print('      |   ')
        print('     / \\ ')
    elif incorrect == 7:
        print('___________')
        print('|          ')
        print('|      O   ')
        print('|     /|\\ ')
        print('|      |   ')
        print('|     / \\ ')
    elif incorrect == 8:
        print(colored('___________',DEAD_COLOR))
        print(colored('|    *   * ',DEAD_COLOR))
        print(colored('|    * O * ',DEAD_COLOR))
        print(colored('|     /|\\ ',DEAD_COLOR))
        print(colored('|      |   ',DEAD_COLOR))
        print(colored('|     / \\ ',DEAD_COLOR))


def end_message(guess_count,secret_word,word_shown):
    '''
    As the user runs out of chances or the word has been gusses before the guess chances
    run out the game comes to end and appropriate messages are displayed accordingly
    '''
    if guess_count<1:                                                                #ran out of guess chances
        print("\nSorry, you lost. The secret word was:"+str(secret_word))
        play_again(secret_word)
    if '-' not in word_shown:                                                         #guesses the correct word befores guess chances ran out
        print("\nCongratulations, the word is :"+str(secret_word))
        play_again(secret_word)


def play_again(secrect_word):
    '''
    At the end of game the user is given options to continue with the same game or start a new game or exit
    '''
    response = input("\n\n\t1.Play the same game again\n\t2.Play a new game\n\t3.exit\n\tEnter your choice: ")
    if response == '1':                                                                 #play the same game/word again
        play_game(secrect_word)
    if response == '2':                                                                 #start a new game
        main()
    else:
        print("Game Over!")                                                             #print message and exit the code
        exit(0)

def show_word(secret_word,word_shown):
    '''
    This function prints the current revealed word
    '''
    print("The word now looks like this: ",end='')
    for i in range(len(secret_word)):
        print(word_shown[i],end='')


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.
    The words are selected in random from the given file
    """
    words=[]
    for line in open(LEXICON_FILE):
        line = line.strip()
        words.append(line)
    return random.choice(words)


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()