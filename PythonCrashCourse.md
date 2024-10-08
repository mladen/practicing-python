# Python Crash Course (with the help of ChatGPT)

- [Python Crash Course (with the help of ChatGPT)](#python-crash-course-with-the-help-of-chatgpt)
  - [General Python](#general-python)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Sets](#sets)
  - [Strings](#strings)
  - [Collections](#collections)
  - [Itertools](#itertools)
  - [Lambda Functions](#lambda-functions)
  - [Exceptions and Errors](#exceptions-and-errors)
    - [Syntax errors](#syntax-errors)
    - [Exceptions](#exceptions)
      - [Raising exceptions](#raising-exceptions)
      - [Custom exceptions](#custom-exceptions)
  - [Logging](#logging)
  - [JSON](#json)
    - [Converting Python dictionaries to JSON format](#converting-python-dictionaries-to-json-format)
    - [Converting JSON data to Python dictionaries](#converting-json-data-to-python-dictionaries)
    - [Encoding custom(!) objects to JSON (HINT: using the `default` parameter)](#encoding-custom-objects-to-json-hint-using-the-default-parameter)
    - [Decoding custom(!) objects from JSON (HINT: using the `object_hook` parameter)](#decoding-custom-objects-from-json-hint-using-the-object_hook-parameter)
  - [Random numbers](#random-numbers)
    - [Random module](#random-module)
    - [Secrets module](#secrets-module)
    - [Numpy random module](#numpy-random-module)
  - [Decorators](#decorators)
    - [Function decorators - working with arguments](#function-decorators---working-with-arguments)
      - [Function decorators - alternative syntax](#function-decorators---alternative-syntax)
    - [Function decorators - multiple decorators](#function-decorators---multiple-decorators)
      - [Function decorators - multiple decorators - alternative syntax](#function-decorators---multiple-decorators---alternative-syntax)
    - [Class decorators](#class-decorators)
  - [Generators](#generators)
  - [Threading vs Multiprocessing](#threading-vs-multiprocessing)
  - [Multithreading](#multithreading)
  - [Multiprocessing](#multiprocessing)
  - [Function arguments](#function-arguments)
  - [The Asterisk (\*) operator](#the-asterisk--operator)
  - [Shallow vs Deep Copying](#shallow-vs-deep-copying)
  - [Context managers](#context-managers)

## General Python

Functions in Python are first class objects, meaning they can be passed around and used as arguments, just like any other object (string, int, float, list, and so on).

```python
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))  # Output: Hello Bob
print(greet_bob(be_awesome))  # Output: Yo Bob, together we are the awesomest!
```

## Lists

- **Explanation**: Ordered, mutable collection of elements, allowing duplicates
- **Syntax**: `my_list = [1, 2, 3]`, `my_list = list([1, 2, 3])`, `my_list = list()`, `my_list = []`
- **Used**: When you need an ordered collection of items that can be modified.
- **Avoid**: When you need a constant collection or fast lookups.

Creating a list:

```python
# The most common way (Creating a list with multiple elements)
my_list = [1, 2, 3] # Create a list
print(my_list)  # Output: [1, 2, 3]

# or (Creating a new list with the same elements multiple times)
my_list = [0] * 5
print(my_list)  # Output: [0, 0, 0, 0, 0]

# or (creating a list using the range() function):
my_list = list(range(10))
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# or (creating a list using the `list()` constructor):
my_list = list()
print(my_list)  # Output: []

# or
my_list = list([1, True, "some string", True])
print(my_list)  # Output: [1, True, 'some string', True]
```

Appending elements:

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

Accessing elements:

```python
my_list = [1, 2, 3]
print(my_list[0])  # Output: 1
```

With negative index we can access elements from the end:

```python
my_list = [1, 2, 3]
print(my_list[-2])  # Output: 2 (second element from the end)
```

Iterating over a list:

```python
my_list = [1, 2, 3]
for element in my_list:
    print(element) # Output: 1 2 3
```

Checking if an element exists in a list:

```python
my_list = ["banana", "cherry", 3]
if "banana" in my_list:
    print("yes")  # Output: yes
else:
    print("no")
```

Concatenating lists:

```python
my_list = [1, 2, 3]
my_second_list = [4, 5]
my_list += my_second_list
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

Slicing a list:

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = my_list[1:5]  # Output: [2, 3, 4, 5] (includes the first index but excludes the last)
b = my_list[1:]  # Output: [2, 3, 4, 5, 6, 7, 8, 9] (from the first index to the end)
c = my_list[:5]  # Output: [1, 2, 3, 4, 5] (from the start to the last index)
d = my_list[::2]  # Output: [1, 3, 5, 7, 9] (from the start to the end, skipping one element)
e = my_list[::-1]  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1] (from the end to the start, reversing)
```

Copying a list:

```python
# NOT RECOMMENDED because it creates a reference to the original list
original_list = [1, 2, 3]
new_list = original_list  # new_list is a reference to original_list
new_list.append(4) # modifying new_list affects original_list
print(original_list)  # Output: [1, 2, 3, 4]
```

```python
# RECOMMENDED because it creates a copy of the original list
original_list = [1, 2, 3]
new_list = original_list.copy()  # new_list is a copy of original_list
new_list.append(4) # modifying new_list does NOT affect original_list
print(original_list)  # Output: [1, 2, 3]

# or

original_list = [1, 2, 3]
new_list = list(original_list)  # new_list is a copy of original_list
new_list.append(4) # modifying new_list does NOT affect original_list
print(original_list)  # Output: [1, 2, 3]

# or

original_list = [1, 2, 3]
new_list = original_list[:]  # new_list is a copy of original_list
new_list.append(4) # modifying new_list does NOT affect original_list
print(original_list)  # Output: [1, 2, 3]
```

List comprehensions (they also create a copy):

> Syntax: `[expression for item in iterable]`

```python
my_list = [1, 2, 3, 4, 5]
squares = [x**2 for x in my_list]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

```python
my_list = [1, 2, 3, 4, 5]
even_squares = [x**2 for x in my_list if x % 2 == 0]
print(even_squares)  # Output: [4, 16]
```

```python
my_list = [1, 2, 3, 4, 5]
odd_squares = [x**2 if x % 2 == 1 else x for x in my_list]
print(odd_squares)  # Output: [1, 2, 9, 4, 25]
```

```python
my_list = [1, 2, 3, 4, 5]
odd_squares = [x**2 if x % 2 == 1 else x**3 for x in my_list]
print(odd_squares)  # Output: [1, 8, 9, 64, 25]
```

Unpacking a list:

> The number of variables on the left and the number of elements on the right have to match.

```python
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

We can unpack multiple elements into one variable using `*`:

```python
my_list = [1, 2, 3, 4, 5]
a, b, *c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3, 4, 5]
```

**Questions:**

> 1. **How to remove elements from a list?**
>
> - You can use methods like `remove(value)`, `pop(index)`, or `del list[index]` to remove elements.

> 2.  **What is the difference between `append()` and `extend()` methods?**
>
> - `append()` adds an element at the end of the list, while `extend()` takes an iterable and adds its elements to the list.

> 3. **Explain list comprehensions and provide an example.**
>
> - List comprehensions provide a concise way to create lists. Example: `[x**2 for x in range(5)]`.

## Tuples

- **Explanation**: Ordered, immutable (cannot be modified after creation) collection of elements. Also, it allows duplicates.
- **Syntax**: `my_tuple = (1, 2, "Max")`, `my_tuple = 1, 2, "Max"`, `my_tuple = tuple([1, 2, "Max"])`, `my_tuple = tuple()`, `my_tuple = ()`
- **Used**: When you need an ordered collection that shouldn't be modified. Also, it's used for objects that belong together.
- **Avoid**: When you need to modify elements frequently.

Creating a tuple:

```python
# The most common way (Creating a tuple with multiple elements)
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1

# or (Creating a tuple with one element)
my_tuple = (1,)  # Note the comma
print(type(my_tuple))  # Output: <class 'tuple'>

# or (Creating a tuple without parentheses)
my_tuple = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)

# or (Creating a tuple from a list)
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# or (Creating a tuple using the `tuple()` constructor and the `range()` function):
my_tuple = tuple(range(10))
print(my_tuple)  # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

Iterating over a tuple:

```python
my_tuple = (1, 2, 3)
for i in my_tuple:
    print(i)  # Output: 1 2 3
```

Checking if an element exists in a tuple:

```python
my_tuple = ("Max", True, 123)
if "Max" in my_tuple:
    print("yes")  # Output: yes
else:
    print("no")
```

Deleting a tuple:

```python
my_tuple = (1, 2, 3)
del my_tuple
print(my_tuple)  # Error: NameError: name 'my_tuple' is not defined
```

Slicing a tuple:

```python
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a = my_tuple[1:5]  # Output: (2, 3, 4, 5) (includes the first index but excludes the last)
b = my_tuple[1:]  # Output: (2, 3, 4, 5, 6, 7, 8, 9) (from the first index to the end)
c = my_tuple[:5]  # Output: (1, 2, 3, 4, 5) (from the start to the last index)
d = my_tuple[::2]  # Output: (1, 3, 5, 7, 9) (from the start to the end, skipping one element)
e = my_tuple[::-1]  # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1) (from the end to the start, reversing)
```

Copying a tuple:

```python
original_tuple = (1, 2, 3)
new_tuple = original_tuple  # new_tuple is a reference to original_tuple
print(new_tuple)  # Output: (1, 2, 3)
```

```python
original_tuple = (1, 2, 3)
new_tuple = original_tuple.copy()  # new_tuple is a copy of original_tuple
print(new_tuple)  # Output: (1, 2, 3)

# or

original_tuple = (1, 2, 3)
new_tuple = tuple(original_tuple)  # new_tuple is a copy of original_tuple
print(new_tuple)  # Output: (1, 2, 3)
```

Getting the number of elements in a tuple:

```python
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3
```

Getting the index of an element:

```python
my_tuple = (1, 2, 3, 2)
print(my_tuple.index(2))  # Output: 1 (index of the first occurrence)
```

Counting the number of occurrences of an element:

```python
my_tuple = (1, 2, 3, 2)
print(my_tuple.count(2))  # Output: 2; 2 occurs 2 times
```

Unpacking a tuple:

> The number of variables on the left and the number of elements on the right have to be the same.

```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

We can unpack multiple elements into one variable using `*`:

```python
my_tuple = (1, 2, 3, 4, 5)
a, *b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4] (b is a list)
print(c)  # Output: 5
```

Comparing tuples with lists (they are similar but not the same):

```python
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
print(my_tuple == my_list)  # Output: True
print(my_tuple is my_list)  # Output: False

# Comparing the number of bytes
import sys
print(sys.getsizeof(my_tuple))  # Output: 48 (bytes)
print(sys.getsizeof(my_list))  # Output: 64 (bytes); lists are larger than tuples even though they have the same elements

# Comparing the time needed to create tuples and lists
import timeit
print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))  # Output: 0.038 (seconds)
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))  # Output: 0.012 (seconds); tuples are faster to create than lists
```

**Questions:**

> 1. **Can you modify a tuple after it has been created?**
>
> - No, tuples are immutable, so their elements cannot be modified after creation.
> - However, you can convert a tuple to a list, modify that list, and then convert it back to a tuple.
>   Example: `my_tuple = tuple(my_list)`

> 2. **How can you concatenate two tuples?**
>
> - You can use the `+` operator: `tuple1 + tuple2`.

> 3. **What is the purpose of using tuples as keys in a dictionary?**
>
> - Tuples, being immutable, can be used as keys in dictionaries when you need a composite key.

> 4. **If you do mytuple = ("Max") what is the type of mytuple?**
>
> - It's a string, because the parentheses are interpreted as the parentheses used for grouping.

> 5. **The difference between tuples and lists. Also, what is the difference in speed/iterating over one vs the other?**
>
> - Tuples are immutable, while lists are mutable.
> - Tuples are faster than lists.
> - Tuples are used when you need immutable data, e.g. for keys in a dictionary, or as a key for a set, or when you're passing data to a function and you don't want that data to be modified.
> - Lists are used when you need mutable data, e.g. you want to be able to add or remove elements.
> - Tuples are created using parentheses, while lists are created using square brackets.
> - Tuples are faster than lists, because they are immutable, so Python doesn't have to do as much work behind the scenes. It is faster to iterate over a tuple than a list, because Python stops iterating over a tuple after reaching the last element, while it has to check the size of a list on every iteration.
> - Tuples have fewer available methods than lists.
> - Tuples are used as keys in dictionaries, while lists cannot be used as keys in dictionaries.
> - Tuples are used in string formatting, while lists cannot be used in string formatting.
> - Tuples are used in named tuples, while lists cannot be used in named tuples.
> - Tuples are returned by some built-in methods, such as `enumerate()`, `zip()`, and `reversed()`.
> - Tuples are used for parallel assignment, while lists cannot be used for parallel assignment.
> - Tuples are used for returning multiple values from a function, while lists cannot be used for returning multiple values from a function.

## Dictionaries

- **Explanation**: Unordered collection of key-value pairs. Allows duplicates. Keys must be unique but values can be duplicated. Mutable.
- **Syntax**: `my_dict = {'key': 'value', 'name': 'Max'}`
- **Used**: For quick lookups based on keys.
- **Avoid**: When order matters, or you need constant time for all operations.

Creating a dictionary:

```python
my_dict = {'name': 'John', 'age': 30}
# print(my_dict['name']) # Output: John
# Notice that we use square brackets for accessing elements,
# just like for lists, but we use keys instead of indexes

# or (using the `dict()` constructor)

my_dict = dict(name='John', age=30) # Note: no quotes for the keys (only for the values)
print(my_dict['name']) # Output: John
```

Accessing values:

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])  # Output: John
# Notice that we use square brackets for accessing elements, just like for lists, but we use keys instead of indexes
```

Updating a dictionary:

```python
my_dict = {'name': 'John', 'age': 30}
my_dict['name'] = 'Max' # dictionaries are mutable, so we can update them
print(my_dict)  # Output: {'name': 'Max', 'age': 30}

# or

my_dict = {'name': 'John', 'age': 30, "email": "john@xyz.com"}
my_dict.update({'name': 'Max', 'age': 30, city: "New York"})
# my_dict.update(name='Max', age=30, city="New York")  # same as above
print(my_dict)  # Output: {'name': 'Max', 'age': 30, 'email': 'john@xyz', 'city': 'New York'}
# Notice: If there are duplicate keys, the last one wins
```

Deleting a key-value pair:

```python
my_dict = {'name': 'John', 'age': 30}
del my_dict['name']
print(my_dict)  # Output: {'age': 30}

# or

# Deleting a specific key-value pair and returning the value
my_dict = {'name': 'John', 'age': 30}
my_dict.pop('name')
print(my_dict)  # Output: {'age': 30}
```

Deleting all elements:

```python
my_dict = {'name': 'John', 'age': 30}
my_dict.clear()
print(my_dict)  # Output: {}
```

Deleting the last inserted key-value pair (Python 3.7+):

```python
my_dict = {'name': 'John', 'age': 30}
my_dict.popitem()
print(my_dict)  # Output: {'name': 'John'}
```

Checking if a key exists:

```python
my_dict = {'name': 'John', 'age': 30}

if 'name' in my_dict:
    print(my_dict['name'])  # Output: John

# or

print(my_dict.get('name'))  # Output: John

# or, with try-except

try:
    print(my_dict['name'])  # Output: John
except KeyError:
    print("Error")
```

Iterating over a dictionary:

```python
my_dict = {'name': 'John', 'age': 30}
for key in my_dict:
    print(key, my_dict[key])  # Output: name John \n age 30

# or

for key, value in my_dict.items(): # items() returns a list of key-value pairs
    print(key, value)  # Output: name John \n age 30

# or

for value in my_dict.values(): # values() returns a list of values in the dictionary
    print(value)  # Output: John \n 30

# or

for key in my_dict.keys(): # keys() returns a list of keys in the dictionary
    print(key)  # Output: name \n age
```

Copying a dictionary:

```python
# NOT RECOMMENDED because it creates a reference to the original dictionary
original_dict = {'name': 'John', 'age': 30}
new_dict = original_dict  # new_dict is a reference to original_dict
new_dict['name'] = 'Max'  # modifying new_dict affects original_dict
print(new_dict)  # Output: {'name': 'Max', 'age': 30};
```

```python
# RECOMMENDED because it creates a copy of the original dictionary
original_dict = {'name': 'John', 'age': 30}
new_dict = original_dict.copy()  # new_dict is a copy of original_dict
print(new_dict)  # Output: {'name': 'John', 'age': 30}

# or

original_dict = {'name': 'John', 'age': 30}
new_dict = dict(original_dict)  # new_dict is a copy of original_dict
print(new_dict)  # Output: {'name': 'John', 'age': 30}

# or

original_dict = {'name': 'John', 'age': 30}
new_dict = {**original_dict}  # new_dict is a copy of original_dict
print(new_dict)  # Output: {'name': 'John', 'age': 30}
```

Merging two dictionaries:

```python
dict1 = {'name': 'John', 'age': 30}
dict2 = {'location': 'London'}
dict1.update(dict2)
print(dict1)  # Output: {'name': 'John', 'age': 30, 'location': 'London'}

# or

dict1 = {'name': 'John', 'age': 30}
dict2 = {'location': 'London'}
dict3 = {**dict1, **dict2}
# Notice: **dict1 unpacks the dictionary, so that we get the key-value pairs as keyword arguments
# Note: If there are duplicate keys, the last one wins
print(dict3)  # Output: {'name': 'John', 'age': 30, 'location': 'London'}
```

Key types in dictionaries:

> - Keys must be immutable (strings, numbers, or tuples with immutable elements).
> - Lists cannot be used as keys because they are mutable, which means they can be modified after creation.

```python
my_dict = {3: 9, 6: 36, 9: 81} # int as a key
print(my_dict[3])  # Output: 9

# or

my_dict = {(1, 2, 3): 6, (4, 5): 9} # tuple as a key
print(my_dict[(4, 5)])  # Output: 9
```

Getting a list of keys, values, or key-value pairs:

```python
my_dict = {'name': 'John', 'age': 30}
print(len(my_dict))  # Output: 2

# Getting a list of keys:
my_dict = {'name': 'John', 'age': 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# Getting a list of values:
my_dict = {'name': 'John', 'age': 30}
print(my_dict.values())  # Output: dict_values(['John', 30])

# Getting a list of key-value pairs:
my_dict = {'name': 'John', 'age': 30}
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30)])
```

**Questions:**

> 1. **How do you check if a key exists in a dictionary?**
>
> - You can use the `in` keyword: `if key in my_dict:`.

> 2. **Explain the difference between `dict.items()`, `dict.keys()`, and `dict.values()`.**
>
> - `items()` returns key-value pairs, `keys()` returns keys, and `values()` returns values.

> 3. **How can you merge two dictionaries?**
>
> - You can use the `update()` method or dictionary unpacking: `merged_dict = {**dict1, **dict2}`.

## Sets

- **Explanation**: Unordered, mutable collection of unique elements.
- **Syntax**: `my_set = {1, 2, 3}`; notice that we use curly brackets for sets, just like for dictionaries, but sets don't have key-value pairs.
- **Used**: When uniqueness matters, and order doesn't.
- **Avoid**: When you need order or key-value pairs.

Creating a set:

```python
# CORRECT way

# The most common way (Creating a set with multiple elements)
my_set = {1, 2, 3, 1}
print(my_set)  # Output: {1, 2, 3}; notice that the duplicate element is removed

# or

my_set = set([1, 2, 3, 1])
print(my_set)  # Output: {1, 2, 3}; notice that the duplicate element is removed

# or

my_set = set("Hello")
print(my_set)  # Output: {'e', 'H', 'l', 'o'}; notice that the duplicate element is removed; also, the elements are not ordered, because sets are unordered

# or

my_set = set()
print(my_set)  # Output: set()

# INCORRECT way (check previous example, and examples before for the correct way)
my_set = {}  # This is wrong! This is an empty dictionary, not an empty set
```

Adding elements:

```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(3)
my_set.add(8)
print(my_set)  # Output: {1, 2, 3, 4, 8}; notice that the duplicate element is not added
print(my_set)
```

Removing elements:

```python
my_set = {1, 2, 3}
my_set.remove(3)
print(my_set)  # Output: {1, 2}
# In case the element does not exist, remove() will raise an error

# or

my_set = {1, 2, 3}
my_set.discard(3)
print(my_set)  # Output: {1, 2}
# In case the element does not exist, discard() will NOT raise an error

# or (clearing a set)
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# or (removing a random element)
my_set = {1, 2, 3}
print(my_set.pop())  # Output: 1; notice that the element removed is random
```

Iterating over a set:

```python
my_set = {1, 2, 3}
for i in my_set:
    print(i)  # Output: 1 2 3
```

Checking if an element exists:

```python
my_set = {1, 2, 3}
if 1 in my_set:
    print("yes")  # Output: yes
else:
    print("no")
```

Union and intersection:

> `union()` will not modify the original set (it will return a new set), but `update()` will.
>
> > `update()` will add elements from the other set to the original set.
> > Example: `my_set.update(other_set)` will add all elements from other_set to my_set.

> `intersection()` will not modify the original set (it will return a new set), but `intersection_update()` will.
>
> > `intersection_update()` will remove all elements that are not in the other set from the original set.
> > Example: `my_set.intersection_update(other_set)` will remove all elements from my_set that are not in other_set.

```python
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Union
u = odds.union(evens)
print(u)  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; if there are duplicates, they are removed

# Intersection
i = odds.intersection(evens)
print(i)  # Output: set(); there are no common elements

i = odds.intersection(primes)
print(i)  # Output: {3, 5, 7}
```

Difference:

> `difference()` will not modify the original set, (it will return a new set), but `difference_update()` will.
>
> > `difference_update()` will remove all elements that are in the other set from the original set
> > Example: `odds.difference_update(primes)` will remove 3, 5, and 7 from odds.

```python
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# Difference
diff = setA.difference(setB) # or setA - setB; returns elements that are in setA but not in setB
print(diff)  # Output: {4, 5, 6, 7, 8, 9}

diff = setB.difference(setA) # or setB - setA; returns elements that are in setB but not in setA
print(diff)  # Output: {10, 11, 12}
```

Symmetric difference:

> `symmetric_difference()` will not modify the original set (it will return a new set), but `symmetric_difference_update()` will.
>
> > `symmetric_difference_update()` will remove all elements that are in both sets from the original set
> > Example: `setA.symmetric_difference_update(setB)` will remove 1, 2, and 3 from setA.

```python
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# Symmetric difference
diff = setA.symmetric_difference(setB) # or setA ^ setB; returns elements that are in setA and setB but not in both
print(diff)  # Output: {4, 5, 6, 7, 8, 9, 10, 11, 12}; notice that the elements that are in both sets are not included
```

Subset and superset:

```python
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}

# Subset
print(setA.issubset(setB))  # Output: False; checks if all elements of setA are in setB
print(setB.issubset(setA))  # Output: True

# Superset
print(setA.issuperset(setB))  # Output: True; checks if all elements of setB are in setA
print(setB.issuperset(setA))  # Output: False
```

Disjoint:

```python
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
setC = {10, 11, 12}

# Disjoint
print(setA.isdisjoint(setB))  # Output: False; checks if setA and setB have no common elements
print(setA.isdisjoint(setC))  # Output: True
```

Copying a set:

```python
# NOT RECOMMENDED because it creates a reference to the original set
original_set = {1, 2, 3}
new_set = original_set  # new_set is a reference to original_set
new_set.add(4) # modifying new_set affects original_set
print(original_set)  # Output: {1, 2, 3, 4}
```

```python
# RECOMMENDED because it creates a copy of the original set
original_set = {1, 2, 3}
new_set = original_set.copy()  # new_set is a copy of original_set
new_set.add(4) # modifying new_set does NOT affect original_set
print(original_set)  # Output: {1, 2, 3}

# or

original_set = {1, 2, 3}
new_set = set(original_set)  # new_set is a copy of original_set
new_set.add(4) # modifying new_set does NOT affect original_set
print(original_set)  # Output: {1, 2, 3}
```

Frozen sets:

> Frozen sets are immutable sets. They are created using the `frozenset()` constructor.

```python
my_set = frozenset([1, 2, 3, 4])
my_set.add(5)  # Error: AttributeError: 'frozenset' object has no attribute 'add'
```

**Questions:**

> 1. **What operations can you perform on sets (union, intersection, difference)?**
>
> - Union: `set1 | set2`, Intersection: `set1 & set2`, Difference: `set1 - set2`.

> 2. **How can you check if a set is a subset or superset of another set?**
>
> - Subset: `set1.issubset(set2)`, Superset: `set1.issuperset(set2)`.

> 3. **Can sets contain mutable elements like lists?**
>
> - No, sets can only contain hashable (immutable) elements.

## Strings

- **Explanation**: Ordered, immutable collection of characters.
- **Syntax**: `my_string = "Hello"`
- **Used**: For representing and manipulating text.
- **Avoid**: When dealing with highly dynamic or binary data.

Creating a string:

```python
my_string = "Hello"

# Triple quotes are used for multi-line strings
my_string = """Hello
World""" # or '''Hello \n World'''
```

Accessing characters:

```python
my_string = "Hello"
print(my_string[0])  # Output: H; we can also use negative indexing: my_string[-1] returns o
```

Changing a character:

```python
# CORRECT way (strings are immutable, so we need to create a new string)
my_string = "Hello"
my_string = my_string[:4] + "o"  # strings are immutable, so we need to create a new string
print(my_string)  # Output: Hello
```

```python
# INCORRECT way (strings are immutable, so we need to create a new string)
my_string = "Hello"
my_string[4] = "o"  # Error: TypeError: 'str' object does not support item assignment
print(my_string)
```

Slicing:

```python
my_string = "Hello World"
print(my_string[1:5])  # Output: ello
print(my_string[1:])  # Output: ello World
print(my_string[:5])  # Output: Hello
print(my_string[:])  # Output: Hello World
print(my_string[::2])  # Output: HloWrd
print(my_string[::-1])  # Output: dlroW olleH
```

Concatenating strings:

```python
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)  # Output: Hello Tom
```

Iterating over a string:

```python
my_string = "Hello"
for i in my_string:
    print(i)  # Output: H e l l o
```

Checking if a substring exists:

```python
my_string = "Hello World"
if "Hello" in my_string:
    print("yes")  # Output: yes
else:
    print("no")
```

Stripping whitespace:

```python
my_string = "   Hello World   "
print(my_string.strip())  # Output: Hello World
# remember that strings (like the original string my_string) are immutable,
# so we need to assign the result to a new variable if we want to keep the
# result of the operation
```

Changing case:

```python
my_string = "Hello World"
print(my_string.lower())  # Output: hello world
print(my_string.upper())  # Output: HELLO WORLD
```

Checking starting/ending:

```python
my_string = "Hello World"
print(my_string.startswith("He"))  # Output: True
print(my_string.endswith("ld"))  # Output: True
```

Finding position:

```python
my_string = "Hello World"
print(my_string.find("o"))  # Output: 4; returns the index of the first occurrence
print(my_string.find("lo"))  # Output: 3
print(my_string.find("p"))  # Output: -1; returns -1 if the substring is not found
```

Counting occurrences:

```python
my_string = "Hello World"
print(my_string.count("o"))  # Output: 2
print(my_string.count("or"))  # Output: 1
print(my_string.count("p"))  # Output: 0
```

Replacing a substring:

```python
my_string = "Hello World"
print(my_string.replace("World", "Universe"))  # Output: Hello Universe
```

Lists and strings:

> Default separator is any whitespace. If you want to split by commas, you can use `my_string.split(',')`.

```python
# Splitting a string into a list of substrings separated by a delimiter
my_string = "how are you doing"
my_list = my_string.split() # the default separator is any whitespace
print(my_list)  # Output: ['how', 'are', 'you', 'doing']

# Joining a list of strings into a single string using a delimiter
my_list = ['how', 'are', 'you', 'doing']
my_string = ' '.join(my_list)
print(my_string)  # Output: how are you doing
```

Good, and bad practice concerning the join() method; also timing the execution time of a program:

```python
from timeit import default_timer as timer

my_list = ['a'] * 1000000
print(my_list)  # Output: ['a', 'a', ... (1000000 times)]

# Bad practice (using for loop)
start = timer()
my_string = ''
for i in my_list:
    my_string += i # a new string object is created at each iteration which is inefficient!
stop = timer()
print(stop - start)  # Output: 0.35600000000000045

# Good practice (using join())
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)  # Output: 0.006999999999999559
```

Formatting strings:

```python
# Using f-strings; Python 3.6+; recommended
var = "Tom"
my_string = f"the variable is {var}"
print(my_string)  # Output: the variable is Tom

# or

var = 3.1234567
my_string = f"the variable is {var:.2f}" # notice that the f-string rounds the value
print(my_string)  # Output: the variable is 3.12

# or (using the format() method; old formatting style)
var = "Tom"
my_string = "the variable is {}".format(var)
print(my_string)  # Output: the variable is Tom

# or (using %; old formatting style)
var = "Tom" # in case we have an integer, we can use %d instead of %s in the string below
my_string = "the variable is %s" % var
print(my_string)  # Output: the variable is Tom
```

**Questions:**

> 1. **How do you concatenate strings in Python?**
>
> - You can use the `+` operator or the `join()` method: `' '.join(['Hello', 'World'])`.

> 2. **Explain the difference between `str()` and `repr()` functions.**
>
> - `str()` is used for creating output for end-user, `repr()` is used for development and debugging.

> 3. **What are some common string methods for manipulation and formatting?**
>
> - Methods like `split()`, `strip()`, `replace()`, and formatting with `format()` or f-strings.

## Collections

- **Explanation**: Collection module providing specialized container datatypes and provides alternatives (with some additional functionalities) to Python's general purpose built-in containers, dict, list, set, and tuple. Those alternatives are Counter, namedtuple, OrderedDict, defaultdict, deque (as well as UserDict and ChainMap).
- **Syntax**: `from collections import Counter, defaultdict`
- **Used**: When you need advanced data structures like named tuples, dictionaries with default values, or ordered dictionaries.
- **Avoid**: For basic lists or dictionaries.

Creating a Counter:

```python
from collections import Counter
my_list = [1, 2, 3, 1, 2, 1]
counter = Counter(my_list) # This will create a dictionary with the elements of the list as keys and their occurrences as values
print(counter)  # Output: Counter({1: 3, 2: 2, 3: 1}); 1 occurs 3 times, 2 occurs 2 times, and 3 occurs 1 time

# or

a = "aaaaabbbbbccccc"
counter = Counter(a)
print(counter)  # Output: Counter({'a': 5, 'b': 5, 'c': 5})
```

Accessing the items (key-value pairs) of a Counter:

```python
print(counter.items())  # Output: dict_items([('a', 5), ('b', 5), ('c', 5)])

# Like with any dictionary, we can access the keys and values separately
print(counter.keys())  # Output: dict_keys(['a', 'b', 'c'])
print(counter.values())  # Output: dict_values([5, 5, 5])

# We can also access the most common elements
# This will return a list of tuples, where the first element of the tuple is the key and the second element is the value
print(counter.most_common(2))  # Output: [('a', 5), ('b', 5)]; returns the 2 most common elements
# The following will return the most common element
print(counter.most_common(1)[0][0])  # Output: a

print(list(my_counter.elements()))  # Output: ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']
# This will return a list with all the elements (keys) of the counter, each repeated as many times as its count
```

Named tuples:

```python
from collections import namedtuple
# Let's define a 2D point (class)
Point = namedtuple('Point', 'x,y') # or Point = namedtuple('Point', ['x', 'y']); The same name should be used for the variable name and the namedtuple
# This created a new class named Point, which we can use to create points

pt = Point(1, -4)
print(pt)  # Output: Point(x=1, y=-4)
print(pt.x, pt.y)  # Output: 1 -4; accessing the elements of the namedtuple
```

Ordered dictionaries:

> Ordered dictionaries are dictionaries that remember the order of the keys that were inserted first.
> Ordered dictionaries became less relevant since Python 3.7, because regular dictionaries are ordered since then.

```python
from collections import OrderedDict
# Regular dictionary
ordered_dict = OrderedDict() # or ordered_dict = {} as of Python 3.7
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 1
print(ordered_dict)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)]); notice that the elements are ordered

# or

ordered_dict = OrderedDict({'b': 2, 'c': 3, 'a': 1})
print(ordered_dict)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)]); notice that the elements are ordered
```

Default dictionaries:

> Default dictionaries are dictionaries that return a default value when the key does not exist (instead of raising `KeyError`).
> For example if the key does not exist (was not set or similar), `my_dict['some_key']` will return the default value instead of raising `KeyError`.

> Default dictionaries are useful when you want to avoid key errors.

```python
from collections import defaultdict
d = defaultdict(int) # int is the default type, also works with list, set, tuple, str, dict, etc.
# Example 1: If we set the float as the default type (defaultdict(float)), the default value will be 0.0
# Example 2: If we set the list as the default type (defaultdict(list)), the default value will be []
d['a'] = 1
d['b'] = 2
print(d['c'])  # Output: 0; returns the default value for the type (0 for int)
```

Deque:

> Deque is a double-ended queue, suitable for efficiently adding and removing elements from both ends.

```python
from collections import deque
d = deque()
d.append(1) # add to the right
d.appendleft(2) # add to the left
print(d)  # Output: deque([2, 1])

d.pop() # remove from the right
d.popleft() # remove from the left
print(d)  # Output: deque([])

d.extend([4, 5, 6]) # add multiple elements to the right
d.extendleft([1, 2, 3]) # add multiple elements to the left
print(d)  # Output: deque([3, 2, 1, 4, 5, 6])

d.rotate(1) # right rotation
print(d)  # Output: deque([6, 3, 2, 1, 4, 5])

d.rotate(-1) # left rotation
print(d)  # Output: deque([3, 2, 1, 4, 5, 6])
```

**Questions:**

> 1. **When would you use `namedtuple` from the `collections` module?**
>
> - `namedtuple` is used when you want to create a simple class for storing data without methods.

> 2. **Explain the purpose of the `deque` data structure.**
>
> - `deque` is a double-ended queue, suitable for efficiently adding and removing elements from both ends.

> 3. **What is the use case for the `defaultdict` class?**
>
> - `defaultdict` is used when you want a dictionary with default values for new keys.

## Itertools

- **Explanation**: Module providing fast, memory-efficient (advanced) tools for handling iterators.
  > Iterators are data types that can be used in a `for` loop.\
  > The most common iterator in Python is the list. The tools are: `product()`, `permutations()`, `combinations()`, `accumulate()`, `groupby()` and infinite iterators like `count()`, `cycle()`, `repeat()` etc.
- **Syntax**: `from itertools import combinations`
- **Used**: When dealing with iterators and combinatorial functions.
- **Avoid**: For simple iteration over lists or ranges.

Creating iterators:

Product:

> The Cartesian product of two sets A and B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B.

```python
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b) # this gives us a Cartesian product of the two lists
print(list(prod))  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]; notice that the result is a list of tuples
```

Permutations:

> Permutations are the different ways in which a collection of items can be arranged, where the order of the arrangement matters.

```python
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a) # this gives us all the possible permutations of the list
print(list(perm))  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]; notice that the result is a list of tuples

# or (we can also specify the length of the permutation)
perm = permutations(a, 2) # this gives us all the possible permutations of length 2
print(list(perm))  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]; notice that the result is a list of tuples
```

Combinations:

> Combinations are the different ways in which a collection of items can be selected, where order of selection does not matter.

```python
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2) # this gives us all the possible combinations of length 2
print(list(comb))  # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]; notice that the result is a list of tuples

comb_wr = combinations_with_replacement(a, 2) # this gives us all the possible combinations with replacement of length 2
print(list(comb_wr))  # Output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]; notice that the result is a list of tuples
```

Accumulate:

> `accumulate()` makes an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).

```python
from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a) # this gives us the accumulated sums by default(!)
print(list(acc))  # Output: [1, 3, 6, 10]; notice that the result is a list of integers

# or (we can also specify the function)
import operator
acc = accumulate(a, func=operator.mul) # this gives us the accumulated products
print(list(acc))  # Output: [1, 2, 6, 24]; notice that the result is a list of integers
```

Groupby:

> `groupby()` makes an iterator that returns consecutive keys and groups from the iterable. The key is a function computing a key value for each element. If not specified or is `None`, key defaults to an identity function and returns the element unchanged. Generally, the iterable needs to already be sorted on the same key function.

```python
from itertools import groupby
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3) # this gives us the elements grouped by the key function
for key, value in group_obj:
    print(key, list(value))  # Output: True [1, 2]; False [3, 4]; notice that the result is a list of integers

# or (we can also use lambda functions)
group_obj = groupby(a, key=lambda x: x < 3) # this gives us the elements grouped by the key function
for key, value in group_obj:
    print(key, list(value))  # Output: True [1, 2]; False [3, 4]; notice that the result is a list of integers
```

Infinite iterators:

> `count(start=0, step=1)` counts up infinitely from `start` by `step`.
> `cycle(iterable)` infinitely iterates over elements of `iterable`.
> `repeat(object, times=None)` repeats `object` infinitely, unless the `times` argument is specified.

```python
from itertools import count, cycle, repeat
for i in count(10): # this will count up infinitely from 10
    print(i)  # Output: 10 11 12 13 14 15 16 17 18 19 20 ...
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a): # this will infinitely iterate over the elements of the list
    print(i)  # Output: 1 2 3 1 2 3 1 2 3 1 2 3 ...
    if i == 3:
        break

for i in repeat(1, 4): # this will repeat the element 1 four times
    print(i)  # Output: 1 1 1 1
```

**Questions:**

> 1. **What is the purpose of the `cycle` function in itertools?**
>
> - `cycle` infinitely iterates over elements of an iterable.

> 2. **Explain the difference between `zip()` and `zip_longest()` functions.**
>
> - `zip()` stops when the shortest iterable is exhausted, `zip_longest()` continues until the longest is exhausted, filling with a specified value for missing elements.

> 3. **How can you use `itertools.chain()` for combining multiple iterables?**
>
> - `itertools.chain(iterable1, iterable2, ...)` combines multiple iterables into a single iterable.

## Lambda Functions

- **Explanation**: Anonymous (without a name), one-liner functions.
- **Syntax**: `lambda arguments: expression` (which returns the result), e.g. `lambda x: x * 2`
- **Used**: When a small function is needed for a short period (like one-time use) or it is used as an argument for a higher-order function like `map()`, `filter()`, `reduce()`, `sorted()`, `min()`, `max()`, `sum()`, `all()`, `any()`, `apply()`, `count()`, `enumerate()`, `len()`, `list()`, `round()`, `sorted()`, `zip()`, etc.
  > Higher-order functions are functions that take other functions as arguments or return them as results.
- **Avoid**: For complex logic or functions that require multiple lines.

Creating a lambda function:

```python
multiply_by_two = lambda x: x * 2
print(multiply_by_two(3))  # Output: 6

# With multiple arguments
add_two_numbers = lambda x, y: x + y
print(add_two_numbers(3, 4))  # Output: 7

# With default arguments
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) # this will sort the list of tuples based on the first element of each tuple
print(points2D_sorted)  # Output: [(1, 2), (5, -1), (10, 4), (15, 1)]; sorted() uses the default sorting criteria (the first element of each tuple); of course, we can also use a lambda function for the sorting criteria

# Here is an example of using a lambda function for the sorting criteria:

# sorted() function takes a key argument, which is a function that is called on each list element before comparing it to other elements
# For example, if we want to sort a list of tuples based on the second element of each tuple, we can do the following
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1]) # this will sort the list of tuples based on the second element of each tuple
print(a)  # Output: [(13, -3), (4, 1), (1, 2), (9, 10)]

# Now, we'll sort by the sum of each tuple:

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[0] + x[1]) # this will sort the list of tuples based on the sum of each tuple
print(a)  # Output: [(1, 2), (4, 1), (13, -3), (9, 10)]
```

map() function:

> map() transforms each element with a function and returns an iterator of results.
> map() transforms each element of an iterable based on a function and returns an iterator of results.
> Syntax: `map(function, iterable)`; iterable can be a list, tuple, set, etc.

```python
original_list = [1, 2, 3, 4, 5]
mapped_list = map(lambda x: x * 2, original_list) # this will multiply each element of the list by 2
print(list(mapped_list))  # Output: [2, 4, 6, 8, 10]; we had to convert the iterator to a list to print it because the result of map() is an map object (iterator)

# or (we can also achieve the same with a list comprehension)

original_list = [1, 2, 3, 4, 5]
mapped_list = [x * 2 for x in original_list]
print(mapped_list)  # Output: [2, 4, 6, 8, 10]
```

filter() function:

> filter() returns an iterator yielding those items of iterable for which function(item) returns true.

```python
original_list = [1, 2, 3, 4, 5]
filtered_list = filter(lambda x: x % 2 == 0, original_list) # this will filter out the odd numbers
print(list(filtered_list))  # Output: [2, 4]; we had to convert the iterator to a list to print it because the result of filter() is an filter object (iterator)

# or (we can also achieve the same with a list comprehension)

original_list = [1, 2, 3, 4, 5]
filtered_list = [x for x in original_list if x % 2 == 0]
print(filtered_list)  # Output: [2, 4]
```

reduce() function:

> reduce() applies a rolling computation to sequential pairs of values in a list.
> reduce() always has two arguments because it always works on two elements at a time.

```python
from functools import reduce
original_list = [1, 2, 3, 4, 5]
reduced_list = reduce(lambda x, y: x + y, original_list) # this will sum all the elements of the list
print(reduced_list)  # Output: 15
```

**Questions:**

> 1. **What are the advantages of using lambda functions over regular functions?**
>
> - Lambdas are concise and can be used for short-lived, simple functions without defining a full function.

> 2. **How can you use lambda functions in conjunction with functions like `map()` and `filter()`?**
>
> - `map(lambda x: x * 2, my_list)` doubles each element in `my_list`.

> 3. **Are there any limitations or scenarios where lambda functions are not suitable?**
>
> - Lambdas are limited to a single expression, making them unsuitable for complex logic or functions with multiple statements. Use regular functions in such cases.

## Exceptions and Errors

- **Explanation**: Events that occur during program execution that disrupt normal flow. Errors can be syntax errors or exceptions.
- **Syntax**:
  ```python
  try:
      # code that may raise an exception
  except SomeException as e:
      # handle exception
  else:
      # executed if no exception
  finally:
      # always executed
  ```
- **Used**: Handling unexpected situations to prevent program termination. In other words, error handling allows us to let the script continue running even if there is an error - except for fatal errors, when we raise an exception using `raise`.
- **Avoid**: Using exceptions for control flow.

### Syntax errors

Syntax errors occurs when the parses encounters an incorrect statement:

```python
a = 5 print(a)  # Error: SyntaxError: invalid syntax; missing a semicolon

# or

print("Hello World"  # Error: SyntaxError: unexpected EOF while parsing; missing a closing parenthesis
```

### Exceptions

Even if a statement is syntactically correct, it may cause an error when executed. Errors detected during execution are called exceptions (or exception error) and are not unconditionally fatal. \
There are several different error classes, all of which are subclasses of `BaseException`.

```python
# Trying to add a string and an integer; raises a TypeError
a = 5 + "10"  # Error: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# or

# Importing a module that does not exist; raises a ModuleNotFoundError (Python 3.6+)
import somemodule  # Error: ModuleNotFoundError: No module named 'somemodule'

# or

# Accessing an undefined variable; raises a NameError
print(b)  # Error: NameError: name 'b' is not defined

# or

# Opening a file that does not exist; raises a FileNotFoundError
with open('file.txt') as f:  # Error: FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
    print(f.read())

# or

# Trying to convert a string that is not a number to an integer; raises a ValueError
# If a function, or operation, receives an argument of the correct type but an inappropriate value, it may still raise a ValueError
a = [1, 2, 3]
a.remove(4)  # Error: ValueError: list.remove(x): x not in list

# or

# Accessing a non-existent index in a list; raises an IndexError
a = [1, 2, 3]
print(a[4])  # Error: IndexError: list index out of range

# Accessing a non-existent key in a dictionary; raises a KeyError
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict["job"])  # Error: KeyError: 'job'

# or

# Division by zero; raises a ZeroDivisionError
a = 5 / 0  # Error: ZeroDivisionError: division by zero
```

#### Raising exceptions

If we want to raise an exception ourselves (when a certain condition is met), we can use the `raise` keyword:

```python
x = -5
if x < 0:
    # raising a BaseException
    raise Exception("x should be positive")  # Error: Exception: x should be positive
```

Second way to raise an exception is using the `assert` statement:

```python
x = -5
assert (x >= 0), "x should be positive"  # Error: AssertionError: x should be positive
```

If we want to handle exceptions, we can use the `try`, `except`, `else`, and `finally` blocks:

```python
try:
    a = 5 / 0
except ZeroDivisionError as e:
    # The program will continue executing after the exception is handled
    print("An error occurred:", e)  # Output: An error occurred: division by zero
else:
    print("No exceptions occurred")  # This will not be executed
finally:
    print("This will be executed no matter what")  # Output: This will be executed no matter what
```

> HINT: The `else` block is executed only if no exceptions are raised in the corresponding `try` block. It provides a way to specify code that should run when no exceptions occur.
>
> HINT: The `finally` block is always executed, regardless of whether an exception occurred or not. It provides a way to specify code that should run no matter what.

We can also catch the type of exception:

```python
try:
    a = 5 / 0
except Exception as e:
    print("An error occurred:", e)  # Output: An error occurred: division by zero
    # The error "division by zero" is an instance of the ZeroDivisionError class
```

> HINT: It is a good practice to catch specific exceptions and handle them accordingly. Catching all exceptions with `except Exception` is not recommended. Basically, we need to know what exceptions we are catching and why.

We can also have multiple statements in the `except` block:

```python
try:
    a = 5 / 1
    b = a + "10"
except ZeroDivisionError as e:
    print("An error occurred:", e)  # This will not be executed
except TypeError as e:
    print("An error occurred:", e)  # Output: An error occurred: unsupported operand type(s) for +: 'float' and 'str'
```

#### Custom exceptions

We can define our own Error classes by subclassing the `BaseException` class:

```python
class ValueTooHighError(Exception): # 'Exception' is the base class for all exceptions
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooLowError("Value is too low", x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)  # Output: Value is too high
except ValueTooLowError as e:
    print(e.message, e.value)  # Output: Value is too low 3
```

**Questions:**

> **1. What is the purpose of the `else` block in a try-except statement?**
>
> The `else` block in a try-except statement is executed only if no exceptions are raised in the corresponding try block. It provides a way to specify code that should run when no exceptions occur.

> **2. How can you raise a custom exception in Python?**
>
> You can raise a custom exception using the `raise` keyword, followed by the exception class and an optional error message. For example:
>
> ```python
> class CustomError(Exception):
>     pass
> raise CustomError("This is a custom exception.")
> ```

> **3. Explain the difference between `except Exception` and `except SomeSpecificException`.**
>
> `except Exception` catches any exception, including built-in and custom exceptions. On the other hand, `except SomeSpecificException` catches only instances of the specified exception class, providing more targeted exception handling.

## Logging

- **Explanation**: Recording information about events for analysis.
- **Syntax**:
  ```python
  import logging
  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
  logging.info("This is an information message.")
  ```
- **Used**: Debugging, monitoring, and analyzing program behavior.
- **Avoid**: Excessive logging that impacts performance.

**Questions:**

> **1. How can you configure different log levels in Python?**
>
> Log levels in Python, from least to most severe, are DEBUG, INFO, WARNING, ERROR, and CRITICAL. You can configure the logging level using `basicConfig` or by setting the level on specific loggers or handlers.

> **2. Explain the difference between `logging.info()` and `logging.debug()`.**
>
> `logging.info()` is used for informational messages, providing details about the program's operation. `logging.debug()` is used for debugging messages, providing more detailed information for troubleshooting.

> **3. What is the purpose of log formatting?**
>
> Log formatting allows you to define the structure of log messages. It includes information such as the timestamp, log level, and the actual log message. Proper log formatting improves readability and consistency in logs.

## JSON

- **Explanation**: Data interchange format based on JavaScript object syntax. JSON is a shorthand for JavaScript Object Notation.
- **Syntax**:
  ```python
  import json
  data = {'key': 'value'}
  json_string = json.dumps(data)
  ```
- **Used**: Sending and receiving data between systems.
- **Avoid**: Storing sensitive or large binary data.

> NOTE: Python already has a built-in package for working with JSON, so you don't need to install anything to get started.

Now we'll see how to encode and decode JSON data.

JSON data looks similar to Python dictionaries, but there are some differences. For example, JSON keys must be strings, and JSON values must be one of the following data types: string, number, object (JSON object), array, boolean, null.
Example:

```python
{
    "name": "John",
    "age": 30,
    "is_student": true,
    "courses": ["Math", "Physics", "Computer Science"],
    "hobbies": ["Reading", "Hiking"],
    "hasChildren": false,
    "address": [
        {
            "type": "home",
            "city": "New York",
            "zip": "10001",
            "street": "123 Main St"
        },
        {
            "type": "work",
            "city": "New York",
            "zip": "10001",
            "street": "456 Elm St"
        }
    ],
}
```

SON supports primitive types (strings, numbers, boolean), as well as nested arrays and objects. Simple Python objects are translated to JSON according to the following conversion:

| Python           | JSON   |
| ---------------- | ------ |
| dict             | object |
| list, tuple      | array  |
| str              | string |
| int, long, float | number |
| True             | true   |
| False            | false  |
| None             | null   |

#### Converting Python dictionaries to JSON format

We can convert Python dictionaries to JSON format using the `json.dumps()` function:

> This is called serialization or encoding.

```python
import json
data = {'name': 'John', 'age': 30, 'city': 'New York'}
personJSON = json.dumps(data, indent=4, sort_keys=True)
# the indent parameter is optional and makes the output more readable
# the sort_keys parameter is optional and sorts the keys alphabetically
# dumps stands for "dump string"

print(personJSON)  # Output: {"age": 30, "city": "New York", "name": "John"}

# We can also write the JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True)
```

#### Converting JSON data to Python dictionaries

If we have a JSON data and we want to convert it to a Python object (dictionary), we can use the `json.loads()` function:

> This is called deserialization or decoding.

```python
import json
personJSON = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(personJSON) # loads stands for "load string"
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# We can also read the JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

#### Encoding custom(!) objects to JSON (HINT: using the `default` parameter)

So far we've worked with a dictionary but let's say we have a custom object and we want to convert/encode it to JSON. We can do that by using the `default` parameter of the `json.dumps()` function:

```python
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 30)

# Version 1: We need to define a custom function to convert the object to a dictionary, because the default function does not know how to serialize the object
def encode_user(o): # o is the object
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')
userJSON = json.dumps(user, default=encode_user) # we pass the custom function to the default parameter
print(userJSON)  # Output: {"name": "John", "age": 30, "User": true}

# Version 2: We can also use a custom JSONEncoder class
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o): # we override the default method
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)

# or (we can use an Encoder directly)
# Version 3

userJSON = UserEncoder().encode(user)
print(userJSON)  # Output: {"name": "John", "age": 30, "User": true}

# or (we can also use a lambda function)
# Version 4
userJSON = json.dumps(user, default=lambda o: o.__dict__) # this will convert the object to a dictionary
print(userJSON)  # Output: {"name": "John", "age": 30}
```

#### Decoding custom(!) objects from JSON (HINT: using the `object_hook` parameter)

If we have a JSON data and we want to convert/decode it to a custom object, we can do that by using the `object_hook` parameter of the `json.loads()` function:

```python
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

userJSON = '{"name": "John", "age": 30}'
user = json.loads(userJSON)
print(user)  # Output: {'name': 'John', 'age': 30}

# Version 1: We need to define a custom function to convert the dictionary to an object, because the default function does not know how to deserialize the object
def decode_user(d): # d is the dictionary
    if User.__name__ in d:
        return User(name=d['name'], age=d['age']) # we create a new User object
    return d
user = json.loads(userJSON, object_hook=decode_user) # we pass the custom function to the object_hook parameter
print(user)  # Output: <__main__.User object at 0x7f8e3c6b3a90>

# Version 2: We can also use a custom JSONDecoder class
from json import JSONDecoder
class UserDecoder(JSONDecoder):
    def decode(self, o): # we override the decode method
        if User.__name__ in o:
            return User(name=o['name'], age=o['age'])
        return o

user = json.loads(userJSON, cls=UserDecoder)

# or (we can use a Decoder directly)
# Version 3
user = UserDecoder().decode(userJSON)
print(user)  # Output: <__main__.User object at 0x7f8e3c6b3a90>

# or (we can also use a lambda function)
# Version 4
user = json.loads(userJSON, object_hook=lambda d: User(**d)) # this will convert the dictionary to an object
print(user)  # Output: <__main__.User object at 0x7f8e3c6b3a90>
```

**Questions:**

> **1. How do you deserialize JSON data in Python?**
>
> Deserialization of JSON data in Python is done using the `json.loads()` function, which parses a JSON-formatted string into a Python object.

> **2. What is the difference between `json.dumps()` and `json.dump()`?**
>
> `json.dumps()` is used to serialize a Python object to a JSON-formatted string, while `json.dump()` is used to write the serialized object directly to a file-like object, such as a file or a socket.

> **3. Can JSON represent complex data structures like custom objects?**
>
> By default, JSON can represent basic data types like strings, numbers, lists, and dictionaries. To represent custom objects, you may need to implement custom serialization using the `default` parameter of `json.dumps()`.

## Random numbers

- **Explanation**: Generating pseudo-random numbers. Python comes with different modules to generate random numbers: random module for pseudo-random numbers, and secrets module for cryptographically strong random numbers and the numpy random module for generating random numbers from various probability distributions (e.g., uniform, normal, binomial, etc.) which generates arrays of random numbers.
- **Syntax**:
  ```python
  import random
  random_number = random.randint(1, 10) # generates a random integer in the inclusive range [1, 10]
  ```
- **Used**: Simulations, games, cryptographic applications.
- **Avoid**: When true randomness is crucial.

**Questions:**

> **1. What is the difference between `random.randint()` and `random.random()`?**
>
> `random.randint(a, b)` generates a random integer in the inclusive range [a, b], while `random.random()` generates a random float in the range [0.0, 1.0).

> **2. How can you generate a random float in a specific range?**
>
> You can use `random.uniform(a, b)` to generate a random float in the range [a, b).

> **3. Explain the purpose of the `random.seed()` function.**
>
> `random.seed()` initializes the random number generator with a given seed value. Using a seed ensures reproducibility, meaning the same sequence of random numbers will be generated if the seed is the same.

### Random module

The `random` module provides functions for generating random numbers. Here are some of the most commonly used functions:

- `random.random()`: Returns a random float in the range [0.0, 1.0).
- `random.uniform()`: Returns a random float in the range [a, b). The result may include `a` but will not include `b`.
- `random.randint(a, b)`: Returns a random integer in the inclusive range [a, b]. The result may include both `a` and `b`.
- `random.normalvariate(mu, sigma)`: Returns a random float from the normal distribution with mean `mu` and standard deviation `sigma`. Example: `random.normalvariate(0, 1)` returns a random float from the standard normal distribution.
- `random.choice(seq)`: Returns a random element from the non-empty sequence `seq`.
- `random.shuffle(seq)`: Shuffles the sequence `seq` in place.
- `random.sample(population, k)`: Returns a list of `k` unique elements from the population sequence.

```python
import random
random_float = random.random()  # generates a random float in the range [0.0, 1.0)

random_int = random.randint(1, 10)  # generates a random integer in the inclusive range [1, 10]

my_list = [1, 2, 3, 4, 5]
random_element_choice = random.choice(my_list)  # returns a random element from the list
random_sample = random.sample(my_list, 3)  # returns a list of 3 unique elements from the list
random_choices = random.choices(my_list, k=3)  # returns a list of 3 elements from the list with replacement. The elements may be repeated.

random.shuffle(my_list)  # shuffles the list in place

random_sample = random.sample(my_list, 3)  # returns a list of 3 unique elements from the list
```

These numbers generated with previous functions are pseudo-random numbers. They are not truly random, but they are generated in a way that is statistically indistinguishable from true randomness. They are reproducible if the same seed is used.

```python
import random

random.seed(1)  # setting the seed to 1
print(random.random())  # Output: 0.13436424411240122
print(random.random())  # Output: 0.8474337369372327
print(random.randint(1, 10))  # Output: 2

random.seed(1)  # setting the seed to 1 again
print(random.random())  # Output: 0.13436424411240122; the same number as before
print(random.random())  # Output: 0.8474337369372327; the same number as before
print(random.randint(1, 10))  # Output: 2; the same number as before
```

This is not recommended for cryptographic purposes, but it is useful for simulations and games.

### Secrets module

The `secrets` module provides functions for generating cryptographically strong random numbers. It is suitable for generating random numbers for security-sensitive applications, such as password generation, token generation, and cryptographic key generation. The `secrets` has only a few functions (three?), but they are designed to be cryptographically secure.
The dissadvantage of the `secrets` module is that it is slower than the `random` module.

```python
import secrets

random_int = secrets.randbelow(10)  # generates a random integer in the range [0, 10). The result may include 0 but will not include 10 (exclusive upper bound)
random_k_random_bits = secrets.randbits(16)  # generates a random integer with 16 random bits

random_choice = secrets.choice([1, 2, 3, 4, 5])  # returns a random element from the list

random_hex = secrets.token_hex(16)  # generates a random hexadecimal string of 16 bytes
random_url = secrets.token_urlsafe(16)  # generates a random URL-safe string of 16 bytes
```

### Numpy random module

The `numpy.random` module provides functions for generating random numbers from various probability distributions, such as uniform, normal, binomial, etc. It is part of the `numpy` library, which is widely used for numerical computing in Python.

```python
import numpy as np

random_float = np.random.random()  # generates a random float in the range [0.0, 1.0)

random_int = np.random.randint(1, 10)  # generates a random integer in the inclusive range [1, 10]

random_normal = np.random.normal(0, 1, 10)  # generates an array of 10 random floats from the standard normal distribution with mean 0 and standard deviation 1

# array of random floats
random_uniform = np.random.uniform(0, 1, 10)  # generates an array of 10 random floats in the range [0.0, 1.0)

random_uniform = np.random.rand(3) # generates an array of 3 random floats in the range [0.0, 1.0)
random_uniform = np.random.rand(3, 3)  # generates a 3x3 array of random floats in the range [0.0, 1.0)
random_uniform = np.random.randint(1, 10, 10)  # generates an array of 10 random integers in the inclusive range [1, 10)
random_uniform = np.random.randint(1, 10, (3, 4))  # generates a 3x4 array of random integers in the inclusive range [1, 10); we've used a tuple to specify the shape of the array

# shuffle
my_list = np.array([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15])
np.random.shuffle(my_list)  # shuffles the array in place; it shuffles the first axis of the array which means that it shuffles the rows
```

NOTE: Numpy random generator uses a different random number generator than the `random` module, so the results may be different.It also has a different seed function.

```python
import numpy as np

np.random.seed(1)  # setting the seed to 1
print(np.random.random())  # Output: 0.417022004702574
print(np.random.random())  # Output: 0.7203244934421581
print(np.random.randint(1, 10))  # Output: 6

np.random.seed(1)  # setting the seed to 1 again
print(np.random.random())  # Output: 0.417022004702574; the same number as before
print(np.random.random())  # Output: 0.7203244934421581; the same number as before
print(np.random.randint(1, 10))  # Output: 6; the same number as before
```

## Decorators

- **Explanation**: Modify or extend the behavior of functions or methods. Decorators are functions that take another function as an argument and return a new function, usually adding some kind of functionality. There are function decorators (more common) and class decorators.
- **Syntax**:

  ```python
  def my_decorator(func): # 'func' is the function to be decorated
      def wrapper():
          print("Something is happening before the function is called.")
          func() # calling the original function which, in this case, is say_hello()
          print("Something is happening after the function is called.")
      return wrapper

  @my_decorator
  def say_hello():
      print("Hello!")

  say_hello()  # Output: Something is happening before the function is called. Hello! Something is happening after the function is called.
  ```

- **Used**: Code reuse, adding functionality to functions or methods.
- **Avoid**: Overusing for simple tasks.

### Function decorators - working with arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs): # We can use as many arguments and keyword arguments as we want
        print("Something is happening before the function is called.")
        func(*args, **kwargs) # calling the original function with its arguments
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("John")  # Output: Something is happening before the function is called. Hello, John! Something is happening after the function is called.
```

TODO: Check the example where we use the `functools.wraps` decorator to preserve the original function's metadata (such as docstring and name).

#### Function decorators - alternative syntax

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

def say_hello(name):
    print(f"Hello, {name}!")

say_hello = my_decorator(say_hello)  # manually applying the decorator
say_hello("John")  # Output: Something is happening before the function is called. Hello, John! Something is happening after the function is called.
```

`say_hello` now refers to the result of applying the `my_decorator` to the original `say_hello` function, which is effectively the `wrapper` function returned by `my_decorator` wrapping around the original `say_hello` function.

### Function decorators - multiple decorators

```python
def my_decorator1(func):
    def wrapper1(*args, **kwargs):
        print("Decorator 1: Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Decorator 1: Something is happening after the function is called.")
    return wrapper1

def my_decorator2(func):
    def wrapper2(*args, **kwargs):
        print("Decorator 2: Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Decorator 2: Something is happening after the function is called.")
    return wrapper2

@my_decorator1 # 2) Applies my_decorator1 to the function returned by my_decorator2 (wrapper2), resulting in a new function wrapped by wrapper1
@my_decorator2 # 1) Applies my_decorator2 to the original say_hello function, resulting in a new function wrapped by wrapper2
def say_hello(name): # The original function
    print(f"Hello, {name}! I am {__name__}!")

say_hello("John")
# Output:
# Decorator 1: Something is happening before the function is called.
# Decorator 2: Something is happening before the function is called.
# Hello, John!
# Decorator 2: Something is happening after the function is called.
# Decorator 1: Something is happening after the function is called.
```

Order of decorators matters, as they are applied from the innermost to the outermost. In this case, `my_decorator2` is the inner decorator, and `my_decorator1` is the outer decorator.

NOTE: In `my_decorator1`, `func` refers to the `wrapper2` function returned by `my_decorator2` wrapping around the original `say_hello` function.

#### Function decorators - multiple decorators - alternative syntax

In Python, when you decorate a function using the `@decorator` syntax, it's essentially shorthand for reassigning the original function name to the wrapper function returned by the decorator.

So, when you write:

```python
@my_decorator1
@my_decorator2
def say_hello(name):
    print(f"Hello, {name}!")
```

It's equivalent to:

```python
say_hello = my_decorator1(my_decorator2(say_hello)) # manually applying the decorators; first my_decorator2 is applied, then my_decorator1
```

Therefore, `say_hello` (the part `say_hello = ...`) now refers to the result of applying both `my_decorator1` and `my_decorator2` to the original `say_hello` function, which is effectively the `wrapper1` function returned by `my_decorator1` wrapping around the `wrapper2` function returned by `my_decorator2`.

NOTE: In `my_decorator1`, `func` refers to the `wrapper2` function returned by `my_decorator2` wrapping around the original `say_hello` function.

### Class decorators

```python
class my_decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        self.func(*args, **kwargs)
        print("Something is happening after the function is called.")

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("John")  # Output: Something is happening before the function is called. Hello, John! Something is happening after the function is called.
```

**Questions:**

> **1. How does the `@decorator` syntax work in Python?**
>
> The `@decorator` syntax is a convenient way to apply a decorator to a function. It is equivalent to writing `function = decorator(function)`.

> **2. Can you chain multiple decorators on a single function?**
>
> Yes, you can chain multiple decorators on a single function by stacking them with the `@` syntax. The order of decorators matters, as they are applied from the innermost to the outermost.

> **3. What is the purpose of using `functools.wraps` with decorators?**
>
> `functools.wraps` is used to preserve the original function's metadata (such as docstring and name) when creating a decorator. It ensures that the decorated function maintains its identity and properties.

These answered questions aim to provide additional clarity and context to each concept.

## Generators

- **Explanation**: Specialized iterators that allow lazy, on-the-fly generation of values.
- **Syntax**:
  ```python
  def my_generator():
      for i in range(5):
          yield i
  ```
- **Used**: Efficiently handle large datasets, infinite sequences.
- **Avoid**: When all values need to be stored in memory at once.

**Questions:**

> **1. How is a generator different from a regular function?**
>
> Generators use the `yield` keyword to produce a series of values on-the-fly, allowing them to save and resume their state between iterations.

> **2. What is the advantage of using a generator over a list?**
>
> Generators use memory more efficiently as they produce values one at a time, making them suitable for large or infinite sequences.

> **3. Explain the role of the `yield` keyword in generators.**
>
> The `yield` keyword is used to produce a value from the generator and temporarily suspend its state until the next iteration.

NOTE: range() is a generator function that produces values on-the-fly, making it memory-efficient for large ranges. It does not store all values in memory at once (like a list does). The `yield` keyword in the `my_generator` function allows it to produce values lazily, one at a time.

NOTE: Every generator is an iterator (for example: range, map, filter, zip, enumerate, etc.) but not every iterator is a generator (for example: list, tuple, dict, set, file objects, etc. are iterators but not generators)

So:

```python
range() # does not store all values in memory at once;
list(range()) # stores all values in memory at once;
```

`yield` pauses the function and saves the state of the function, so it can be resumed later by calling the `next()` function on the generator object. When the function is resumed, it continues from where it left off.
If the function contains a `yield` statement, it becomes a generator function. When you call a generator function, it returns a generator object, which is an iterator.
The memory contains only one value at a time, so it is memory-efficient for large or infinite sequences.

```python
def my_generator():
    for i in range(5):
        yield i

gen = my_generator() # calling the generator function returns a generator object

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
```

## Threading vs Multiprocessing

- **Explanation**: Concurrent execution using threads or processes.
- **Syntax**:
  ```python
  import threading
  import multiprocessing
  ```
- **Used**: Improving performance for I/O-bound or CPU-bound tasks.
- **Avoid**: Global Interpreter Lock (GIL) can limit benefits in certain scenarios.

**Questions:**

> **1. What is the difference between threading and multiprocessing in Python?**
>
> Threading uses multiple threads within a single process, while multiprocessing uses multiple processes, each with its own interpreter and memory space.

> **2. When is threading preferred over multiprocessing?**
>
> Threading is preferred for I/O-bound tasks, where waiting for external resources like databases or network calls is a significant portion of the work.

> **3. How does the Global Interpreter Lock (GIL) impact multithreading?**
>
> The Global Interpreter Lock (GIL) in CPython prevents multiple native threads from executing Python bytecodes concurrently, limiting the effectiveness of multithreading for CPU-bound tasks.

## Multithreading

- **Explanation**: Concurrent execution using multiple threads within a single process.
- **Syntax**:
  ```python
  import threading
  ```
- **Used**: I/O-bound tasks, parallel execution of non-CPU-intensive operations.
- **Avoid**: CPU-bound tasks, due to the Global Interpreter Lock (GIL).

**Questions:**

> **1. How can you create and start a thread in Python?**
>
> You can create a thread by subclassing the `Thread` class or by passing a target function to the `Thread` constructor. Call the `start()` method to begin execution.

> **2. Explain the Global Interpreter Lock (GIL) and its impact on multithreading.**
>
> The Global Interpreter Lock (GIL) in CPython prevents multiple native threads from executing Python bytecodes concurrently, limiting the effectiveness of multithreading for CPU-bound tasks.

> **3. What is the purpose of the `threading.Lock` class?**
>
> The `threading.Lock` class is used to synchronize access to shared resources among multiple threads. It ensures that only one thread can acquire the lock at a time.

## Multiprocessing

- **Explanation**: Concurrent execution using multiple processes.
- **Syntax**:
  ```python
  import multiprocessing
  ```
- **Used**: CPU-bound tasks, parallel execution of CPU-intensive operations.
- **Avoid**: Excessive use for I/O-bound tasks, due to increased overhead.

**Questions:**

> **1. How can you create and start a process in Python?**
>
> You can create a process by subclassing the `Process` class or by passing a target function to the `Process` constructor. Call the `start()` method to begin execution.

> **2. Explain the difference between `multiprocessing.Process` and `threading.Thread`.**
>
> `multiprocessing.Process` creates a new process with its own memory space, while `threading.Thread` creates a new thread within the same process, sharing memory space.

> **3. What is inter-process communication (IPC) in multiprocessing?**
>
> Inter-process communication (IPC) is a mechanism for processes to communicate and share data. In multiprocessing, it's essential for coordinating tasks and exchanging information between processes.

## Function arguments

- **Explanation**: Values passed to a function during its invocation.
- **Syntax**:
  ```python
  def my_function(arg1, arg2="default", *args, **kwargs):
      # function body
  ```
- **Used**: Passing data to functions with flexibility.
- **Avoid**: Excessive use of mutable default arguments.

**Questions:**

> **1. Explain the difference between positional and keyword arguments.**
>
> Positional arguments are passed based on the order, while keyword arguments are identified by parameter names. Mixing both is allowed.

> **2. What is the purpose of the `*args` and `**kwargs` syntax in function definitions?\*\*
>
> `*args` allows a function to accept any number of positional arguments, and `**kwargs` allows it to accept any number of keyword arguments.

> **3. How can you specify default values for function arguments?**
>
> Default values for function arguments can be specified in the function definition, providing a fallback when the argument is not explicitly passed.

## The Asterisk (\*) operator

- **Explanation**: Performs various operations, such as unpacking.
- **Syntax**:
  ```python
  *my_list, last_item = [1, 2, 3, 4, 5]
  result = sum(*my_list)
  ```
- **Used**: Unpacking iterables, collecting multiple arguments in functions.
- **Avoid**: Overusing, which can lead to unclear code.

**Questions:**

> **1. How does the `*args` syntax differ from using a single asterisk in other contexts?**
>
> In function parameters, `*args` collects extra positional arguments, while in other contexts, a single asterisk unpacks iterables.

> **2. What is the purpose of the `*` operator in function calls?**
>
> The `*` operator in function calls unpacks an iterable into separate arguments, allowing functions to accept variable numbers of arguments.

> **3. How can you use the `*` operator for unpacking nested iterables?**
>
> The `*` operator can be nested to unpack elements from multiple nested iterables simultaneously.

## Shallow vs Deep Copying

- **Explanation**: Creating copies of objects with different levels of depth.
- **Syntax**:
  ```python
  import copy
  shallow_copy = copy.copy(original_list)
  deep_copy = copy.deepcopy(original_list)
  ```
- **Used**: Avoiding unintended modifications to shared mutable objects.
- **Avoid**: Deep copying large structures with circular references.

**Questions:**

> **1. What is the difference between shallow copy and deep copy?**
>
> A shallow copy creates a new object but does not recursively copy nested objects. A deep copy creates a new object and recursively copies all nested objects.

> **2. When should you use a shallow copy?**
>
> Shallow copy is suitable when the outer structure is sufficient, and modifying nested objects won't affect the original.

> **3. When should you use a deep copy?**
>
> Deep copy is necessary when you want a completely independent copy of an object, including all nested objects.

## Context managers

- **Explanation**: Objects managing resources using the `with` statement.
- **Syntax**:
  ```python
  with open("file.txt", "r") as file:
      content = file.read()
  ```
- **Used**: Managing resources like files, databases, or network connections.
- **Avoid**: Overusing for simple tasks that don't require resource management.

**Questions:**

> **1. What is the primary purpose of a context manager?**
>
> A context manager is used to acquire and release resources automatically, ensuring proper setup and cleanup.

> **2. How does a context manager work with the `with` statement?**
>
> The `with` statement simplifies resource management by ensuring that the context manager's `__enter__` and `__exit__` methods are properly invoked.

> **3. Can you create your own context manager in Python?**
>
> Yes, you can create a context manager by defining a class with `__enter__` and `__exit__` methods or by using the `contextlib` module's `contextmanager` decorator.
