#!/usr/bin/env python3

from bool_functions import return_true

class TestString:
    '''string_functions.py'''
    
    def test_return_true(self):
        '''contains a function "return_true" that returns True.'''
        assert return_true() == True
