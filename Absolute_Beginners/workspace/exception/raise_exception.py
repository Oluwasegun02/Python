def add_name(name):
    """Add a new name to the database"""
    if len(name) < 2:
        raise ValueError('Name is too short.')
    print(f'Name added: {name}')


try:
    add_name('a')
except ValueError as ve:
    print(f'unable to add name: {str(ve)}')