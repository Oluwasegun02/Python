file_path = 'output.txt'

text_lines =[
    '\nHello\n',
    'My name is: \n',
    'Segun',
]
with open(file_path, 'a') as f:
    f.writelines(text_lines)
