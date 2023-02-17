#File handling
  #write()
  #read()
  #append()
  #readbylines
  
f=open('u.txt','w')  
content =f.write('this is a write file')
print(content)
f.close()

f=open('u.txt','r')  
content =f.read()
print(content)
f.close()


f=open('u.txt','a')  
content =f.write("this is additional file by using append")
print(content)
f.close()

f=open('u.txt','r')  
content =f.read()
print(content)
f.close()