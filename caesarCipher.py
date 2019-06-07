# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

#import pyperclip

# the string to be encrypted/decrypted
print('enter the message--')
message = input()
   # the encryption/decryption key
print('enter the key ?')
key = input()
key =int(key)
# tells the program to encrypt or decrypt
print('enter 1 to select encryption mode or 2 to select decryption mode ')
mode = input() # set to 'encrypt' or 'decrypt'

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
      #Encrypt Non-Letter Characters
#LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`a bcdefghijklmnopqrstuvwxyz{|}~'
length =len(LETTERS)

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
message = message.upper()
# run the encryption/decryption code on each symbol in the message string
for symbol in message:
      if symbol in LETTERS:
 # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == '1':
           num = (num + key)%length
        elif mode == '2':
           num = (num - key)%length

 # handle the wrap-around if num is larger than the length of

 # LETTERS or less than 0
        
 # add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]
      else:
 # just add the symbol without encrypting/decrypting
       translated = translated + symbol

 # print the encrypted/decrypted string to the screen
print(translated)

 # copy the encrypted/decrypted string to the clipboard
#pyperclip.copy(translated)
