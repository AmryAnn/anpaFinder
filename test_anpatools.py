# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:45:33 2022

@author: aarid

Tests for anpatools
"""

import unittest
import os

from anagram_palyndrom_finder import anpatools

class StringObjectTests(unittest.TestCase):
    def setUp(self):
        self.string_a = anpatools.StringObject('listen')
        self.substring = self.string_a.substring(' silent')

    def test_append(self):
        appended_string = self.string_a.append()
        self.assertEqual(appended_string, 'listen silent')

    def test_remove(self):
        truncated_string = self.string_a.remove()
        self.assertEqual(truncated_string, 'listen')

    def test_mirror_string(self):
        mirror = self.string_a.mirror_string()
        self.assertEqual(mirror, 'netsil')

    def test_load_string(self):
        loaded_string = self.string_a.load_string('test_loadfile.txt')
        self.assertEqual(loaded_string, 'data loaded')

    def test_save_string(self):
        expected = self.string_a.string
        save_file = 'test_savefile.txt'
        try:
            self.string_a.save_string(save_file)
            with open(save_file, 'rU') as s:
                text = s.read()
        finally:
            os.remove(save_file)
        self.assertEqual(expected, text)


unittest.main()
