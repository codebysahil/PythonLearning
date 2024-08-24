my_dict = dict()
print(my_dict)  # {}

my_dict2 = {}
print(my_dict2)  # time complexity and space complexity is o(1) for an empty dictionary

eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)
eng_sp1 = {'one':'uno','two':'dos'}
print(eng_sp1) # time complexity and space complexity is o(n) for an  dictionary
# list of tuples to create a dictionary

eng_sp_list = [('one','uno'),('two','dos')]

eng_sp2 = dict(eng_sp_list)
print(eng_sp2)

myDict = {'name':'eddy','age':36}
print(myDict)
myDict['name'] = 'george'
print(myDict)
myDict['isEmployee'] = True
print(myDict)

# Traversing the dictionary

def tranverseDict(dict):
    for key in dict:
        print(key,':\t' ,dict[key])


tranverseDict(myDict)


def searchDict(dict,key):
    if key in dict:
        print("The value is " , dict[key])
    else:
        print("not found ..")


searchDict(myDict,'rohan')