# Lecture Notes: Tuples

## #1 Tuples
### What are tuples?
- Tuples are a datatype similar to a list, with the exception that they are immutable

- Characteristics:
    - Immutable : you cannot edit the data of a tuple with having to reassign it.
    - Ordered : Like lists they have an order, and you can access the elements by index
    - Like lists, they can store a variety of objects including duplicate objects

### Why bother:

- Create a collection that will not be changed by you or another dev

- Iterating over a tuple is faster than iterating over a list.

### Creating Tuples

```python
# we use () to define tuples
empty_tup = ()

# singleton, tuple with one item
singleton = ('element',) # requires a trailing comma

print(type(singleton))
print(singleton)
```

### Multi-element tuples

```python
#multi-element tuple: don't need a trailing comma

pop_tup = ('this', 'is', 'a', 'populated','tuple')
print(pop_tup)

variety_tup = (4, 'Five', 6.0, [7,8,9], {'ten': 10}) #can store just about anything
print(variety_tup)

duple =(True, True, True, False, False, False) #and also store duplicates
print(duple)
```

### Packing tuples

```python
# packing tuples : without parens
packed = 't-shirt', 'pants', 'jacket', 'socks'
print(packed)
print(type(packed))

#pakcing vars into tuple
tup_pack = pop_tup, variety_tup, duple
print(tup_pack)
```

### Indexing and Slicing into tuples

```python
pop_tup = ('this', 'is', 'a', 'populated','tuple')
print(pop_tup[3][4])
print(pop_tup[1])


variety_tup = (4, 'Five', 6.0, [7,8,9], {'ten': 10}) #can store just about anything
print(variety_tup[3][0])


print(tup_pack)
print(tup_pack[1][-1]['ten'])
```

```python
#Slicing [start:stop] : default start = 0 and stop = end of the tuple
# specified stop value is not included

duple =(True, True, True, False, False, False) #and also store duplicates
print(duple[:3]) #return a sub-tuple from 0-3 

print(duple[1:4])

print(duple[3:6])
```

### In class indexing
```python
historical_record = ("Medieval Era", ("Knights", "Castles", ("King", "Queen")), "Renaissance Period")
print(historical_record[1][2][1])
```

## #2 Immutability

### Immutablitiy means the data of a tuple cannot be adjusted in its location in memory

```python
tup1 = (1,2,3,4,5)
print(tup1)

tup1[3] = 'four' # Will throw a TypeError since tuples cant do this

#YOU CANT CHANGE TUPLE DATA IN PLACE
```

```python
#  Small work around to chane items in a tuple
#convert the tuple into a list, make changes, convert back to tuple
tup1 =  1,2,3,4,5
print(id(tup1))
tup1 = list(tup1)
tup1[3] = 'four'
tup1 = tuple(tup1)
print(id(tup1))
```

```python
#-- concatenating tuples : adding them together

tup1 = 1,2,3,4,5
tup2 = 6,7,8,9,10

tup1 += tup2
print(tup1)
```

```python
#-- repeating tuples

short_story = 'A tale', #make sure to have your trailing comma
print(short_story)
anthology = short_story * 3
print(anthology)
```

## #3 Unpacking Tuples

```python
#packing tuples reminder

packed = 'bacon', 'lettuce', 'tomato'
print(packed)

#basic upacking

first, second, third = packed

print(first)
print(second)
print(third)

#Will throw a ValueError if the vars and items are not equal
#-- too many values to unpack
#-- not enough values to unpack
```

```python
#extended unpacking : takes addition varless values and packs them into a list

#everything that doesnt have a home, ends up in the star bin
enhanced_blt = 'bacon', 'lettuce', 'tomato', 'mayo', 'avocado', 'everthing bagel seasoning'
print(enhanced_blt)
first, second, third, *condiments = enhanced_blt
print(first)
print(second)
print(third)
print(condiments)

story = 'intro', 'conflict', 'build', 'big reveal', 'climax', 'conclusion'

beginning, fight, *middle, end = story
print(beginning)
print(tuple(middle))

print(end)
print(fight)

#You can't have multiple * expressions or you'll get a SyntaxError
```

## #4 Looping

Looping over tuples is the exact same as looping over lists

```python
#we can write a function that loops over a given tuple

## EX 1
def tup_loop(atuple):

    for item in atuple:
        print(item)

my_tup = 'apple', 'banana', 'orange'

tup_loop(my_tup)

## EX 2
def while_tup(atuple):
    i = 0
    while i < len(atuple):
        print(atuple[i])
        i+= 1

teams = 'Bull Dogs' , 'Falcons', 'Hawks', 'Braves'

while_tup(teams)
```

### Enumerate function

```python
#-- enumerate() : allows you to iterate over the index and item at the same time


today = 'woke up', 'ate breakfast', 'went to the gym', 'prepped lecture', 'ate lunch', 'graded', 'meetings', 'in class'

# enumerate() returns a tuple of each item and its index
for task in enumerate(today): #task is a tuple of the index and item
    print(task[1])

print('--------------------')

for idx, task in enumerate(today):
    print(idx)
    print(task)
```

## #5 Methods

```python
#Tuples don't have too many methods

#-- tuple.count(item) : counts how many times an item appears in a tuple

shopping = 'eggs', 'milk', 'creamer', 'creamer', 'creamer', 'creamer', 'chicken'

print(shopping.count('creamer'))

#-- len(tuple) : give the length of the tuple

print(len(shopping))

#-- tuple.index(item) : returns the first index of an item

print(shopping.index('chicken'))
print(shopping.index('creamer'))


#-- Membership checks of a tuple, if item in tuple, 'in', Returns True or False depending

print('creamer' in shopping)
print('Cinnamon Toast Crunch' in shopping)

nest = 'start', ('early', 'middle', 'towards end'), 'end'

for item in nest:
    if isinstance(item, tuple) and 'most' in item:
        print('I found the middle')
```