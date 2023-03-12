import os
base_dir = os.getcwd()
#print(base_dir)
sub_dir='output'
full_dir_path = os.path.join(base_dir, sub_dir)
#print(full_dir_path)
os.makedirs(full_dir_path, exist_ok=True)
file_path = os.path.join(full_dir_path, 'message.txt')
with open(file_path, 'a') as msg:
    msg.write('Hello\n')