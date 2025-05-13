# class P:
#     def __init__(self,bank,house,x):
#         self.bank=bank
#         self.house=house
#         self.x=x

# class C(P):
#     # def __init__(self,bank1,house1):
#     #     self.bank1=bank1
#     #     self.house1=house1
    
#     def show(self):
#         print(self.bank,self.house)
#         # print(self.house,self.house1)

# # obj1=P('HDFC','MP')        
# # obj1=P('IDFC','Kolar')        
# # obj1.show_details()    

# # obj=C
# # obj1=C()
# obj1=C('HDFC','Kolar',100)
# obj1.show()
         



# class P:
#     def add(self):
#         print("From add class")


#     def __init__(self,bank,house,x):
#         self.bank=bank
#         self.house=house
#         self.x=x

# class C(P):
    
#     def show(self):
#         super().add()
#         print(self.bank,self.house)
#     def add(self):
#         print("From child class")    

# obj1=C('HDFC','Kolar',100)
# obj1.show()
# obj1.add()         


# method overriding= in same class if multiple methods of same name is called this that will be override 
# overloading=Python does not support overloading




# Example of single level inheritance

# class A:
#     def first(self):
#         print("From parent class")

# class B(A):
#     def second(self):
#         print("From child class")

# obj=B()
# obj.first()
# obj.second()




# class A:
#     def first(self):
#         print("From parent class")

# class B(A):
#     def second(self):
#         print("From child class")

# class C(B):   
#     pass     

# obj=C()
# obj.first()
# obj.second()
       

# class A:
#     def first(self):
#         print("From parent class")

# class B(A):
#     def second(self):
#         print("From child class")

# class C(B):   
#     pass     

# obj=C()
# obj.first()
# obj.second()
       

# Multilevel inheritance:-

# father            mother

        #   child


# class A:
#     def first(self):
#         print("From parent class")

# class B(A):
#     def second(self):
#         print("From child class")

# class C(A,B):   
#     pass     

# obj=C()
# obj.first()
# obj.second()


'''
4.  Hierarchical inheritance 

                                -Parent 
                            |       
'''


class Parent:
    def home(self):
        print("From parent class")

    def bank(self):
        print("From parent bank")    
class child1(Parent):
    pass    
class child2(Parent):
    pass 

obj1=child1()
obj2=child2()

obj1.home()
obj2.home()
obj1.bank()
obj2.bank()

       
