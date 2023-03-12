cart = [
    {'name': 'Pencil'},
    {'name': 'Paper'},
    {'name': 'Stapler'},
]

try:
    item = cart[2]
    product = item['name']

except IndexError:
    print('Not in cart.') 
except KeyError:
    print('Product key not found')
except LookupError:
    print('Index or key not found.')
else:
    print(f'Product: {product}')
finally:
    print('Finished checking.')
