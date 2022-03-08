<div align="center">

# Python Programming Language Notes

### Most of References are from [Complete Python3 Bootcamp](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp) and this is [course instructor](https://www.udemy.com/user/joseportilla/). Some are Youtube , Linkin instructors , websites and more. Make Credit For All Source References!

</div>

<br>

<details><summary>Data Structure and Algorithms</summary>
<p>
<br>

# Data Structure and Algorithms

<details><summary>Data Structure</summary>
<p>
<br>

# Data Structure

`A data structure is just an intentional arrangement of data`


</p>
</details>

---

<details><summary>Algorithms</summary>
<p>
<br>

# Algorithms


</p>
</details>

</p>
</details>

---

<details><summary>Chapter-1</summary>
<p>
<br>

# Object and Data Structure Basics

<details><summary>1. Number</summary>
<p>
<br>

## Number

Python has various "types" of numbers (numeric literals). Integers are just whole numbers, positive or negative. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.

```py
print(4E2)

a = .1 + .1 + .1 + .3 
print(type(a))
print(a)
# if sum the floating point number, result will not accuracy
# To accuracy, u can use a decimal module

import decimal
b = decimal.Decimal('.1')
c = decimal.Decimal('.3')
a = b + b + b -c
print(a)
print(type(a))

# or import module
from decimal import *
b = Decimal('.1')
```

### _Basic Arithmetic_

The // operator (two forward slashes) truncates the decimal without rounding, and returns an integer result.

Order of Operations followed in Python

`PEMDAS ==> Parentheses, Exponents, Multiplication, Division, Addition, Subtraction`

```python
# Addition
print(2+1)

# Subtraction
print(2-1)

# Multiplication
print(2*2)

# Division
print(3/2)

# Floor Division
print(7//4)

# Modulo
print(7%4)

# Powers
print(2**3)

# Can also do roots this way
print(4**0.5)

# Nested Arithmetic
print(2 + 10 * 10 + 3)
```

### _Assigning Variables_

Variable assignment follows name = object, where a single equals sign = is an assignment operator

```python
a = 5
```

</p>
</details>

---

<details><summary>2. String</summary>
<p>
<br>

## String

Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).This idea of a sequence is an important one in Python

```python
print('Hello World 1')
```

## _String Basics_

Python's built-in len() function counts all of the characters in the string, including spaces and punctuation.

```python
print(len('Hello World'))
```

## _String Indexing_

We know strings are a sequence, which means Python can use indexes to call parts of the sequence. In Python, we use brackets [] after an object to call its index. We should also note that indexing starts at 0 for Python.

```python
# Assign s as a string
s = 'Hello World'
print(s[0])
print(s[1])
print(s[2])
```

We can use a : to perform slicing which grabs everything up to a designated point. For example:

```python
print(s[1:])
print(s[:3])

#Everything
print(s[:])

# Last letter (one index behind 0 so it loops back around)
print(s[-1])

# Grab everything, but go in steps size of 1
print(s[::1])

# We can use this to print a string backwards
print(s[::-1])
```

## _String Properties_

It's important to note that strings have an important property known as immutability. This means that once a string is created, the elements within it can not be changed or replaced.

```python
# Let's try to change the first letter to 'x'
print(s[0] = 'x')

# multiplication symbol to create repetition!
print(s[0]*10)
```

## _Basic Build-in String method_

Objects in Python usually have built-in methods. These methods are functions inside the object. Methods are in the form:
`object.method(parameters)`

```python
# Upper Case a string
print(s.upper())

# Lower Case
print(s.lower())

# Split a string by blank space (this is the default)
print(s.split())

# Split by a specific element (doesn't include the element that was split on)
print(s.split('W'))

# string module
import string
xxx = string.ascii_lowercase
print(xxx)

text = 'We are ready'
text.split()[::-1]

joinMethod = ' '.join(['Hello','I','am','Lewis'])
print(joinMethod)
```

## _Print Formatting with Strings_

String formatting lets you inject items into a string rather than trying to chain items together using commas or string concatenation. As a quick comparison, consider:

```python
player = 'Thomas'
points = 33

print('Last night, '+player+' scored '+str(points)+' points.')  # concatenation

print(f'Last night, {player} scored {points} points.' )         # string formatting

# Print statement
state_list = [1,2,3,4]
print("Below starts with space")
print("", state_list[0])
print("", *state_list, sep=".")
print("", *state_list, sep="\n")
```

## _Formatting with the .format() method_

`'String here {} then also {}'.format('something1','something2')`

```python
# index position
print('The {2} {1} {0}'.format('fox','brown','quick'))

# assigned keywords
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))

# reused , avoiding duplication
print('A {p} saved is a {p} earned.'.format(p='penny'))
```

## _Alignment, padding and precision with .format()_

Within the curly braces you can assign field lengths, left/right alignments, rounding parameters and more

```python
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
```

<br>

By default, .format() aligns text to the left, numbers to the right. You can pass an optional <,^, or > to set a left, center or right alignment:

```python
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
```

<br>

You can precede the aligment operator with a padding character

```python
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
```

## _Formatted String Literals (f-strings)_

```python
name = 'Fred'

print(f"He said his name is {name}.")
```

<br>

`print(f"result: {value:{width}.{precision}}")`

Note that with f-strings, precision refers to the total number of digits, not just those following the decimal. This fits more closely with scientific notation and statistical analysis. Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it:

```python
# test also
# num = 23.45678
num = 23.45
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")


print(f"My 10 character, four decimal number is:{num:10.4f}")

```

</p>
</details>

---

<details><summary>3. List</summary>
<p>
<br>

# List

Earlier when discussing strings we introduced the concept of a sequence in Python. Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!

```python
my_list = ['A string',23,100.232,'o']
```

Just like strings, the len() function will tell you how many items are in the sequence of the list.

```python
len(my_list)
```

## _Indexing and slicing_

```python
my_list = ['one','two','three',4,5]

# Grab element at index 0
print(my_list[0])

# Grab index 1 and everything past it
print(my_list[1:])

# Grab everything UP TO index 3
print(my_list[:3])

# Make the list double
print(my_list * 2)

# Again doubling not permanent
print(my_list)
```

## _Basic List Methods_

```python
# Create a new list
list1 = [1,2,3]

# Append an item at the end of the list
list1.append('append me!')
list1.append([4,5,6]) # [1,2,3,[4,5,6]]

# Extend the list to another list as item
list1.entend([4,5,6]) # [1,2,3,4,5,6]

# Pop off the 0 indexed item
list1.pop(0)

# Default popped index is -1
list1.pop()

# List index isn't out of range
list1[100]

print(list1)

new_list = ['a','e','x','b','c']

# Use reverse to reverse order (this is permanent!)
new_list.reverse()

# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort()

list4 = [5,3,4,6,1]
sorted(list4)
```

## _Nesting Lists_

```python
# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

# Grab first item in matrix object
matrix[0]


# Grab first item of the first item in the matrix object
matrix[0][0]
```

## _List Comprehensions_

```python
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
```

</p>
</details>

---

<details><summary>4. Dictionaries</summary>
<p>
<br>

# Dictrionaries

Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

```python
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
print(my_dict['key2'])

# dictionaries are very flexible in the data types they can hold
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Let's call items from the dictionary
my_dict['key3']

# Can call an index on that value
my_dict['key3'][0]

# Can then even call methods on that value
my_dict['key3'][0].upper()
```

We can also create keys by assignment. For instance if we started off with an empty dictionary,

```python
# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

print(d)
```

## _Nesting with Dictionaries_

```py
# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# Keep calling the keys
d['key1']['nestkey']['subnestkey']
```

## _Dicrionaries Methods_

```py
# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}

# Method to return a list of all keys
d.keys()

# Method to grab all values
d.values()

# Method to return tuples of all items  (we'll learn about tuples soon)
d.items()
```

`Can you sort a dictionary? Why or why not?`

\*Answer: No! Because normal dictionaries are `mappings not a sequence.`

</p>
</details>

---

<details><summary>5. Unpacking List and Dictionary</summary>
<p>
<br>

# Unpacking List and Dictionary

```py
lst = [1,2,3]
lstModify = [*lst,4,5]
print(lstModify)

dic = {'name': 'wai', 'university': 'Mandalay'}
dicModify = {**dic , 'name': 'Lewis'}
print(dicModify)
```

Advance Examle : 

```py
users= [
    {'name': 'Lewis' , 'age': 22, 'boolean': False},
    {'name': 'Jackson' , 'age': 10, 'boolean': False},
    {'name': 'Davis' , 'age': 18, 'boolean': False},
    {'name': 'Simon' , 'age': 27, 'boolean': False},
    {'name': 'Lucy' , 'age': 20, 'boolean': False}
]

def less20(user):
    """Return True if user age is less than or equal 20 and pass if not"""
    if user['age'] <= 20:
        return {**user, 'boolean': True}
    return user

print(list(map(less20, users)))
```


