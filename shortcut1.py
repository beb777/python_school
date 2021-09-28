

condition = True
if condition:
    x = 1
else:
    x = 0
print(x)
'''
shortcut for the above statement

'''
condition = False
x = 1 if condition else 0
print(x)
'''
number separation to make more readable using underscore 
'''
z = 1000000000000
y = 200000000000
sum = z + y
print(sum)

z = 1_000_000_000_000
y = 200_000_000_000
sum = z + y
print(sum)
print(f'{sum:,}')
