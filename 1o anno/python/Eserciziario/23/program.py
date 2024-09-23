import immagini
import json


def es23(fileJson, filePng):
    '''
    Abbiamo un file di tipo json contenente una matrice (lista di liste) M i cui elementi 
    sono stringhe. La matrice e' il risultato della codifica di un'immagine.
    L'immagine ha ampiezza w e altezza h dove w e' il numero di colonne della matrice M e h 
    il numero di righe. Il colore (r,g,b) del  pixel di coordinate x,y e' codificato con 
    la stringa presente in M[y][x], piu' precisamente la stringa e' composta da 9 cifre. 
    Le tre piu' significative sono la codifica di r, le tre centrali sono la codica di g e le tre 
    meno significative la codifica di b.  

    Scrivete la funzione es7(fileJson, filePng) che riceve come argomenti:
        :param fileJson: il path del file json dove si trova la matrice dell'immagine codificata
        :param filePng:  il path del file PNG dove salvare l'immagine decodificata.
        :return: il colore che appare piu' spesso tra quelli dei pixel dell'immagine (a parita'
        viene selezionato il colore che precede nell'ordinamento crescente 
        rispetto alla prima, alla seconda e poi alla terza coordinata).
    '''
    with open(fileJson, encoding = 'utf-8') as f:
        fstr = f.read()
    fstr = fstr[2:-2].split('], [')
    img = []
    img_seq = []
    for row_str in fstr:
        row_str = row_str[2:-2].split('", "')
        row = []
        for RGB in row_str:
            row.append(tuple([int(RGB[:3]), int(RGB[3:6]), int(RGB[6:])]))
            img_seq.append((tuple([int(RGB[:3]), int(RGB[3:6]), int(RGB[6:])])))
        img.append(row)
    immagini.save(img, filePng)
    out = [[], 0]
    for RGB in img_seq:
        count = img_seq.count(RGB)
        if count > out[1]:
            out = [[RGB], count]
        elif count == out[1]:
            out[0].append(RGB)
    return sorted(out[0])[0]
    

print(es23('3cime.json', 'o2.png'))
