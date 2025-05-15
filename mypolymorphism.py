####################################Polymorphism##########################################

# class A:
#     def add(**n): 
#         print(n)
# obj=A
# obj.add(name="hello",course="python")
       


       ####################################Polymorphism##########################################

class A:
    def add(self,*n):
        sum=0
        for i in n:
            sum=sum+i
        print(sum) 
obj=A()
obj.add()
obj.add(1)
obj.add(1,2,3,4,5)