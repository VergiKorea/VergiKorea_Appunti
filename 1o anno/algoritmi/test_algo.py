# -*- coding: utf-8 -*-

def sort_rel(A):
    a=0
    for i in range(len(A)):
        if(A[i]<0):
            temp = A[a]
            A[a] = A[i]
            A[i] = temp
            a=a+1
    return A

print(sort_rel([1,2,3,4,5,6,-1,-2,-3,-4,-5]))

