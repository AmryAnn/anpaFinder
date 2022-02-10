# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 05:48:02 2022

@author: aarid
"""

import itertools
from html.parser import HTMLParser

class StringObject:
    '''Various functions for stored strings'''
    def __init__(self, string=None, sub_string=None, load_file=None, save_file=None):
        self.string = string
        self.sub_string = sub_string
        self.load_file = load_file
        self.save_file = save_file

    def __repr__(self):
        '''Return a string representation of string object'''
        return self.string

    def append(self, sub_string):
        '''Appends a sub_string to string,
        and returns the appended string.'''
        self.string = str(self.string) + sub_string
        return self.string

    def remove(self, sub_string):
        ''' Removes a sub_string from string, and returns
        the truncated string.'''
        self.string = self.string.replace(sub_string, '')
        return self.string

    def mirror_string(self):
        '''Returns the mirrored string of string.'''
        mirror = self.string[::-1]
        return mirror

    def load_string(self, load_file):
        '''Loads a string from load_file and returns that string.'''
        with open(load_file) as self.string:
            self.string = self.string.read()
        return self.string

    def save_string(self, save_file):
        '''Saves the string to save_file.'''
        with open(save_file, 'w') as saved:
            saved.write(self.string)


class Anagram(StringObject):
    '''Inherits from StringObject class and can get anagrams of string.'''
    def __init__(self, string):
        StringObject.__init__(self)
        self.string = string

    def get_anagrams(self):
        '''Takes string and returns a list of string's anagrams.'''
        anagrams = [''.join(perm) for perm in itertools.permutations(self.string)]
        return anagrams


class Palyndrome(StringObject):
    '''Inherits from StringObject and can identify palindromes.'''
    def __init__(self, string):
        StringObject.__init__(self)
        self.string = string

    def find_palindromes(self):
        '''Checks if mirrored string is equal to string.
        If true, returns the mirrored string.'''
        mirror = StringObject.mirror_string(self)
        if mirror == str(self.string):
            palindrome = mirror
        return palindrome


class ParserHTML(HTMLParser):
    """Inherits from HTMLParser in python standard library.
    Parses text from inside <p> tags, adds text to a list, returns the list"""
    data_list = []
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_data = False
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.is_data = True
    def handle_endtag(self, tag):
        if tag == 'p':
            self.is_data = False
    def handle_data(self, data):
        if self.is_data:
            self.data_list.append(data)
        return self.data_list
