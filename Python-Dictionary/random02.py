# **
# **


# n = int(input("enter the no of rows"))
#
# for i in range(n,n+1):
#     for j in range(i+1):
#         print("*" * j)
#


# for i in range(1,4): # ( 1,2,3)
#     for j in range(1,2): # ( 1,2) ==> 1
#         print(j)
#
# n = int(input("enter the no of rows"))
#
# for i in range(n):
#     print("*" * n)
#
# n = int(input("enter the no of rows"))
#
# for i in range(n):
#     print(str(i+1) * n)


# n = int(input("enter the no of rows"))
# chr_index = 65
#
# for i in range(n):
#
#     print(chr(chr_index) * n)
#     chr_index = chr_index+1
#
#
#
n = int(input("enter the no of rows"))
for i in range(n):
    print(chr(65+i)  * n )