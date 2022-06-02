import sys
from Taquin2 import *
from TaquinFinalFinal import *

## ========================================================================
# Proyecto Taquin
# Analisis de algoritmos
# Pontificia Universidad Javeriana
## ========================================================================

from tkinter import * 
import time

global taquin , t 


print("---------------------------------------------Taquin--------------------------")
#Dato de entrada de tamaño del tablero
print("¿Que tamaño desea el tablero de juego?")
tam = input()
t=int(tam)

n = []
x=1
# Resultado esperado
for i in range(t):
  numeros = []
  for j in range(t):   
    if i==t-1 and j==t-1:
      numeros.append(0)
    numeros.append(x)
    x=x+1
  #end for
  if i==t-1:
    numeros.pop()
  n.append(numeros)
#end for


tablero=n

print("VALORES",n)

#inicializacion
taquin = Taquin(tablero)
s = Solu(taquin,t)

taquin = taquin.aleatorio()
s =Solu(taquin,t)
s.sol()