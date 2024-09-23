import immagini


def es4(fimm, fimm1, h1, w1):
    '''    
    Si definisca la  funzione es4(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e fimm1 di due file .PNG. e due interi h1 e w1 maggiori di zero.
    - legge l'immagine da fimm e crea una seconda  immagine. L'immagine da creare 
      ha h1 volte la lunghezza di quella letta e w1 volte la larghezza di quella letta e si ottiene 
      sostituendo ad ogni pixel dell'immagine letta un rettangolo di pixels di altezza h e ampiezza w aventi 
      tutti il colore del pixel originario.
    - salva l'immagine creata all'indirizzo fimm.
    - restituisce la tupla con il colore che compare piu' spesso nell'immagine letta e in 
    caso di parita' di occorrenze massime il colore del pixel che viene prima lessicograficamente.
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    
    img = immagini.load(fimm)
    img1 = [[img[h//h1][w//w1] for w in range(w1*len(img[0]))] for h in range(h1*len(img))]
    immagini.save(img1, fimm1)
    img_dict = {}
    for row in img1:
        for RGB in row:
            if RGB not in img_dict:
                img_dict[RGB] = 0
            else:
                img_dict[RGB]+=1
    return max(img_dict)

print(es4('cubo.png','test8_3.png',1,3))