upset = {'Love Crush', 'google', 'N8'}
upset1 = {12, 92, 22, 'google'}
# update 
""" print('Update')
upset.update(upset1)
print(upset)
# uninon 
upset2 = {False, 'Covida', 'Love you', 12, 'google'}
print('Union')
# Return new set 
up3 = upset1.union(upset2)
print(up3)
# intersection_update
print('intersection_update')
upset.intersection_update(upset1)
print(upset) # google 
print('intersection')
# return a new set 
up4 = upset1.intersection(upset2) # 12, 'google'
print(up4) """
# symmetric_difference_update 
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple', 'cherry'}
upset.symmetric_difference_update(upset1) 

# return a new set 
xy = x.symmetric_difference(y)
print(xy) # 
