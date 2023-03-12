def output_welcome_text(first_name, 
                        last_name, 
                        age, 
                        location, 
                        returning_user=True):
    """output welcome text with users details"""
    if returning_user:
        msg_start = f'Welcome back {first_name} {last_name}!'
    else:
        msg_start = f'Welcome {first_name} {last_name}!'
    msg = f'{msg_start} you are {age} and from {location}.'
    print(msg)


output_welcome_text(
    'Segun',
    'Adegboyega',
    age=19,
    location='Nigeria'
)