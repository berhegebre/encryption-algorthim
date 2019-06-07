"""# Detect English module
# http://inventwithpython.com/hacking (BSD Licensed)

# To use, type this code:
# import detectEnglish
# detectEnglish.isEnglish(someString) # returns True or False
# (There must be a "dictionary.txt" file in this directory with all English
# words in it, one word per line. You can download this from
# http://invpy.com/dictionary.txt)"""

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    #will remove the non-letter characters from the string,such as 
    #numbers and punctuation, 
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0    # no words at all, so return 0.0 if stop here.
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
	#If isEnglish() is called with only one argument, the default arguments are used
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    # If this number is greater than or equal to the wordPercentage parameter, 
    # then True is stored in wordsMatch. Otherwise, False is stored in wordsMatch.
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
    #We want isEnglish() to return True only if both the wordsMatch and lettersMatch
    #variables contain True

"""
N.B:
All of the work we’ve done in this chapter is so that any program
can do the following:
>>> import detectEnglish
>>> detectEnglish.isEnglish('Is this sentence English text?')
True
>>>

"""


