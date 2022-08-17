# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:35:13 2022

@author: RAVI TEJ
"""
text=input("Please enter a string:")

def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter, count)

most_frequent(text)
