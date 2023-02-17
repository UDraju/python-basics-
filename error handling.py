#error/exception handling 

#syntax 
#   try:
#       print(x)
#     except:
#           print(e)
#       finally:
#           print("this is completed")

# we can as many as exceptions cases

#types of Indexes
 #indexerror - we will get this errors in LIST AND TUPLE > index out of array
 

try:
    print(s)
# except Exception as u: # this will show you the what's the error in try block 
#     print(u)

except:
    print('Exception')
finally:
    print('this will return the value')  
    
    
print("---------------- wil see few general error's")

s=0
r=21
try:
    print(s=-r)
except:
    print('this')
finally:
    print('this is finally')               

