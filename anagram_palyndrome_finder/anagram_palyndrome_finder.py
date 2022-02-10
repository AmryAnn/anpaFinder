# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 05:59:03 2022

@author: aarid
"""

import urllib.request
import argparse

import anpatools

def access_webpage(url):
    """
    Opens and reads a webpage from URL and returns raw HTML from webpage.
    """
    webpage = urllib.request.urlopen(url)
    content = webpage.read().decode()
    return content

def parse_page(content):
    """
    Takes raw html as input and parses text from <p> tags.
    Returns a list of parsed text
    """
    pars = anpatools.ParserHTML()
    pars.feed(str(content))
    parsed_data = pars.data_list
    return parsed_data

def clean_data(data_list):
    """
    Takes a list of strings and splits multi-word strings into single word
    elements. 
    Appends the split elements having more than 2 letters to a new list
    unless the element is already in the list.
    Returns the new list.
    """
    string_list = []
    for items in data_list:
        words = items.split(' ')
        for word in words:
            if (len(word) > 2) and (word not in string_list):
                string_list.append(word)
                if word.startswith('['):
                    string_list.remove(word)
    return string_list


#Add command line argument
parser = argparse.ArgumentParser(description='Process web url.')
parser.add_argument('--url', type=str, required=True,\
                    help='Web address to the page to analyze.')


#Assign command line arguments
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
