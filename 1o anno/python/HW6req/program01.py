#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
È una tranquilla serata di dicembre e mentre fuori piove a dirotto
ricevi una chiamata dalla tuo amico Bart, poco esperto di computer.
Dopo averlo calmato, ti racconta di essersi messo al
pc per cercare un regalo perfetto sull'onda del successo dei siti di
e-commerce alternativi, facendo ricerche sui siti più disparati
utilizzando un traduttore automatico. Ti racconta di essere finito
su un sito con il dominio .atp, pensando che avesse a che fare
con il tennis, sua grande passione. Dopo aver
seguito un paio di prodotti sullo strano sito, si è accorto che
il suo browser rispondeva più lentamente e il puntatore del mouse
cominciava ad andare a scatti. Dopo pochi secondi, gli è apparso un
messaggio di avvertimento che lo informava di essere stato
infettato da un ransomware di ultima generazione, che prende
di mira i file del pc. Colto dal panico, si è ricordato della
tua impresa con gli spartiti dei Tarahumara e ti ha chiamato
affinché lo aiuti a recuperare i suoi file. Il giorno dopo,
ti rechi a casa di Bart e analizzi la situazione: come pensavi,
il ransomware è il famigerato Burl1(ONE), che cifra i file del pc
memorizzando la chiave di cifratura all'interno delle immagini
con estensione .png, trasformandole in puzzle complicatissimi.
Poiché Bart memorizza le sue immagini su un servizio on cloud,
riesci a recuperare le immagini originali in modo da poter
risalire alla chiave di cifratura del ransomware. Riuscirai
a trovare tutte le chiavi? Bart conta su di te!

