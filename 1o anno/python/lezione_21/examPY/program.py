#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla FINE di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# DEBUG=True vi attiva anche lo STACK TRACE degli errori per sapere il numero
# di linea di program.py che genera l'errore.
################################################################################


    
# %% ----------------------------------- EX.3 ----------------------------------- #
"""
Ex3: 6 punti (+3 opzionali)
Sia dato un albero definito da oggetti di tipo BinaryNode contenuti nel file tree.py
Assumiamo che la radice si trovi a profondità 0.
Vogliamo trasformare l'albero come segue:
    Dati j < k, interi
    - per ogni nodo che si trova a profondità j, il suo valore
      deve essere sostituito con la somma dei valori di tutti i nodi
      di quel sottoalbero che sono a profondità compresa tra j e k (inclusi)
    - infine la funzione ritorna il numero di nodi sommati

Definire quindi la funzione ex3(root, j, k) ricorsiva o che fa uso di funzioni
ricorsive che riceve come argomenti:
    - root: un nodo di tipo Node, radice dell'Albero
    - j : un intero che indica il livello minimo dei nodi da sommare
    - k : un intero che indica il livello massimo dei nodi da sommare
Opzionale: (3 punti)
La funzione ritorna il numero totale di nodi sommati

Esempio: se l'albero è
                             profondità
                1               0
            /       \ 
           2         7          1
         /   \      / 
        3    5     8            2
       /      \     \ 
      4        6     8          3
la chiamata ex3(root, 1, 2) modificherà l'albero come segue
                1
            /       \ 
           10        15         10=2+3+5  15=7+8
         /   \      / 
        3    5     8
       /      \     \ 
      4        6     8
e la funzione tornerà 5, che è il numero di nodi tra profondità 1 e profondità 2 comprese
(ovvero i nodi 2, 7, 3, 5, 8)

"""

import os

def ex3(root, j, k):
    # INSERISCI QUI IL TUO CODICE
    pass


# %% ----------------------------------- EX.4 ----------------------------------- #
"""
Ex4: 6+3 punti
Si definisca la funzione ex4(path, outfile) ricorsiva o che fa uso di funzioni
ricorsive che prende in ingresso due stringhe che rappresentano un path e un
nome di file, rispettivamente. La funzione deve ricercare all'interno della
directory indicata da path e in tutte le sue subdirectory, tutti i file con
estensione '.txt' e calcolare per ogni file trovato il numero che si ottiene
sommando il valore unicode dei soli caratteri alfabetici in esso contenuti.
La funzione deve costruire il dizionario che ha per chiave ogni file trovato
compreso di percorso relativo e per valore il numero calcolato per ogni file.

(+3 punti) La funzione può anche salvare nel file 'outfile' il percorso di tutti
file individuati e il valore di ogni file, separati da un carattere di
tabulazione. Ogni riga del file contiene il percorso di un file con il suo valore.
I percorsi dei file devono essere salvati in 'outfile' in ordine decrescente per valore
trovato; in caso di parità, in ordine crescente per profondità della
directory in cui sono contenuti; in caso di ulteriore parità, in ordine alfabetico.

Ad esempio, la funzione ex('ex4/honchos', 'ex4_1.txt') dovrà ritornare il
dizionario:

{'ex4/honchos/crescendos/sensitisation.txt': 6212,
'ex4/honchos/finny.txt': 9481,
'ex4/honchos/interlineation.txt': 3295,
'ex4/honchos/analysable.txt': 1919}
ed opzionalmente salvare nel file
'ex4_1.txt': le righe
ex4/honchos/finny.txt	9481
ex4/honchos/crescendos/sensitisation.txt	6212
ex4/honchos/interlineation.txt	3295
ex4/honchos/analysable.txt	1919

È proibito usare la funzione os.walk.
Si possono usare le funzioni os.listdir, os.path.isfile, os.isdir e la
concatenazione di stringhe con il carattere "/" per generare i percorsi
dei file.
"""

def ex4(path, outfile):
    # INSERISCI QUI IL TUO CODICE
    pass

###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