</p>
</details>

---

<details><summary>6. Tuples</summary>
<p>
<br>

# Tuples

In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.

## _Why to use Tuples_

`You may be wondering, "Why bother using tuples when they have fewer available methods?" To be honest, tuples are not used as often as lists in programming, but are used when immutability is necessary. If in your program you are passing around an object and need to make sure it does not get changed, then a tuple becomes your solution. It provides a convenient source of data integrity.`

## _Constructing with tuples_

The construction of a tuples use () with elements separated by commas.

```py
# Create a tuple
t = (1,2,3)

# Check len just like a list
len(t)

# Can also mix object types
t = ('one',2)

# Show
print(t)

# Use indexing just like we did in lists
t[0]


# Slicing just like a list
t[-1]
```

## _Basic Tuples Method_

```py
# Use .index to enter a value and return the index
t.index('one')

# Use .count to count the number of times a value appears
t.count('one')
```

## _Immutability_

`It can't be stressed enough that tuples are immutable.`

```py
# they will print out error!
t[0]= 'change'

t.append('nope')
```

</p>
</details>

---

<details><summary>7. Sets</summary>
<p>
<br>

# Sets

`Sets are an unordered collection of unique elements. A set has only unique entries. We can construct them by using the set() function.`

```py
x = set()

# We add to sets with the add() method
x.add(1)

#Show
print(x)

# Add a different element
x.add(2)

# Try to add the same element
x.add(1)

# show
print(x)

# That's because a set is only concerned with unique elements! We can cast a list with multiple repeat elements to a set to get the unique elements.

# Create a list with repeats
list1 = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
set(list1)
```

</p>
</details>

---

<details><summary>8. Booleans</summary>
<p>
<br>

# Booleans

`Python comes with Booleans (with predefined True and False displays that are basically just the integers 1 and 0). It also has a placeholder object called None.`

```py
# Set object to be a boolean
a = True
print(a)

# Output is boolean
print(1>2)

# We can use None as a placeholder for an object that we don't want to reassign yet:

# None placeholder
b = None

print(b)

print(1 < 2 < 3)
# The above statement checks if 1 was less than 2 and if 2 was less than 3. We could have written this using an and statement in Python:

print(1<2 and 2<3)
```

## And | Or

```py
a = 0

name = a or 'wai'
name1 = 'wai' or 'hay'

greet = a and 'hay'
greet1 = 'hello' and 'hay'

# Or
"""If on the left side is true, it breaks and returns it. Although on the left side is false, it works on the right side."""

# And
"""If on the left side is true, it works continue to the right end. If on the left side is false, it breaks in it."""


```

Note For Stupid Way

- Or => if flase (or) this works
- And => if false (and) this breaks


---

## isinstance

```py
a = [1,2]
b = {'name': 'wai'}
if isinstance(a, list):
    print('It is list')
else:
    print('Not')

if isinstance(b, dict):
    print('it is dictionary')
else:
    print('not')
```

</p>
</details>

---

</p>
</details>

---

<details><summary>Chapter-2</summary>
<p>
<br>

# Python Statements

<details><summary>1. Python Statements</summary>
<p>
<br>

# Python Vs Other Languages

```python
Version 1 (Other Languages)

if (a>b){
    a = 2;
    b = 4;
}
Version 2 (Python)

if a>b:
    a = 2
    b = 4
```

`Python gets rid of () and {} by incorporating two main factors: a colon and whitespace. The statement is ended with a colon, and whitespace is used (indentation) to describe what takes place in case of the statement.`

`Another major difference is the lack of semicolons in Python. Semicolons are used to denote statement endings in many other languages, but in Python, the end of a line is the same as the end of a statement.`

## _Indentation_

Here is some pseudo-code to indicate the use of whitespace and indentation in Python:

```py
# Other Languages

if (x)
    if(y)
        code-statement;
else
    another-code-statement;

# Python

if x:
    if y:
        code-statement
else:
    another-code-statement
```

</p>
</details>

---

<details><summary>2. if, elif, else Statements</summary>
<p>
<br>

# if, elif, else Statements

if Statements in Python allows us to tell the computer to perform alternative actions based on a certain set of results.

Verbally, we can imagine we are telling the computer:

"Hey if this case happens, perform some action"

We can then expand the idea further with elif and else statements, which allow us to tell the computer:

"Hey if this case happens, perform some action. Else, if another case happens, perform some other action. Else, if none of the above cases happened, perform this action."

```py
if case1:
    perform action1
elif case2:
    perform action2
else:
    perform action3
```

<br>

```py
loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')

# Another

person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person =='George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")
```

</p>
</details>

---

<details><summary>3. For Loops</summary>
<p>
<br>

# For Loops

A for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, such as keys or values.

The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside your loop, for example if you wanted to use if statements to perform checks.

```py
list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')

# Start sum at zero
list_sum = 0
for num in list1:
    list_sum += num
print(list_sum)

# With Tuple
tup = (1,2,3,4,5)
for t in tup:
    print(t)
```

If you are iterating through a sequence that contains tuples, the item can actually be the tuple itself. During the for loop we will be unpacking the tuple inside of a sequence and we can access the individual items inside that tuple!

```py
list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)

# Now with unpacking!
for (t1,t2) in list2:
    print(t1)
```

With tuples in a sequence we can access the items inside of them through unpacking! The reason this is important is because many objects will deliver their iterables through tuples.

Dictionary methods: .keys(), .values() and .items(), In Python each of these methods return a dictionary view object. It supports operations like membership test and iteration, but its contents are not independent of the original dictionary – it is only a view.

```py
d = {'k1':1,'k2':2,'k3':3}

# Create a dictionary view object
d.items()

# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v)

list(d.keys())
# dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():
sorted(d.values())
```

</p>
</details>

---

<details><summary>4. While Loops</summary>
<p>
<br>

# While Loops

The while statement in Python is one of most general ways to perform iteration. A while statement will repeatedly execute a single statement or group of statements as long as the condition is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.

```py
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

else:
    print('All Done!')
```

## _break , continue, pass_

We can use break, continue, and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:

`break`: Breaks out of the current closest enclosing loop.

`continue`: Goes to the top of the closest enclosing loop.

`pass`: Does nothing at all.

break and continue statements can appear anywhere inside the loop’s body.

```py
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue

# break

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue
```

## _Infinity running Loop with while_

```py
# DO NOT RUN THIS CODE!!!!
while True:
    print("I'm stuck in an infinite loop!")
```

</p>
</details>

---

<details><summary>5. For else</summary>
<p>
<br>

# For else

```py
def notice_informal(nums):
    for i in nums:
        if i in (10,20,30):
            print('Yes,it is.')
    else:
        print('No,it is not.')
    print('This is outside.')

notice_informal([1,2,3,4,5])

notice_informal([1,2,3,4,4,4,10])

```

`else is working every situation. We want to print out only else when we don't do even looping is ending. So, we need to break out if we do. while is also same.`

```py
def notice_informal2(nums):
    for i in nums:
        if i in (10,20,30):
            print('Yes,it is.')
            break
    else:
        print('No,it is not.')
    print('This is outside.')

notice_informal2([1,2,3,4])

notice_informal2([2,3,5,2,1,10])
```

</p>
</details>

---

<details><summary>6. Useful Operator</summary>
<p>
<br>

# Useful Operator

There are a few built-in functions and "operators" in Python

## _Range_

The range function allows you to quickly generate a list of integers, this comes in handy a lot, so take note of how to use it! There are 3 parameters you can pass, a start, a stop, and a step size.

This is a generator function, so to actually get a list out of it, we need to cast it to a list with list(). What is a generator? Its a special type of function that will generate information and not need to save it to memory.

```py
range(0,11)

# Notice how 11 is not included, up to but not including 11, just like slice notation!
list(range(0,11))
list(range(0,12))

# Third parameter is step size!
# step size just means how big of a jump/leap/step you
# take from the starting number to get to the next number.
list(range(0,11,2))
list(range(0,101,10))
```

## _Enumerate_

enumerate is a very useful generator function to use with for loops.

```py
index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

```

Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry about creating and updating this index_count or loop_count variable

```py
# save it to memory
print(enumerate('abcd'))

# list out the data
print(list(enumerate('abcd')))

# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
```

## _Zip_

`use the zip() function to quickly create a list of tuples by "zipping" up together two lists.`

