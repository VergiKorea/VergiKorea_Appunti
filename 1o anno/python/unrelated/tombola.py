# -*- coding: utf-8 -*-
import random
from tabulate import tabulate
from tkinter import *

class Banco:
    def __init__(self):
        self.num_estrarre = banco = [i for i in range(0,100)]
    def getNums(self):
        return self.num_estrarre
    def estrai(self):
        i=0
        while i==0:
            num = random.randint(0,99)
            if num in self.num_estrarre:
                i=1
                self.num_estrarre.remove(num)
                return num
    def getLen(self):
        return len(self.num_estrarre)

class Cartella:
    def __init__(self):
        self.cartella_griglia = []
        while len(self.cartella_griglia)<3:
            rand = bin(random.randint(1,511))
            if rand.count('1') == 5:
                rand = [*rand][2:]
                if len(rand) < 9:
                    rand = ['0']*(9-len(rand))+rand
                row = []
                for i in range(len(rand)):
                    if rand[i] == '0':
                        row.append(' ')
                    elif rand[i] == '1':
                        if i == 0:
                            row.append(random.randint(0,9))
                        elif i == 8:
                            row.append(random.randint(80,90))
                        else:
                            row.append(random.randint(i*10,i*10+9))
                self.cartella_griglia.append(row)
        self.cartella_griglia = tabulate(self.cartella_griglia)
    def getCartella(self):
        finestra_cartella = Tk()
        finestra_cartella.title('Cartella')
        finestra_cartella.geometry('500x300')
        label = Label(text = self.cartella_griglia)
        label.pack()
        mainloop()
                
                
banco1 = Banco()
cartella1 = Cartella()
cartella1.getCartella()

        
        
