# Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import  sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = """If a man is offered a fact which goes against his
instincts, he will scrutinize it closely, and unless the evidence is
overwhelming, he will refuse to believe it. If, on the other hand, he is
offered something which affords a reason for acting in accordance to his
instincts, he will accept it even on the slightest evidence. The origin of
myths is explained in this way. -Bertrand Russell"""
    myKey = getRandomKey()#'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    print(myKey)
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    checkValidKey(myKey)
    if myMode == 'encrypt':
       translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    #pyperclip.copy(translated)
    print()
    #print('This message has been copied to the clipboard.')
 

def checkValidKey(key): 
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()



""" 
   Encrypting Spaces and Punctuation
The simple substitution cipher in this chapter only encrypts the letters in the plaintext. 
  
If you want the simple substitution program to encrypt more than just the letter characters, make
the following changes:
simpleSubCipher.py
  LETTERS = r!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXY
             Z[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

myKey = /{9@6hUf:q?_)^eTi|W1,NLD7xk(-SF>Iz0E=d;Bu#c]w~'VvHKmpJ+}s8y& XtP43.b[OA!*\Q<M%$ZgG52YloaRCn"`rj
  

  The code that differentiates between upper and lowercase letters on lines 58 to 62 can be replaced
with these two lines:
simpleSubCipher.py
 symIndex = charsA.find(symbol.upper())
 if symbol.isupper():
 translated += charsB[symIndex].upper()
 else:
 translated += charsB[symIndex].lower()
 symIndex = charsA.find(symbol)
 translated += charsB[symIndex]

  """  