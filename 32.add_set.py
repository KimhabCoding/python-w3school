var_set = {"Hack Crush", "Love Cr", "Python"}
#syntax: var.add('Love you')
var_set.add('Facebook')
print(var_set)
#syntax: var.update('iterable')
vs2 = {"Hack Crush", "Love Cr", "Python", "Love you now", "Who am I"}
vs2_2 = {'Hack2', 'Love you hack'}
vs2.update(vs2_2)
# Update 
print('***Update***')
print(vs2)
# Update Other iterable 
v3 = ['List2', 'Void-19', 'N8']
vs2.update(v3)
print('Update vs2 second')
print(vs2)