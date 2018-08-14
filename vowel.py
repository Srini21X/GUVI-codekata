# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:54:45 2018

@author: HP
"""
N=10
word=input()
'''w=word.lower()
f=w[0]'''
if len(word)>0 and word.isalpha():
    if word in ('a','e','i','o','u'):
        print('Vowel')
    elif word.isalpha():
        print('Consonant')
    else:
        print('invalid')

    