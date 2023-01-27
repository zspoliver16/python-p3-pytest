#!/usr/bin/env python3

from string_functions import return_string, interpolate_string

class TestString:
    '''string_functions.py'''
    
    def test_return_string(self):
        '''contains a function "return_string()" that returns a variable of type str.'''
        assert type(return_string()) == str

    def test_interpolate_string(self):
        '''contains a function "interpolate_string()" that takes a string and inserts it into another string.'''
        assert interpolate_string('Guido') == 'Hello, Guido!'