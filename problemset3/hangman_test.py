# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    ans = True
    for i in range(len(secretWord)):
        if not (secretWord[i] in lettersGuessed):
            ans = False
            break
    return ans


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ans = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            ans += secretWord[i]
        else:
            ans +='_'
    return ans


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    # import string
    ans = ''
    for letter in string.ascii_lowercase:
        if not (letter in lettersGuessed):
            ans += letter
    return ans    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Loading word list from file...'
    print '55900 words loaded.'
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+ str(len(secretWord)) + ' letters long.'
    lettersGuessed = []
    mistakensMade = 0
    
    while not isWordGuessed(secretWord, lettersGuessed) and mistakensMade < 8:
        availableLetters = getAvailableLetters(lettersGuessed)
        print 'You have ' + str(8-mistakensMade) + ' guesses left.'
        print 'Available letters: ' + availableLetters
        guess_letter = raw_input('Please guess a letter: ')
        if not (guess_letter in availableLetters):
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            continue
        else:
            lettersGuessed.append(guess_letter)
            if guess_letter in secretWord:
                print 'Good guess:' + getGuessedWord(secretWord, lettersGuessed)
                continue
            else:
                print "Oops! That letter is not in my word:" + getGuessedWord(secretWord, lettersGuessed)
                mistakensMade += 1
                continue
    if isWordGuessed(secretWord, lettersGuessed):
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was else. '
                
            
        
        
    
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'banana'
hangman(secretWord)
