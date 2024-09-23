

import immagini
def es49(fimm1,fimm2,fimm3):
    '''
    Si definisca la  funzione es49(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini e crea la terza immagine da salvare all'indirizzo fimm3. 
      La terza immagine si ottiene dalle prime due. Ha ampiezza  minima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza minima tra le altezze di fimm1 e fimm2.
      il pixel [i][j] dell'immagine ha lo stesso colore del pixel corrispondente
      dell'immagine fimm1 se i e j sono entrambi numeri pari o entrambi numeri dispari, 
      ha il colore del pixel corrispondente in  fimm2 altrimenti
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel presenti nell'immagine creata per i quali  la somma delle 
      tre coordinate del colore e' un numero dispari.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    # inserisci qui il tuo codice
    imm1 = immagini.load(fimm1)
    imm2 = immagini.load(fimm2)
    imm3 = [[None for _ in range(min(len(imm1[0]), len(imm2[0])))] for _ in range(min(len(imm1), len(imm2)))]
    out = 0
    for r in range(len(imm3)):
        for c in range(len(imm3[0])):
            if r%2 == c%2:
                imm3[r][c] = imm1[r][c]
            else:
                imm3[r][c] = imm2[r][c]
            if sum(imm3[r][c])%2 == 1:
                out+=1
    immagini.save(imm3, fimm3)
    return out


print(es49('foto1.png','foto2.png','test1.png'))