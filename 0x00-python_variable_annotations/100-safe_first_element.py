#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations:
{'lst': typing.Sequence[typing.Any],
'return': typing.Union[typing.Any, NoneType]}
"""

from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Function safe_first_element  """
    if lst:
        return lst[0]
    else:
        return None
