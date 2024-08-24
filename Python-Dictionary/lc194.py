# wap to get value from the dict for the given key
myDict = {101: 'DU', 102: 'PU',103: 'MDU',104:'KU'}
key = int(input("enter the key you want the value for ..."))

if key in myDict: # 101,102,103,104
    print(myDict[key])
else:
    print("key not found")


if key in myDict:
    print(myDict.get(key))
else:
    print("key is not available")