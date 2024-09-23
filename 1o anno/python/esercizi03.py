from typing import Any, Callable, List


# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')


################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che restituisce una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return 'Ciao '+name


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    i=0
    f=0
    isTrue1 = True
    isTrue2 = True
    for index in range(len(string)):
        if string[index] not in ' ':
            isTrue1 = False
        if isTrue1 == True:
            i+=1
        if string[::-1][index] not in ' ':
            isTrue2 = False
        if isTrue2 == True:
            f+=1
    return string[i:-(f)]

# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    output = []
    i=0
    while i<len(string):
        if string[i] in characters[0] and len(string[i:])>=len(characters):
            if string[i:i+len(characters)] in characters:
                output.append(string[:i])
                string = string[:i+len(characters)]
                i=-1
        i+=1
    if output == []:
        output = [string]
    return output


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    i=0
    while i+len(find)<=len(string):
        if string[i:i+len(find)] in find:
            string = f'{string[:i]}{replace}{string[i+len(find):]}'
        i+=1
    return string

# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    if decrypt == False:
        return string
    output = ''
    for char in string:
        if char in ' ':
            output=f'{output}{char}'
        elif (char.isupper()==True and ord(char)-offset>90) or (char.isupper()==False and ord(char)-offset>122):
            output=f'{output}{chr(ord(char)-offset-26)}'
        elif (char.isupper()==True and ord(char)-offset<65) or (char.isupper()==False and ord(char)-offset<97):
            output=f'{output}{chr(ord(char)-offset+26)}'
        else:
            output=f'{output}{chr(ord(char)-offset)}'
    return output

# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 17, False)
print_test(caesar_cypher, 'tzrf gzggf', 17, True)

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    somma = 0
    for n in elements: somma += n*n
    return somma

# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    if len(elements)>0:
        return max(elements)


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    output = []
    for el in elements:
        if el not in output:
            output.append(el)
    return output


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    return elements[::-1]


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e restituisce una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    output = []
    for el in elements:
        if isinstance(el, list) == True:
            output.extend(flatten_list(el))
        else:
            output.append(el)
    return output

# Test funzioni
print_test(sum_squares, [1, 2, 3])
print_test(max_element, [1, 2, 3, -1, -2])
print_test(max_element, [-1, -2])
print_test(max_element, [])
print_test(remove_duplicates, [1, 2, 3, 2, 3])
print_test(reverse_list, [1, 2, 3])
print_test(flatten_list, [1, [2, 3]])
print_test(flatten_list, [1, [2, [3, 4]]])
