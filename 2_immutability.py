from helper import d

# Immutability means the data of a tuple cannot be adjusted at its location in memory

tup1 = (1,2,3,4,5)
print(tup1)

# tup1[3] = 'four' # throws a TypeError since tuples can do this, lists can though!

# YOU CANNOT CHANGE TUPLE DATA IN PLACE

d()

# small workaround  to change items in a tuple
# we can type cast the tuple into a list, make our changes, convert it back to a tuple
print(id(tup1))
tup1 = list(tup1) # type cast into a list
tup1[3] = 'four' # change some data
tup1 = tuple(tup1) # type cast back into a tuple
print(id(tup1))

print(tup1)

d()

#-- Concatenating tuples : adding them together

tup1 = 1,2,3,4,5
tup2 = 6,7,8,9,10
tup1 += tup2
print(tup1)

#-- repeating tuples

short_story = 'A Tale',
print(short_story)
anothology = short_story * 3
print(anothology)