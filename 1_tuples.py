from helper import d

# Tuples!

# What are tuples?
#-- Tuples are a data type that are similar to lists, with the exception that they are immutable

#-- immutable : you cannot change or edit the data of a tuple, but we can reassign what is stored in a variable
#-- ordered : just like lists they have an order, we can access elements ina tuple by indexing
#-- like lists, tuples can store a variety of objects, any data type, including duplicate elements

# why bother?
# you can create a collection of data that cannot be changed by you or another developer
# iterating over a tuple is much faster than iterating over a list


# We can use () to define tuples, just like a list we use [] empty_list = []
empty_tup = () # <------ emtpy tuple

# singleton, tuple with one element inside of it
singleton = ('element',) # requires a trailing comma for python to see it as a tuple

print(type(singleton))
print(singleton)

d()

# Tuple with multiple items inside of it
# With multiple items inside of a tuple, you no longer need a trailing comma

pop_tup = ('this', 'is', 'a', 'populated', 'tuple')
print(type(pop_tup))
print(pop_tup)

variety_tup = (4, 'five', 6.0, [7,8,9], {'ten': 10}, (11,)) # can store just about anything
print(type(variety_tup))
print(variety_tup)

duple = (True, True, True, False, True, False, True) # can also store duplicate data
print(type(duple))
print(duple)

d()
# packing tuples

# we can pack tuples, without parenthesis
packed = 't-shirt', 'pants', 'jacket', 'tuple'
print(type(packed))
print(packed)

# packing multiple tuples into one variable
tup_pack = pop_tup, variety_tup, duple
print(type(tup_pack))
print(tup_pack)

d()

# indexing into a tuple

pop_tup = ('this', 'is', 'a', 'populated', 'tuple')
print(pop_tup[3][4]) # looking at the 3rd index and then indexing into the string stored there to get what is at the 4th index
print(pop_tup[1])
print(pop_tup[1][1])

variety_tup = (4, 'five', 6.0, [7,8,9], {'ten': 10}, (11,))
print(variety_tup[3][0])

d()

# slicing [start:stop:step] : default start = 0 and stop = end of the tuple
# if you specify a stop value, that stop value is non-inclusive

duple = (True, True, True, False, True, False, True)
sub_tup = duple[:3] # creating a slice (which results in a "sub tuple")
print(sub_tup[1]) # indexing into that new sub tuple
print(duple[1:4])
print(duple[3:6])

d()

historical_record = ('Medieval Era', ('knights', 'Castles', ('King', 'Queen')), 'Rennaissance Period')
print(historical_record[1][2][1]) # the string 'Queen' only
print(historical_record[1][1:]) # sub tuple/ slice of 'Castles', 'King', 'Queen'

d()

#indecies      0     1     2      3         4          5
variety_tup = (4, 'five', 6.0, [7,8,9], {'ten': 10}, (11,))
print(variety_tup[3][1]) # 8
print(variety_tup[4]['ten']) # 10