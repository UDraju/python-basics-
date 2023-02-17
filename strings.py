#string is immutable 
#string can be denoted as '' ,"",''' '''
a="ses's"
print(a)

#string functions
  #UPPER
  #LOWER
  #STARTSWITH
  #ENDSWITH
  #STRIP
  #COUNT
  #SPLIT
  #REPLACE
  #format
  


s='this'
s1="        this is also string          "
s2='''this
is 
also 
3rd level
string'''

print(type(s))
print(type(s1))
print(type(s2))  ##### all are strings 

print('this is UPPER function')
n="australia"
print(n.upper())


print('this is LOWER function')
n="australia"
print(n.lower())

print('this is REPLACE function')
print(s2.replace("is","replaced"))

print('this is STRIP function')
j=s1.strip() #we can specify the strip 
print(j)

print('this is SPLIT function')
print(s2.split()) #split will change the sting to LIST

print('this is STARTWITH function')
print(s2.startswith('t')) #this is case sesitive please specify the exact character 
#
#
#



print('this is STRIP function')
print(s.endswith('s'))

print('this is FORMAT function')
print('he is no.{} and his name is {}{}'.format (1,'John','Mic'))

s2='this is not a code but this is a basic steps'
print('this is COUNT function')
print(s2.count('a'))

