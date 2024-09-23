

def es16(s, k):
    '''
    Es 5: 3 punti
    progettare la funzione es16(s,k) che: 
    - riceve  in input una stringa s di caratteri   ed un intero k 
    - costruisce la lista con  le diverse sottostringhe  di s  in cui compaiono 
      esattamente k caratteri distinti
    - restituisce la lista delle sottostringhe dopo averla ordinata  per
      lunghezze decrescenti e, a parita' di lunghezza, in ordine lessicografico
   Nota che la lista non deve contenere duplicati.
   Si ricorda che una sottostringa di s e' quello che si ottiene da s eliminando 0 o piu' 
   caratteri iniziali  e 0 o piu' caratteri finali.
   ESEMPI: 
   con  s='aabbb' e k=1 la funzione restituisce la lista ['bbb', 'aa', 'bb', 'a', 'b']
   cons s='bcafedg' e k=3 la funzione restituisce la lista ['afe', 'bca', 'caf', 'edg', 'fed']
   cons s='ccaabbdd' e k=3 la funzione restituisce la lista 
        ['aabbdd', 'ccaabb', 'aabbd', 'abbdd', 'caabb', 'ccaab', 'abbd', 'caab']
    '''
    
    subs = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    out = []
    for string in subs:
        set_s = set(string)
        if len(set_s) == k:
            out.append(string)
    out = sorted(list(set(out)))
    return sorted(out, key=len, reverse = True)
    



print(es16('ccaabbdd', 3))
    
