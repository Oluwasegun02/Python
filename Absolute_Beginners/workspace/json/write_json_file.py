import json
import os

dir_path = os.path.join(os.getcwd(), 'output')
os.makedirs(dir_path, exist_ok=True)
json_path = os.path.join(dir_path, 'user.json')

user = {
    'name': 'Segzy',
    'age': 19,
    'is_active': True,
    'fav_nums': [1, 4, 6, 8, 9],
}

with open(json_path, 'w') as jf:
    json.dump(user, jf, sort_keys=True, indent=2)