names = ['Brooke', 'segun', 'hemmy']

# Update name by index
names[2] = 'olumide'

# Append name
names.append('mojisola')

#Extend list with 3 more items
names.extend(['jame','diva', 'timileyin', 'diva'])

# Remove name
names.remove('segun')

# Remove first namefrom list
removed_from_list = names.pop(0)
print(f'Removed: {removed_from_list}')

# count the number of name that is given 
count = names.count('diva')
print('{} diva in the list '.format(count))

# Print list of names
print(names)

# Print names as specific index
print(names[2])

if 'jame' in names:
    print('jame is in the list')

if 'segun'not in names:
    print('segun is  Not in the list')