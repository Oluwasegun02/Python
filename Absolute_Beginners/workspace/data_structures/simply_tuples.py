things = ('Car', 'Fan', 'Cup', 'Mog', 'Glass', 'Mog')

print(things)

# number of times 'Mog' appears
mug_count = things.count('Mog')
print('Mog appears {} times.'.format(mug_count))

# Index of 'Mog'
mog_index = things.index('Mog')
print(' Index of Mog: ', mog_index, 'good to have Mug writing as Mog', mug_count, 'times')

# 
first_item = things[0]
print('frist item ', first_item)