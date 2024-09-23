#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Una proprietaria terriera in California, Lida, eredita un
appezzamento di terreno. La superficie è modellata come un lotto
rettangolare di grandezza variabile. Il lotto di terra è
rappresentato come un'immagine codificata come lista di liste.

Per far fruttare l'appezzamento di terra, Lida decide di affittare la
terra ad altre persone. Per fare ciò, può decidere di dividere la
terra in quattro parti. Nel caso in cui decida di non affittare la sua
proprietà nessuna divisione è effettuata. Al contrario, nel caso in
cui la proprietà venga divisa in quattro sotto parti, delle linee di
demarcazione colorate vengono create, per tutelare i confini, appunto.
Le linee hanno uno spessore di un solo pixel. Non è dato sapere come
e dove le line verranno poste (non vi è una regolarità), e neppure
sappiamo quale è il colore che verrà usato a priori.  Conosciamo
solamente che le linee sono allineate agli assi.

I quattro locatari che ricevono le quattro proprietà potrebbero
prendere la solita decisione che Lida ha preso in precedenza oppure
no: essi potrebbero subaffittare ancora una volta le loro piccole
proprietà ad altre persone, oppure, potrebbero decidere di tenere la
terra tutta per loro. La decisione della suddivisione per ogni
locatario è indipendente alle altre. Per esempio, il locatario #1 può
decidere di subaffittare ancora, mentre il locatario #2 può tenere la
proprietà, mentre i locatari #3, #4 possono suddividere ancora. Quello
che sappiamo è che se subaffittano, dividono sempre in quattro
parti. Infatti, nel caso in cui dividano ancora la proprietà,
seguiranno una strategia simile di impostare i loro confini tracciando
delle linee di demarcazione degli stessi. Sicuramente useranno un
colore che è diverso dai colori usati da Lida (e da altri eventuali in
precedenza) tuttavia i quattro locatari usano il solito colore fra
loro, allo stesso livello di suddivisione.

NOTA: E' importante ricordare che il colore del background (bg) dell'
appezzamento non è dato (cioè non sappiamo a priori se il bg è
nero, bianco oppure blue). Sappiamo però che il colore di background
della terra NON è usato da nessuno dei locatari (ne da Lida) per
marcare i confini.

Il processo di suddivisione può continuare fino a quando tutti i
locatari in tutte gli appezzamenti decidono di smettere col subaffitto.
Questo processo descritto fino ad ora, ci porta all'immagine che è
data in input al vostro programma.

NOTA: Potete assumere che l'ipotetico appezzamento di terreno più
piccolo (rettangolo più piccolo possibile) abbia il lato più corto di
due pixel.

Riflettete bene sul problema e una volta che siete sicuri di una
soluzione, progettate su carta una soluzione (questa soluzione poi
deve essere descritta nella pseudo codice) e poi implementate un
programma ex1(input_file, output_file) che:
   - legge il file indicato dal parametro 'input_file' usando
     il modulo libreria 'images'.
   - pre-processa l'immagine, se necessario, e implementa una funzione
     *ricorsiva* per risolvere i requisiti sottostanti.
   - si deve contare tutte gli appezzamenti di terra che sono nell'
     immagine e restituire questo conteggio. Il programma deve
     restituire il numero di rettangoli con il colore del background
     dell'immagine che vi sono presenti. Riferendosi alla figura
     semplificata sottostante:

        # +++++++++++++++++++
        # +-1-|-2-|---------+
        # ++++a+++|----5----+
        # +-3-|-4-|---------+
        # ++++++++b++++++++++
        # +-------|--7-|-8--+
        # +---6---|++++c+++++
        # +-------|-10-|-9--+
        # +++++++++++++++++++
  
    l'approccio deve restituire un intero che corrisponde a 10 in
    questo caso (numero totale di rettangoli). I numeri posti nella
    figura soprastante sono stati inseriti solo per chiarire il
    concetto. (I dati sono privi di tali numeri inseriti, ovviamente).
    - infine, dato che l'agenzia immobiliare deve registrare
    tutti i confini che sono creati, il programma deve costruire un'
    immagine di output di grandezza 1x(N+1). L'immagine codifica come
    primo pixel il colore del background. Poi, deve codificare la
    gerarchia dei colori di tutti gli N colori usati per suddividere
    la terra in sotto rettangoli. La gerarchia dei colori e' definita
    "visitando" prima in profondita' il lotto in alto a sx, poi in
    alto a dx, poi in basso a sx, e infine in basso a dx. I colori
    devono essere salvati in ordine inverso rispetto alla visita
    effettuata. Con riferimento all'immagine semplificata precedente,
    assumendo che i colori dei confini di demarcazione siano descritti
    dalla lettere al loro centro, allora l'immagine di output deve
    contenere:
             out_colors = bg b c a


    Un altro esempio un pochino piu' complesso:

         +++++++++++++++++++++++++++++++++++++
         +-1-|-2-|---------|--------|--------+
         ++++a+++|----5----|---6----|----7---+
         +-3-|-4-|---------|--------|--------+
         ++++++++b+++++++++|++++++++c+++++++++
         +-------|--9-|-10-|--------|--------+
         +--8----|++++d++++|---13---|---14---+
         +-------|-11-|-12-|--------|--------+
         ++++++++++++++++++e++++++++++++++++++
         +-15|-16|---------|--------|-21|-22-+
         ++++f+++|---19----|---20---|+++g+++++
         +-17|-18|---------|--------|-23|--24+
         ++++++++h+++++++++|++++++++l+++++++++
         +-------|-26-|-27-|--------|-31-|-32+
         +--25---|++++m++++|---30---|+++n+++++
         +-------|-29-|-28-|--------|-33-|-34+
         +++++++++++++++++++++++++++++++++++++

         num. rect: 34
         gerarchia dei colori:
         bg e l n g h m f c b d a


