# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 05:59:03 2022

@author: aarid
"""

import argparse

import anpatools
import scrapeParseClean




#Add command line argument
parser = argparse.ArgumentParser(description='Process web url.')
parser.add_argument('--url', type=str, required=True,\
                    help='Web address to the page to analyze.')


#Assign command line arguments
args = parser.parse_args()
URL = args.url

# # #TEST
# URL = "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html"

#Function calls
web_content = scrapeParseClean.access_webpage(URL)
parsed_list = scrapeParseClean.parse_page(web_content)
data_strings = scrapeParseClean.clean_data(parsed_list)
data_words = scrapeParseClean.split_sentence(data_strings)


anagrams = anpatools.Anagram()
anagram_groups = anagrams.find_anagrams(data_words)
print(anagram_groups)


palindromes = [anpatools.Palyndrome(n) for n in data_words]
for palyndrome in palindromes:
    pal = palyndrome.find_palindromes()
    if pal is not None:
        print(pal)

# #Test
# URL = "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html"
# web_content = access_webpage(URL)
# print(web_content)
# parsed_list = parse_page(web_content)
# print(parsed_list)
# data_strings = clean_data(parsed_list)
# print(data_strings)
# data_words = split_sentence(data_strings)
# print(data_words)