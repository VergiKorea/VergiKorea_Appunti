import immagini

'''    
    Es 12: 4 punti
    Progettare la  funzione es13(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e  fimm1 di due file .PNG. 
    - legge l'immagine da fimm ne modifica i colori dei pixel e  la salva poi 
      all'indirizzo fimm1.
    - restituisce infine il numero di colori DIFFERENTI presenti nell'immagine modificata.
      I colori dei pixel dalla nuova immagine si ottengono a partire da quelli 
      dell'immagine originaria con la seguente  procedura:.
      le tuple dei DIFFERENTI colori presenti nella prima immagine vengono ordinate in 
      ordine crescente.
      La sequenza ordinata di tuple  che si ottiene viene suddivisa a gruppi di 50 (se il 
      numero totale di tuple non e' un multiplo di 50 allora l'ultimo gruppo avra' 
      meno di 50 elementi). 
      I colori corrispondenti alle tuple che compaiono come  primo elemento di 
      ciascun gruppo saranno i colori assegnati ai pixel dell'immagine.
      tutti i pixel che avevano colori corrispondenti a tuple finite in uno stesso 
      gruppo avranno come colore quello corrispondente alla prima tupla del gruppo.
      Ad esempio i pixel che avevano colori corrispondenti alle tuple finite nelle prime 50 posizioni 
      della sequenza ordinata  avranno ora tutti lo stesso colore (dato dal colore corrispondente 
      alla tupla che occupa la prima posizione  della sequenza), i pixel 
      che avevano colori le cui tuple  nella sequenza occupano le posizioni 
      da 50 a 99 avranno tutti lo stesso  colore (corrispondente alla tupla in posizione  
      50) ecc. ecc. 
      Sull'immagine Fig1.png la funzione deve produrre il file RisFig1.png e restituire il numero ?
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
def es13(fimm,fimm1):
    imm = immagini.load(fimm)
    imm_seq = []
    for row in imm:
        for RGB in row:
            imm_seq.append(RGB)
    imm_seq = sorted(list(set(imm_seq)))
    imm_seq2 = []
    imm_seq2_row = []
    for RGB in imm_seq:
        if len(imm_seq2_row) == 50:
            imm_seq2.append(imm_seq2_row)
            imm_seq2_row = []
        imm_seq2_row.append(RGB)
    imm1 = [[imm[i][j] for j in range(len(imm[0]))] for i in range(len(imm))]
    imm_seq = []
    for r in range(len(imm)):
        for c in range(len(imm[0])):
            for row in imm_seq2:
                if imm[r][c] in row:
                    imm1[r][c] = row[0]
                    imm_seq.append(row[0])
    immagini.save(imm1,fimm1)
    return len(set(imm_seq))+1
    

print(es13('Foto1.png', 'testFoto1.png'))