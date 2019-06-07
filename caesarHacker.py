
print('enter the message ')
message = input()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
#Non-Letter Characters
#LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`a bcdefghijklmnopqrstuvwxyz{|}~'
length =len(LETTERS)

for key in range(length):
	translated = ''

	for symbol in message:
	    if symbol in LETTERS:
		    num = LETTERS.find(symbol)
		    num = (num - key) % length   
		    #modulo operation
            translated = translated + LETTERS[num]
        else:
        	translated = translated + symbol
    print('key #%s: %s' %(key, translated))