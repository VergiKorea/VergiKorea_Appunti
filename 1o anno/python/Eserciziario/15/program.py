

import immagini
def es15(fimm1,fimm2,fimm3):
    '''    
    Es 3: 6 punti
    Si definisca la  funzione es3(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini DI DIMENSIONI DIVERSE e crea la terza immagine da salvare all'indirizzo fimm3.
      La terza immagine si ottiene dalle prime due. Ha ampiezza  massima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza massima tra le altezze di fimm1 e fimm2.
      Per quanto riguarda i colori dei pixel della nuova immagine:
      il pixel [y][x] avra' colore nero (vale a dire (0,0,0)) se presente in entrambe
      le immagini originarie o in nessuna delle due. In caso contrario assumera' il   colore 
      del pixel dell'unica immagine originaria in cui e' presente.
      (guardate le immagini di test per chiarimenti)
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel di colore nero presenti  nell'immagine creata.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    imm1 = immagini.load(fimm1)
    imm2 = immagini.load(fimm2)
    imm3 = [[(0,0,0) for _ in range(max(len(imm1[0]), len(imm2[0])))] for _ in range(max(len(imm1), len(imm2)))]
    for r in range(len(imm3)):
        for c in range(len(imm3[0])):
            if (r < len(imm1) and c >= len(imm2[0])) or (c < len(imm1[0]) and r >= len(imm2)):
                imm3[r][c] = imm1[r][c]
            elif (r < len(imm2) and c >= len(imm1[0])) or (c < len(imm2[0]) and r >= len(imm1)):
                imm3[r][c] = imm2[r][c]
    immagini.save(imm3, fimm3)
    cnt = 0
    for row in imm3:
        for RGB in row:
            if RGB == (0,0,0): cnt+=1
    return cnt
        
                                                                                    