print 'please think of a number between 0 and 100!'
low = 0
high = 100

while True:
    medium = (low + high)/2
    print 'Is your secret number '+str(medium)+'?'
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'h':
        high  = medium
    elif ans == 'l':
        low = medium
    elif ans == 'c':
        print 'Game over. Your secret number was: ' + str(medium)
        break
    else:
        print 'Sorry, I did not understand your input.'