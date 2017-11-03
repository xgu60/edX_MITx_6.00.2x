from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    
    m_score = 0
    b_word = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            if getWordScore(word, n) > m_score:
                m_score = getWordScore(word, n)
                b_word = word
            else:
                continue
        else:
            continue
    return b_word
        
   
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    while calculateHandlen(hand) > 0:
        print 'Current Hand:' , 
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        
        if word == None:
            break
            
        else:
            score += getWordScore(word, n)
            print '"' + word +'"' + ' earned ' + str(getWordScore(word, n)) + ' points. Total: '+ str(score) + ' points' 
            print ' '
            hand = updateHand(hand, word)

    print 'Goodbye! Total score: ' + str(score) + ' points.'
    
                
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    last_hand = {}
    while True:
        user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if user_input == 'e':
            break
        elif user_input == 'n':
            last_hand = dealHand(HAND_SIZE)
            while True:
                second_input = raw_input('Enter u to have yourself play, c to have the computer play:')
                if second_input == 'u':
                    playHand(last_hand, wordList, HAND_SIZE)
                    break 
                elif second_input == 'c':
                    compPlayHand(last_hand, wordList, HAND_SIZE)
                    break  
                else:
                    print 'Invalid command.'  
                    print ' '
                    continue
            continue
        elif user_input == 'r':
            if last_hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
                continue
            else:
                while True:
                    second_input = raw_input('Enter u to have yourself play, c to have the computer play:')
                    if second_input == 'u':
                        playHand(last_hand, wordList, HAND_SIZE)
                        break 
                    elif second_input == 'c':
                        compPlayHand(last_hand, wordList, HAND_SIZE)
                        break  
                    else:
                        print 'Invalid command.'  
                        print ' '
                        continue
               
        else:
            print 'Invalid command.'
            print ' '
            continue  
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


