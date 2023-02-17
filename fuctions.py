#building blocks of code
#reuability --we can use the fuction in any code
# function starts with " def fucntion name :"
#instead of print we use "return" in the functions

#Why we use return insted of return
   #as we have multiple funtions in one package

def ses(*a):
    print(a)
#ses(3,2,5) we can't pass the many values to single key 
#we need to use "* key" as this will store values TUPLE
# "*a" is called as arbitary argument 

ses(3,5,6,76)

print("will use keyword arguments-kwargs")
#like above with "**a" is stores values as DICTIONARY(key and value)

def sesha(**a):
    print(a,)
sesha(name='ses',age =26) #lot to learn here 

print("-------------single parameter/argument")
def fn(name):
    print(name)
fn('john')    

print("-------------Double parameter/argument")
def fn(name,age):
    print(name,age)
fn('john',23) 

print("-------------will use same with return statement")
def fn(a,b):
    return a+b
c=fn('john','king') 
print(c)

print("-------------will use same with return statement")
def fn(a):
    return a*3
print(fn(3))

print("-------------will use same with return statement")
def fn(a,b):
    return a*b+3+4
print(fn(3,5))

print("-------------will use PASS")
def fn(a,b):
   pass #they won't return any 



print("-------------will use LIST and for loop")
def fn1(a):
    for i in a:
        print(i)
fn1([1,2,3,4,5])        

