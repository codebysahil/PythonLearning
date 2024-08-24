# access data from the dictionary

ds = {101: 'John', 200: 'Ravi' , 300 : 2000 }

print(ds[101]) # ds[key]

print(ds[200])

# if specified key is not available then key error

# print(ds[900]) # KeyError: 900

key = int(input("Enter the key"))

if key in ds:
    print(ds[key])
    ds[key] = "Test"
    print(ds)
else:
    print("key is not available")
    ds[key] = "Test1"
    print(ds)
print("-------------")

