#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Write a 'discount' function that takes an import and a discount percentage in input, and returns
the discount import (i.e. import = 1000, discount = 20, return = 800).

2. Write a 'seconds' function that takes in input an amount of time in (hh, mm, ss) and returns the convertion
in seconds (i.e. hh = 2 , mm = 1 e ss = 11 , return = 7271).

'''

def discount(x, y):
	x = x - (x*y/100)
	return x
	
print "20% discount on 1000$ is ", scontato(1000, 20)

def secondi(hh, mm, ss):
	ss = ss + mm*60 + hh*60*60
	return ss

print "2 hours, 1 minute and 11 seconds are ", secondi(2, 1, 11) , " seconds."
