# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:32:08 2024

@author: Marius
"""



def perm(set_a):
    set_a = set(set_a)
    output = []
    if len(set_a)<2:
        return [tuple(set_a)]
    for el1 in set_a:
        for perm_ist in perm(set_a-set([el1])):
            output.append(tuple([el1])+tuple(perm_ist))
    return output

print(perm([1,2,3]))
        