 # wap to get the o/p in the format ( if n =3 )
    AAA
    BBB
    CCC


n = int(input("enter the no of rows"))
for i in range(n):
    print(chr(65+i)  * n )
