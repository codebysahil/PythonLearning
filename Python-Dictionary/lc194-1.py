# finding key based on values

myDict = {101: 'DU', 102: 'PU',103: 'MDU',104:'KU'}

val = input("Enter the value you want key for...")

for k,v in myDict.items():
    # print(k)
    if myDict[k] == val:
        print(k)






