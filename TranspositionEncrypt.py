#The steps for encrypting are:
#1. Count the number of characters in the message and the key.
#2. Draw a number of boxes equal to the key in a single row. (For example, 12 boxes for a
#key of 12.)
#3. Start filling in the boxes from left to right, with one character per box.
#4. When you run out of boxes and still have characters left, add another row of boxes.
#5. Shade in the unused boxes in the last row.
#6. Starting from the top left and going down, write out the characters. When you get to the
#   bottom of the column, move to the next column to the right. Skip any shaded boxes. This
#   will be the ciphertext.



#PROGRAMME


#import pyperclip

def main():
    print('enter your message')
    myMessage = input()
    print('enter cipher key ')
    myKey = input()
    myKey = int(myKey)
    ciphertext = encryptMessage(myKey, myMessage)
# Print the encrypted string in ciphertext to the screen, with
# a | (called "pipe" character) after it in case there are spaces at
# the end of the encrypted message.
    print(ciphertext + '|')
# Copy the encrypted string in ciphertext to the clipboard.
    #pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key #list data type

    # Loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()