vdict = {'product_id': 123484, 'product_name': 'CocaCola', 'price': 2000}
# product_id is key , 123484 is value
print('loop by key in dict')
for kh in vdict: 
    print(kh)

# loop by value 
print('\nLoop by value')
for i in vdict: 
    print(vdict[i])
    
# Return value of dict 
print('\nLoop by values()') 
for i1 in vdict.values(): 
    print(i1)
    
# Return value of dict 
print('\nLoop by keys()') 
for i2 in vdict.keys(): 
    print(i2)

# Return key and value of dict 
print('\nReturn key and value of dict')
for x, y in vdict.items():
    print('Key') 
    print([x])
    print('value') 
    print([y])
    