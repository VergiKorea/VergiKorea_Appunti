'''
    Es 11: 3 punti
progettare la funzione es11(ftesto) che, preso in input 
l'indirizzo di un file di testo restituisce un dizionario avente per chiavi delle stringhe 
ed attributo liste di  stringhe.
Il file di testo contiene stringhe distinte di caratteri, si guardi 
ad esempio il file f9.txt. 
Le chiavi del dizionario si ottengono dalle stringhe presenti nel file dopo aver 
eliminato da queste le vocali ed aver riordinato lessicograficamente i caratteri rimanenti 
(ad esempio dalla stringa 'angelo' si ottine la chiave 'gln').
Attributo della chiave e' la lista contenente le stringhe del file che l'hanno generata. 
Nota che  stringhe diverse possono generare una stessa chiave come nel caso 
di  'casa', 'caso' e 'cose'
Le stringhe nella lista devono comparire  ordinate per lunghezza decrescente, a parita' 
di lunghezza, lessicograficamente.

Ad Esempio, per il file di testo f10.txt  la funzione restituisce  il dizionario:
{'prt': ['parto', 'porta'], 
'r': ['era', 'ora'], 
'pr': ['arpia', 'arpa'], 
'cs': ['casa', 'cosa'], 
'fll': ['follia', 'fallo', 'folla'], 
'rt': ['otre', 'tre'], 
'lp': ['piolo', 'polo']
}
'''

def es11(ftesto):
    def chiave(string):
        vocali = 'aeiou'
        out = []
        for char in string:
            if char not in vocali:
                out.append(char)
        return ''.join(sorted(out))
        
    with open(ftesto, encoding='utf-8') as f:
        fstr = f.read()
    fstr = fstr.replace('\n',' ').split()
    out_dict = {}
    for string in fstr:
        key = chiave(string)
        if key not in out_dict:
            out_dict[key] = [string]
        else:
            out_dict[key].append(string)
    for key in out_dict:
        out_dict[key] = sorted(sorted(out_dict[key]), key=len, reverse = True)
    return out_dict

print(es11('ft10a.txt'))
