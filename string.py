# \n means newline
print('Ashwani \n Kumar')

#Strings can be concatenated with the + operator, and repeated with *.

string1='Ashwani'
string2='Kumar'
print(string1+string2)

# we can put space by ' '
print(string1+' '+string2)

#we can repeat string with * operator
print(string1*3+string2)

#Two or more string are automatically concatenated.

print('string1' 'string2')

#Strings can be indexed with the first character having index 0

print(string1[0])

print(string1[2:3])

print(string1[-6])

print(string1[2:7])

print(string1[:2]+string1[2:])

print(string1[2:])

str='J'+string1[2:]

print(str)

str1=string1[:2]+'KU'

print(str1)

s="python"

print(s[::-1])

print(len(string1))

print('abc'.capitalize())

#Cout the string in the sentence

msg="hey this is python"

str = 't'

print(msg.count(str))

# find the string in sentence

msg="hey this is python"

str="python"

print(msg.find(str))

#indexd string
str="this is python"
substr1="is"
print (str.index(substr1))

#change the case of string

string1="Hello Python" 
print(string1.swapcase())

# trip the string
string2="@@@@@@@@welcome to PYTHON"  
print(string2.lstrip('@'))  

string1="Hello Python" 
print(string1.lower())

string1="Hello Python" 
print(string1.upper())

string1="Hello Python" 
print(string1.islower())

string1="Hello Python" 
print(string1.isupper())
