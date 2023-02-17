#LIST this will be denoted in [] brackets and may contain any datatypes,The index will start from "0".
#list is mutable as this will change dynamically by using the LIST methods  


#lets find the lenght of list 

Ses=[28,90.6,"ss","kl","vk"]
print(len(Ses))
print(type(Ses))

##will try same on nested list
print("NESTED LIST")
Raju=[26,93,[2,4,"OP"],"ss"]
print(Raju[2][2]) #we got output as "OP"


#LIST METHODS
 #APPEND -
 #EXTEND
 #REMOVE 
 #INSERT
 #INDEX
 #COUNT(1)
 
print("append")
Ses=[28,90.6,"ss","kl","vk"]
Ses.append("checking methods")
print(Ses)

print("Extend")
Ses.extend([5,98,96,"extend"])
print(Ses)


print("Insert")
Ses.insert(2,"this is insert") # 2 is index postion is the LIST
print(Ses)


print(Ses.count("kl"))


print("REMOVE")
Ses.remove(5) #here we have to give the give the element in the list
              # in POP methods we have to give index number
print(Ses)




print(len(Ses))


Ses= [2,3.0,"U",True]
print(Ses)

Ses.pop(1) #this will delete the index 1 which is 3.0
print(Ses)

Ses.reverse()
print(Ses)


#will try to use SORT

ss=[2,6,3,21,12,12.0]
ss.sort()
print(ss)

for i in ss:
    print(i+(31)/1)
