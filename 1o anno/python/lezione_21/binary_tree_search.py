#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:12:12 2020

@author: lizardking
"""


class BinaryNode:

    def __init__(self, value, sx=None, dx=None):
        self.value = value
        self.sx = sx
        self.dx = dx
        
    def height(self):
        Hsx = 0 if not self.sx else self.sx.height()
        Hdx = 0 if not self.dx else self.dx.height()
        return max(Hsx, Hdx) + 1
    
    def diameter(self):
        # calcolo percorso masssimo su radice
        Hsx = 0 if not self.sx else self.sx.height()
        Hdx = 0 if not self.dx else self.dx.height()
        D_root = Hsx + Hdx + 1
        # calcolo percorso max. sul destro
        D_dx = 0 if not self.dx else self.dx.diameter()
        # poi sul sinistro
        D_sx = 0 if not self.sx else self.sx.diameter()
        # prendo il massimo
        return max(D_root, D_dx, D_sx)

    def viz(self,i=1):
        if self.sx is None and self.dx is None:
            return str(self.value)
        
        Sx = '' if not self.sx else '\n' + '\t'*(i) + self.sx.viz(i=i+1)
        Dx = '' if not self.dx else '\n' + '\t'*(i) + self.dx.viz(i=i+1)
        return str(self.value) + Sx + Dx        

    def __repr__(self):
        return self.viz()
    
    def find_pre(self, f_value):
        '''Ricerca pre order'''
        if self.value == f_value:
            return True
        elif self.sx and self.sx.find_pre(f_value):
            return True
        elif self.dx and self.dx.find_pre(f_value):
            return True
        else:
            return False
                            
    def find_in(self, f_value):
        '''Ricerca in order'''
        if self.sx and self.sx.find_in(f_value):
            return True
        elif self.value == f_value:
            return True
        elif self.dx and self.dx.find_in(f_value):
            return True
        else:
            return False
        
    def find_post(self, f_value):
        '''Ricerca in post'''
        if self.sx and self.sx.find_post(f_value):
            return True
        elif self.dx and self.dx.find_post(f_value):
            return True
        elif self.value == f_value:
            return True
        else:
            return False

    def print_tree_pre(self, sign='>'):
        print(self.value, end=sign)
        if self.sx:
            self.sx.print_tree_pre(sign=sign)
        if self.dx:
            self.dx.print_tree_pre(sign=sign)
        
    def print_tree_in(self, sign='>'):
        if self.sx:
            self.sx.print_tree_in(sign=sign)
        print(self.value, end=sign)
        if self.dx:
            self.dx.print_tree_in(sign=sign)

    def print_tree_post(self, sign='>'):
        if self.sx:
            self.sx.print_tree_post(sign=sign)
        if self.dx:
            self.dx.print_tree_post(sign=sign)
        print(self.value, end=sign)

    def print_tree(self, order='pre', sign='>'):
        if order == 'pre':
            self.print_tree_pre(sign=sign)
        elif order == 'in':
            self.print_tree_in(sign=sign)
        elif order == 'post':
            self.print_tree_post(sign=sign)
        else:
            pass
        print()

        
if __name__ == '__main__':
    # ------------ TREES -------------------#
    root = BinaryNode(1, BinaryNode(6, BinaryNode(2), BinaryNode(3)),
                      BinaryNode(7, BinaryNode(4), BinaryNode(5))
                      )
    root_full = BinaryNode(1, BinaryNode(6, BinaryNode(2), BinaryNode(3)),
                           BinaryNode(7, BinaryNode(4, BinaryNode(8), BinaryNode(9)),
                                      BinaryNode(5, BinaryNode(10), BinaryNode(11)))
                           )

    root_partial = BinaryNode(1, BinaryNode(6, BinaryNode(2), None),
                              BinaryNode(7, BinaryNode(5))
                              )
    root_list = BinaryNode(1, BinaryNode(6, BinaryNode(2), None),
                           None
                           )
    
    print('# ------------ Testing the search -------------------#')
    works = lambda root, v, op  : op([root.find_pre(v), root.find_in(v), root.find_post(v)])
    
    print('> Should test True (testing positive cases)')
    print(all([works(root, v, all) for v in [1, 6, 2, 3, 7, 4, 5]]))
    print(all([works(root_partial, v, all) for v in [1, 6, 2, 7, 5]]))
    print(all([works(root_list, v, all) for v in [1, 6, 2]]))

    print('> Should test False (testing negative cases)')
    print(any([works(root, v, any) for v in [-1, 8, 0, 9, 10, -2, 100]]))
    print(any([works(root_partial, v, any) for v in [-1, 8, 0, 9, 10, -2, 100]]))
    print(any([works(root_list, v, any) for v in [-1, 8, 0, 9, 10, -2, 100]]))

    print('# ------------ Navigating the trees -------------------#')
    root_ord = BinaryNode(1, BinaryNode(2, BinaryNode(4), BinaryNode(5)),
                          BinaryNode(3, BinaryNode(6), BinaryNode(7))
                          )
    print('Profondita (pre)')
    root_ord.print_tree(order='pre')
    print('Profondita (in)')    
    root_ord.print_tree(order='in')
    print('Profondita (post)')
    root_ord.print_tree(order='post')
    
    print('# ---- Espressioni Aritmetiche -----------#')
    expr_root = BinaryNode('+', BinaryNode('x', BinaryNode(3), BinaryNode(4)),
                           BinaryNode('1')
                           )
    print('expr (pre)')
    expr_root.print_tree(order='pre', sign=' ')
    print('expr (in)')
    expr_root.print_tree(order='in', sign=' ')
    print('expr (post)')
    expr_root.print_tree(order='post', sign=' ')
    
    print('# ---- Altezza -----------#')
    #%%
    n0 = BinaryNode(0)
    n1 = BinaryNode(1, n0)
    n2 = BinaryNode(2)
    n3 = BinaryNode(3, n1, n2)
    n4 = BinaryNode(4)
    n5_root = BinaryNode(5, n4, n3)
    n5_root.height()
    n5_root.diameter()