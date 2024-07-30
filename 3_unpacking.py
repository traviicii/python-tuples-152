from helper import d

# Unpacking Tuples

# reminder
packed = 'bacon', 'lettuce', 'tomato'
print(packed)

# Basic unpacking

first, second, third = packed
print(first)
print(second)
print(third)

# Will throw ValueError if the variables and items are not equal in number
#-- too many values to unpack, not enough variables
#-- too many variables, not enough data to unpack into them
d()

# Extended unpacking : *var takes any additional data and packs it into a list

enhanced_blt = 'bacon', 'lettuce', 'tomato', 'mayo', 'avocado', 'everything bagel seasoning'
print(enhanced_blt)

d()

first, second, third, *condiments = enhanced_blt
print(first)
print(second)
print(third)
print(condiments)
d()

story = 'intro', 'conflict', 'buildup', 'big reveal', 'climax', 'conclusion'
beginning, fight, *middle, end = story
print(beginning)
print(fight)
print(tuple(middle))
print(end)

# you can not have multiple * expressions or you'll get a SyntaxError