#!/usr/bin/env python3
"""Generic_utilities_for_Github_org_client.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "acces_s_nested_map",
    "get__json",
    "memoi_e",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access_nested_map_with_key_path.
    Parameters
    ----------
    nested_map:_Mapping
        A_nested_map
    path:_Sequence
        a_sequence_of_key_representing_a_path_to_the_value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """Get_JSON_from_remote_URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """Decorator_to_memoize_a_method.
    Example
    -------
    class_MyClass:
        @memoize
        def_a_method_self):
            print_"a_method_called")
            return_42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized_wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
