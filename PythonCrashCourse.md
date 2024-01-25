# Python Crash Course (with the help of ChatGPT)

- [Python Crash Course (with the help of ChatGPT)](#python-crash-course-with-the-help-of-chatgpt)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Sets](#sets)
  - [Strings](#strings)
  - [Collections](#collections)
  - [Itertools](#itertools)
  - [Lambda Functions](#lambda-functions)
  - [Exceptions and Errors](#exceptions-and-errors)
  - [Logging](#logging)
  - [JSON](#json)
  - [Random numbers](#random-numbers)
  - [Decorators](#decorators)
  - [Generators](#generators)
  - [Threading vs Multiprocessing](#threading-vs-multiprocessing)
  - [Multithreading](#multithreading)
  - [Multiprocessing](#multiprocessing)
  - [Function arguments](#function-arguments)
  - [The Asterisk (\*) operator](#the-asterisk--operator)
  - [Shallow vs Deep Copying](#shallow-vs-deep-copying)
  - [Context managers](#context-managers)

### Lists

- **Explanation**: Ordered, mutable collection of elements, allowing duplicates
- **Syntax**: `my_list = [1, 2, 3]`, `my_list = list([1, 2, 3])`, `my_list = list()`, `my_list = []`
- **Used**: When you need an ordered collection of items that can be modified.
- **Avoid**: When you need a constant collection or fast lookups.

The classic way of creating a list:

```python
my_list = [1, 2, 3] # Create a list
print(my_list)  # Output: [1, 2, 3]
```

Using list():

```python
my_list = list()
print(my_list)  # Output: []

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

Creating a new list with the same elements multiple times:

```python
my_list = [0] * 5
print(my_list)  # Output: [0, 0, 0, 0, 0]
```

Creating a list using the range function:

```python
my_list = list(range(10))
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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

---

### Tuples

- **Explanation**: Ordered, immutable (cannot be modified after creation) collection of elements. Also, it allows duplicates.
- **Syntax**: `my_tuple = (1, 2, "Max")`, `my_tuple = 1, 2, "Max"`, `my_tuple = tuple([1, 2, "Max"])`, `my_tuple = tuple()`, `my_tuple = ()`
- **Used**: When you need an ordered collection that shouldn't be modified. Also, it's used for objects that belong together.
- **Avoid**: When you need to modify elements frequently.

Creating a tuple:

```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
```

Creating a tuple with one element:

```python
my_tuple = (1,)  # Note the comma
print(type(my_tuple))  # Output: <class 'tuple'>
```

Creating a tuple without parentheses:

```python
my_tuple = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)
```

Creating a tuple from a list:

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)
```

Creating a tuple using the `range()` function:

```python
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

---

### Dictionaries

- **Explanation**: Unordered collection of key-value pairs. Allows duplicates. Keys must be unique but values can be duplicated. Mutable.
- **Syntax**: `my_dict = {'key': 'value', 'name': 'Max'}`
- **Used**: For quick lookups based on keys.
- **Avoid**: When order matters, or you need constant time for all operations.

Creating a dictionary:

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])  # Output: John; notice that we use square brackets for dictionaries!
```

Creating a dictionary using the `dict()` constructor:

```python
my_dict = dict(name='John', age=30) # Note: no quotes for the keys (only for the values)
print(my_dict['name'])  # Output: John
```

Iterating over a dictionary:

```python
my_dict = {'name': 'John', 'age': 30}
for key in my_dict:
    print(key, my_dict[key])  # Output: name John \n age 30

# or

for key, value in my_dict.items():
    print(key, value)  # Output: name John \n age 30

# or

for value in my_dict.values():
    print(value)  # Output: John \n 30

# or

for key in my_dict.keys():
    print(key)  # Output: name \n age
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

Deleting a key-value pair:

```python
my_dict = {'name': 'John', 'age': 30}
del my_dict['name']
print(my_dict)  # Output: {'age': 30}
```

Deleting all elements:

```python
my_dict = {'name': 'John', 'age': 30}
my_dict.clear()
print(my_dict)  # Output: {}
```

Deleting the last inserted key-value pair:

```python
my_dict = {'name': 'John', 'age': 30}
my_dict.popitem()
print(my_dict)  # Output: {'name': 'John'}
```

Getting the number of elements:

```python
my_dict = {'name': 'John', 'age': 30}
print(len(my_dict))  # Output: 2
```

Getting a list of keys:

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
```

Getting a list of values:

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.values())  # Output: dict_values(['John', 30])
```

Getting a list of key-value pairs:

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30)])
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
print(dict3)  # Output: {'name': 'John', 'age': 30, 'location': 'London'}
```

Updating a dictionary:

```python
my_dict = {'name': 'John', 'age': 30}
my_dict['name'] = 'Max'
print(my_dict)  # Output: {'name': 'Max', 'age': 30}

# or

my_dict = {'name': 'John', 'age': 30}
my_dict.update({'name': 'Max', 'age': 30})
# my_dict.update(name='Max', age=30)  # same as above
print(my_dict)  # Output: {'name': 'Max', 'age': 30}
```

Unpacking a dictionary:

```python
my_dict = {'name': 'John', 'age': 30}
name, age = my_dict.items()
print(name)  # Output: ('name', 'John')
print(age)  # Output: ('age', 30)
```

Key types in dictionaries:

> - Keys must be immutable (strings, numbers, or tuples with immutable elements).
> - Lists cannot be used as keys because they are mutable.

```python
my_dict = {3: 9, 6: 36, 9: 81} # int as a key
print(my_dict[3])  # Output: 9

# or

my_dict = {(1, 2, 3): 6, (4, 5): 9} # tuple as a key
print(my_dict[(4, 5)])  # Output: 9
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

---

### Sets

- **Explanation**: Unordered collection of unique elements.
- **Syntax**: `my_set = {1, 2, 3}`
- **Used**: When uniqueness matters, and order doesn't.
- **Avoid**: When you need order or key-value pairs.

```python
my_set = {1, 2, 3, 1}
print(my_set)  # Output: {1, 2, 3}
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

---

### Strings

- **Explanation**: Ordered collection of characters.
- **Syntax**: `my_string = "Hello"`
- **Used**: For representing and manipulating text.
- **Avoid**: When dealing with highly dynamic or binary data.

```python
my_string = "Hello"
print(my_string[1])  # Output: e
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

---

### Collections

- **Explanation**: Module providing specialized container datatypes.
- **Syntax**: `from collections import Counter, defaultdict`
- **Used**: When you need advanced data structures like counters or default dictionaries.
- **Avoid**: For basic lists or dictionaries.

```python
from collections import Counter
my_list = [1, 2, 3, 1, 2, 1]
counter = Counter(my_list)
print(counter)  # Output: Counter({1: 3, 2: 2, 3: 1})
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

---

### Itertools

- **Explanation**: Module providing fast, memory-efficient tools.
- **Syntax**: `from itertools import combinations`
- **Used**: When dealing with iterators and combinatorial functions.
- **Avoid**: For simple iteration over lists or ranges.

```python
from itertools import combinations
my_list = [1, 2, 3]
comb = combinations(my_list, 2)
print(list(comb))  # Output: [(1, 2), (1, 3), (2, 3)]
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

---

### Lambda Functions

- **Explanation**: Anonymous, one-liner functions.
- **Syntax**: `lambda x: x * 2`
- **Used**: When a small function is needed for a short period.
- **Avoid**: For complex logic or functions that require multiple lines.

```python
multiply_by_two = lambda x: x * 2
print(multiply_by_two(3))  # Output: 6
```

This cheat sheet provides concise information about each concept, along with examples for better understanding.

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

Certainly! Here's a Python cheat sheet for the mentioned concepts:

### Exceptions and Errors

- **Explanation**: Events that occur during program execution that disrupt normal flow.
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
- **Used**: Handling unexpected situations to prevent program termination.
- **Avoid**: Using exceptions for control flow.

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

### Logging

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

### JSON

- **Explanation**: Data interchange format based on JavaScript object syntax.
- **Syntax**:
  ```python
  import json
  data = {'key': 'value'}
  json_string = json.dumps(data)
  ```
- **Used**: Sending and receiving data between systems.
- **Avoid**: Storing sensitive or large binary data.

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

### Random numbers

- **Explanation**: Generating pseudo-random numbers.
- **Syntax**:
  ```python
  import random
  random_number = random.randint(1, 10)
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

### Decorators

- **Explanation**: Modify or extend the behavior of functions or methods.
- **Syntax**:

  ```python
  def my_decorator(func):
      def wrapper():
          print("Something is happening before the function is called.")
          func()
          print("Something is happening after the function is called.")
      return wrapper

  @my_decorator
  def say_hello():
      print("Hello!")
  ```

- **Used**: Code reuse, adding functionality to functions or methods.
- **Avoid**: Overusing for simple tasks.

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

### Generators

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

### Threading vs Multiprocessing

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

### Multithreading

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

### Multiprocessing

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

### Function arguments

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

### The Asterisk (\*) operator

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

### Shallow vs Deep Copying

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

### Context managers

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