Il ransomware Burl1 memorizza la chiave di cifratura dividendo
in tasselli quadrati le immagini con estensione .png ed eseguendo
o meno delle rotazioni dei singoli tasselli di 90, 180 oppure 270°, 
ovvero eseguendo una, due o tre rotazioni a destra. La chiave avrà
rispettivamente una 'R' (right) una 'F' (flip) o una 'L' (left) a
seconda della rotazione fatta. L'assenza di rotazione indica il
carattere 'N'. Per ogni immagine è necessario ricostruire la chiave
di cifratura sotto forma di una lista di stringhe: ogni stringa
corrisponde alla sequenza di rotazioni di ogni tassello di una
riga. Per cui un'immagine 100x60 in cui i tasselli hanno dimensione
20 nasconderà una chiave di cifratura di 15 caratteri, organizzati
in tre stringhe da cinque caratteri ognuna. Infatti, ci saranno
5 tasselli per riga (100//20 = 5) e 3 righe (60//20 = 3).
Per scoprire le rotazioni eseguite devi utilizzare l'immagine
che hai recuperato dal cloud per eseguire il confronto con
l'immagine cifrata.

Devi scrivere la funzione
jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
che prende in ingresso 
- il nome del file contenente l'immagine con i tasselli ruotati, 
- il nome del file contenente l'immagine con i tasselli non ruotati, 
- un intero che indica la dimensione del lato dei tasselli quadrati, 
- il nome di un file di testo da decifrare con la chiave di cifratura 
- e il nome in cui salvare il file decifrato.

La funzione deve restituire la chiave di cifratura nascosta
nell'immagine in puzzle_image, ovvero la sequenza di
rotazioni da fare per ricostruire l'immagine iniziale e decifrare
il file in input.

Ad esempio, confrontando l'immagine in test01_in.png con test01_exp.png
e considerando i tasselli quadrati da 20 pixel, è possibile
stabilire che le rotazioni applicate sono state
            - 'LFR' per i tasselli della prima riga
            - 'NFF' per i tasselli della seconda riga e
            - 'FNR' per i tasselli della terza riga
            Per cui la chiave da ritornare sarà: ['LFR', 'NFF', 'FNR'].
            
La decifratura del file si ottiene attuando una trasformazione del
cattere in posizione i mediante il carattere della chiave in posizione
i modulo la lunghezza della chiave.

Ad esempio, se la chiave è ['LFR', 'NFF', 'FNR'], la chiave è lunga 9 
e bisogna decifrare il carattere in posizione 14 del file in input,
bisogna considerare il carattere in posizione 14%9 = 5 della chiave,
ovvero 'F'.
Le trasformazioni per la decifratura sono le seguenti:
    - R = text[i] sostituito dal carattere con ord seguente
    - L = text[i] sostituito dal carattere con ord precedente
    - N = resta invariato
    - F = swap text[i] con text[i+1]. Se i+1 non esiste, si considera 
          il carattere text[0].

Ad esempio, se la chiave di cifratura è LFR e il testo cifrato è BNVDCAP,
il testo in chiaro sarà AVOCADO, in quanto la decifratura è la seguente:

step     key      deciphering-buffer
1        LFR      BNVDCAP -> ANVDCAP
         ^        ^
2        LFR      ANVDCAP -> AVNDCAP
          ^        ^
3        LFR      AVNDCAP -> AVODCAP
           ^        ^
4        LFR      AVODCAP -> AVOCCAP
         ^           ^
5        LFR      AVOCCAP -> AVOCACP
          ^           ^
6        LFR      AVOCACP -> AVOCADP
           ^           ^
7        LFR      AVOCADP -> AVOCADO
         ^              ^

'''

# %%
import images

def decrypt(chiave: str, encrypted_file: str):
    with open(encrypted_file, encoding='utf-8') as f:
        encrypted_file_content = f.read()
    decrypted_str = ''
    for i in range(len(encrypted_file_content)):
        index = i%len(chiave)
        if chiave[index] in 'R':
            decrypted_str += chr(ord(encrypted_file_content[i])+1)
        elif chiave[index] in 'L':
            decrypted_str += chr(ord(encrypted_file_content[i])-1)
        elif chiave[index] in 'N':
            decrypted_str += encrypted_file_content[i]
        elif chiave[index] in 'F':
            if i == len(encrypted_file_content)-1:
                decrypted_str += encrypted_file_content[0]
                encrypted_file_content = f'{encrypted_file_content[i]}{encrypted_file_content[1:i]}{encrypted_file_content[0]}'
            
            else:
                decrypted_str += encrypted_file_content[i+1]
                encrypted_file_content = f'{encrypted_file_content[:i]}{encrypted_file_content[i+1]}{encrypted_file_content[i]}{encrypted_file_content[i+2:]}'
            
    return decrypted_str
            
def jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
    img_in = images.load(puzzle_image)
    img_out = images.load(plain_image)
    
    chiave = []
    chiave_str = ''
    
    for h in range(len(img_in)//tile_size):
        img_riga = img_out[h*tile_size:h*tile_size+tile_size]
        img_riga_critt = img_in[h*tile_size:h*tile_size+tile_size]
        chiave_riga = ''
        for w in range(len(img_in[0])//tile_size):
            img_istanza = [row[w*tile_size:w*tile_size+tile_size] for row in img_riga]
            img_istanza_critt = [row[w*tile_size:w*tile_size+tile_size] for row in img_riga_critt]
            
            if img_istanza == img_istanza_critt:
                chiave_riga+='N'
            elif img_istanza == [[row[i] for row in img_istanza_critt[::-1]] for i in range(len(img_istanza_critt[0]))]:
                chiave_riga+='R'
            elif img_istanza == [[row[len(img_istanza_critt[0])-1-i] for row in img_istanza_critt] for i in range(len(img_istanza_critt[0]))]:
                chiave_riga+='L'
            elif img_istanza == [row[::-1] for row in img_istanza_critt[::-1]]:
                chiave_riga+='F'
            
            
            
        chiave.append(chiave_riga)
        chiave_str+=chiave_riga
    
    decrypted_str = decrypt(chiave_str, encrypted_file)
    new_file = open(plain_file, 'w', encoding='utf-8')
    new_file.write(decrypted_str)
    
    return chiave
        
if __name__ == '__main__':
    import time
    start = time.time()
    print(jigsaw('tests/test05_in.png', 'tests/test05_exp.png', 80,
                                    'tests/test05_enc.txt', 'output/test05_out.txt'))
    end = time.time()
    print(end-start)