```py
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

# This one is also a generator!
zip(mylist1,mylist2)

list(zip(mylist1,mylist2))

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
```

## _in & not in_

We've already seen the in keyword during the for loop, but we can also use it to quickly check if an object is in a list

```py
print('x' in ['x','y','z'])

print('x' in [1,2,3])

print('x' not in ['x','y','z'])

print('x' not in [1,2,3])
```

## _min & max_

Quickly check the minimum or maximum of a list with these functions.

```py
mylist = [10,20,30,40,100]

print(min(mylist))

print(max(mylist))
```

## _Random_

Python comes with a built in random library.

```py
import random

random()                             
# Random float:  0.0 <= x < 1.0

randrange(0, 101, 2)                
# Even integer from 0 to 100 inclusive but not include end-Point

randint(0, 2)
# Include end-Point

choice(['win', 'lose', 'draw'])      
# Single random element from a sequence

deck = 'ace two three four'.split()
shuffle(deck)                        
# Shuffle a list

sample([10, 20, 30, 40, 50], k=4)    
# Four samples without replacement
```

</p>
</details>

---

<details><summary>7. List Comprehension</summary>
<p>
<br>

# List Comprehension

In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.

List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets.

```py
# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print(lst)

# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)

# Nested list comprehension
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)

```

</p>
</details>

---

</p>
</details>

---

<details><summary>Chapter-3</summary>
<p>
<br>

# Methods and Function


<details><summary>Methods</summary>
<p>
<br>

# Methods

Methods are essentially functions built into objects. Later on in the course we will learn about how to create our own objects and methods using Object Oriented Programming (OOP) and classes.

Methods perform specific actions on an object and can also take arguments, just like a function.


`object.method(arg1,arg2,etc...)`

```py
lst = [1,2,3,4,5]
print(lst.append(6))
print(lst.count(3))
```

</p>
</details>

---

<details><summary>Functions</summary>
<p>
<br>

# Functions

## _`What is a function?`_

Formally, a function is a useful device that groups together a set of statements so they can be run more than once. They can also let us specify parameters that can serve as inputs to the functions.

On a more fundamental level, functions allow us to not have to repeatedly write the same code again and again. If you remember back to the lessons on strings and lists, remember that we used a function len() to get the length of a string. Since checking the length of a sequence is a common task you would want to write a function that can do this repeatedly at command.

Functions will be one of most basic levels of reusing code in Python, and it will also allow us to start thinking of program design (we will dive much deeper into the ideas of design when we learn about Object Oriented Programming).

---

## _`Why even use functions?`_
Put simply, you should use functions when you plan on using a block of code multiple times. The function will allow you to call the same block of code without having to write it multiple times. This in turn will allow you to create more complex Python scripts. To really understand this though, we should actually write our own functions!


```py
def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (docstring) goes.
    When you call help() on your function it will be printed out.
    '''
    # Do stuff here
    # Return desired result
```

You must indent to begin the code inside your function correctly. Python makes use of `whitespace` to organize code. Lots of other programing languages do not do this, so keep that in mind.

Next you'll see the docstring, this is where you write a basic description of the function. You'll be able to read these docstrings by hovering onto a function name when you call in. Docstrings are not necessary for simple functions, but it's good practice to put them in so you or other people can easily understand the code you write.

After all this you begin writing the code you wish to execute.

```py
def hello():
    print('hello')

hello()

"""If you forget the parenthesis () when function calls, it will simply display the fact that say_hello is a function."""

print(hello)

```

## _Accepting Parameters(Put Arguments)_

```py
def greeting(name):
    print(f'hello {name}')

greeting('Wai')
```

## _Return_

If we actually want to save the resulting variable we need to use the return keyword.

`return` allows a function to return a result that can then be stored as a variable, or used in whatever manner a user wants.

```py
def addNum(num1,num2):
    return num1 + num2

addNum(1,2)

# Can also save as variable due to return
result = addNum(4,5)
print(result)

# if we input string
addNum('one','two')

# Another 

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

makes_twenty(18,2)
makes_twenty(20,3)
makes_twenty(2,3)
```

### _`Very Common Question: "What is the difference between return and print?"`_
The return keyword allows you to actually save the result of the output of a function as a variable. The print() function simply displays the output to you, but doesn't save it for future use.


### _Example :_

### **Check if any number in a list is even**

`return breaks out of the loop and exits the function`

```py
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Otherwise we don't do anything
        else:
            pass

check_even_list([1,2,3]) # True

check_even_list([1,1,1]) # 
```

And try another way

```py
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # This is WRONG! This returns False at the very first odd number!
        # It doesn't end up checking the other numbers in the list!
        else:
            return False

# UH OH! It is returning False after hitting the first 1
check_even_list([1,2,3])
```

`Correct Approach: We need to initiate a return False AFTER running through the entire loop`

```py
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False

check_even_list([1,2,3])

check_even_list([1,3,5])
```

### **Return all even numbers in a list**

```py
def check_even_list(num_list):
    
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers

check_even_list([1,2,3,4,5,6])

check_even_list([1,3,5])
```

### **Returning Tuples for Unpacking**

Recall we can loop through a list of tuples and "unpack" the values within them


```py
stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]

for item in stock_prices:
    print(item)

for stock,price in stock_prices:
    print(stock)

for stock,price in stock_prices:
    print(price)

# with function
work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)

employee_check(wor_hours)
```

### **Interactions between functions**

Functions often use results from other functions, let's see a simple example through a guessing game. There will be 3 positions in the list, one of which is an 'O', a function will shuffle the list, another will take a player's guess, and finally another will check to see if it is correct. This is based on the classic carnival game of guessing which cup a red ball is under.

```py
from random import shuffle

# Initial List
mylist = [' ','O',' ']


def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    shuffle(mylist)
    
    return mylist

def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        
        # Recall input() returns a string
        guess = input("Pick a number: 0, 1, or 2:  ")
    
    return int(guess)    

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)


# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)
```

### **Function Composition and Curry**

```py
import random

def shuffleList(lst):
    """Shuffle and shuffled list"""

    random.shuffle(lst)
    return lst 

def guess():
    """guess number and return number"""

    guess = ''
    while guess not in [0,1,2]:
        guess = int(input('Guess number 0,1,2: '))
    return guess

def check(fun1,fun2):
    """This is function composition and takes two function"""

    def another(lst):
        """This is curry function"""

        shuffle = fun1(lst)
        guess = fun2()
        if shuffle[guess] == 'O':
            print(shuffle)
            print('yes your guess is true')
        else:
            print(shuffle)
            print('Try another')
    return another

lis = ['','','O']

check(shuffleList,guess)(lis)
```

### **Just For Fun**

```py
def almostThere(num):
    a = num > 100
    b = 200 - num
    print(a,b)
    return not a or b

print(almostThere(109))
```

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

```py
def has33(lst):
    for i in range(0, len(lst)-1):
        if lst[i:i+2] == [3,3]:
            return True 
    return False

print(has33([1,2,3,1,3]))
```

Given a string, return a string where for every character in the original there are three characters

```py
def paperDoll(text):
    result = ''
    for i in text:
        result+= i*3
    return result

print(paperDoll('Hello'))
```

'69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


```py
def summer_69(lst):
    result = 0
    add = True

    for i in lst:
        while add:
            if i != 6:
                result += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
    return result

# Check
print(summer_69([2, 1, 6, 9, 11]))
```

Write a function that takes in a list of integers and returns True if it contains 007 in order


```py
def spy_game(lst):
    """To Check the list it orders 0 0 7"""
    check = [0,0,7,'a']
    for i in lst:
        if i == check[0]:
            check.pop(0)
        else:
            pass
    return len(check) == 1

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0])) 
```

Write a function that returns the number of prime numbers that exist up to and including a given number

```py
# By convension, 0 and 1 are not prime number
def prime(nums):
    result = [2]

    for i in range(3,nums,2):
        for x in range(3,i,2):
            if i % x == 0:
                break
        else:
            result.append(i)
    print(result)
    return len(result)

print(prime(5))
```

Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24

```py
# with recursion

n = 0
def test(x,n):
    if len(x) == n: return 1
    return x[n] * test(x,n+1)

print(test([1, 2, 3, -4],n))
```
</p>
</details>

---

<details><summary>Lambda expression, Map, Filter</summary>
<p>
<br>

# Lambda expression, Map, Filter

# _map Function_

The map function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list.

```py
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

mynames = ['John','Cindy','Sarah','Kelly','Mike']

map(splicer,mynames)

# To get the results, either iterate through map() 
# or just cast to a list
list(map(splicer,mynames))
```

---

# _filter Function_

