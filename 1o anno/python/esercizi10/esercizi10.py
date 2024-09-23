# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato


def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Definire una funzione che crea un'immagine di dimensione 600x600 (pixels), 
# interamente bianca.
# La funzione prende i seguenti parametri:
#  - points: una lista di coppie, che rappresentano dei punti
#            all'interno dell'immagine. I punti sono rappresentati con coordinate 
#            (x, y), dove (0, 0) è l'angolo in basso a sinistra dell'immagine
#  - d: la dimensione dei punti. Ad esempio, se d=5, i punti sono dei quadrati 5x5.
#       Si può assumere che d sia sempre dispari
#  - c: una tupla rappresentante un colore
#  - outfile: il nome del file su cui scrivere l'immagine
#
# La funzione deve disegnare i punti, e le linee che connettono due punti consecutivi 
# (l'ultimo punto della lista verrà connesso col primo).
# Ad esempio, se:
#  - points = [(10, 30), (14, 99), (0, 2)]
#  - d = 5
#  - c = (0, 0, 0)
#
# La funzione disegnare un punto in ognuna delle coordinate specificate in points. Il 
# punto sarà un quadrato di lato 5x5 (pixels), centrato nel punto specificato nelle coordinate
# e con colore c. Dopodichè, la funzione disegnerà una linea 
# che connette il punto (10, 30) al punto (14, 99), e una linea che connette il punto
# (14, 99) al punto (0, 2). Il colore delle linee è lo stesso dei punti.
#
# Per disegnare una linea fra un generico punto (x1, y1) e un punto (x2, y2), bisogna colorare tutti i punti 
# (x, y), tali che la distanza fra (x1, y1) e (x, y), sommata alla distanza fra (x, y) e (x2, y2), è uguale
# alla distanza fra (x1, y1) e (x2, y2). Per calcolare la distanza, usare la formula 
# distanza = sqrt((x1-x2)**2 + (y1-y2)**2). Fare attenzione alla conversione da float a interi e viceversa.
# (L'eguaglianza dotrebbe essere non un "uguale" ma un "quasi uguale")
#
# Vedere l'esempio test_1.png.
#
# Provare a sviluppare una soluzione ottimizzata in cui si evita di scandire tutti i pixel dell'immagine
# per disegnare le linee.
def img_draw(points: List[Tuple[int]], d: int, c: Tuple[int], outfile: str):
    
    def distanza(x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    img_mat = [[(255,255,255) for _ in range(600)]for _ in range(600)]
    for y in reversed(range(0, 600)):
        for x in range(600):
            for i, (x1,y1) in enumerate(points):
                if i<len(points)-1:
                    dist_2points = distanza(*points[i], *points[i+1])
                    if (y-y1 in range(-d//2,d//2+1) and x-x1 in range(-d//2,d//2+1)) or dist_2points-.005 <= distanza(*points[i],x,y)+distanza(x,y,*points[i+1]) <= dist_2points+.005:
                        img_mat[-y][x] = c
                else:
                    dist_2points = distanza(*points[i], *points[0])
                    if (y-y1 in range(-d//2,d//2+1) and x-x1 in range(-d//2,d//2+1)) or dist_2points-.005 <= distanza(*points[i],x,y)+distanza(x,y,*points[0]) <= dist_2points+.005:
                        img_mat[-y][x] = c
    images.save(img_mat, outfile)
                    
                    

# Implementare una funzione che, sfruttando la funzione sviluppata precedentemente, disegni un quadrato
# da salvare sul file outfile.
def square(outfile: str):
    img_draw([(200,200),(400,200),(400,400),(200,400)], 15, (0,0,0), outfile)

# Implementare una funzione che, sfruttando la funzione sviluppata precedentemente, disegni una stella a 5 punte,
# da salvare sul file outfile.
def five_point_star(outfile: str):
    img_draw([(300,400),(400,150),(150,300),(450,300),(200,150)], 15, (0,0,0), outfile)

img_draw([(100, 320), (141, 99), (50, 50)], 15, (0, 0, 0), "test_1.png")
img_draw([(0, 320), (141, 99), (500, 50), (14, 26), (500, 12), (300, 152)], 15, (0, 255, 0), "test_2.png")
square("square.png")
five_point_star("fpstar.png")

