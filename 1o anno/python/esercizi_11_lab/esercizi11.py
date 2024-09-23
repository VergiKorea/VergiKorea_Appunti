# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import json
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


# Helper functions
def load_json(filename):
    with open(filename) as f:
        return json.load(f)


# Helper functions
def save_json(filename, js):
    with open(filename, 'w') as f:
        json.dump(js, f, indent=2)

# Questo esercizio differisce dai precedenti perchè implementeremo sia funzione
# che classi.
# Implementare la classe Shape che ha un metodo area2() che calcola l'area
# al quadrato chiamando il metodo area(), e la funzione color() che ritorna una
# una tuple (g,g,g) dove g è un valore tra 0 e 1 passato al construttore come
# un parametro di nome gray.
# Implementare la classe Circle, derivata da Shape, che ha un costruttore che
# prende il raggio radius e il colore gray, e implementa il metodo area().
# Implementare la classe Polygon, derivata da Shape, che ha un metodo sides()
# che ritorna il numero di lati.
# Implementare la classe Square, derivata da Polygon, che ha un costruttore che
# prende il lato side e il colore gray e implementa area() e sides().
# Implementare la classe Triangle, derivata da Polygon, che ha un costruttore
# che prende il lato side e il colore gray e implementa area() e sides().
# L'area e sqrt(3)/4 l^2.
# In tutti i construttori i parametri sono opzionali e inizializzati a 1.
# Per ogni classe, aggiungere il metodo `repr` che stampa la chiamata al
# construttore che ha creato quell'oggetto. Ad esempio, Circle.repr(self),
# stampa 'Circle(radius=..., gray=...)' con i valori relativi; e il metodo
# __eq__ che verifica se due oggetti della stessa classe sono uguali.


class Shape:
    def __init__(self, gray=1, **kwargs):
        assert 0<=gray<=1
        self.gray = gray
        
    def area2(self):
        return self.area()**2
    
    def area(self):
        raise NotImplementedError
    
    def color(self):
        return (self.gray, self.gray, self.gray)
    
    def __repr__(self):
        return f'{type(self).__name__}({", ".join((k, str(v))) for k, v in vars(self)})'
    def __eq__(self,o):
        return isinstance(self, type(o))

class Circle(Shape):
    def __init__(self, gray=1, radius=1, **kwargs):
        self.radius = radius
        super().__init__(gray=gray)
    def area(self):
        return (self.radius**2)*math.pi


class Polygon(Shape):
    def __init__(self, gray=1, **kwargs):
        super().__init__(gray=gray)
    def sides(self):
        raise NotImplementedError
        
class Square(Polygon):
    def __init__(self, gray=1, side=1, **kwargs):
        self.side = side
        super().__init__(gray=gray)
    def area(self):
        return self.side**2
    def sides(self):
        return 4
    

class Triangle(Polygon):
    def __init__(self, gray=1, side=1, **kwargs):
        self.side = side
        super().__init__(gray=gray)
    def area(self):
        return (math.sqrt(3)/4)*self.side**2
    def sides(self):
        return 3


# Implementare una funzione che prende una shape e ne calcola l'area al quadrato.
def get_area2(shape: Shape):
    return shape.area2()


# Implementare una funzione che prende una lista di shapes e ne calcola 
# la somma delle aree.
def get_area(shapes: List[Shape]):
    return sum([shape.area() for shape in shapes])


# Implementare una funzione che prende una lista di shapes e ne calcola il
# numero do lati, saltando le shapes che non hanno lati, come il Circle.
def get_sides(shapes: List[Shape]):
    return sum([shape.sides() for shape in shapes if isinstance(shape, Polygon)])


# Implementare una funzione che conta il numero di Square in una lista di Shape.
def count_square(shapes: List[Shape]):
    i=0
    for shape in shapes:
        if isinstance(shape, Square): i+=1
    return i


# Implementare una funzione che conta il numero di Polygon in una lista di Shape.
def count_poly(shapes: List[Shape]):
    i=0
    for shape in shapes:
        if isinstance(shape, Polygon): i+=1
    return i


# Implementare una funzione che carica una file JSON e ritorna una lista di
# Shapes. Il file JSON è formato da una lista di dizionari che hanno come
# chiavi i parametri dei construttori e una chiave aggiuntiva '__type__'
# con il nome della classe. Per caricare un json usate load_json(filename).
# Suggerimento: usare **kwargs per semplicità.
def from_json(filename: str) -> List[Shape]:
    list_output = []
    list_attr = load_json(filename)
    for obj in list_attr:
        if obj['__type__'] == 'Square':
            list_output.append(Square(obj['gray'], obj['side']))
        elif obj['__type__'] == 'Circle':
            list_output.append(Circle(obj['gray'], obj['radius']))
        elif obj['__type__'] == 'Triangle':
            list_output.append(Triangle(obj['side']))
    return list_output


# Implementare una funzione che converte una lista di Shapes in una lista
# di dizionari che hanno come chiavi i parametri dei construttori e la chiave
# __type__ descritta sopra.
# Per implementarlo, si può usare isinstance() per fare ogni classe separatemente,
# oppure usare vars() per elecare le variabili di ogni classe e type().__name__
# per il nome del tipo.
def to_dict(shapes: List[Shape]) -> List[dict]:
    list_output = []
    for shape in shapes:
        list_output.append({**{'__type__': type(shape).__name__}, **shape.__dict__})
    return list_output

# Implementare una funzione che converte una lista di Shapes in una lista
# di dizionari che hanno come chiavi i parametri dei construttori e la chiave
# __type__ descritta sopra. Per salvare un Json usate save_json(filename, js).
# Basta salvare i dizionari scritti da to_dict().
def to_json(filename: str, shapes: List[Shape]) -> None:
    list_dict = to_dict(shapes)
    save_json(filename, list_dict)


# Test funzioni
c = Circle(0.5, 2)
print(c.area())
print(c.area2())
print(c.color())
s = Square(0.5, 3)
print(s.area())
print(s.area2())
print(s.sides())
t = Triangle(0.5, 3)
print(t.area())
print(t.area2())
print(t.sides())

check_test(get_area2, 1, Square(side=1))
check_test(get_area, 2, [Square(side=1), Square(side=1)])
check_test(get_area, 4.574605355482013, [Square(
    side=1), Circle(radius=1), Triangle(side=1)])
check_test(get_sides, 7, [Square(side=1), Circle(radius=1), Triangle(side=1)])
check_test(count_square, 1, [Square(side=1),
           Circle(radius=1), Triangle(side=1)])
check_test(count_poly, 2, [Square(side=1), Circle(radius=1), Triangle(side=1)])
check_test(from_json, [Square(side=1, gray=0), Circle(
    radius=1), Triangle(side=1)], 'shapes.json')
check_test(to_dict, [{'__type__': 'Square', 'side': 1, 'gray': 0}, {'__type__': 'Circle', 'radius': 1, 'gray': 1}, {
           '__type__': 'Triangle', 'side': 1, 'gray': 1}], [Square(side=1, gray=0), Circle(radius=1), Triangle(side=1)])
check_test(to_json, None, 'shapes_out.json', [
           Square(side=1, gray=0), Circle(radius=1), Triangle(side=1)])
