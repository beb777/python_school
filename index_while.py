import os
email = os.getenv('EMAIL')
name = 'bethelhem'
index = 0
while index <len(name):
    letter = name[index]
    print(index, letter)
    index = index+1
print(email)