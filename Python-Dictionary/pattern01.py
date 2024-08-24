# n = int(input("enter the number of rows ")) # n =3
#
# for i in range(1,n+1): # ( 1,4) ==> (1,2,3)
#     for j in range(i):# j ( 1)
#         # print("*" * n)
#           print(i)
#           print("----")
#           print(j)


# n = int(input("enter the number of rows ")) # n =3
#
# for i in range(1,n+1): # ( 1,4) ==> (1,2,3)
#     for j in range(i):# j ( 1)
#         # print("*" * n)
#         #   print(i)
#         #   print("----")
#           print(j, end = '')
#           print("----")


n = int(input("enter the integer no of values"))
for i in range(1,n+1):
    for j in range(i,i+1):
        print("*" * n)
