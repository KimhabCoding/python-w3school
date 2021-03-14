var_dictcopy = {'username': 'HKimhab', 'comment': 'Love you', 'facebook_account': 'HOR Kimhab'}
print(var_dictcopy)
print('Method copy dictionary')

new_vardict = var_dictcopy.copy()
print('New copy dictionary')
print(new_vardict)

# method 2 
print('Method copy dictionary Style2')
print('Method Copy2', dict(var_dictcopy))