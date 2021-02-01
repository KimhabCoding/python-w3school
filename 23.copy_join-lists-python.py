list1 = ['FoodPanda', 'Nham24', 'PassApp', 'ABA']
# finallist1 = list1.copy()
# Method 2 Style Copy 
finallist2 = list(list1)
print(finallist2)

# Join Lists 
# Style Join 1 
list2 = [1, 2, 45, 67, 92, 12, 22, '012']

list12 = list1 + list2 
list21 = list2 + list1 

# Style Join 2 
for x in list2:
      list1.append(x)
      
# Style Join 3 Extend 
list12.extend(list1)
# print(list12)
print(list21)
print(list1)
print('List12')
print(list12)
