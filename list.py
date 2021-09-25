subscribe = 1000
likes = 100
comment = 50
# if subscribe > 1000 and likes > 50 and comment = 50:
#   print('good video')
# in short we can use list
condition = [subscribe > 500,
             likes > 50,
             comment > 50
        ]

if all(condition):
    print('good video')
# if subscribe > 1000 or likes or 50 and comment = 50:
#   print('good video')

check = [subscribe > 500,
             likes > 50,
             comment > 50
        ]
if any(condition):
    print('good')