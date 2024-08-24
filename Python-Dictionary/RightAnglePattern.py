# wap to print Right Angle Triangle pattern with * symbols

# for example 
# if n = 5 then o/p should be 

# *
# **
# ***
# ****
# *****



n = int(input("Enter the no of rows for the triangle"))
for i in range(1, n + 1):
    print("*" * i)
