

'''
    Es 9: 3 punti
    Si definisca la funzione es9(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
      qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
      della cartella da eventuali file di tipo .txt.
      La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
      una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
      sottocartella.
      Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
      alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
      crescente rispetto alla prima componente.
      File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempio: con es9('Informatica/Software') viene restituita la lista:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''

import os

def es9(pathDir):
    subDirs = []
    if os.path.isfile(pathDir):
        if pathDir[-4:] == '.txt':
            return os.path.getsize(pathDir)
        else:
            return 0
    if os.path.isdir(pathDir):
        txt_bytes = [os.path.basename(pathDir), 0]
        for file in os.listdir(pathDir):
            if os.path.isfile(os.path.join(pathDir, file)):
                txt_bytes[1]+=es9(os.path.join(pathDir, file))
            if os.path.isdir(os.path.join(pathDir, file)):
                subDirs.extend(es9(os.path.join(pathDir, file)))
        subDirs.append(tuple(txt_bytes))
        return sorted(subDirs, key = lambda el: (-el[1], el[0]))



print(es9('C:/Users/Marius/Desktop/uni/python/Eserciziario/9/Informatica'))
    
        
