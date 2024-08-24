# setdefault(k,v) --> if the specified key is not available then the new key value will be added
# if the specified key is available then value is returned without any replacement

d = {101:'s',102:'q'}

print(d.setdefault(103,'we'))
print(d)