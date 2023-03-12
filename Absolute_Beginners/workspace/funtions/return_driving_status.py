def is_old_enough(age, location):
    """Return boolean which determines if the user is old enough to drive."""
    if age >= 17 and location == "UK":
        return True

    if age >= 16 and location == 'Canada':
        return True
    
    if age >= 18 and location == 'Nigeria':
        return True

    return False

def output_driving_status(age, location, passed_driving_test):
    """Output message stating users driving status."""
    old_enough = is_old_enough(age, location)
    if old_enough is False:
        print('YOu are not old enough to drive yet.')
        return
    
    if passed_driving_test is False:
        print('You may learn to drive.')
    else:
        print('You are allowed to drive')

output_driving_status(18, 'Nigeria', False)