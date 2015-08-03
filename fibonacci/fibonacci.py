# -*- coding: utf-8 -*-

from math import sqrt


def fibonacci(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

