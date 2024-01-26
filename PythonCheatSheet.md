# Python Cheat Sheet

> With the help of my little friend (Copilot)

## Data Types and Data Structures

| Type      | Mutable | Ordered | Allows duplicates | Constructor  | Example                        | Collection of   | Note                                                             | Category       |
| --------- | ------- | ------- | ----------------- | ------------ | ------------------------------ | --------------- | ---------------------------------------------------------------- | -------------- |
| `int`     | No      |         |                   | `int()`      | `-5`                           |                 | Note: `int` is a whole number                                    | data type      |
| `float`   | No      |         |                   | `float()`    | `3.27`                         |                 | Note: `float` is a decimal number                                | data type      |
| `complex` | No      |         |                   | `complex()`  | `1 + 2j`                       |                 | Note: `complex` is a complex number                              | data type      |
| `bool`    | No      |         |                   | `bool()`     | `True`                         |                 | Note: `bool` is a boolean value; it's a subclass of `int`        | data type      |
| `str`     | No      | Yes     | Yes               | `''` or `""` | `'hello'`                      | characters      | Note: `str` is a sequence of characters                          | data type      |
| `list`    | Yes     | Yes     | Yes               | `[]`         | `[1, 'two', 3.0]`              | elements        | Note: lists are mutable sequences                                | data structure |
| `tuple`   | No      | Yes     | Yes               | `()`         | `(1, 'two', 3.0)`              | elements        | Note: tuples are immutable lists                                 | data structure |
| `set`     | Yes     | No      | No                | `{}`         | `{1, 2, 3}`                    | elements        | Note: set also uses `{}` but it does not contain key-value pairs | data structure |
| `dict`    | Yes     | No      | No                | `{}`         | `{'key1': 1.0, 'key2': False}` | key-value pairs | Note: dict also uses `{}` but it does not contain elements       | data structure |

## Collections like Counter, namedtuple, OrderedDict, defaultdict, deque (as well as UserDict and ChainMap)

| Collection    | Description                                                             | Example                                                                                    |
| ------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `Counter`     | A dict subclass for counting hashable objects.                          | `Counter('hello')`                                                                         |
| `namedtuple`  | Factory function for creating tuple subclasses with named fields.       | `Point = namedtuple('Point', ['x', 'y'])`<br>`p = Point(1, y=2)`<br>`p[0] + p[1]`          |
| `OrderedDict` | A dict subclass that remembers the order entries were added.            | `OrderedDict([('a', 1), ('b', 2), ('c', 3)])`<br>`OrderedDict({'a': 1, 'b': 2, 'c': 3})`   |
| `defaultdict` | A dict subclass that calls a factory function to supply missing values. | `defaultdict(int, {'a': 1, 'b': 2, 'c': 3})`<br>`defaultdict(lambda: 2, {'a': 1, 'b': 2})` |
| `deque`       | A list-like sequence optimized for data accesses near its endpoints.    | `deque('hello', maxlen=5)`                                                                 |
| `UserDict`    | A wrapper around dictionary objects for easier dict subclassing.        | `UserDict({'a': 1, 'b': 2, 'c': 3})`                                                       |
| `ChainMap`    | A class for creating a single view of multiple mappings.                | `ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})`                                             |

## Operators

