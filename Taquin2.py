import random


## ---------------------------------------------------
class Taquin2:
    def __init__(self, w):

        # Matriz dada por el tamaño ingresado en parametro W 
        self.m_celdas = [[0 for j in range(w)] for i in range(w)]

        # se llenan los valores de cada celda
        # se aumenta el valor en cada iteracion para no repetir numero
        h = 0
        for i in range(len(self.m_celdas)):
            for j in range(len(self.m_celdas)):
                self.m_celdas[i][j] = h
                h += 1
            #end for
        #end for

        # Se inicializan indices menos 1, ya que el indice maneja el 0
        i = len(self.m_celdas)-1
        j = len(self.m_celdas)-1

        # Movimiento de las casillas
        for k in range(100):
          
          # Se usa N. entre el 1-4 para identificar la direccion del movimiento
          numero = random.randint(1,4)
          movimiento = 0
          aux = self.m_celdas[i][j]
          aux2 = 0
#
          # 1 se mueve a la derecha
          if(numero == 1 and len(self.m_celdas)!=j+1):   
             # cantidad de celdas en las que se movera
            movimiento = random.randint(1,(len(self.m_celdas))-j-1)
            aux2 = j
            
            for h in range(movimiento):              
              # Se ajusta la matriz segun el movimiento
              self.m_celdas[i][aux2] = self.m_celdas[i][aux2+1]
              aux2 += 1
            #end for
            j = aux2
          #end if

          # 2 se mueve a la izquierda 
          if(numero == 2 and j!=0):    
             # cantidad de celdas en las que se movera
            movimiento = random.randint(1,j)
            aux2 = j
            
            for h in range(movimiento):              
              # Se ajusta la matriz segun el movimiento
              self.m_celdas[i][aux2] = self.m_celdas[i][aux2-1]
              aux2 -= 1
            #end for
            j = aux2
          #end if  
            
          # 3 se mueve a arriba
          if(numero == 3 and i!=0):   
             # cantidad de celdas en las que se movera
            movimiento = random.randint(1,i)
            aux2 = i
            
            for h in range(movimiento):
              # Se ajusta la matriz segun el movimiento
              self.m_celdas[aux2][j] = self.m_celdas[aux2-1][j]
              aux2 -= 1
            #end for
            i = aux2
          #end if  

          # 4 se mueve a abajo
          if(numero == 4 and len(self.m_celdas)!=i+1):   

            # cantidad de celdas en las que se movera
            movimiento = random.randint(1,(len(self.m_celdas))-i-1)
            aux2 = i
            
            for h in range(movimiento):
              # Se ajusta la matriz segun el movimiento
              self.m_celdas[aux2][j] = self.m_celdas[aux2+1][j]
              aux2 += 1
            #end for
            i = aux2
          #end if  
          self.m_celdas[i][j] = aux
          
        #end for
    # end def

## ---------------------------------------------------
      
    # Se define construccion del tablero GUI
    def __str__(self):
      
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

    def resuelto(self):
          
      return False
    #end def

    def jugar(self):
     
      while self.resuelto():        
        h = 0
        for i in range(len(self.m_celdas)):
          for j in range(len(self.m_celdas)):
              self.m_celdas[i][j] = h
              h += 1
            #end for
        #end for
        print(self.GUI())
      #end for
    #end def

          # Se define construccion del tablero GUI
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
  
# end class

## eof - Taquin2.py
