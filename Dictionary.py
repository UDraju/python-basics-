#
#update
#pop
#clear
#copy

dic={}
print(type(dic)) 

dic={'name':'sesha','ph':651876544}
print(dic) # this will display the whole dic 
print(type(dic)) 
print(dic['ph'])

#we can input list in the dictionary
print('-------LIST IN DICTIONARY')
dic={'name':'sesha','ph':[651876544,892928298,1923738739,3989]}
print(dic['ph'][3])

print('------display only keys from the dic')
print(dic.keys())

print('------display only values from the dic')
print(dic.values())


print('------pop the key from the dic')
print(dic.pop('name')) #this will remove the 'name from dic 
print(dic) 
