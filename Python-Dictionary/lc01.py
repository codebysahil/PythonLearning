# dictionary --> when you need to represent objects in the key value format

d = {101: 'John', 200: 'Ravi' , 'A' : 2000 , 101 : 'Shiva'}  # k1: V1 , k2:v2
# Old values will be replaced by the new value
# no gurantee for the insertion order


print(d)


print("-------------------------Creation of Dictionary--------")

d1 = {} # empty dictionary
d2 = dict()
print(d1)
print(d2)
print("-----------------------------")

# if you know data already

d3 = {101: 'John', 200: 'Ravi' , 'A' : 2000 , 101 : 'Shiva' }

print("-----------------------------")
# from other collections to dictionary

l = [(10,'a'),(20,'b'),(30,'c')] # List of tuples

# Various combination possible
# 1. Tuples of Tuples
# 2 Set of tuples
# 3. Set of Tuples
# 4 List of Lists
# 5 Tuple of Lists
# 6 Set of Lists    ------- Not Possible


d4 = dict(l)
print(d4)  # {10: 'a', 20: 'b', 30: 'c'}

print("-----by set of tuples --- ")
ls = {(10,'a'),(20,'b'),(30,'c')}
d5 = dict(ls)
print(d5)
print("---- by list of list-----")
ll = [[10,'a'],[20,'b'],[30,'c']]
d6 = dict(ll)
print(d6)

print(" ----- By using dynamic input")

dd = eval(input("enter dictionary"))
print(dd)

