tuple1 = ('I love my crush', 'Love you', 'Steve Jobs', 'Elon Mask')
print(tuple1[0])
print(tuple1[2])
# Note 
"""
    index of tuple = len-1 
    e.g len = 3, index = 2 
"""
print('***Negative Index[-1]')
print(tuple1[-1])
print('[1:3]')
print(tuple1[1:3])
print('[3:]')
print(tuple1[3:])
print('[:2]')
print(tuple1[:2])
print('[-4:-1]')
print(tuple1[-4:-1])
print('Check item in tuples')
if 'steve Jobs' in tuple1:
    print('Yes it is.')
else: 
    print('No it is.')