NOTA: è vietato importare/usare altre librerie o aprire file tranne
quello indicato

NOTA: il sistema di test riconosce la presenza di ricorsione SOLO se
    la funzione/metodo ricorsivo è definita a livello esterno.  NON
    definite la funzione ricorsiva all'interno di un'altra
    funzione/metodo altrimenti fallirete tutti i test.
"""

import images

def out_col(img_in, bg):    
    out = []
    countX = {}
    countY = {}
    for r in range(len(img_in)):
        if img_in[r][0] != bg and len(set([img_in[r][c] for c in range(len(img_in[0]))])) == 1: 
            if img_in[r][0] not in countY: countY[img_in[r][0]] = [r]
            else: countY[img_in[r][0]].append(r)
    for c in range(len(img_in[0])):
        if img_in[0][c] != bg and len(set([img_in[r][c] for r in range(len(img_in))])) == 1: 
            if img_in[0][c] not in countX: countX[img_in[0][c]] = [c]
            else: countX[img_in[0][c]].append(c)
    
    if len(countX)>0 and len(countY)>0:
        for key in countY:
            if len(countY[key]) == 1:
                r1 = countY[key][0]
        for key in countX:
            if len(countX[key]) == 1:
                c1 = countX[key][0]
        #per assicurarmi di avere la croce che divide in 4 l'immagine il programma dovrebbe assicurarsi che la linea sia continua da cima a fondo | NOTA BENE: ancora non è perfetto e l'output non è completamente corretto, dagli te un'occhiata pensando a sto ragionamento e vedi cosa riesci a tirarne fuori
        
        out.append(img_in[r1][c1])
        sub_img = []
        for row in img_in[r1+1:]:
            sub_img.append(row[c1+1:])
        out.extend(out_col(sub_img, bg))
        sub_img = []
        for row in img_in[:r1-1]:
            sub_img.append(row[c1+1:])
        out.extend(out_col(sub_img, bg))
        sub_img = []
        for row in img_in[r1+1:]:
            sub_img.append(row[:c1-1])
        out.extend(out_col(sub_img, bg))
        sub_img = []
        for row in img_in[:r1-1]:
            sub_img.append(row[:c1-1])
        out.extend(out_col(sub_img, bg))
    return list(filter(lambda color: color != [], out))
    
def ex1(input_file,  output_file):
    # write your code here
    img_in = images.load(input_file)
    bg = img_in[0][0]
    img_out = [bg]
    img_out.extend(out_col(img_in, bg))
    img_out = [img_out]
    images.save(img_out, output_file)


if __name__ == '__main__':
    # write your tests here
    print(ex1('C://Users\mariu\Desktop\python\HW8rec\puzzles\hard01.in.png', 'C://Users/mariu/Desktop/python/HW8rec/puzzles/test_hard01.png'))
