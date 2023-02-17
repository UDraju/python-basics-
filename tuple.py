#Tuple is immutable 
#tuple will be defined in parathesis ()
# this is empty tuple -- t()


#operations is tuple are 
  #1membership
  #2.Repetitions
  #3.iterations
  #4.Concatination
  
  #funtion is tuple are
    ##min
    ##max
    ##sum
    ##sorted
    
ss=("ses",2,2.2,(23,48,96),True)
a=(2,4,6,98,92)
print(ss[3][1])
print(type(ss))
print(ss)
print(len(ss))
print(ss*2) ##repetations - this will just repeat the tuple 

print("below is for tuple concatination")
print(ss+a) #concatination - this will add another tuple after 1st tuple

print("below is for Memebership, this will just check the element in tuple")
print(3 in a)

print("below is for tuple iteration")

for i in a:
    print(i)
    
print("will try the fuctions ")

print(sorted(a))   #just use min, max , sum and sorted  
