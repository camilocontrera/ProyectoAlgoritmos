import random
import itertools
import collections
import time
from tkinter import *
from Taquin2 import *
#Clase del nodo
class Nodo:

    def __init__(self, taquin, padre=None, dir=None):
        self.taquin = taquin
        self.padre = padre
        self.dir = dir
    #end def

    @property
    def estado(self):
        return str(self)
    #end def

    @property 
    def camino(self):
        nodo, p = self, []
        while nodo:
            p.append(nodo)
            nodo = nodo.padre
        #end while
        yield from reversed(p)
    #end def
    @property
    def resuelto(self):
        return self.taquin.resuelto
    #end def

    @property
    def acciones(self):
        return self.taquin.acciones
    #end def

    def __str__(self):
        return str(self.taquin)
    #end def

#Clase de la solucion
class Solu:

    def __init__(self, inicio, t):
        self.inicio = inicio
        self.m_celdas = [[0 for j in range(t)] for i in range(t)]
    #end def
# Solucion por anchura
    def sol(self):
        print("Buscar Solucion:")
        print(self.inicio.tablero)
        global j
        cola = collections.deque([Nodo(self.inicio)])
        arbol  = set()
        arbol.add(cola[0].estado)
        while cola:
            nodo = cola.pop()
            if nodo.resuelto:
              #Valida si el nodo es el nodo de la solucion
            	z= list(nodo.camino)
            	self.final(z)
            	print("Solucion Encontrada", len(z) , " Pasos")
            	break
            #end if
              #Revisa los siguientes nodos posibles y verifica en el arbol 
            for movimiento, dir in nodo.acciones:
                hijos = Nodo(movimiento(), nodo, dir)             
                if hijos.estado not in arbol:
                    cola.appendleft(hijos)
                    arbol.add(hijos.estado)
                #enf if
            #end for
        #end while  
      #end def
      #Imprime el retroceso con los hijos y los padres para la solucion
    def final(self , p , i=1):
    	nodo = p[0]
    	p=p[1:]
    	x=nodo.taquin.convL()
    	print("PASO:",i," : ",x) 
      
    	if p:
            t = 0
            for k in range(len(self.m_celdas)):
              for j in range(len(self.m_celdas)):                
                self.m_celdas[k][j] = x[t]
                t += 1 
            #end for
            print(self.GUI())
            self.final(p, i+1)
      #end if
    	else :
         print("ACABO")
    #end def  
    #Imprime en pantalla el tablero  
    def GUI(self):
      
        p=0
        # Esquina superior izquierda - inicio del tablero
        s = "      ┌─────"
      
        for k in range(len(self.m_celdas) - 1):
            s += "┬─────"
        # end for
        s += "┐\n    "
        for k in range(len(self.m_celdas)):
            s += "  │  " + chr(ord('A') + k)
        # end for
        s += "  │\n"

        for i in range(len(self.m_celdas[0])):
            s += "├─────"
            for k in range(len(self.m_celdas)):
                s += "┼─────"
            # end for
            s += "┤\n"
            s += "│  " + chr(ord('A') + i) + "  "
            for j in range(len(self.m_celdas)):
                if (self.m_celdas[i][j] > 99):
                    s += "| "
                else:
                    s += "|  "
                #end if
                if self.m_celdas[i][j] == (len(self.m_celdas) * len(self.m_celdas)):
                    s += "  "
                else:
                    s += str(self.m_celdas[i][j])
                #end if
                if (self.m_celdas[i][j] > 9):
                    s += " "
                else:
                    s += "  "
                #end if
                p = p + 1
            # end for
            s += "|\n"
        # end for
        s += "└─────"
        for k in range(len(self.m_celdas)):
            s += "┴─────"
        # end for

        # Esquina inferior derecha - fin del tablero
        s += "┘\n"

        return s

    # end def
#Clase del tablero taquin y movimienots
class Taquin:

    def __init__(self, tablero):
        self.width = len(tablero[0]) 
        self.tablero = tablero

    @property
    def resuelto(self):

        tab = []
        sol = True
        for i in range (self.width):
	        tab.extend(self.tablero[i]);

        for j in range (len(tab)-2):
        	if (tab[j]!=(tab[j+1]-1)):
        		sol = False;
        if tab[-1] != 0 :
        	sol = False;
        return sol
#Manejo de los movimeintos de cada estado
    @property 
    def acciones(self):
        def movi(at, to):
            return lambda: self.movimiento(at, to)

        movimientos = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcciones = {'D':(i, j-1),
                      'I':(i, j+1),
                      'AB':(i-1, j),
                      'AR':(i+1, j)}

            for dir, (r, c) in direcciones.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.tablero[r][c] == 0:
                    movimiento = movi((i,j), (r,c)), dir
                    movimientos.append(movimiento)
        return movimientos
#Inicializador del tablero en aleatoreo
    def aleatorio(self):
        taquin = self
        for k in range(200):
            taquin = random.choice(taquin.acciones)[0]()
        x=taquin.convL()
        print(x)       
        self = taquin
        taquin.tablero = self.tablero
        return taquin

    def copia(self):
        tablero = []
        for fila in self.tablero:
            tablero.append([x for x in fila])
        return Taquin(tablero)

    def movimiento(self, at, to):
        copia = self.copia()
        i, j = at
        r, c = to
        copia.tablero[i][j], copia.tablero[r][c] = copia.tablero[r][c], copia.tablero[i][j]
        return copia

    def convL(self):
    	L=[]
    	for i in self.tablero:
    		L.extend(i)
    	return L 

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for i in self.tablero:
            yield from i