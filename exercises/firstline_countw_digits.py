#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

1. firstline(t, s) returns the first line of the sting t that contains the string s; 
if s is not in t returns None.

t = u ' ' 'Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza. ' ' ' 
firstline(t, 'non')
returns
u'del doman non c’è certezza.'

2. countw(t, w) returns the number of occurrencies of the word w in the string t.

t = 'three witches watch three watches.'
countw(t, 'three')
returns 
2

3. digits(t) returns a list of numeric sequences contained in the string t.

t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
digits(t)
returns
['23', '06', '7867555', '345', '675665676', '34565']

'''

def firstline(t, s):
	lines = t.splitlines()
	for line in lines:
		if s in line:
			return line

def countw(t, w):
	for c in t:
		if c.isalpha() == False:
			t = t.replace(c, ' ')
	words = t.split()
	count = 0
	for word in words:
		if word == w:
			count += 1
	return count

def digits(t):
	for c in t:
		if not c.isdigit():				
				t = t.replace(c, ' ')
	tlist = t.split()
	return tlist

