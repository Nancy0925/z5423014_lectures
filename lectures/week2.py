lst1 = ['a']
#print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
#print(f'This is lst2: {lst2}')

lst2[1].append('c')
#print(f"This is lst2 after modifying it: {lst2}")

#print(f"This is lst1 after modifying lst2: {lst1}")

lst1 = ['a']
#print(f'This is lst1: {lst1}')

lst3 = ['b', ['a']]
#print(f'This is lst3: {lst3}')

lst3[1].append('c')
#print(f"This is lst3 after appending 'c': {lst3}")

print(f"This is lst1 after modifying lst3: {lst1}")