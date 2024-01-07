# Python Testing Cheatsheet

    Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

    The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

    Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

    Integration tests will test interactions between every part of your code.

## `unittest` — Unit Testing Framework

### Basics

``` python
import unittest

class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
```

### Running Tests

- Run all tests in a file: `python -m unittest filename.py`
- Run a specific test in a file: `python -m unittest filename.TestClass.test_method`

## `unittest.mock` — Mock Object Library

### Basics

``` python
from unittest.mock import Mock

# Create a mock object
mock_obj = Mock()

# Set a return value for the mock
mock_obj.some_method.return_value = 42

# Use the mock
result = mock_obj.some_method()
```

### Mocking Read-Only Property

``` python
from unittest.mock import PropertyMock

class MyClass:
    @property
    def readonly_property(self):
        return 42

# Mock the readonly property
with patch('module.MyClass.readonly_property', new_callable=PropertyMock) as mock_property:
    mock_property.return_value = 24
    instance = MyClass()
    assert instance.readonly_property == 24
```

## `parameterized` — Parameterized Testing

### Install

``` python
pip install parameterized
```

### Example

``` python
import unittest
from parameterized import parameterized

class MyTest(unittest.TestCase):

    @parameterized.expand([
        ("case1", 1, 2, 3),
        ("case2", 2, 3, 5),
        ("case3", 5, 5, 10),
    ])
    def test_addition(self, name, a, b, expected_result):
        result = a + b
        self.assertEqual(result, expected_result)
```

## Memoization

### Using `functools.lru_cache`

``` python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

This cheatsheet provides a quick reference for using `unittest`, `unittest.mock`, `parameterized` for parameterized testing, and memoization with `functools.lru_cache`.