| Operator                   | Description                                                                  | Example                                     |
| -------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------- |
| `len(s)`                   | Length of `s`                                                                | `len('hello')`                              |
| `s[i]`                     | `i`th item of `s`, origin 0                                                  | `'hello'[1]`                                |
| `s[i:j]`                   | Slice of `s` from `i` to `j`                                                 | `'hello'[1:4]`                              |
| `s[i:j:k]`                 | Slice of `s` from `i` to `j` with step `k`                                   | `'hello'[1::2]`                             |
| `x in s`                   | `True` if `x` is an item of `s`                                              | `'e' in 'hello'`                            |
| `x not in s`               | `True` if `x` is not an item of `s`                                          | `'e' not in 'hello'`                        |
| `s + t`                    | Concatenation of `s` and `t`                                                 | `'hello' + ' ' + 'world!'`                  |
| `s * n`                    | `n` copies of `s`                                                            | `'hello' * 3`                               |
| `s[i] = x`                 | Item `i` of `s` is replaced by `x`                                           | `s = 'hello'; s[1] = 'a'`                   |
| `s[i:j] = t`               | Slice of `s` from `i` to `j` is replaced by the contents of the iterable `t` | `s = 'hello'; s[1:3] = 'xyz'`               |
| `del s[i:j]`               | Same as `s[i:j] = []`                                                        | `s = 'hello'; del s[1:3]`                   |
| `s[i:j:k] = t`             | The elements of `s[i:j:k]` are replaced by those of `t`                      | `s = 'hello'; s[1:5:2] = 'xyz'`             |
| `del s[i:j:k]`             | Same as `s[i:j:k] = []`                                                      | `s = 'hello'; del s[1:5:2]`                 |
| `s.append(x)`              | Appends `x` to the end of the sequence (same as `s[len(s):len(s)] = [x]`)    | `s = [1, 2, 3]; s.append(4)`                |
| `s.clear()`                | Removes all items from `s` (same as `del s[:]`)                              | `s = [1, 2, 3]; s.clear()`                  |
| `s.copy()`                 | Creates a shallow copy of `s` (same as `s[:]`)                               | `s = [1, 2, 3]; t = s.copy()`               |
| `s.extend(t)`              | Appends the contents of `t` to `s` (same as `s[len(s):len(s)] = t`)          | `s = [1, 2, 3]; t = [4, 5, 6]; s.extend(t)` |
| `s *= n`                   | Updates `s` with its contents repeated `n` times                             | `s = [1, 2, 3]; s *= 2`                     |
| `s.insert(i, x)`           | Inserts `x` into `s` at the index given by `i` (same as `s[i:i] = [x]`)      | `s = [1, 2, 3]; s.insert(1, 4)`             |
| `s.pop([i])`               | Retrieves the item at `i` and also removes it from `s`                       | `s = [1, 2, 3]; s.pop(1)`                   |
| `s.remove(x)`              | Removes the first item from `s` where `s[i] == x`                            | `s = [1, 2, 3]; s.remove(2)`                |
| `s.reverse()`              | Reverses the items of `s` in place                                           | `s = [1, 2, 3]; s.reverse()`                |
| `s.sort([key], [reverse])` | Sorts the items of `s` in place                                              | `s = [1, 2, 3]; s.sort()`                   |

## Math Operations

| Operation               | Description                                                                      | Example                     |
| ----------------------- | -------------------------------------------------------------------------------- | --------------------------- |
| `x + y`                 | Sum of `x` and `y`                                                               | `3 + 2`                     |
| `x - y`                 | Difference of `x` and `y`                                                        | `3 - 2`                     |
| `x * y`                 | Product of `x` and `y`                                                           | `3 * 2`                     |
| `x / y`                 | Quotient of `x` and `y`                                                          | `3 / 2`                     |
| `x // y`                | Floored quotient of `x` and `y`                                                  | `3 // 2`                    |
| `x % y`                 | Remainder of `x / y`                                                             | `3 % 2`                     |
| `-x`                    | `x` negated                                                                      | `-3`                        |
| `+x`                    | `x` unchanged                                                                    | `+3`                        |
| `abs(x)`                | Absolute value or magnitude of `x`                                               | `abs(-3)`                   |
| `int(x)`                | `x` converted to integer                                                         | `int('3')`                  |
| `float(x)`              | `x` converted to float                                                           | `float(3)`                  |
| `complex(re, im)`       | A complex number with real part `re`, imaginary part `im`. `im` defaults to `0`. | `complex(3, 2)`             |
| `c.conjugate()`         | Conjugate of the complex number `c`                                              | `complex(3, 2).conjugate()` |
| `divmod(x, y)`          | The pair `((x-x%y)/y, x%y)`                                                      | `divmod(3, 2)`              |
| `pow(x, y)` or `x ** y` | `x` to the power of `y`                                                          | `pow(3, 2)` or `3 ** 2`     |
