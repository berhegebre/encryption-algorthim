# Transposition Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
#import pyperclip
import detectEnglish, transpositionDecrypt


def main():
    # You might want to copy & paste this text from the source code at
    # http://invpy.com/transpositionHacker.py
    myMessage2 ='hlwlhlph.eoodeoyol r l tn'

    myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu plri
ch nitaalr eiuengiteehb(e1 hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaetee
oinebcdkyremdteghn.aa2r81a condari fmps" tad l t oisn sit u1rnd stara nvhn fs
edbh ee,n e necrg6 8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h a
ihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.
rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh
meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a
ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofg
BRe bwlmprraio po droB wtinue r Pieno nc ayieeto'lulcih sfnc ownaSserbereiaSm
-eaiah, nnrttgcC maciiritvledastinideI nn rms iehn tsigaBmuoetcetias rn"""
    print(myMessage)
    hackedMessage = hackTransposition(myMessage2)
    
    if hackedMessage == None:
        print('hlwlhlph.eoodeoyol r l tn|')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        #pyperclip.copy(hackedMessage)


def hackTransposition(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # brute-force by looping through every possible key
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
           # Check with user to see if the decrypted key has been found.
           print()
           print('Possible encryption hack:')
           print('Key %s: %s' % (key, decryptedText[:100]))
           #To be sure, this prints out the first 100 characters of the decryptedText 
           print()
           print('Enter D for done, or just press Enter to continue hacking:')
        
           response = input('> ')

           """The strip() string method returns a version of the string that has any
           whitespace at the beginning and end of the string stripped out."""
           if response.strip().upper().startswith('D'):#D for done
               return decryptedText

    return None

if __name__ == '__main__':
    main()
