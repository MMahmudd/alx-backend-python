#!/usr/bin/env python3
"""Has a function_with_annotated_parameters_and
return_values_with_appropriate_types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns_a_list of_tuples with_the_length_of_each_element"""
    return [(i, len(i)) for i in lst]
