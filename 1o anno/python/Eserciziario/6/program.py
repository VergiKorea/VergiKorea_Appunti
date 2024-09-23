import albero

def es6(percorsi):
   '''
   Si definisca la funzione es6(testo) ricorsiva (o che fa uso di funzioni o 
   metodi ricorsive/i) che:
   - riceve come argomento:
      - un insieme di stringhe che hanno la proprietà che ciascuna è stata 
      ottenuta a partire dallo stesso albero binario
         (in cui ciascun nodo contiene un solo carattere), risalendo da ciascuna 
         foglia fino alla radice e concatenando
         i valori dei nodi
         NOTA l'albero è localmente ordinato da sinistra a destra, ovvero:
         - ciascun figlio sinistro contiene un carattere minore di quello del padre
         - ciascun figlio destro contiene un carattere maggiore di quello del padre
   - ricostruisce l'albero originale e lo torna come risultato

   Esempio: se l'albero da ricostruire è
                     i     
                     |
             |-----------------|               
             h                 m 
             |                 |   
         |--------|        |------|   
         c        j        k      p
         |        |               |
      |-----|  |-----|         |-----|
      a     f  g     k         m     q    

   L'insieme di stringhe è
      { 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }

   ATTENZIONE: è VIETATO usare i metodi della classe AlberoBinario

   '''
   # inserisci qui il tuo codice
   def ric_albero(string):
        subAlbero = albero.AlberoBinario(string[-1])
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        if len(string) == 1:
            return subAlbero
        elif alfabeto.index(string[-1]) > alfabeto.index(string[-2]):
            subAlbero.sx = ric_albero(string[:-1])
        elif alfabeto.index(string[-1]) < alfabeto.index(string[-2]):
            subAlbero.dx = ric_albero(string[:-1])
        return subAlbero
   
   def unisci_alberi(lista_alberi):
       albero_out = albero.AlberoBinario(lista_alberi[0].valore)
       for tree in lista_alberi:
           if tree.sx:
               albero_out.sx = unisci_alberi([tree.sx for tree in lista_alberi if tree.sx])
           if tree.dx:
               albero_out.dx = unisci_alberi([tree.dx for tree in lista_alberi if tree.dx])
       return albero_out
       
   
   percorsi = list(percorsi)
   albero1 = albero.AlberoBinario(percorsi[0][-1])
   lista_alberi = []
   for el in percorsi:
       tree = ric_albero(el)
       lista_alberi.append(tree)
   
   return unisci_alberi(lista_alberi)


print(es6({ 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }))




