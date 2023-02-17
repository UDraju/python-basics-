#sets are defined in {}, there will be no indexes
#no duplicates

#set funtions --add() ,update() , length(),pop()
#set operations -- union, differnt, intersections, disjoint, subset

#set eliminate the duplicates 

s={1,1,2,2,3}
print(s) #this is how it eliminates the duplicates

s1={}  # if you don't give any elements in curly braces, it will treat that as DICT
print(type(s1))


#funtions
print('add')
a={1,2,3.3,True}
a.add('python')
print(a)

print('remove')
a.remove(3.3)
print("the value removed from the set",a)


print('update')
a.update(['pythonclass']) #here we have passed LIST, even this will update as set
print(a)




print("FUNTIONS")

f={1,2,4.4,8,5,3}
f1={5,7,8.8,3,4.4}

print(f.union(f1))

print(f.difference(f1)) #f set resulted after removing the matching elements

print(f.intersection(f1)) #output looks same numbers from both sets 

print(f.isdisjoint(f1)) #if bot set elements are same o/p will be FALSE

print(f.issubset(f1))#two subsets to be same for getting the output as TRUE




