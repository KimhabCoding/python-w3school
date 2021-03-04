dict_py = {
    # username is key and HKimhab is value 
    'username': 'HKimhab', 
    'honey name': 'Crush DSK', 
    'position': 'Web Developer'
}

# dict['key']
print(dict_py['honey name'])

# Dict.get('key')
print(dict_py.get('username'))

# Get all keys 
kh = dict_py.keys()
print('Before change')
print(kh)

print('After Change')
dict_py['phone_number'] = '0963456921'
print(kh)
# print(dict_py.keys())

print('\nDict.values()')
kh = dict_py.values()
print('Before change')
print(kh)

print('After Change')
dict_py['phone_number'] = '0963456922'
print(kh)

dict_item = dict_py.items()
print('\nGet Items()')
print(dict_item)

print('\n Add key by items')
dict_py['facebook name'] = 'Kimhab'
print(dict_item)

print('\nCheck if key Exits')
if 'username' in dict_py: 
    print('Key in dict')
else:
    print('Key is not in dict')