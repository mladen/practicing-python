# Python Cheat Sheet

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
