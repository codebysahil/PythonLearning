# pop returns corresponding value
# if provided key not available

d = {100: 'a', 200: 'b', 300: 'c', 400: 'd'}
print(d.pop(300))  # c this is pop with only one argument

print(d)
# print(d.pop(700)) # KeyError: 700

print(d.pop(700, 'no key found'))  # pop method with two argument
# d.popitem() -- removes a random key value pair and returns that item
print("----------------")
d1 = {100: 'a', 200: 'b', 300: 'c', 400: 'd'}
print(d1.popitem())  # in tuple form
print(d1)
print(d1.popitem())
print(d1.popitem())
print(d1.popitem())
# print(d1.popitem()) KeyError: 'popitem(): dictionary is empty'
# to remove all key value pair from the dict
print("----------------")
d2 = {100: 'a', 200: 'b', 300: 'c', 400: 'd'}
print(d2.clear())
print(d2)
d2.clear()