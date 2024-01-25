# Python Cheat Sheet

## Data Types and Data Structures

| Type      | Mutable | Ordered | Constructor  | Example                        | Collection of   |
| --------- | ------- | ------- | ------------ | ------------------------------ | --------------- |
| `int`     | No      | N/A     | `int()`      | `-5`                           | N/A             |
| `float`   | No      | N/A     | `float()`    | `3.27`                         | N/A             |
| `complex` | No      | N/A     | `complex()`  | `1 + 2j`                       | N/A             |
| `bool`    | No      | N/A     | `bool()`     | `True`                         | N/A             |
| `str`     | No      | Yes     | `''` or `""` | `'hello'`                      | characters      |
| `list`    | Yes     | Yes     | `[]`         | `[1, 'two', 3.0]`              | elements        |
| `tuple`   | No      | Yes     | `()`         | `(1, 'two', 3.0)`              | elements        |
| `set`     | Yes     | No      | `{}`         | `{1, 2, 3}`                    | elements        |
| `dict`    | Yes     | No      | `{}`         | `{'key1': 1.0, 'key2': False}` | key-value pairs |

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
