
import collection

print ('hello python !')
gg=-5%3
print(gg)
i=10
while i>0:
  print (i)
  i=i-1
print ('///////////////////////////////// ')
print ('in and not in')
if'hello' in 'hello world':
     print('yes hello is found in hello world !')
if 'Hello' not in 'hello world':
    print('but Hello is not found in hello world')    
print (' ')
print ('about list')
mylist=[]
for i in range(10):
    mylist =mylist+[i]
print('the list value is ' ,mylist)    
print (' ////////////////////////////')
print ('about randome')

import random
random.seed(42)
for i in range(5):
 print(random.randint(1, 10))

print('/////////////////////////// ')
print('List variables don’t actually containlists at all, they contain references to lists. ')
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
print(spam)
cheese[1] = 'Hello!'
print(spam)
print(cheese)


print('/////////////////////// ')
fo = open('C:\\Users\\berhe gebre\\Documents\\pythone\\spam.txt','r')
content = fo.read() 
print(content)

print('//////////////////////// ')
print('The round function')
roun=round(4.2)
print(roun)
roun=round(4.2543)
print(roun)
roun=round(4.2553,2)
print(roun)

print('//////////////////////// ')

print(' about dictionarys ')
spam = {'key1':'this is a value','key2':42}
value=spam['key1']
print(value)
value=spam['key2']
print(value)
spam['key2']=43 #changing items using indexes
value=spam['key2']
print('the changed value is %s' %(value))
print('//////////////////////// ')

print('the split() method')
splitvlaue='My very energetic mother just served us Nutella.'.split()
print('split when ever space is :  %s \n' %(splitvlaue))

splitvlaue= 'helloXXXworldXXXhowXXXareXXyou?'.split('XXX')
print('split when ever xxx is :  %s\n' %(splitvlaue))

print('//////////////////////// \n')
print('multiple assignment trick \n')
spam ='hello'
eggs ='goodbye'
print(spam)
print(eggs)
print(' \n')
spam, eggs=eggs, spam
print(spam)
print(eggs)

print('//////////////////////// \n')

print('finding the gcd \n')
gcd=collection.gcd(21,49)
print('the gcd of 21 and 42 is %s' %(gcd))

print('/////////////////////////')
print('finding modular inverse \n')
invese= collection.findModInverse(7,26)
print('the modular inverse id %s \n' %(invese))

print('/////////////////////////')
print('some pythone operators also notice the multiple return type \n')

aa,bb,cc =collection.simplefun(7,2)
print('a//b is : %s a**b is: %s a mod b is:%s ' %(aa,bb,cc))

print('/////////////////////////\n')
print(' continue statement')
for i in range(3):
    print(i)
    continue# Hello will be skiped b/c of continue
    print('Hello!')

let ='AQUICKBOWNFXJMPSVRTHELZYDG'
letters=list(let)
print(letters)
letters.sort()#the sort() list method modifies the list in place and does not have a return value
# Never do like this: let=letters.sort()
print(letters)




grade =95

if grade>=90:
    RESULT ="A"

else: 
    RESULT ="B"
print('/////////////////////////\n')
print (RESULT)










