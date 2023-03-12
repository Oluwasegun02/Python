x = 1
while x < 10:
    if x == 4:
        '''this code don't show 4 while printing'''
        x += 1
        continue
       # or break
    print(x)
    x += 1