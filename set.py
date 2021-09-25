x = [3, 5, 5, 3, 5, 5]
# to remove dublication convert a list to set
print(x)
x = list(set(x))
print(x)
repeted = max(set(x), key=x.count)
print(repeted)