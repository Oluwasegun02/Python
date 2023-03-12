names = {'hemmy', 'brooke', 'segun', 'Adebayo'}

print(names)

# Add new person
names.add('Olu')
print('After add: {}'.format(names))

#Remove a person
names.remove('segun')
print(f'After remove: {names}')

# Clear set
names.clear()
print(f'After clear {names}')