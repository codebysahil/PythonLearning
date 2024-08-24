# operators in dictionary

d1 = {100:'A', 200: 'C'}
d2 = {300: 'C', 400: 'D'}
d3 = {100:'A', 200: 'C'}

# d3 = d1 + d2 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#  d4 =d1 * 3  # TypeError: unsupported operand type(s) for *: 'dict' and 'int'


print(d1 == d2) # False
print(d1 == d3) # True content must be same and not the order

# relational operators not applicable to dictionary
# membership operator checks only for keys not values

print(100 in d1)
print(100 in d2)