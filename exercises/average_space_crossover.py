#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Write an average(vals) function that takes in input a list of (numeric only) values and returns the average. 
2. Write a space(s, k) function that takes in input a string s and an integer k and returns a new string that
contains the chars in s, separated by k spaces (i.e. space('hello everyone', 1) returns 'h e l l o  e v e r y o n e').
3. Write a crossing_over(m, f) function that takes in input two lists with the same length 
and returns the crossover of the two lists as in the example:
crossing_over([1, 3, 5], [2, 4, 6]) --> [1, 2, 3, 4, 5, 6]

'''

def average(vals):
	num = 0
	div = len(vals)
	for val in vals:
		num += val
	avg = num/div 
	return avg

print average([2,3,6,1,5])

def space(s, k):
	letters_list = []
	fstring = ''
	for c in s:
		letters_list.append(c)
	for c in letters_list:
		fstring += c
		fstring += " " * k
	return fstring

print space('hi all', 3)

def crossing_over(m, f):
	for element in f:
		m.append(element)
	m.sort()
	return m

print crossing_over([1, 3, 5], [2, 4, 6])
