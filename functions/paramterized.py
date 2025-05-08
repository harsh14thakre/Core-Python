# #############################Relation between parameters#####################################################

# def Add(x,y):
#     print(x,y)
#     return x+y
# a=10
# b=4
# z=Add(x=a,y=b)
# print(z)


# def Add(x,y):
#     print(x,y)
#     return x+y
# a=int(input("Enter any number"))
# b=int(input("Enter any number"))
# z=Add(x=a,y=b)
# print(z)

# def add(*n):
#     print(n)
#     print(type(n))

# add()
# add(10)    


# variable length argument

# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# z=add(2,3,4,5,6,4,7)    
# print(z)


# def add(*n):
#     sum=0
#     for i in n:
#         for j in i:
#             sum=sum+j
#     return sum
# n=eval(input("Enter all values"))
# z=add(n)        
# print(z)


# #######################################keyword variable length argumments########################################

# def show(**n):
#     print(n)
#     print(type(n))
#     for i,j in n.items():
#         print(i,j)

# show(name="Harsh",age=20)        






# relation between parameter and arguments

# x=10
# if x:
#     x=20
#     print(x)
# print(x)    

# ----------------------------------------------------------------------------------

# x=10
# def display():
#     x=20
#     print(x)
# display()    
# print(x) 
# 


# x=10
# def display():
#     x=20
#     print(x)
#     print(id(x))
# display()    
# print(x)       

# x=10
# if x:
#     x=20
#     print(x)
#     print(id(x))    


x=10
def dis():
    x=20
    print(globals()['x'])
   
dis()    
     


