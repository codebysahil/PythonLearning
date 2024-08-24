# wap to enter name and marks in a dict and display them on call

n = int(input("Enter number of student"))

stuDict ={}
for i in range(n):
    name = input("enter name of the student")
    marks = int(input("enter marks of the student"))
    stuDict[name] = marks

print(stuDict) # {'rakes': 47, 'sunam': 78, 'rohan': 89, 'macmohan': 89}


print("-------------------------------------------------------------")

for name in stuDict:
    print(name, '\t \t' ,stuDict[name])