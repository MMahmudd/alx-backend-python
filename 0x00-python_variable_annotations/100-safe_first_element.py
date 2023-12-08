#!/usr/bin/env python3
""" Has_Augmented code_with the_correct_duck-typed_annotations."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the_irst_element_of_a_list_or_None if_the list_is_empty."""
    if lst:
        return lst[0]
    else:
        return None
