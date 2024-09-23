def es3(ins1, ins2):
    '''
    progettare la funzione es3(ins1, ins2) che:
    - riceve  in input due insiemi  di numeri naturali
    - trova le terne (a,b,c) con a,b e c in insi1 con la proprieta' che a<b<c e a+b+c e' in insi2
    - restituisce l'insieme di tutte le triple trovate.
    Nella lista restituita le triple devono essere  rappresentate tramite tuple e le
    varie tuple devono comparire nella lista per somma di componenti crescenti e in caso di parita'
    in ordine lessicografico crescente.
    ESEMPIO:
    se ins1={ 2,4,5,6,8,9} e ins2={5,15,19,25} la funzione restituisce la lista
    [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
    ''' 
    abc_ins = []
    for a in ins1:
        abc = [a]
        for b in filter(lambda b: b>a, ins1):
            abc.append(b)
            for c in filter(lambda c: c>b, ins1):
                abc.append(c)
                if a+b+c in ins2:
                    abc_ins.append(tuple(abc))
                abc = [a,b]
            abc = [a]
    return sorted(abc_ins, key=(lambda tupl: tupl[0]+tupl[1]+tupl[2]))

print(es3({ 2,4,5,6,8,9}, {5,15,19,25}))
print(es3({ 1,2,4,5,6,8,9}, {16,18}))
