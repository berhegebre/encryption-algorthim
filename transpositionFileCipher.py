#ENCRYPTING AND DECRYPTING FILES 


# Transposition Cipher Encrypt/Decrypt File
# http://inventwithpython.com/hacking (BSD Licensed)
import time, os, sys, TranspositionEncrypt, transpositionDecrypt
#The sys module is imported for the exit() function.
def main():
    print('enter file name')
    inputFilename = input()
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file.
    print('enter key length')
    myKey = input()
    myKey = int(myKey)

    print('select encrypt or decrypt mode ')
    myMode = input() # set to 'encrypt' or 'decrypt'
    
    if myMode == 'encrypt':
        outputFilename = inputFilename+'encrypted.txt'
    elif myMode == 'decrypt':
    	outputFilename = inputFilename+'decrypted.txt'

    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
       print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %(outputFilename))
       response = input('> ')
       if not response.lower().startswith('c'):
           sys.exit()

    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long the encryption/decryption takes.
    startTime = time.time() 
    if myMode == 'encrypt':
        translated = TranspositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()
 
    print('Done %sing %s (%s characters).' % (myMode, inputFilename,len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()



    