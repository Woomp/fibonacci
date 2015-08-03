#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `fibonacci` module.
"""

import pytest
from fibonacci import fibonacci

TEST_DATA = (
    pytest.mark.xfail(raises=ValueError)((-1, 0)),
    pytest.mark.xfail(raises=ValueError)((1.4, 2)),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (8, 21),
    (24, 46368),
    (49, 7778742049),
    (64, 10610209857723),
    (128, 251728825683549488150424261),
    (256, 141693817714056513234709965875411919657707794958199867),
)


@pytest.mark.parametrize("number, result", TEST_DATA)
def test_fibonacci_calculation_positive(number, result):
    """Compare each expected result with a calculated one."""
    assert fibonacci.fibonacci(number) == result