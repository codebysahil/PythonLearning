d = {100: 'durga', 102: 'ravi'}
print(d)
d[300] = 'shiva'
print(d)
d[100] = 'sunny'
print(d)

print("-------------------Deleting the key value pair-------")

del d[100]
print(d)
# del d[400] # key error if the key does not exsist

# deleting multiple key value pair

del d[102],d[300]

print(d)

# del d[100] // key error