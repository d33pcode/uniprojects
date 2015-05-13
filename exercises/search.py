#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Define search(lst, andc, orc, notc) that returns a new list of strings.
Each and every element of lst will be in the final list only if every element of andc is inside an element of lst, at least one element of orc (only if orc is not empty...) is inside an element of lst and no element in notc is inside an elemnt of lst.

For example, if 
lst = ['mela','pera','melo']

>>> search(lst,['el','a'],['ra','pe','m'],['tt','lo'])
returns ['mela']
>>> search(lst,[],['ra','pe','m'],['tt','lo'])
returns ['mela','pera']
>>> search(lst,['el','a'],[],['tt','lo'])
returns ['mela']
...

'''

#note to self: calling vars with a '-' in the name makes Python angry :( 

def search(lst, andc, orc, notc):
	flist = []							
	a_check = 0							
	o_check = 0							
	n_check = 0	
	for element in lst:
		for c in andc:	
			if c in element:
				a_check +=1	
		if len(orc) != 0:		
				for w in orc:
					if w in element:	
						o_check = 1
		else:
			o_check = 1		
		for y in notc:					
				if y in element:		
					n_check = 1 		
		if a_check == len(andc) and o_check > 0 and n_check == 0 :	
			flist.append(element)
	return flist				
lst = ['mela','pera','melo']
print search(lst,['el','a'],['ra','pe','m'],['tt','lo'])
