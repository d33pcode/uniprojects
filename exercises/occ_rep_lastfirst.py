#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

1. occ(lst, v) returns a list that contains the indexes of the occurencies of v in the lst.
Examples:
lst = ['red','blue','red','gray','yellow','red']
occ(lst, 'red') returns [0,2,5]
occ(lst, 'green') ritorna []

2. rep(lst, k) returns a list (without repetitions) of all the values that recur at leas k times in lst.
Examples:
lst = [1,2,1,5,3,4,2,1,3,5,6] 

rep(lst, 2) returns [1,2,5,3]
rep(lst, 3) returns [1]
rep(lst, 4) returns []


3. lastfirst(lst) returns the first word that begins with a different char 
from the last char of the previous word in the input list (if it doesn't exist, returns None).
Examples:
lastfirst(['sole','elmo','orco','alba','asta']) ritorna 'alba'
lastfirst(['sky','you','use','ear','right']) ritorna None

'''

def occ(lst, v):
	flist = []
	n = 0
	for c in lst:
		if c == v:
			n = lst.index(c, n)
			flist.append(n)
			n +=1
	return flist
	
	
def rep(lst, k):
	final_list = []
	for element in lst:
		occurr = lst.count(element)
		if occurr >= k:
			if element not in final_list:
				final_list.append(element)
	return final_list
	

def lastfirst(lst):
	n = 0
	l = len(lst)
	for x in range(l-1):
		if lst[n][len(lst[n])-1] == lst[n+1][0]:
			n += 1
		elif lst[n][len(lst[n])-1] != lst[n+1][0]:
			return lst[n+1]