The filter function returns an iterator yielding those items of iterable for which function(item) is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.

```py
def check_even(num):
    return num % 2 == 0 

nums = [0,1,2,3,4,5,6,7,8,9,10]

filter(check_even,nums)

list(filter(check_even,nums))
```

---

# _lambda Expression_

lambda expressions allow us to create "anonymous" functions.

`lambda's body is a single expression, not a block of statements.`

The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.

`Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. There is key difference that makes lambda useful in specialized roles:`

## **_So why would use this?_**
Many function calls need a function passed in, such as map and filter. Often you only need to use the function you are passing in once, so instead of formally defining it, you just use the lambda expression.


```py
# this is form lambda expression
lambda num: num ** 2

# You can even pass in multiple arguments into a lambda expression.
lambda x,y : x + y

list(map(lambda num: num ** 2, my_nums))

list(filter(lambda n: n % 2 == 0,nums))
```

#### **_Keep in mind the more comples a function is, the harder it is to translate into a lambda expression, meaning sometimes its just easier (and often the only way) to create the def keyword function. Not every function can be translated into a lambda expression._**
</p>
</details>

---

<details><summary>Nested Statements and Scope</summary>
<p>
<br>

# Nested Statements and Scope

When you create a variable name in Python the name is stored in a name-space. Variable names also have a scope, the scope determines the visibility of that variable name to other parts of your code.

This is where the idea of scope comes in. Python has a set of rules it follows to decide what variables (such as x in this case) you are referencing in your code. Lets break down the rules:

This idea of scope in your code is very important to understand in order to properly assign and call variable names.

In simple terms, the idea of scope can be described by 3 general rules:

- Name assignments will create or change local names by default.
- Name references search (at most) four scopes, these are:
  - local
  - enclosing functions
  - global
  - built-in
- Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.

The statement in #2 above can be defined by the LEGB rule.

LEGB Rule:

- L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

- E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

- G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

- B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...


### _Local_

```py
# x is local here:
f = lambda x:x**2
```

### _Enclosing function locals_

```py
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    print(name)
    hello()

greet()
```

### _Global_

```py
name = 'This is a global name'

print(name)
```

### _Built-in_

```py
# These are the built-in function names in Python (don't overwrite these!)
len
```

---

# Local Variables

When you declare variables inside a function definition, they are not related in any way to other variables with the same names used outside the function - i.e. variable names are local to the function. This is called the scope of the variable. All variables have the scope of the block they are declared in starting from the point of definition of the name.


```py
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)
```

---

# Global Variables

If you want to assign a value to a name defined at the top level of the program (i.e. not inside any kind of scope such as functions or classes), then you have to tell Python that the name is not local, but it is global. We do this using the global statement. It is impossible to assign a value to a variable defined outside a function without the global statement.

You can use the values of such variables defined outside the function (assuming there is no variable with the same name within the function). However, this is not encouraged and should be avoided since it becomes unclear to the reader of the program as to where that variable’s definition is. Using the global statement makes it amply clear that the variable is defined in an outermost block.


```py
x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
```

#### **_keep in mind is that everything in Python is an object! I can assign variables to functions just like I can with numbers!_**

</p>
</details>

---

<details><summary>*args and **kwargs</summary>
<p>
<br>

# *args and **kwargs

```py
def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

myfunc(40,60,20)
```

# _*args_

When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values. Rewriting the above function:

```py
def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)

# It is worth noting that the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. To demonstrate this:

def myfunc(*spam):
    return sum(spam)*.05

myfunc(40,60,20)
```

---

# _**kwargs_

Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs.

```py
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple')
```

---

# _*args and **kwargs combined_

You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs


```py
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange')

# Placing keyworded arguments ahead of positional arguments raises an exception:
myfunc(fruit='cherries',juice='orange','eggs','spam')
```


</p>
</details>


</p>
</details>

---

<details><summary>Chapter-4</summary>
<p>
<br>

# Object Oriented Programming

In python, Everything is an object.

```py
print(type(1))
print(type([]))
print(type({}))
print(type(()))
print(type('hay'))
```

# _class_

User defined objects are created using the class keyword. The class is a blueprint to create concrete instances in the memory. From classes we can construct instances. 

`An instance is a specific object created from a particular class.`

```py
class Human:
    # this is class object attribute or class variable/data
    body = {
        'brain': True,
        'arm': True,
        'leg': True,
        'tail': False
    }

    # this is object attributes
    def __init__(self,name,mark): # Constructor of the class
        self.name = name
        self.mark = mark

    # this is object method
    def passGrade10(self):
        return f'His name is {self.name} and I get {self.mark} mark.'

    def goUniversity(self, university):
        self.university = university
        return f'I am studying at the {self.university} university.'


lewis = Human('Lewis', 438)
kacy = Human('Kacy', 562)
print(lewis.passGrade10()) 
print(kacy.passGrade10())
print(lewis.goUniversity('Technology'))
print(kacy.goUniversity('Medical'))
print(lewis.body)
lewis.body['tail'] = True
print(kacy.body)
```


`An attribute is a characteristic of an object. A method is an operation we can perform with the object.`


`lewis and kacy` are the `instances` of the `human`. Each instance has its own attributes independent of other instances. These attributes are also called `encapsulate`(သီးသန့်ကွဲထွတ်) that means they belong to the object, not from the class.


`body` is the class variable or data. This doesn't associated with the instance object `lewis and kacy`. If we change the class data, all the instances will change. It is `not encapsulate` that means it exists all the same object in every instance of the class.


`self` - The first argument when we create any method or attribute is the self argument. This argument specifies the instance on which you call the method or attribute.


Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects.

# Inheritance and Polymorphism

## _Inheritance_


Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).

## _Polymorphism_

We've learned that while functions can take in different arguments, methods belong to the objects they act on. In Python, polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in.


```py
class Human:
    # this is class object attribute or class variable/data
    body = {
        'brain': True,
        'arm': True,
        'leg': True,
        'tail': False
    }

    # this is object attributes
    def __init__(self,*args):
        self.name = args[0]
        self.mark = args[1]

    # this is object method
    def passGrade10(self):
        return f'His name is {self.name} and I get {self.mark} mark.'

    def goUniversity(self, university):
        self.university = university
        return f'I am studying at the {self.university} university.'

    def age(self,age):
        self.age= age
        return self.age   


# Inheritance 
# Medical is the Derived Class
# Human is the base class   
class Medical(Human):
    def __init__(self,*args):
        self.office = args[2]
        # Inheritance initialized the attributes
        super().__init__(*args)
        # Can use Human.__init__(self,*args)

    def goUniversity(self, university):
        """This modifies the method"""
        return f'I am not attending the {university} university because I am from {self.office}. '

    def goOffice(self):
        """Extends new method"""
        return f'I am working {self.office} office '

    
class Technological(Human):
    def __init__(self, *args):
        self.field = args[2]
        self.language = args[3]

        # Inheritance initialized the attributes
        Human.__init__(self,*args)

    def goal(self,passion):
        """Extends new method"""
        self.passion = passion
        return f'I am {self.field} field and learning {self.language}. I want to become {self.passion} '

    # def age(self,age):
    #     """This is inheritance the method attributes"""
    #     super().age(age) 
    #  this will return none because it only inheritance method attributes and doesn't return anything

    def age(self,age):
        """This inheritance and modify the method attributes"""
        super().age(age)
        year = 2021 - self.age

        return f'I was born in {year}'



phyo = Human('phyo', 300)
print(phyo.passGrade10())
print(phyo.goUniversity('Oxford'))


kyaw = Medical('kyaw', 400, 'yangon')
print(kyaw.office)
print(kyaw.passGrade10())
print(kyaw.goUniversity('mandalay'))


aung = Technological('Aung', 500, 'IT' , 'Python')
print(aung.goUniversity('StandFord'))
print(aung.goal('Python Programmer'))


print(aung.age(21))
print(kyaw.age(21))

# class object attribute will have all instance object and inheritanced object
print(aung.body)
```

## _Special Methods_

Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax.

```py
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book 

# This will be error because this has deleted
print(book)
```

---

# Example

