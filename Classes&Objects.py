#Classes&Objects
#Class is blue print of the objects
#A class contains 'n' no.of objects 
#object is base class in the python 
#Class keyword is used to create the class 
#python constructor is defined in __init__()
#python doesn't allow multiple constructors i.e., No constructor overloading

#class name should starts with Capital's

# class Sesha:
#     d=12
#     print('this is a new class')
#     def disp(self):
#         a=10
#         b=90
#         print(a,b)
#    # disp(self=2)    
# object=Sesha()
# object.disp()  
# print(object.d)


class Mobile:
    def __init__(self,Brand,batttery,origin,model, Camera, Price):
        self.Brand=Brand
        self.battery=batttery
        self.origin=origin
        self.model=model
        self.camera=Camera
        self.price=Price
    def display(self):
        print("Brand",self.Brand) 
        print("battery",self.battery)  
        print("origin",self.origin)  
        print("Model",self.model)  
        print("camera",self.camera)  
        print("Price",self.price) 
        print("---------break-------") 

for i in range(3):      
  obj=Mobile("apple","4310mah","IS","19pro","100mp",'12k')
  obj.display()      
        
        
        
class Mobile2:
    def __init__(self):
        print("this is init method")
        print("this is from same init")
        print("init function will show you all the prints in the CLASS ")
    def display(self):
        print('this is display')
obj=Mobile2()
obj.display()
                    