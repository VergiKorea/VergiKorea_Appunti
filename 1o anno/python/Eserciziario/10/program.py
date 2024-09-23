  
    

'''
    Es 10: 3 punti
progettare la funzione es10(ftesto,k) che, presi in input 
l'indirizzo di un file di testo ed un intero k, restituisce una stringa di caratteri lunga k.
Il file di testo contiene stringhe di diversa lunghezza 
(una per riga ed ogni riga termina con '\n'), si guardi 
ad esempio il file f9.txt. 
I k caratteri della stringa restituita  dalla funzione si ottiengono
considerando le stringhe lunghe k presenti nel file di testo. 
L'i-mo carattere della stringa sara' il carattere che compare con maggior 
frequenza come i-mo carattere delle stringhe lunghe k nel file di testo (in caso 
di parita' di occorrenze viene scelto il carattere che precede 
gli altri lessicograficamente). 
Nel caso il file di testo non contenga parole lunghe k allora viene restituita 
la stringa vuota.  
Ad Esempio, per il file di testo f9.txt e k=3 la funzione restituisce  la stringa 'are' a 
seguito della presenza in f9.txt delle seguenti 4 stringhe lunghe 3:
tre
due
amo
ora 
'''
def es10(ftesto,k):
    with open(ftesto, encoding='utf-8') as f:
        fstr = f.read()
    fstr = list(filter(lambda el: len(el)==k, fstr.split('\n')))
    out = ''
    if len(fstr) == 0:
        return out
    else:
        for i in range(len(fstr[0])):
            f = sorted([string[i] for string in fstr])
            f_count = 0
            f_count_char = []
            for char in f:
                if f.count(char)>f_count:
                    f_count = f.count(char)
                    f_count_char = [char]
                elif f.count(char)==f_count:
                    f_count_char.append(char)
            if len(f_count_char) == 1:
                out+=f_count_char[0]
            else:
                out+=sorted(f_count_char)[0]
                    
            
    return out

print(es10('ft9.txt', 3))
    
