# Ma  kes the wordPatterns.py File
# http://inventwithpython.com/hacking (BSD Licensed)
# Creates wordPatterns.py based on the words in our dictionary
# text file, dictionary.txt. (Download this file from
# http://invpy.com/dictionary.txt)
import pprint
def getWordPattern(word):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
            wordPattern.append(letterNums[letter])
            return '.'.join(wordPattern)


def main():
    allPatterns = {}

    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()
    for word in wordList:
        # Get the pattern for each string in wordList.
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement.
    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()


if __name__ == '__main__':
    main()





""" The getWordPattern() function takes one string argument and returns a string of that
word’s pattern. For example, if getWordPattern() were passed the string 'Buffoon' as
an argument then getWordPattern() would return the string '0.1.2.2.3.3.4'."""