```py
# PasudoCode
"""
make deckCards
give cards to players from deckCards
round_no = 0
while game_on:
    plus to round_no

    if players cards are zero:
        print who win and lose
        game_on is flase
        break

    give players hand card by removing players cards to war

    at_war = true

    while at_war:

        if one of the player card is greater than other:
            give cards to winner
            at_war is false
            

        if they are equal:

            check whether players cards are less than 5, if true:
                print winner is more than 5 cards
                game_on is false
                break

            else they are more than 5:

                take 5 cards from players cards and give to player hand cards to war again their cards

"""

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

import random

class Card:
    """Single card properties"""
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    

class Deck:
    """On the table cards"""
    def __init__(self):
        self.allCards = []

        for suit in suits:
            for rank in ranks:
                self.allCards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.allCards)

    def dealCard(self):
        return self.allCards.pop()

class Player:
    """Player info and cards"""
    def __init__(self,name):
        self.name = name
        self.playerCards = []

    def addCards(self,card):
        if isinstance(card, list):
            self.playerCards.extend(card)
        else:
            self.playerCards.append(card)

    def dealOne(self):
        return self.playerCards.pop(0)


# From psudoCode

deckCards = Deck()
deckCards.shuffle()

playerOne = Player('Lewis')
playerTwo = Player('Corner')

for i in range(26):
    playerOne.addCards(deckCards.dealCard())
    playerTwo.addCards(deckCards.dealCard())

roundNo = 0
gameOn = True

while gameOn:

    roundNo += 1
    print(f'Round number {roundNo} ')

    if len(playerOne.playerCards) == 0:
        print(f'Player {playerTwo.name} is win because out of range')
        gameOn = False
        break

    if len(playerTwo.playerCards) == 0:
        print(f'Player {playerOne.name} is win because out of range')
        gameOn = False
        break

    playerOneHand = []
    playerOneHand.append(playerOne.dealOne())

    playerTwoHand = []
    playerTwoHand.append(playerTwo.dealOne())

    atWar = True

    while atWar:

        if playerOneHand[-1].value > playerTwoHand[-1].value:
            playerOne.addCards([playerOneHand[-1],playerTwoHand[-1]])
            atWar = False

        elif playerTwoHand[-1].value > playerOneHand[-1].value:
            playerTwo.addCards([playerTwoHand[-1],playerOneHand[-1]])
            atWar = False

        else:
            print('atwar')

            if len(playerOne.playerCards) < 5:
                print(f"Player {playerOne.name} unable to play war! Game Over at War")
                print(f"Player {playerTwo.name} Wins!")
                gameOn = False
                break

            elif len(playerTwo.playerCards) < 5:
                print(f"Player {playerTwo.name} unable to play war! Game Over at War")
                print(f"Player {playerOne.name} Wins!")
                gameOn = False
                break

            else:
                for i in range(5):
                    playerOneHand.append(playerOne.dealOne())
                    playerTwoHand.append(playerTwo.dealOne())
```


</p>
</details>

---

<details><summary>Chapter-5</summary>
<p>
<br>

# Module and Packages


</p>
</details>


---

<details><summary>Chapter-6</summary>
<p>
<br>

# Errors and Exception Handling


</p>
</details>


---

<details><summary>Chapter-7</summary>
<p>
<br>

# Build-in Function

<details><summary>Numeric Functions</summary>
<p>
<br>

# Numeric Functions

```py
x = -47
# Return the absolute value of the argument.
print(abs(x))

# Return the tuple (x//y, x%y).
print(divmod(47,3))


```

</p>
</details>

---

<details><summary>String Functions</summary>
<p>
<br>

# String Functions

```py
str = 'Yes, this is a string 🍿'
print(repr(str))

# Return an ASCII-only representation of an object. As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes.
print(ascii(str))

# Return the Unicode code point for a one-character string.
print(ord('🤜'))

# Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
print(chr(129308))

```

</p>
</details>

---

<details><summary>Container Functions</summary>
<p>
<br>

# Container Functions

```py
x = [1,2,3,4,5]
# Return a reverse iterator over the values of the given sequence.
y = reversed(x)
print(y)

# Return the sum of a 'start' value (default: 0) plus an iterable of numbers. When the iterable is empty, return the start value. This function is intended specifically for use with numeric values and may reject non-numeric types.
z = sum(x,10)
print(z)

# With a single iterable argument, return its smallest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the smallest argument.
print(min(x))

# With a single iterable argument, return its biggest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the largest argument.
print(max(x))
```

</p>
</details>

---


<details><summary>map()</summary>
<p>
<br>

# map()

map() is a built-in Python function that takes in two or more arguments: a function and one or more iterables, in the form:

map(function, iterable, ...)
map() returns an iterator - that is, map() returns a special object that yields one result at a time as needed. We will learn more about iterators and generators in a future lecture. For now, since our examples are so small, we will cast map() as a list to see the results immediately.

```py
def fahrenheit(celsius):
    return (9/5)*celsius + 32
    
temps = [0, 22.5, 40, 100]
F_temps = map(fahrenheit, temps)

#Show
print(list(F_temps))

# with lambda expression
list(map(lambda x: (9/5)*x + 32, temps))
```

## _map() with multiple iterables_

map() can accept more than one iterable. The iterables should be the same length - in the event that they are not, map() will stop as soon as the shortest iterable is exhausted.

For instance, if our function is trying to add two values x and y, we can pass a list of x values and another list of y values to map(). The function (or lambda) will be fed the 0th index from each list, and then the 1st index, and so on until the n-th index is reached.

```py
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

list(map(lambda x,y:x+y,a,b))

# Now all three lists
list(map(lambda x,y,z:x+y+z,a,b,c))
```

</p>
</details>

---

<details><summary>filter()</summary>
<p>
<br>

# filter

The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns True.

The function filter(function,list) needs a function as its first argument. The function needs to return a Boolean value (either True or False). This function will be applied to every element of the iterable. Only if the function returns True will the element of the iterable be included in the result.

Like map(), filter() returns an iterator - that is, filter yields one result at a time as needed.

```py
lst =[47,11,42,13]
def test(num):
    return num>15
a = list(filter(test,lst))
print(a)

users= [
    {'name': 'Lewis' , 'age': 22, 'boolean': False},
    {'name': 'Jackson' , 'age': 10, 'boolean': False},
    {'name': 'Davis' , 'age': 18, 'boolean': False},
    {'name': 'Simon' , 'age': 27, 'boolean': False},
    {'name': 'Lucy' , 'age': 20, 'boolean': False}
]
b = list(filter(lambda user: user['age'] >= 18, users))
print(b)
```

</p>
</details>

---

<details><summary>reduce()</summary>
<p>
<br>

# reduce()

The function reduce(function, sequence, initial) continually applies the function to the sequence. It then returns a single value.

If seq = [ s1, s2, s3, ... , sn ], calling reduce(function, sequence) works like this:

- At first the first two elements of seq will be applied to function, i.e. func(s1,s2)
- The list on which reduce() works looks now like this: [ function(s1, s2), s3, ... , sn ]
- In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
- The list looks like this now: [ function(function(s1, s2),s3), ... , sn ]
- It continues like this until just one element is left and return this element as the result of reduce()

```py
from functools import reduce

lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)

#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b

#Find max
reduce(max_find,lst)
```

# _reduce() Example_

**filter function with reduce**

```py
from functools import reduce

users= [
    {'name': 'Lewis' , 'age': 22, 'boolean': False},
    {'name': 'Jackson' , 'age': 10, 'boolean': False},
    {'name': 'Davis' , 'age': 18, 'boolean': False},
    {'name': 'Simon' , 'age': 27, 'boolean': False},
    {'name': 'Lucy' , 'age': 20, 'boolean': False}
]

def over18(lst,iter):
    if iter['age'] > 18:
        lst.append(iter['name']) 
        return lst
    else:
        return lst

b = reduce(over18,users, [])
print(b)
```

---

**Create Object**

```py
from functools import reduce

lst = [['mark_johansson', 'waffle_iron', 80, 2],
['mark_johansson', 'blender', 200, 1],
['mark_johansson', 'knife', 10, 4],
['Nikita_Smith', 'waffle_iron', 80, 1],
['Nikita_Smith', 'knife', 10, 2],
['Nikita_Smith', 'pot', 20, 3]]

def obj(obj,line):
    obj[line[0]] = obj.get(line[0]) or []

    obj[line[0]].append({
        'name': line[1],
        'price': line[2],
        'quanlity': line[3]
    })

    return obj

a = reduce(obj,lst,{})
print(a)
```

</p>
</details>

---

<details><summary>Zip</summary>
<p>
<br>

# Zip

zip
zip() makes an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

zip() is equivalent to:

```py
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
```

zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables.

```py
# zip the list together
x = [1,2,3]
y = [4,5,6]
list(zip(x,y))

# One iterable is longer than the other
x = [1,2,3]
y = [4,5,6,7,8]
list(zip(x,y))

# with dictionary
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}
list(zip(d1,d2))

list(zip(d2,d1.values()))

# Switch keys and values of two dictionaries
def switcharoo(d1,d2):
    dout = {}
    
    for d1key,d2val in zip(d1,d2.values()):
        dout[d1key] = d2val
    
    return dout

print(switcharoo(d1,d2))
```
</p>
</details>

