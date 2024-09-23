def es19(ftesto):
    '''
    Es 10: 6 punti
    Una matrice  di interi e' registrata all'interno di un file di testo.
    Il file contiene linee vuote inframmezzate a  linee corrispondenti alle righe della matrice. 
    All'interno  delle linee corrispondenti alle righe della matrice ciascun  intero della 
    riga della matrice compare preceduto da uno o piu' spazi.
    Si veda ad esempio il file fm10_1.txt dove e' registrata la matrice:
     1 20  3 40  5
    60  7  8  9 10
    11 12 13 14 15
    Si definisca la  funzione es19(ftesto) che, 
    - riceve l'indirizzo di un file di testo in cui e' registrata la matrice di interi.
    - restituisce una coppia (tupla) contenente:
        - la matrice nel formato di lista di liste di interi
        - la somma degli elementi della cornice esterna della matrice (prima e ultima riga e prima e ultima colonna)
    Ad esempio per il filefm10_1.txt la funzione es10 deve restituire:
        ([[ 1, 20,  3, 40,  5],
          [60,  7,  8,  9, 10],
          [11, 12, 13, 14, 15]],
          204)
    '''
    with open(ftesto, encoding='utf-8') as f:
        fstr = f.read()
    fMat = []
    for row in fstr.split('\n'):
        if row != '':
            fMat.append([int(n) for n in row.split()])
    tot = 0
    for i in range(len(fMat)):
        if len(fMat[i]) == 1:
            tot+=fMat[i][0]
        else:
            if i == 0 or i == len(fMat)-1:
                tot+=sum(fMat[i])
            else:
                tot+=fMat[i][0]+fMat[i][-1]
    return fMat, tot
    
print(es19('fm10_3.txt'))
