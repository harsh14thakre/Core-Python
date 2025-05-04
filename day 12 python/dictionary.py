# Collection of elements (Pair of key value)
# represented in {} with comma seperated elements
# Key must be unque
# Value may be duplicate
# Indexing not supported
# Slicing not supported
# Mutable in nature
# E.g=> d={'name':'Harsh', 'age':37,'Qualification':'M.tech'}

d={'name':'Harsh', 'age':37,'Qualification':'M.tech'}
# # print(d)
# # print(max(d))
# # print(min(d))
# # print(type(d))
# # print(id(d))



# # Methods of dictionary

# # print(d.clear())
# # print(d)

# # x=d.copy()
# # print(x,d)
# # print(id(x),id(d))

# # l=['name','age','qualification']
# # d1=dict.fromkeys(l)
# # print(d1)

# l='Harsh'
# d1=dict.fromkeys(l,100)
# print(d1)

# print(d.get('age'))
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d.popitem())
# print(d)
# d.pop('age')
# print(d)


# d.setdefault('name','rahul')
# print(d)


# d.setdefault('greed','M.tech')
# print(d)


d1={'greed': 'Mtech', 'city': 'Bhopal'}
d.update('name')

d['name']='Rahul'    #Update
print(d)  

print(d['name'])        #read

d['greed']='M.tech'
print(d)