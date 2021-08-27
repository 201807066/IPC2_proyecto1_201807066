import os, sys

from matrizTerreno.nodoT import NodoTerreno, NodoEncabezado
from matrizTerreno.encabezado import ListaEncabezado

from graphviz import Digraph, dot

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

    def recorrerFilas(self):
        eFila = self.eFilas.primero
        print("--> Recorrido por filas")

        while eFila != None:
            aux = eFila.acceso

            print("\nFila: " + str(aux.fila))
            print("Columna: Valor")
            while aux != None:
                print(str(aux.columna) + "           "+ str(aux.valor))
                aux = aux.derecha

            eFila = eFila.siguiente

    
    def recorrerColumnas(self):
        eColumna = self.eColumnas.primero
        print("--> Recorrido por Columnas")

        while eColumna != None:
            aux = eColumna.acceso
            
            print("\nColumna: " + str(aux.columna))
            print("Fila: Valor")
            while aux != None:
                print(str(aux.fila) + "          " + str(aux.valor))
                aux = aux.abajo

            eColumna = eColumna.siguiente

    def recorrido(self, Xi, Yi, Xf, Yf):
        pass

    def imagenDot(self):
        f = Digraph(format = "png", name = "salida")
        f.attr(size = "8.5")

        eFila = self.eFilas.primero
        eColumna = self.eColumnas.primero

        cont = 0

        while eFila:
            f.node(str(cont), "Fila: " + str(eFila.id))
            cont += 1
            eFila = eFila.siguiente

        f.node(str(cont), "Null")
        cont = 0
        eFila = self.eFilas.primero
        while eFila:
            f.edge(str(cont), str(cont + 1 ))
            cont += 1
            eFila = eFila.siguiente
    

        f.render()
        os.system("salida.gv.png")
        pass

    def reporte(self, terreno):
        nombre = "graphviz"
        with open(nombre + ".dot", "w") as dot:
            dot.write('digraph Matriz{\n')
            dot.write('node[shape=box fontname=courier fillcolor="#FFEDBB" style=filled]\n')
            dot.write('subgraph cluster{\n')
            dot.write('root[label="0,0", fillcolor="#FF5733"]\n')
            dot.write('label=' + terreno+'\n')
            dot.write('bgcolor = "#33FF82"\n')
            dot.write('edge[dir="both"]\n')


            #Consigo los nodos de las filas
            eFila = self.eFilas.primero
            contF = 1
            while eFila != None:
                dot.write('F'+str(contF)+'[label="'+str(eFila.id) +'", group = 1, fillcolor = "#DDEA3A"]\n')
                contF += 1
                eFila = eFila.siguiente

            #Enlazo los nodos de las filas
            contTFS = 1
            while contTFS != contF:
                dot.write('F'+str(contTFS)+'->F'+str(contTFS+1)+'\n')
                contTFS += 1
            
            dot.write('F'+str(contTFS)+'[label="Null" fillcolor="red"]\n')

            #Conigo los nodos de las columnas
            eColumna = self.eColumnas.primero
            contC = 1
            while eColumna != None:
                dot.write('C'+str(contC)+'[label="'+str(eColumna.id) +'", group = '+str(contC+1)+ ', fillcolor = "#DDEA3A"]\n')
                contC += 1
                eColumna = eColumna.siguiente
            
            #Enlazo los nodos de las columnas
            contTCS = 1
            while contTCS != contC:
                dot.write('C'+str(contTCS)+'->C'+str(contTCS+1)+'\n')
                contTCS += 1
            
            dot.write('C'+str(contTCS)+'[label="Null" fillcolor="red"]\n')

            #Enlazamos la cabezera a las filas y columnas    
            dot.write('root -> F1\n')
            dot.write('root -> C1\n')

            eColumna = self.eColumnas.primero
            contC = 1
            dot.write('{rank=same; root')
            while eColumna != None:
                dot.write(', C'+str(contC))
                contC += 1
                eColumna = eColumna.siguiente 
            dot.write(',C'+str(contC)+'\n')
            dot.write('}\n')
            dot.write('}\n')
            dot.write('}')
        