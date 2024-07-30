from helper import d

# Tuple methods

# tuples don't have any methods of their own

#-- tuple.count(item) : counts how many times an items appears in a tuple

shopping = 'eggs', 'milk', 'creamer', 'creamer', 'creamer', 'chicken'

print(shopping.count('creamer'))
print(shopping.count('chicken'))

d()

#-- len(tuple) : returns the length of the given item

print(len(shopping))

d()

#-- tuple.index(item) : return the first index of that item

print(shopping.index('creamer'))
print(shopping.index('chicken'))

d()

#-- membership checks of a tuple, if item in tuple, 'in', return True or False

print('creamer' in shopping)
print('Cinnamon Toast Crunch' in shopping)

nest = 'start', ('early', 'middle', 'towards end'), 'end'

for item in nest:
    if isinstance(item, tuple) and 'middle' in item:
        print('I found the middle!!')