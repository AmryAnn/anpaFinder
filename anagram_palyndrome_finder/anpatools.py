# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 05:48:02 2022

@author: aarid
"""

import itertools
from html.parser import HTMLParser

class StringProcessing:
    ''' Stores and processes a string '''

    def __init__(self, string=None, sub_string=None, load_file=None, save_file=None):
        self.string = string
        self.sub_string = sub_string
        self.load_file = load_file
        self.save_file = save_file

    def __repr__(self):
        return self.string

    def append(self, sub_string):
        ''' Appends a sub string to the class object,
        and returns the appended string'''
        self.string = str(self.string) + sub_string
        return self.string

    def remove(self, sub_string):
        ''' Removes a substring from the class object, and returns
        the truncated string'''
        self.string = self.string.replace(sub_string, '')
        return self.string

    def mirror_string(self):
        ''' Returns the mirrored string'''
        mirror = self.string[::-1]
        return mirror

    def load_string(self, load_file):
        ''' Loads a string from a file and returns that string'''
        with open(load_file) as self.string:
            self.string = self.string.read()
        return self.string

    def save_string(self, save_file):
        ''' Saves the string to a file'''
        with open(save_file, 'w') as saved:
            saved.write(self.string)


class Anagram(StringProcessing):
    '''A child class of StringProcessing for finding anagrams'''

    def __init__(self, string):
        StringProcessing.__init__(self)
        self.string = string

    def get_anagrams(self):
        '''Takes a string and returns the string's anagrams'''
        anagrams = [''.join(perm) for perm in itertools.permutations(self.string)]
        return anagrams


class Palyndrome(StringProcessing):
    '''A child class of StringProcessing for identifying palindromes'''

    def __init__(self, string):
        StringProcessing.__init__(self)
        self.string = string

    def find_palindromes(self):
        '''Checks if mirrored string is equal to string'''
        mirror = StringProcessing.mirror_string(self)
        if mirror == str(self.string):
            return mirror


class ParserHTML(HTMLParser):
    data_list = []
    def __init__(self):
        HTMLParser.__init__(self)
        self.IsData = False
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.IsData = True
    def handle_endtag(self, tag):
        if tag == 'p':
            self.IsData = False
    def handle_data(self, data):
        if self.IsData:
            self.data_list.append(data)
        #print(self.data_list)
        return self.data_list
