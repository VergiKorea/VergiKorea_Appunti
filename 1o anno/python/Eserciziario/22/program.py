import immagini
import json


def es22(filePng, fileJson):
    '''
    Abbiamo un file contenente un'immagine PNG che bisogna leggere, codificare e infine salvare 
    in un file JSON.
    L'immagine va codificata in una matrice (lista di liste) M di stringhe 
    di dimensioni w per h dove w e' l'ampiezza  dell'immagine  mentre h e' la sua altezza. 
    La cella M[i][j] deve contenere una stringa 
    di 9 caratteri ottenuti concatenando nell'ordine le componenti R, G e B del colore del pixel 
    corrispondente nell'immagine (dopo aver espresso ciascuno dei tre interi come stringa di 
    tre caratteri). Ad esempio  il colore (0,0,0) sara' codificato come '000000000' e 
    il colore (50,10,200) come '050010200'.
    Bisogna infine determinare la stringa di 9 caratteri che e' presente nella matrice 
    con maggior frequenza (a parita' di frequenza quella che precede lessicograficamente le altre).


    Scrivete la funzione es22(filePng, fileJson) che riceve come argomenti:
        :param filePng:  il path del file PNG che dovete codificare
        :param fileJson: il path del file json dove salvare la codifica ottenuta
        :return: la stringa lessicograficamente piu' piccola tra quelle che compaiono 
        nella matrice con piu' frequenza.
    '''
    img = immagini.load(filePng)
    img_seq = []
    for r in range(len(img)):
        for c in range(len(img[0])):
            str_RGB = ''
            for col in img[r][c]:
                str_col = str(col)
                while len(str_col) < 3:
                    str_col = '0'+str_col
                str_RGB+=str_col
            img[r][c] = str_RGB
            img_seq.append(str_RGB)
    img_str = ['["'+'", "'.join(row)+'"]' for row in img]
    img_str = '['+', '.join(img_str)+']'
    with open(fileJson, 'w') as f:
        f.write(img_str)
    img_seq.sort(key=lambda el: img_seq.count(el))
    count = [[], 0]
    for RGB in set(img_seq):
        cnt = img_seq.count(RGB)
        if cnt > count[1]:
            count[0] = [RGB]
            count[1] = cnt
        elif cnt == count[1]:
            count[0].append(RGB)
    return sorted(count[0])[0]
print(es22('italia.png', 'o1.json'))