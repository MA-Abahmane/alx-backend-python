#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations
to the function
Hint: look into TypeVar
"""

from typing import Mapping, Any, Union, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None)\
 -> Union[Any, T]:
    """ Function safely_get_value  """
    if key in dct:
        return dct[key]
    else:
        return default
