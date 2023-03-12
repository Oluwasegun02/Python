dog = {
    'name': 'Daisy',
    'breed': 'Chihuahua',
    'coluor': 'Fawn',
}
print(dog)

dog['age'] = 10
print(dog)

dog['age'] = 11
print(dog)

# removed from the dictionary
age = dog.pop('age')
print(f'Removed age: {age}')
print(dog)

# after removing the age try to retrive it and set the defuat vvalue to Age not set
age = dog.get('age', 'Age not set')
print(f'Age after removing it: {age}')

# Copy the dictionary
fog = dog.copy()
print(f'copy the dog to fog: {fog}')

# Clear the dictionary
dog.clear()
print(dog)