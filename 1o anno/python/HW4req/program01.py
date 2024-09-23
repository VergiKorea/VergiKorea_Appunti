#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ajeje la bibliotecaria ha recentemente trovato una stanza nascosta
nella biblioteca di Keras (un posto fantastico situato in
Umkansa, il villaggio più grande delle Montagne Bianche).
Lì ha scoperto diversi libri contenenti
spartiti musicali di antiche canzoni Tarahumara e ha,
quindi, invitato un amico musicista a dare un'occhiata.
Il musicista le ha detto che è una scoperta sensazionale,
dato che gli spartiti sono scritti in notazione Tarahumara,
una popolazione ormai estinta, ma molto famosa per 
aver influenzato i musicisti della Sierra Nevada. Per poter
riprodurre i brani le suggerisce di farli tradurre in una
notazione familiare ai musicisti Umkansaniani, ultimi
discendenti dei Tarahumara, in modo che possano riprodurli.

I Tarahumara scrivevano le note usando numeri invece di lettere:
0 al posto di A, 1 al posto di B e così via, fino a 7 al posto di G. 
Le note bemolle (b) e diesis (#)
(vedi la nota 3 sotto, se non sai cosa sono bemolle e diesis)
erano seguite rispettivamente da un - e da un + 
(ad esempio, 0- significa A bemolle). 
Inoltre, ripetevano semplicemente lo stesso numero più volte 
per rappresentare la durata della nota. 
Ad esempio, 0000 significa che la nota A ha una lunghezza di 4, 
mentre 0-0-0-0- significa che la nota A bemolle ha una lunghezza di 4.

Le pause venivano scritte come spazi:
ad esempio, dodici spazi rappresentano una pausa lunga 12. 
Sia le note che le pause potevano estendersi su
diverse linee della partitura (ad esempio, iniziando dalla linea
x e continuando sulla riga x+1, x+2 e così via).
Infine, gli spartiti musicali erano scritti da destra
a sinistra e dall'alto verso il basso, mentre andare accapo 
non significava nulla in termini di partitura musicale.

Gli Umkansaniani, invece, sono soliti scrivere le note utilizzando lettere,
e ogni nota è seguita dalla sua durata (quindi, l'esempio
sopra verrebbe scritto come A4). 
Le note bemolle e diesis sono seguite rispettivamente 
da una 'b' o da una '#' (ad esempio, A bemolle è scritto Ab, 
quindi l'esempio sopra verrebbe scritto ad Ab4). 
Le pause vengono scritte utilizzando la lettera P, seguita dalla 
loro durata e non viene utilizzato alcuno spazio.
Infine, gli Umkansaniani sono abituati a leggere la musica da
sinistra a destra, scritta su una singola riga.

Poiché Ajeje sa che sei un abile programmatore, 
ti fornisce una cartella contenente la trascrizione
di tutte le canzoni di Tarahumara che ha trovato, 
organizzate in più sottocartelle e file (un brano per file).
Inoltre, ha preparato un file indice in cui ogni riga
contiene il titolo di una canzone Tarahumara (tra virgolette),
seguito da uno spazio e dal percorso del file contenente
quella canzone (tra virgolette, relativa alla cartella principale).
Vorrebbe tradurre tutte le canzoni elencate nell'indice e 
salvarle in nuovi file, ciascuno denominato con il titolo 
della canzone che contiene (con estensione .txt),
in una struttura di cartelle corrispondente a quella originale.
Inoltre, vorrebbe archiviare nella cartella principale della
struttura creata un file indice contenente su ogni riga
il titolo di una canzone (tra virgolette) e la corrispondente
lunghezza del brano, separati da uno spazio. 
Le canzoni nell'indice devono essere ordinate per lunghezza decrescente e, 
se la durata di alcuni brani è la stessa, in ordine alfabetico ascendente. 
La durata di una canzone è la somma delle durate
di tutte le note e delle pause di cui è composta.

Sarai capace di aiutare Ajeje nel tradurre le canzoni
Tarahumara in canzoni Umkansaniane?

Nota 0: di seguito viene fornita una funzione per
Umkansanizzare le canzoni di Tarahumara; 
dopo essere stata eseguita, deve restituire un dizionario 
in cui ogni chiave è il titolo di una canzone
ed il valore associato è la durata del brano.

Nota 1: l'indice delle canzoni da tradurre è il file 'index.txt'
che si trova nella directory passata nell'argomento source_root

Nota 2: l'indice delle canzoni tradotte è il file 'index.txt'
che deve essere creato nella directory passata nell'argomento target_root

Nota 3: le note bemolle e diesis sono solo versioni "alterate".
di note regolari; per esempio un A# ("A diesis") è la
versione alterata di un A, cioè una nota A che è un
mezzo tono più alto del A regolare; lo stesso vale per
note bemolle, che sono mezzo tono più basse delle note normali;
dal punto di vista dei compiti, note bemolle e diesis
devono essere trattate allo stesso modo delle note regolari 
(ad eccezione della loro notazione).

Nota 4: Usiamo la notazione inglese delle note A B C D E F G.

Nota 5: potete usare le funzioni della libreria 'os' per creare le directory necessarie
(ad esempio os.makedirs)
'''

from os import mkdir, makedirs, path

def load_file(filename: str):
    with open(filename, encoding='utf-8') as f:
        return f.read()    

def len_spartito(spartito: str):
    spartito = ''.join([f'{line[::-1]}' for line in load_file(spartito).split('\n')])
    return len(spartito.replace('+','').replace('-',''))


    
def convert(spartito: str):
    conv_dict = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '+': '#', '-': 'b', ' ': 'P'}
    spartito = load_file(spartito).split('\n')
    spartito_caratteri = []
    i=-1
    for line in spartito:
       for char in line[::-1]:
           if char in '+-':
               spartito_caratteri[i]+=conv_dict[char]
           else:
               spartito_caratteri.append(conv_dict[char])
               i+=1
    
    out_spartito, substr = '', ''
    num = 0
    for char in spartito_caratteri:
        num+=1
        if char != substr:
            out_spartito += f'{str(num)}{char}'
            substr=char
            num=0
    return out_spartito[1:]+str(num+1)
            

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    if '/' in target_root or '\\' in target_root:
        makedirs(target_root)
    else:
        mkdir(target_root)
        
    index = list(map(lambda string: list(map(lambda string: string.replace('"',''),list(string.split('" "')))),load_file(source_root+'/index.txt').split('\n')))

    if index[-1] == ['']:
        index = index[0:-1]
    
    index_out = {}
    for row in index:
        source_title, target_title = row[1], row[0]
        index_out[target_title] = len_spartito(path.join(source_root, source_title))
        
        
        if '/' in source_title:
            subdir = source_title[:source_title.index('.')-2]
            makedirs(path.join(target_root, subdir), exist_ok=True)
        else:
            subdir = ''
            
        with open(path.join(target_root, subdir, f'{target_title}.txt'),'w', encoding='utf-8') as new_file:
            new_file.write(convert(path.join(source_root, source_title)))
            
    index_out = dict(sorted(index_out.items(), key=lambda item: (-item[1], item[0])))
    index_out_str = ''
    for key in index_out:
        index_out_str=f'{index_out_str}"{key}" {str(index_out[key])}\n'
    new_file = open(path.join(target_root, 'index.txt'),'w')
    new_file.write(index_out_str)
    return index_out
    
    

if __name__ == "__main__":
    pass