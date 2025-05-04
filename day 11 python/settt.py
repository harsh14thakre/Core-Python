# Collection of unique elements
# represented in {} with comma seperated elements
# Unordered collection
# indexing not supported
# Slicing not supported
# mutable in nature


# s={10,10,30,10,50,60}
# print(s)
# print(len(s))
# print(max(s))
# print(min(s))
# print(type(s))
# print(id(s))
# print(sum(s))


# s={2,4,6,'Neeraj',3,1,'Raj'}
# s.add('Rahul')
# print(s)
# s.update(5,6,4)   #do not update not iterable
# print(s)


# s.update('kapil','pinku')
# print(s)

# l1=[10,20,30]
# l2=[2,4,6]
# s.update(l1,l2)
# print(s)
# print(s.pop()) 
# print(s)
# s.remove('Neeraj')
# print(s)
# s.remove('neeraj')  #key error
# print(s)
# s.discard('raj')
# print(s)
# sl=s.copy
# print(sl)
# print(id(s),id(sl))
# s.clear()
# print(s)
# x=set()
# print(x)
# print(type(x))

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}

s1.intersection(s2)
print(s1)
# s1.intersection_update(s2)
# print(s1)

# s1.intersection.update(s2)
# print(s1)

# print(s1.difference(s2))
# print(s1)

# print(s1.symmetric_difference(s2))
# print(s1)


# print(s2.difference(s1))

# s2.difference_update(s1)
# print(s2)

# print(s1.isdisjoint())

# s3={1,2,3}
# s4={4,5,6}
# print(s3.isdisjoint(s4))

# s5={1,2,3,4,5,6,7,8,9}
# s6={4,5,6}
# print(s6.issubset(s5))
# print(s5.issuperset(s6))

# s1={10,20,30}
# s2={10,20,30}

# print(id(s1),id(s2))
# print(sum(s1))
# print(s1.clear())
# print(s1.copy())
# print(s1.pop())   #it removes first element
# print(s1.remove(30))    #ans=None
# print(s1.add(40)) # ans=none
# print(s1.clear()) # ans=none
 