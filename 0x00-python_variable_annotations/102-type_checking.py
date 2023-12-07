#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and apply necessary changes:
{'lst': typing.Tuple, 'factor': <class 'int'>, 'return': typing.List}
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Function zoom_array """
    zoomed_in: Tuple = tuple([item for i in range(factor) for item in lst])
    return list(zoomed_in)


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
