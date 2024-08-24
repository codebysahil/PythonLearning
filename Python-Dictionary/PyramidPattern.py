# wap a program to print pyramid 

# enter the no of rows for the pyramid height4
#    * 
#   * * 
#  * * * 
# * * * * 

n = int(input("enter the no of rows for the pyramid height"))

for i in range(n):
    print(' ' * (n-i-1) + '* ' * (i+1) )