---

<details><summary>Enumerate</summary>
<p>
<br>

# enumerate()

In this lecture we will learn about an extremely useful built-in function: enumerate(). Enumerate allows you to keep a count as you iterate through an object. It does this by returning a tuple in the form (count,element). The function itself is equivalent to:

```py
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```

<br>

```py
lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number)
    print(item)

# enumerate() takes an optional "start" argument to override the default value of zero:
months = ['March','April','May','June']
list(enumerate(months,start=3))
```
</p>
</details>

---

<details><summary>all() and any()</summary>
<p>
<br>

# all() and any()


all() and any() are built-in functions in Python that allow us to conveniently check for boolean matching in an iterable. all() will return True if all elements in an iterable are True. It is the same as this function code:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
any() will return True if any of the elements in the iterable are True. It is equivalent to the following function code:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

```py
lst = [True,True,False,True]

print(all(lst))
print(any(lst))
```

</p>
</details>

---

<details><summary>complex()</summary>
<p>
<br>

# complex()

complex() returns a complex number with the value real + imag*1j or converts a string or number to a complex number.

If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

If you are doing math or engineering that requires complex numbers (such as dynamics, control systems, or impedance of a circuit) this is a useful tool to have in Python.

```py
# Create 2+3j
complex(2,3)

complex(10,1)

complex('12+2j')
```

</p>
</details>

---

<details><summary>Some Example</summary>
<p>
<br>

**Problem 1**
Use map() to create a function which finds the length of each word in the phrase (broken by spaces) and returns the values in a list.

The function will have an input of a string, and output a list of integers.

**Problem 2**
Use reduce() to take a list of digits and return the number that they correspond to. For example, [1, 2, 3] corresponds to one-hundred-twenty-three.
Do not convert the integers to strings!

**Problem 3**
Use filter to return the words from a list of words which start with a target letter.

**Problem 4**
Use zip() and a list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them. Look at the example output below:
concatenate(['A','B'],['a','b'],'-')
output: ['A-a', 'B-b']

**Problem 5**
Use enumerate() and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.

**Problem 6**
Use enumerate() and other skills from above to return the count of the number of items in the list whose value equals its index.

```py
def word_lengths(str):
    return list(map(len, str.split()))
print(word_lengths('How long are the words in this phrase'))


from functools import *
def digits_to_num(lst):
    return reduce(lambda x,y: x * 10 + y, lst, 0)
print(digits_to_num([3,4,3,2,1]))


def filter_words(lst, let):
    return list(filter(lambda x: x.startswith(let), lst))
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))


def concatenate(L1,L2, con):
    return [con.join((x,y)) for x,y in zip(L1,L2)]
print(concatenate(['A','B'],['a','b'],'-'))


def d_list(lst):
    return {v: i for i,v in enumerate(lst)}
print(d_list(['a','b','c']))


def count_match_index(lst):
    return len([v for i,v in enumerate(lst) if i == v])
print(count_match_index([0,2,2,1,5,5,6,10]))
```

</p>
</details>


</p>
</details>

---

<details><summary>Chapter-8</summary>
<p>
<br>

# Python Decorators


</p>
</details>

---

<details><summary>Chapter-9</summary>
<p>
<br>

# Python Generator

# _Iterators and Generators_

Generators allow us to generate as we go along, instead of holding everything in memory.

We've touched on this topic in the past when discussing certain built-in Python functions like range(), map() and filter().

Let's explore a little deeper. We've learned how to create functions with def and the return statement. Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off. This type of function is a generator in Python, allowing us to generate a sequence of values over time. The main difference in syntax will be the use of a yield statement.

In most aspects, a generator function will appear very similar to a normal function. The main difference is when a generator function is compiled they become an object that supports an iteration protocol. That means when they are called in your code they don't actually return a value and then exit. Instead, generator functions will automatically suspend and resume their execution and state around the last point of value generation. The main advantage here is that instead of having to compute an entire series of values up front, the generator computes one value and then suspends its activity awaiting the next instruction. This feature is known as state suspension.

Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) in cases where we don’t want to allocate the memory for all of the results at the same time.

`If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator.`

```py
# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)

print(list(gencubes(10)))

def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)

print(list(genfibon(10)))
```

# _next() and iter() built-in functions_
A key to fully understanding generators is the next() function and the iter() function.

The next() function allows us to access the next element in a sequence.

```py
def simple_gen():
    for x in range(3):
        yield x

# Assign simple_gen 
g = simple_gen()
noValue = 'There is no value'
print(next(g,noValue))
print(next(g,noValue))
print(next(g,noValue))
print(next(g,noValue))
# After yielding all the values next() caused a StopIteration error. What this error informs us of is that all the values have been yielded. 
# Second argument is default value if StopIteration error occurs.

# iter() function
s = 'hello'

#Iterate over string
for let in s:
    print(let)
# that doesn't mean the string itself is an iterator! We can check this with the next() function:

print(next(s))

# this means that a string object supports iteration, but we can not directly iterate over it as we could with a generator function. The iter() function allows us to do just that!

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
```

## _Generator Comprehension_

```py
# this is generator comprehension
lst = [1,2,3,4,5]
gen = (i for i in lst if i > 2)
print(gen)
```

## _List Comprehension_

```py
# this is list comprehension
lst = [1,2,3,4,5]
lcom = [i for i in lst if i > 2]
print(lcom)
```

</p>
</details>


---

<details><summary>Chapter-10</summary>
<p>
<br>

# Advanced Python Modules

<details><summary>Collection Module</summary>
<p>
<br>

# Collection Module

The collections module is a built-in module that implements specialized container data types providing alternatives to Python’s general purpose built-in containers. We've already gone over the basics: dict, list, set, and tuple.


# _Counter_

Counter is a dict subclass which helps count hashable objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

```py
from collections import Counter

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print(Counter(lst))

print(Counter('aabsbsbsbhshhbbsbs'))

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

c = Counter(words)
print(c.most_common(2))
```

</p>
</details>

---

<details><summary>Opening and Reading files</summary>
<p>
<br>

# _Opening and Reading files_

File has modes: 
- 'r'	open for reading (default)
- 'w'	open for writing, truncating the file first
- 'x'	create a new file and open it for writing
- 'a'	open for writing, appending to the end of the file if it exists
- 'b'	binary mode
- 't'	text mode (default)
- '+'	open a disk file for updating (reading and writing)

```py
f = open('write.txt','wt')
f.write('Write the text. if something has, overwrite text')
f = open('write.txt','a+')
f.write('Appending the some text.')
f.close()

# create text.txt file before code
file = open('text.txt', 'rt')
writeFile = open('text_copy.txt','wt')

for i in file:
    print(i)

# copy text file
for line in file:
    # check out print function. You can use this
    # print(line.strip(),file=writeFile)
    writeFile.write(line)
file.close()
writeFile.close()

# Have you already a photo? 
photo = open('myphoto.jpg','rb')
wPhoto = open('myphoto_copy.jpg','wb')
buffer = photo.read()
wPhoto.write(buffer)
photo.close()
wPhoto.close()
```

# _Getting Directories_
Python has a built-in `os module` that allows us to use operating system dependent functionality.

```py
import os
# Getting the current work diractory
print(os.getcwd())

# Listing Files in Diractory
print(os.listdir())
# In any diractory you can pass
print(os.listdir('/Users/wailwinphyo/'))
```

# _Moving Files_
You can use the built-in shutil module to to move files to different locations. Keep in mind, there are permission restrictions, for example if you are logged in a User A, you won't be able to make changes to the top level Users folder without the proper permissions

```py
import shutil, os
shutil.move('text.txt', '/Users/wailwinphyo/Desktop/')
```

# _Deleting Files_
NOTE: The os module provides 3 methods for deleting files:

- os.unlink(path) which deletes a file at the path your provide
- os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
- shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.

All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.

```py
import send2trash
send2trash.send2trash('text.txt')
```

# _Walking through a directory_

Often you will just need to "walk" through a directory, that is visit every file or folder and check to see if a file is in the directory, and then perhaps do something with that file. Usually recursively walking through every file and folder in a directory would be quite tricky to program, but luckily the os module has a direct method call for this called os.walk(). 

```py
for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    
    # Now look at subfolders
```

</p>
</details>

---

<details><summary>Datetime Module</summary>
<p>
<br>

# _DateTime Module_

Python has the datetime module to help deal with timestamps in your code. Time values are represented with the time class. Times have attributes for hour, minute, second, and microsecond. They can also include time zone information. The arguments to initialize a time instance are optional, but the default of 0 is unlikely to be what you want.

