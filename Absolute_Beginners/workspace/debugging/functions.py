def add(x, y):
    """Add two numbers together and return resuit."""
    result = x + y
    return result

output_prefix = 'Total'
total = add(34, 9)
meg = f'{output_prefix} {total}'

print(meg)