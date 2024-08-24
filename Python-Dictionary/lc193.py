# get only keys from the dictionary using get key method

d2 = {900:'A', 200: 'B', 300: 'C', 400: 'D'}
k = d2.keys() # ([900, 200, 300, 400])
v = d2.values()
print(v)
print(k)

print("----" * 3)

for val in d2.keys() :
    # print(val)
    #print("----")
    print(d2[val])

print("-----------")

for x in d2.values():
    print(x)


# how to get items in python similar to entry in java

i = d2.items()
print(i) # dict_items([(900, 'A'), (200, 'B'), (300, 'C'), (400, 'D')]) List of tuples

for x1 in i:
     print(x1)

print("--------")
for k,v in d2.items():
    print(k,'\t \t ', v)
