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

### Lists

- **Explanation**: Ordered, mutable collection of elements.
- **Syntax**: `my_list = [1, 2, 3]`
- **Used**: When you need an ordered collection of items that can be modified.
- **Avoid**: When you need a constant collection or fast lookups.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

> ### Important questions and answers
>
> 1. **How to remove elements from a list?**
>
> - You can use methods like `remove(value)`, `pop(index)`, or `del list[index]` to remove elements.
>
> 2.  **What is the difference between `append()` and `extend()` methods?**
>
> - `append()` adds an element at the end of the list, while `extend()` takes an iterable and adds its elements to the list.
>
> 3. **Explain list comprehensions and provide an example.**
>
> - List comprehensions provide a concise way to create lists. Example: `[x**2 for x in range(5)]`.

---

### Tuples

- **Explanation**: Ordered, immutable collection of elements.
- **Syntax**: `my_tuple = (1, 2, 3)`
- **Used**: When you need an ordered collection that shouldn't be modified.
- **Avoid**: When you need to modify elements frequently.

```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
```

> ### Important questions and answers
>
> 1. **Can you modify a tuple after it has been created?**
>
> - No, tuples are immutable, so their elements cannot be modified after creation.
>
> 2. **How can you concatenate two tuples?**
>
> - You can use the `+` operator: `tuple1 + tuple2`.
>
> 3. **What is the purpose of using tuples as keys in a dictionary?**
>
> - Tuples, being immutable, can be used as keys in dictionaries when you need a composite key.

---

### Dictionaries

- **Explanation**: Unordered collection of key-value pairs.
- **Syntax**: `my_dict = {'key': 'value'}`
- **Used**: For quick lookups based on keys.
- **Avoid**: When order matters, or you need constant time for all operations.

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])  # Output: John
```

> ### Important questions and answers
>
> 1. **How do you check if a key exists in a dictionary?**
>
> - You can use the `in` keyword: `if key in my_dict:`.
>
> 2. **Explain the difference between `dict.items()`, `dict.keys()`, and `dict.values()`.**
>
> - `items()` returns key-value pairs, `keys()` returns keys, and `values()` returns values.
>
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

> ### Important questions and answers
>
> 1. **What operations can you perform on sets (union, intersection, difference)?**
>
> - Union: `set1 | set2`, Intersection: `set1 & set2`, Difference: `set1 - set2`.
>
> 2. **How can you check if a set is a subset or superset of another set?**
>
> - Subset: `set1.issubset(set2)`, Superset: `set1.issuperset(set2)`.
>
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

> ### Important questions and answers
>
> 1. **How do you concatenate strings in Python?**
>
> - You can use the `+` operator or the `join()` method: `' '.join(['Hello', 'World'])`.
>
> 2. **Explain the difference between `str()` and `repr()` functions.**
>
> - `str()` is used for creating output for end-user, `repr()` is used for development and debugging.
>
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

> ### Important questions and answers
>
> 1. **When would you use `namedtuple` from the `collections` module?**
>
> - `namedtuple` is used when you want to create a simple class for storing data without methods.
>
> 2. **Explain the purpose of the `deque` data structure.**
>
> - `deque` is a double-ended queue, suitable for efficiently adding and removing elements from both ends.
>
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

> ### Important questions and answers
>
> 1. **What is the purpose of the `cycle` function in itertools?**
>
> - `cycle` infinitely iterates over elements of an iterable.
>
> 2. **Explain the difference between `zip()` and `zip_longest()` functions.**
>
> - `zip()` stops when the shortest iterable is exhausted, `zip_longest()` continues until the longest is exhausted, filling with a specified value for missing elements.
>
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

> ### Important questions and answers
>
> 1. **What are the advantages of using lambda functions over regular functions?**
>
> - Lambdas are concise and can be used for short-lived, simple functions without defining a full function.
>
> 2. **How can you use lambda functions in conjunction with functions like `map()` and `filter()`?**
>
> - `map(lambda x: x * 2, my_list)` doubles each element in `my_list`.
>
> 3. **Are there any limitations or scenarios where lambda functions are not suitable?**
>
> - Lambdas are limited to a single expression, making them unsuitable for complex logic or functions with multiple statements. Use regular functions in such cases.
