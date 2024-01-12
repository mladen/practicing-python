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

- **Explanation**: Ordered, mutable collection of elements.
- **Syntax**: `my_list = [1, 2, 3]`
- **Used**: When you need an ordered collection of items that can be modified.
- **Avoid**: When you need a constant collection or fast lookups.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
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

- **Explanation**: Ordered, immutable collection of elements.
- **Syntax**: `my_tuple = (1, 2, 3)`
- **Used**: When you need an ordered collection that shouldn't be modified.
- **Avoid**: When you need to modify elements frequently.

```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
```

**Questions:**

> 1. **Can you modify a tuple after it has been created?**
>
> - No, tuples are immutable, so their elements cannot be modified after creation.

> 2. **How can you concatenate two tuples?**
>
> - You can use the `+` operator: `tuple1 + tuple2`.

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