## _time_

Let's take a look at how we can extract time information from the datetime module. We can create a timestamp by specifying datetime.time(hour,minute,second,microsecond)

`Note: A time instance only holds values of time, and not a date associated with the time.`

```py
import datetime

mytime = datetime.time(2,20,46,20)

print(mytime)
print(mytime.hour)
print(mytime.minute)
print(mytime.microsecond)
print(type(mytime))

# We can also check the min and max values a time of day can have in the module:

print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
```

## _Dates_

datetime (as you might suspect) also allows us to work with date timestamps. Calendar date values are represented with the date class. Instances have attributes for year, month, and day. It is easy to create a date representing today’s date using the today() class method.

```py
import datetime

today = datetime.date.today()

print(today)
print(today.year)
print(today.month)
print(today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())

# As with time, the range of date values supported can be determined using the min and max attributes.
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)

# Another way to create new date instances uses the replace() method of an existing date. For example, you can change the year, leaving the day and month alone.

d1 = datetime.date(2015, 3, 11)
print(d1)
d1 = d1.replace(year=1990)
print('After replace : ', d1)
```

## _Arithmetic_

We can perform arithmetic on date objects to check for time differences.

```py
from datetime import datetime

date1 = datetime(2021,11,3,12,52)
date2 = datetime(2020,11,3,22,22)

result = date1 - date2
print(result)
print(type(result))
print(result.seconds)
print(f'Calculate exceed seconds {(60*30)+(14*3600)}')
print(result.total_seconds())
print(f'Calculate total seconds {(60*30)+(14*3600)+((3600*24)*364)}')
```

</p>
</details>

---

<details><summary>Math and Random Module</summary>
<p>
<br>

# _Math and Random Module_

## _Rounding Numbers_

```py
import math
value = 4.35
print(math.floor(value))
print(math.celi(value))
print(round(value))
```

## _Mathematical Constants_

```py
import math
from math import pi

print(pi)
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
```

## _Logarithmic Values_

```py
import math

print(math.e)

# Log Base e
print(math.log(math.e))
print(math.log(10))

# math.log(x,base) base 10
print(math.log(100,10))
```

## _Trigonometrics Functions_

```py
import math

print(math.sin(10))
print(math.degrees(math.pi/2))
print(math.radians(180))
```

## _Random Integer_

Return random integer in range [a, b], including both end points.

```py
import random
print(random.randint(0,10))
```

## _Understanding a seed_

Setting a seed allows us to start from a seeded psuedorandom number generator, which means the same random numbers will show up in a series. Note, you need the seed to be in the same cell if your using jupyter to guarantee the same results each time. Getting a same set of random numbers can be important in situations where you will be trying different variations of functions and want to compare their performance on random values, but want to do it fairly (so you need the same set of random numbers each time).

```py
import random

random.seed(101)
for i in range(10):
    print(random.randint(0,100))
# Run multiple time, it will show the same result
```

## _Random with Sequences_

```py
import random

mylist = list(range(0,10))
print(mylist)
# Choose a random element from a non-empty sequence.
print(random.choice(mylist))
```

## _Sample with Replacement_

Take a sample size, allowing picking elements more than once. Imagine a bag of numbered lottery balls, you reach in to grab a random lotto ball, then after marking down the number, you place it back in the bag, then continue picking another one.

```py
randomList = random.choices(population=mylist, k=15)
print(randomList)
```

## _Sample without Replacement_

Once an item has been randomly picked, it can't be picked again. Imagine a bag of numbered lottery balls, you reach in to grab a random lotto ball, then after marking down the number, you leave it out of the bag, then continue picking another one.

```py
randomList = random.sample(population=mylist, k=15)
print(randomList)
```

## _Shuffle a list_

Note: This effects the object in place!

```py
# Don't assign this to anything!
random.shuffle(mylist)
print(mylist)
```

# _Random Distributions_

```py
# Uniform Distribution
# Continuous, random picks a value between a and b, each value has equal change of being picked.
print(random.uniform(a=0,b=100))

# Normal/Gaussian Distribution
print(random.gauss(mu=0,sigma=1))
```

</p>
</details>

---

<details><summary>Regular Expression</summary>
<p>
<br>


# _Overview of Regular Expressions_

Regular Expressions (sometimes called regex for short) allows a user to search for strings using almost any sort of rule they can come up. For example, finding all capital letters in a string, or finding a phone number in a document.

Regular expressions are notorious for their seemingly strange syntax. This strange syntax is a byproduct of their flexibility. Regular expressions have to be able to filter out any string pattern you can imagine, which is why they have a complex string pattern format.

```py
import re

text = "The person's phone number is 408-555-1234. Call soon!"
pattern = 'phone'
search = re.search(pattern , text)
print(search)

# Now we've seen that re.search() will take the pattern, scan the text, and then returns a Match object. If no pattern is found, a None is returned

pattern = 'NONE TEXT'
search = re.search(pattern, text)
print(search)

# there is also a span, start and end index information
search.span()
search.start()
search.end()

# If you wanted the actual text that matched, you can use the .group() method
search.group()
```

If the pattern occurs more than once,  it only matches the first instance. If we wanted a list of all matches, we can use `.findall()` method:

```py
text = 'my phone is new phone'
pattern = 'phone'
search = re.findall(pattern, text)
print(search)

for i in search:
    print(i.group())
```

# _Identifiers for Characters in Patterns_

Characters such as a digit or a single string have different codes that represent them. You can use these to build up a pattern string. Notice how these make heavy use of the backwards slash \ . Because of this when defining a pattern string for regular expression we use the format: `r'mypattern'`

placing the r in front of the string allows python to understand that the \ in the pattern string are not meant to be escape slashes.

Below you can find a table of all the possible identifiers:

<table>
    <thead>
        <tr>
            <th>Character</th>
            <th>Description</th>
            <th>Example pattern code</th>
            <th>Example Match</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>\d</td>
            <td>A digit</td>
            <td>file_\d\d</td>
            <td>file_25</td>
        </tr>
        <tr>
            <td>\w</td>
            <td>Alphanumeric</td>
            <td>\w-\w\w\w</td>
            <td>A-b_1</td>
        </tr>
        <tr>
            <td>\s</td>
            <td>White space</td>
            <td>a\sb\sc</td>
            <td>a b c</td>
        </tr>
        <tr>
            <td>\D</td>
            <td>A non digit</td>
            <td>\D\D\D</td>
            <td>ABC</td>
        </tr>
        <tr>
            <td>\W</td>
            <td>Non-alphanumeric</td>
            <td>\W\W\W\W\W</td>
            <td>*-+=)</td>
        </tr>	
        <tr>
            <td>\S</td>
            <td>Non-whitespace</td>
            <td>\S\S\S\S</td>
            <td>Yoyo</td>
        </tr>	
    </tbody>
</table>

```py
text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone.group())
```

# Quantifiers

Now that we know the special character designations, we can use them along with quantifiers to define how many we expect.

<table >
    <tr>
        <th>Character</th>
        <th>Description</th>
        <th>Example Pattern Code</th>
        <th >Exammple Match</th>
    </tr>
    <tr >
        <td><span >+</span></td>
        <td>Occurs one or more times</td>
        <td>	Version \w-\w+</td>
        <td>Version A-b1_1</td>
    </tr>
    <tr >
        <td><span >{3}</span></td>
        <td>Occurs exactly 3 times</td>
        <td>\D{3}</td><td>abc</td>
    </tr>
    <tr >
        <td><span >{2,4}</span></td>
        <td>Occurs 2 to 4 times</td>
        <td>\d{2,4}</td>
        <td>123</td>
    </tr>
    <tr >
        <td><span >{3,}</span></td>
        <td>Occurs 3 or more</td>
        <td>\w{3,}</td>
        <td>anycharacters</td>
    </tr>
    <tr >
        <td><span >\*</span></td>
        <td>Occurs zero or more times</td>
        <td>A\*B\*C*</td>
        <td>AAACC</td>
    </tr>
    <tr>
        <td><span >?</span></td>
        <td>Once or none</td>
        <td>plurals?</td>
        <td>plural</td>
    </tr>
</table>

```py
search = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(search.group())
```

# _Groups_

What if we wanted to do two tasks, find phone numbers, but also be able to quickly extract their area code (the first three digits). We can use groups for any general task that involves grouping together regular expressions (so that we can later break them down).

```py
pattern_compile = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
search = re.search(pattern_compile, text)
print(search.group())

# group index starts from 1
print(search.group(1))
print(search.group(2))
print(search.group(3))
```

# _Additional Regex Syntax_

## Or operator |

