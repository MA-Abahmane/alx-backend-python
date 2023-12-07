# Python Variable Annotations Cheatsheet

## Introduction

Variable annotations in Python provide a way to declare the type of a variable without assigning a value. This can enhance code readability and serve as documentation for developers.

```python
# Syntax: variable_name: annotation
```

## Basic Annotations

### Built-in Types

```python
# Integer
x: int = 10

# Float
y: float = 3.14

# String
name: str = "John"

# Boolean
is_active: bool = True
```

### Lists and Tuples

```python
# List of integers
numbers: list[int] = [1, 2, 3]

# Tuple of strings
coordinates: tuple[str, str] = ("latitude", "longitude")
```

### Custom Classes

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Using custom class in annotations
john: Person = Person("John", 25)
```

## Optional and Default Values

```python
from typing import Optional

# Optional type
optional_value: Optional[int] = None

# Default values
default_value: int = 42
```

## Multiple Annotations

```python
# Multiple annotations on one line
a: int; b: str; c: float

# Multiple annotations with values
x, y, z: int, str, float = 10, "hello", 3.14
```

## Type Aliases

```python
from typing import List

# Type alias for a list of integers
IntList = List[int]

# Using type alias in annotations
numbers_list: IntList = [1, 2, 3]
```

## Union Types

```python
from typing import Union

# Union type
result: Union[int, float] = 42

# Multiple possible types
mixed_types: Union[int, str, bool] = "hello"
```

## Any Type

```python
from typing import Any

# Any type
dynamic_value: Any = "any value here"
```

## Conclusion

Variable annotations in Python are a powerful tool for providing type hints and improving code clarity. They can be especially useful when working with type checkers like `mypy`.

For more detailed information on type hints and annotations, refer to the [Python Type Hints documentation](https://docs.python.org/3/library/typing.html).
