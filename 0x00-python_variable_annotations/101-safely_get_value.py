#!/usr/bin/env python3
"""Has_method that_safely gets_value_from_dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely_gets_value from_dictionary.
    Args:
        dct (dict): Dictionary_to_get value_from.
        key (str): Key_to get_value_from.
        default_Default_value to_return if_key is_not_found.
    Returns:
        Value_from_dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
