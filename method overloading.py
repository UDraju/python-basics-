#same class ,same functions but different parameters

# print("---------this is method loading ---------")

# class A:
#     def fun1(self,a,b):
#         return a+b
#     def fun2(self,a,b,c):
#         return a+b+c
#     def fun2(self,a,b,c,d=9):
#         return a+b+c+d
# obj=A()
# # obj.fun2(1,3,6)    
# print(obj.fun2(9,5,6))



#different class ,same functions but different parameters
print("---------this is method Over riding ---------")

class A:
    def disp(self):
        print("this is class A")
class B(A):
    def disp(self):
        print("this is class b")
        super().disp()
obj=B()    
obj.disp()
    


