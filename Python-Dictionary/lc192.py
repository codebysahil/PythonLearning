d = {}  # by default considers are dict
d= {100:'Sahil'}
print(type(d))

# length --> returns the no of items present in the dictionary

d2 = {900:'A', 200: 'B', 300: 'C', 400: 'D'}
print(len(d2))
print(len(d))
print(d2.get(100))
print(d2.get(900)) # no key error but the ' None '  to get value associated with key

print(d2.get(900,"This key is not available"))
print("-------------------------------------------------------------")

# update method in dictionary

d.update(d2) # 
print(d)