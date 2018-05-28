#!/usr/bin/python
# -*- coding:utf8 -*-


def factorial(n):
    assert n >= 0, "Factorial not definied for negative values."

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial(0))
