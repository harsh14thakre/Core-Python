## Abstraction
'''    
                  => Inherit ABC
->Abstract class  => Used atleast one abstract method decoratore    
->Abstract method => Used abstract method decorator with no body
->concrete method => method name with body
'''


"******************************ABSTRACTIONS**************************************************"

# from abc import ABC,abstractmethod

# class A(ABC):
#     def first(self):
#         print("from first method")
        
        
#     @abstractmethod
#     def second(self):
#         pass
#     @abstractmethod
#     def third(self):
#         pass





from abc import ABC, abstractmethod
class Senior(ABC):
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    @abstractmethod
    def div(self):pass

class Junior(Senior):
    def multi(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    
obj=Junior()
d=obj.multi(10,20)        
print(d)



