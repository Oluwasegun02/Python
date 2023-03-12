def output_welcome_text(name, returning_user=True):
    """output welcome text with provided name."""
    if returning_user:
        message = f'Werlcome back {name}!'
    else:
        message = f'Welcome {name}!'
    print(message)

output_welcome_text(name='segun')
output_welcome_text('hemmy', False)
output_welcome_text('olumide', returning_user=True)