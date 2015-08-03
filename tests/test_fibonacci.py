#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fibonacci
----------------------------------

Tests for `fibonacci` module.
"""

import pytest
from fibonacci import fibonacci

POSITIVE_TEST_DATA = (
    (1, 1),
    (2, 1),
    (3, 2),
    (8, 21),
    (24, 46368),
    (49, 7778742049),
    (64, 10610209857723),
)

NEGATIVE_TEST_DATA = (
    (128, ),
    (256, ),
    (512, )

)


@pytest.mark.parametrize("number, result", POSITIVE_TEST_DATA)
def test_fibonacci_calculation(number, result):
    assert fibonacci.fibonacci(number) == result
