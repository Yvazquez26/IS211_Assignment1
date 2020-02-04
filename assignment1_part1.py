#!/usr/bin/env python
# coding: utf-8

## This is assignment 1 part 1 that includes fuctions and exceptions.

def listDivide(numbers, divide=2):
    """Divides elements in a list by an integer. Returns the quantity
    of elements that is divisible by that integer.
    
    Args:
        numbers (list): list of integers.
        divide (int): default value of 2 to divide numbers by.
    
    Returns:
        int: The number of elements divisible by the divisor.
   
    Examples:
        >>> listDivide([2,6,8)
            3
        >>> listDivide([1,2,3,5,8,15], 1)
            6
    """
    divcount = 0
    for item in numbers:
        if item % divide is 0:
            divcount += 1
    return divcount


class ListDivideException(Exception):
    """Incorrect calculation class."""
    pass


def testListDivide():
    """A function to test ListDivide and what it performs.
    
    Args:
        numbers (list): list of integers
        
    Returns: 
        int: The number of elements divisible by the divisor.
        
    Examples:
        >>> listDivide([1,2,3,4,5])
            2
        >>> listDivide([2,4,6,8,10])
            5
        >>> listDivide([30, 54, 63,98, 100], divide=10)
            2
        >>> listDivide([])
            0
        >>> listDivide([1,2,3,4,5], 1)
            5
    """
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException
    elif listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException
    elif listDivide([30, 54, 63, 98, 100], 10) != 2:
        raise ListDivideException
    elif listDivide([]) != 0:
        raise ListDivideException
    elif listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException

print listDivide([2,4,6])
print listDivide([1,2,3,5,8,15], 1)

print listDivide([1,2,3,4,5])
print listDivide([2,4,6,8,10])
print listDivide([30, 54, 63,98, 100], divide=10)
print listDivide([])
print listDivide([1,2,3,4,5], 1)




