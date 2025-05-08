# lambda parameters :expression
# x=lambda p,q :print(p+q)

# r=int(input("Enter any value"))
# s=int(input("Enter any value"))

# x(r,s)


# x=lambda p,q :print(p+q)

# r=int(input("Enter any value"))
# s=int(input("Enter any value"))      (error)

# x(r,s)
# print(x(x,s)+5)




# x=lambda p,q : p+q

# r=int(input("Enter any value"))
# s=int(input("Enter any value"))      

# x(r,s)
# print(x(x,s)+5)



# l=[2,4,6,8,10]
# x=list(map(lambda x:x**2,l))
# print(x)

# l=[1,2,3,4,5,6,7,8,9]
# x=list(filter(lambda x:x if x%2==0 else None,l))
# print(x)

# l=[1,2,3,4,5,6,7,8,9]
# x=list(filter(lambda x: x%2==0,l))
# print(x)

import functools
l=[1,2,3,4,5,6,7,8,9]
x=functools.reduce(lambda a,b: a if a>b else b,l)
print(x)


