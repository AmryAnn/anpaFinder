# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 05:59:03 2022

@author: aarid
"""

import urllib.request
import argparse

import anpatools

def access_webpage(url):
    '''Opens URL and reads webpage'''
    webpage = urllib.request.urlopen(url)
    content = webpage.read().decode()
    return content

def parse_page(content):
    """
    Parameters
    ----------
    content : str
        Raw HTML text.

    Returns
    -------
    parsed_data : list
        A list of strings parsed from <p> tags in raw HTML text.
    """
    pars = anpatools.ParserHTML()
    pars.feed(str(content))
    parsed_data = pars.data_list
    return parsed_data

def clean_data(data_list):
    """
    Parameters
    ----------
    data_list : list
        A list of strings, each element may have one or more words.

    Returns
    -------
    string_list : list
        A new list of strings, each element being a single word.
    """
    string_list = []
    for items in data_list:
        words = items.split(' ')
        for word in words:
            string_list.append(word)
    return string_list


#Add command line argument
parser = argparse.ArgumentParser(description='Process web url.')
parser.add_argument('--url', type=str, required=True,\
                    help='Web address to the page to analyze.')

#Assign command line arguments'
args = parser.parse_args()
URL = args.url

#Function calls
web_content = access_webpage(URL)
parsed_list = parse_page(web_content)
data_strings = clean_data(parsed_list)

anagrams = [anpatools.Anagram(n) for n in data_strings]
for anagram in anagrams:
    print(anagram.get_anagrams())

palindromes = [anpatools.Palyndrome(n) for n in data_strings]
for palindrome in palindromes:
    pal = palindrome.find_palindromes()
    if pal is not None:
        print(pal)
