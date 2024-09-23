

def es17(ls, k):
    '''
    Es 7: 6 punti 
    progettare la funzione es17(ls,k) che: 
    - riceve  in input una lista di parole ls ed un intero k
    - cancella da ls le parole che contengono almeno k  caratteri uguali (sia in maiuscolo che in minuscolo)
    - restituisce il numero di parole cancellate da ls. 
    Nota che al termine della funzione la lista passata come parametro deve risultare modificata
    (ricorda che le liste sono mutabili). 
     ESEMPI:
     Se ls=[ 'ananas', 'pera', 'banana', 'melone', 'kiwi','albicocca'] e k=3
     la funzione restituisce 3 e la lista ls diventa ['pera', 'melone', 'kiwi']  
     Se ls=[ 'Angelo', 'Andrea', 'Osvaldo', 'Anna', 'Monica', 'Adele'] e k=2
     la funzione restituisce 4 e la lista ls diventa ['Angelo', 'Monica']
    '''
    original_len = len(ls)
    i=0
    while i<len(ls):
        for char in ls[i]:
            if ls[i] in ls:
                if ls[i].lower().count(char.lower()) >= k:
                    ls.pop(i)
                    i-=1
        i+=1
    return original_len - len(ls)

print(es17(['Angelo', 'Andrea', 'Osvaldo', 'Anna', 'Monica', 'Adele'], 2))
