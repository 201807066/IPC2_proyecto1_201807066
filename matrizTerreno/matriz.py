from nodoT import NodoTerreno, NodoEncabezado
from encabezado import ListaEncabezado

class Matriz():
    def __init__(self):
        self.eFilas = ListaEncabezado()
        self.eColumnas = ListaEncabezado()

    def insertar(self, fila, columna, valor):
        nuevo = NodoTerreno(fila, columna, valor)

        #Inserción de encabezado por fila
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = NodoEncabezado(fila)
            eFila.acceso = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            #Aqui se ordena el nodo de una fila por medio de la columna
            if nuevo.columna < eFila.acceso.columna:
                nuevo.derecha = eFila.acceso
                eFila.acceso.izquierda = nuevo
                eFila.acceso = nuevo
            else:
                aux = eFila.acceso
                while aux.derecha != None:
                    if nuevo.columna < aux.derecha.columna:
                        nuevo.derecha = aux.derecha
                        aux.derecha.izquierda = nuevo
                        nuevo.izquierda = aux
                        aux.derecha = nuevo
                        break
                    aux = aux.derecha
                if aux.derecha == None:
                    aux.derecha = nuevo
                    nuevo.izquierda = aux

        #Inserción de encabezado por columna
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = NodoEncabezado(columna)
            eColumna.acceso = nuevo
            self.eColumnas.setEncabezado(eColumna)
        else:
            # Aqui se ordenada el nodo de una columna por medio de la fila
            if nuevo.fila < eColumna.acceso.fila:
                nuevo.abajo = eColumna.acceso
                eColumna.acceso.arriba = nuevo
                eColumna.acceso = nuevo
            else:
                aux = eColumna.acceso
                while  aux.abajo != None:
                    if nuevo.fila < aux.abajo.fila:
                        nuevo.abajo = aux.abajo
                        aux.abajo.arriba = nuevo
                        nuevo.arriba = aux
                        aux.abajo = nuevo
                        break
                    aux = aux.abajo 
                if aux.abajo == None:
                    aux.abajo = nuevo
                    nuevo.arriba = aux
            
m = Matriz()
m.insertar(1,1,32)
m.insertar(1,2,100)