def es21(matrice):
    '''
    es21(matrice) presa la matrice di caratteri rappresentata tramite una lista di liste di caratteri, 
    la restituisce dopo averne ordinato le colonne in ordine lessicografico. 
    La matrice passata in input al termine della funzione non deve risultare modificata.  
    Ad esempio se la matrice di input e'
     [['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']] 
    la funzione restituira' la matrice:
     [['a','a','g','f'],
      ['b','b','m','g'],
      ['q','s','n','z']]     
    '''

    matrice2 = []
    for c in range(len(matrice[0])):
        row = []
        for r in range(len(matrice)):
            row.append(matrice[r][c])
        matrice2.append(row)
    for r in range(len(matrice2)):
        matrice2[r] = sorted(matrice2[r])
    matrice_out = []
    for c in range(len(matrice2[0])):
        row = []
        for r in range(len(matrice2)):
            row.append(matrice2[r][c])
        matrice_out.append(row)
    return matrice_out
        
print(es21([['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']] ))