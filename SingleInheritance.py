#this is single inheritance
# class parent:
#     def fun(self):
#         print("this is parent class ")
# class child(parent):
#     def fun1(self):
#         print("this is child class")
# obj=child()
# obj.fun1()     
# obj.fun()  


# print("this is multi level Inhertance")

# class parent:
#     def fun(self):
#         print("this is parent ")
# class child(parent):
#     def fun1(self):
#         print("this is child")
# class gchild(child):
#     def fun2(self):
#         print("this is gchild")
# obj=gchild()
# obj.fun2()  
# obj.fun1()    
# obj.fun()                    


# print("this is Hierar Inhertance")

# class parent:
#     def fun(self):
#         print("this is parent ")
# class child(parent):
#     def fun1(self):
#         print("this is child")
# class child2(parent):
#     def fun2(self):
#         print("this is child2")
# # obj=child2()
# obj=child() 
# obj.fun1()    
# obj.fun()  
# # obj.fun2()

# print("this is Multiple Inhertance")

# class Father:
#     def fun(self):
#         print("this is Father ")
# class Mother():
#     def fun1(self):
#         print("this is Mother")
# class child(Father,Mother):
#     def fun2(self):
#         print("this is child")
# obj=child()
# obj.fun()
# obj.fun1()
# obj.fun2()



print("------this is Super Keyword------")

class A:
    def __init__(self):
        print("this is class A")
class B(A):
    # def __init__(self):
    #     super().__init__()  
    #     print("thi is class B")  
    def __init__(self):
        super().__init__()
        print("thi is MF") 
class C(B):
    def __init__(self):
        super().__init__()
        print("this is class c")     
class D(C):
    def __init__(self):
        super().__init__()
        print("this is class d")                
obj=D()        