Use the pipe operator to have an or statment.

```py
match = re.search(r"man|woman","This man was here.")
print(match.group())

match = re.search(r"man|woman","This woman was here.")
print(match.group())
```

## The Wildcard Character

Use a "wildcard" as a placement that will match any character placed there. You can use a simple period

```py
print(re.findall(r'.at','The cat in the hat sat here'))
print(re.findall(r'.at','The bat went splat'))

# One or more non-whitespace that ends with 'at'
re.findall(r'\S+at',"The bat went splat")
```

## Starts with and Ends With

We can use the ^ to signal starts with, and the $ to signal ends with:

```py
# Ends with a number
print(re.findall(r'\d$','This ends with a number 2'))

# Starts with a number
print(re.findall(r'^\d','1 is the loneliest number.'))
```

## Exclusion

To exclude characters, we can use the ^ symbol in conjunction with a set of brackets []. Anything inside the brackets is excluded. For example:

```py
phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]',phrase))

# To get the words back together, use a + sign
print(re.findall(r'[^\d]+',phrase))

# We can use this to remove punctuation from a sentence.
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
match = re.findall(r'[^!.?]+',test_phrase)
print(''.join(match))

match2 = re.findall(r'[^!.?\s]+',test_phrase)
print(' '.join(match2))
```

# _Brackets for Grouping_

As we showed above we can use brackets to group together options, for example if we wanted to find hyphenated words:

```py
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are.'
print(re.findall(r'[\w]+-[\w]+',text))
```

# _Parenthesis for Multiple Options_

If we have multiple options for matching, we can use parenthesis to list out these options. For Example:

```py
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)',text))
print(re.search(r'cat(fish|nap|claw)',texttwo))

# None returned
print(re.search(r'cat(fish|nap|claw)',textthree))
```
</p>
</details>

---

<details><summary>Timing your code</summary>
<p>
<br>

# Timing Your Code

Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project. Python has a built-in timing module to do this.

## _Example Function or Script_

Here we have two functions that do the same thing, but in different ways. How can we tell which one is more efficient? Let's time it!

```py
def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]
print(func_one(10))

def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str,range(n)))
print(func_two(10))
```

# Timing Start and Stop

We can try using the time module to simply calculate the elapsed time for the code. Keep in mind, due to the time module's precision, the code needs to take at least 0.1 seconds to complete.

```py
import time

# STEP 1: Get start time
start_time = time.time()

# Step 2: Run your code you want to time
result = func_one(1000000)

# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)
```

```py
# STEP 1: Get start time
start_time = time.time()

# Step 2: Run your code you want to time
result = func_two(1000000)

# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)
```

# Timeit Module

What if we have two blocks of code that are quite fast, the difference from the time.time() method may not be enough to tell which is fater. In this case, we can use the timeit module.

The timeit module takes in two strings, a statement (stmt) and a setup. It then runs the setup code and runs the stmt code some n number of times and reports back average length of time

```py
import timeit

setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""

setup2 = """
def func_two(n):
    return list(map(str,range(n)))
"""

stmt = """
func_one(100)
"""

stmt2 = """
func_two(100)
"""

test = timeit.timeit(stmt,setup,number=100000)
print(test)
```
</p>
</details>

---

<details><summary>Unzipping and Zipping Files</summary>
<p>
<br>

# Unzipping and Zipping Files

As you are probably aware, files can be compressed to a zip format. Often people use special programs on their computer to unzip these files, luckily for us, Python can do the same task with just a few simple lines of code.

# _Zipping Files_

The zipfile library is built in to Python, we can use it to compress folders or files. To compress all files in a folder, just use the os.walk() method to iterate this process for all the files in a directory.

```py
import zipfile

f = open('first.txt','wt')
f.write('This is file one')
f.close()

f = open('second.txt', 'wt')
f.write('this is file two')
f.close()

zip_file = zipfile.ZipFile('fileZip.zip', 'w')
zip_file.write('first.txt',compress_type=zipfile.ZIP_DEFLATED)
zip_file.write('second.txt',compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()
```

# _Extracting from Zip Files_

We can easily extract files with either the extractall() method to get all the files, or just using the extract() method to only grab individual files.

```py
zip_obj = zipfile.ZipFile('fileZip.zip','r')
zip_obj.extractall("extracted_content")
```

# _Using shutil library_

Often you don't want to extract or archive individual files from a .zip, but instead archive everything at once. The shutil library that is built in to python has easy to use commands for this:

The shutil library can accept a format parameter, format is the archive format: one of "zip", "tar", "gztar", "bztar", or "xztar".

```py
import shutil

directory_to_zip='C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules'

# Creating a zip archive
output_filename = 'example'
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',directory_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')
```

</p>
</details>

</p>
</details>

---

<details><summary>Chapter-11</summary>
<p>
<br>



</p>
</details>

---

<details><summary>Chapter-12</summary>
<p>
<br>

# Working with images

## _Overview of working with images_

By leveraging the power of some common libraries that you can install, such as PILLOW, Python gains the ability to work with and manipulate images for simple tasks. You can install Pillow by running:

`pip install pillow`

In case of any issues, you can refer to their official documentation on installation. But for most computers, the simple pip install method should work.

# Working with Pillow Library

## _Opening Images_

You can use Pillow to open image files.

```py
from PIL import Image

mac = Image.open('example.jpg')
print(type(mac))

# to view the image
mac.show()
```

## _Image Information_

```py
# (width, height)
print(mac.size)
print(mac.filename)
print(mac.format_description)
```

## _Cropping Images_

To crop images (that is grab a sub section) you can use the crop() method on the image object. The crop() method returns a rectangular region from this image. The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate.

Note! If you take a look at the documentation string, it says the tuple you pass in is defined as (x,y,w,h). These variables can be a bit decieving. Its not really a height or width that is being passed, but instead the end coordinates of your width and height.

All the coordinates of box (x, y, w, h) are measured from the top left corner of the image. Again, all 4 of these values are coordinates!

```py
mac.crop((0,0,100,100))

#For the mac image this isn't a very useful demonstration. Let's use another image instead:
pencils = Image.open("pencils.jpg")
pencils.show()
print(pencils.size)

# Start at top corner (0,0)
x = 0
y = 0

# Grab about 10% in y direction , and about 30% in x direction
w = 1950/3
h = 1300/10

pencils.crop((x,y,w,h)).show()


#Now let's try the pencils from the bottom
print(pencils.size)
x = 0 
y = 1100
w = 1950/3
h = 1300
pencils.crop((x,y,w,h)).show()

# for mac photo

print(mac.size)
halfway = 1993/2
x = halfway - 200
w = halfway + 200

y = 800
h = 1257

mac.crop((x,y,w,h)).show()
```

## _Copying and Pasting Images_

We can create copies with the copy() method and paste images on top of others with the paste() method.

```py
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))
mac.paste(im=computer,box=(796,0))
mac.show()
```

## _Resizing_

You can use the resize() method to resize an image

```py
print(mac.size)
h,w = mac.size
new_h = int(h/3)
new_w = int(w/3)

# Note this is not permanent change
# for permanent change, do a reassignment
# e.g. mac = mac.resize((100,100))
mac.resize((new_h,new_w)).show()
```

## _Rotating Images_

You can rotate images by specifying the amount of degrees to rotate on the rotate() method. The original dimensions will be kept and "filled" in with black. You can optionally pass in the expand parameter to fill the new rotated image to the old dimensions.

```py
pencils.rotate(90).show()
```

## _Transparency_

We can add an alpha value (RGBA stands for RED,Green,Blue, Alpha) where values can go from 0 to 255. If Alpha is 0 the image is completely transparent, if it is 255 then its completely opaque.

You can create your own color here to check for possible values: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool

We can adjust image alpha values with the putalpha() method:

```py
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
red.putalpha(128)
blue.putalpha(128)

blue.paste(red,box=(0,0),mask=red)
blue.show()
```

Transparency and masking can be much more complex than what we've shown here, if you find yourself needing something more, check out the documentation: [Click](https://pillow.readthedocs.io/en/stable/)


## _Saving Images_

Let's save this updated "blue" image as 'purple.png' in this folder.

```py
blue.save("purple.png")
Let's check to make sure that worked:

purple = Image.open("purple.png")
purple
```

## _Exercise_

```py
word = Image.open('word_matrix.png')
mask = Image.open('mask.png')
mask = mask.resize((1015,559))
mask.putalpha(100)

word.paste(mask,box=(0,0),mask=mask)
word.show()
```

</p>
</details>

---

<details><summary>Chapter-13</summary>
<p>
<br>

# PDFs and Spreadsheets



</p>
</details>