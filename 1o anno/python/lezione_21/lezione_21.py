#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:02:26 2021

@author: lizardking
"""

from rtrace import TraceRecursion # thanks Prof. Sterbini!

import os
# %% tornza dizionario dei file con dimensioni in byte (assemblo in CODA)

def find_file_with_size(folder, ext):
    rez = {}
    for fname in os.listdir(folder):
        # mi rende i file  e dir in folder
        # mi riprocuro il percorso assoluto
        full_path = f"{folder}/{fname}"
        if os.path.isfile(full_path):
            # se siamo nel caso del file controllo estensione
            if full_path.endswith(ext):
                # ok lo aggiungo alla lista la dimensione 
                # in byte tramite modulo  os.stat
                rez[full_path] = os.stat(full_path).st_size
                # result[full_path] = os.stat(full_path).st_size
        else:
            # ottengo il dizionario per le sotto cartelle
            D_files = find_file_with_size(full_path, ext)
            # unisco i due dizionari
            # si puo' anche fare con update invece che
            # con unpack
            rez.update(D_files)
            #rez = {**rez, **D_files}
    # torno per eventuali chiamate sopra di me
    return rez
#%%%% eval
find_file_with_size('.','py')
upper = find_file_with_size('..','py')

# %% tornza dizionario dei file con dimensioni in byte (assemblo all'ANDATA)
def find_file_with_size_andata(folder, ext, rez=None):
    init = False
    if rez is None:
        rez, init = {}, True
    for fname in os.listdir(folder):
        # mi rende i file  e dir in folder
        # mi riprocuro il percorso assoluto
        full_path = f"{folder}/{fname}"
        if os.path.isfile(full_path):
            # se siamo nel caso del file controllo estensione
            if full_path.endswith(ext):
                # ok lo aggiungo alla lista la dimensione 
                # in byte tramite modulo  os.stat
                rez[full_path] = os.stat(full_path).st_size
        else:
            # ottengo il dizionario per le sotto cartelle
            find_file_with_size_andata(full_path, ext, rez=rez)
    # torno per eventuali chiamate sopra di me
    return rez if init else None

#%%%% eval
find_file_with_size_andata('.','py')
upper2 = find_file_with_size_andata('..','py')
assert upper == upper2, 'uppers not equals'

# %% Alberi binari e Alberi N-ari
# si veda il file binary_tree_search.py e slides in PDF

# dopo esercizio pausa?

##################################################
#                 PAUSA ?                        #
##################################################



# %% Introduzione agli Alberi di Gioco

## Gioco del Tris (filetto o tic-tac-toe) lo vediamo
## nella prossime lezioni

# Consideriamo questo gioco:
# dato lo stato della lista L
# calcolare tutti gli altri stati
# considerando come mossa la seguente proprieta':
    # Mossa: due elementi consecutivi
    # devono avere il solito resto se divisi per due
    # prossimo stato:
    # quando la mossa **si verifica**
    # allora si passa ad un nuovo stato con una nuova lista L'
    # che sostituisce agli elementi consecuitivi 
    # la somma dei due consecutivi (passo di riduzione)
    
# Enumerare tutti i possibili stati
# e tornare tutte le foglie dell'albero di gioco
L = [99, 1, 3, 5, 20] # [d d d p]

class GameTree:
    def __init__(self, state):
        self.state = state
        self.state_viz = [ 'd' if s%2 == 1 else 'p'  for s in state] # per debug
        self.nexts = []
        self.next_states() # completa nexts
        
    def condition(self, pre, post):
        # se solito resto dai la somma
        if pre % 2 == post % 2:
            return pre + post
        
    def next_states(self):
        # andiamo di 2 in due quindi ci 
        # fermiamo ad uno prima della fine
        for i in range(len(self.state)-1):
            pre, post = self.state[i:i+2] # prende i e i+1
            somma = self.condition(pre, post)
            # se sono nella condizione
            # allora facciamo una mossa
            if somma: # if somma is not None
                # copio gli stati
                state = self.state[:]
                # quei 2 valori li sostituisci
                # con la somma
                state[i:i+2] = [somma]
                ## altro modo alternativo per farlo
                ## ma va commentato linea 124
                ## va tolto i e i+1
                # state = state[:i] + [somma] + state[i+2:]
                # enumero gli stati successivi
                self.nexts.append(GameTree(state))
                
    def __repr__(self, livello=0):
        rez =  '\t'*livello + f"{self.state} {self.state_viz}"
        for node in self.nexts:
            rez += '\n'+ node.__repr__(livello+1)
        return rez
    
    def leaves(self):
        # se foglia non ho stati futuri
        if not self.nexts:
            return [ (self.state, self.state_viz)] # list of tuple of lists
        # assemblo le foglie di tutti i figli
        leaves = []
        for node in self.nexts:
            leaves.extend(node.leaves())
        return leaves
    
    def leaves_external_list(self, L):
        if not self.nexts:
            # al contrario di prima combino  all'andata
            # semplicemente facendo append solo quando
            # sono nella foglia
            L.append((self.state, self.state_viz))
            
        # riapplico su tutti i figli
        for node in self.nexts:
            node.leaves_external_list(L)
            
#%% Exec GameTree
    
tree = GameTree(L)
print(tree)
W = tree.leaves()
# domanda chiesta a lezione
L = [] # questa verra' popolata in maniera distruttiva
       # viene fatto un append ogni volta che andiamo in una foglia
tree.leaves_external_list(L)
assert W == L, 'le due liste  devono essere uguali'