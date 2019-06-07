#The steps for decrypting are:
#1. Calculate the number of columns you will have by taking the length of the message and
#   dividing by the key, then rounding up.
#2. Draw out a number of boxes. The number of columns was calculated in step 1. The
#   number of rows is the same as the key.
#3. Calculate the number of boxes to shade in by taking the number of boxes (this is the
#   number of rows and columns multiplied) and subtracting the length of the ciphertext
#   message.
#4. Shade in the number of boxes you calculated in step 3 at the bottom of the rightmost
#   column.
#5. Fill in the characters of the ciphertext starting at the top row and going from left to right.
#   Skip any of the shaded boxes.
#6. Get the plaintext by reading from the leftmost column going from top to bottom, and
#   moving over to the top of the next column.


#PROGRAMM
# Transposition Cipher Decryption
# http://inventwithpython.com/hacking (BSD Licensed)

import math#, pyperclip
def main():
    print('enter your message')
    myMessage = input()
    print('enter cipher key ')
    myKey = input()
    myKey = int(myKey)
    plaintext = decryptMessage(myKey, myMessage)   
    print(plaintext + '|')
    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    
    #pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)

    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()










































