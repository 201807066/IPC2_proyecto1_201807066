import os, sys

from os import startfile, system

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


    def reporte(self, terreno):
        nombre = "graphviz"
        with open(nombre + ".dot", "w") as dot:
            dot.write('digraph Matriz{\n')
            dot.write('node[shape=circle fontname=courier fillcolor="#FFEDBB" style=filled]\n')
            dot.write('subgraph cluster{\n')
            dot.write('root[label="0", fillcolor="#FF5733"]\n')
            dot.write('label=' + terreno+'\n')
            dot.write('bgcolor = "#33FF82"\n')
            dot.write('edge[dir="none"]\n')


            #1. Consigo los nodos de las filas----------------------------------------------------------------
            efila = self.eFilas.primero

            while efila != None:
                dot.write('F'+str(efila.id)+'[label="'+str(efila.id) +'", group = 1, fillcolor = "#DDEA3A"]\n')
                efila = efila.siguiente
            

            #2.Enlazo los nodos de las filas----------------------------------------------------------------
            efila = self.eFilas.primero

            while efila != None:
                if efila.siguiente != None:
                    dot.write('F'+str(efila.id)+'->F'+str(efila.siguiente.id)+'\n')
                efila = efila.siguiente
            

            #3. Consigo los nodos de las columnas----------------------------------------------------------------

            ecolumna = self.eColumnas.primero

            while ecolumna != None:
                dot.write('C'+str(ecolumna.id)+'[label="'+str(ecolumna.id) +'", group = '+str(int(ecolumna.id)+1)+ ', fillcolor = "#DDEA3A"]\n')
                ecolumna = ecolumna.siguiente
            
            #4. Enlazo los nodos de las columnas----------------------------------------------------------------

            ecolumna = self.eColumnas.primero

            while ecolumna != None:
                if ecolumna.siguiente != None:
                    dot.write('C'+str(ecolumna.id)+'->C'+str(ecolumna.siguiente.id)+'\n')
                ecolumna = ecolumna.siguiente

            #Enlazamos la cabezera a las filas y columnas---------------------------------------------------------------- 
            dot.write('root -> F1\n')
            dot.write('root -> C1\n')

            eColumna = self.eColumnas.primero
            contC = 1
            dot.write('{rank=same; root')
            while eColumna != None:
                dot.write(', C'+str(contC))
                contC += 1
                eColumna = eColumna.siguiente

            dot.write('}\n')


            #Busco los datos ingresados en la matriz recorriendo mi matriz por medio de filas----------------------------------------------------------------
            efila = self.eFilas.primero

            while efila != None:
                aux = efila.acceso
                while aux != None:
                    dot.write('datoF'+str(aux.fila)+'_C'+str(aux.columna)+'[label="'+str(aux.valor) +'", group = '+str(int(aux.columna) + 1)+' , fillcolor = "#48C9B0"]\n')
                    aux = aux.derecha
                efila = efila.siguiente

            #------------------------------------------------------------------------------------#
            # /*Ahora alineamoso fila por fila*/

            efila = self.eFilas.primero

            while efila != None:
                aux = efila.acceso
                dot.write("\n")

                dot.write('F'+str(aux.fila)+' -> datoF'+str(aux.fila)+'_C'+str(aux.columna)+'\n')
                while aux != None:
                    if aux.derecha != None:
                        dot.write('datoF'+str(aux.fila)+'_C'+str(aux.columna)+' -> datoF'+str(aux.fila)+'_C'+str(int(aux.columna)+1)+'\n')
                    aux = aux.derecha
                efila = efila.siguiente

            #---------------------------------------------------------------------------#
            #Agregamos {rank} para ordenar la fila
            efila = self.eFilas.primero

            while efila != None:
                aux = efila.acceso
                dot.write('\n')
                
                
                dot.write('{rank = same; F'+ str(efila.id))
                while aux != None:
                    dot.write(', datoF'+str(aux.fila)+'_C'+str(aux.columna))
                    
                    aux = aux.derecha
                
                dot.write('}')
                
                efila = efila.siguiente

            #-----------------------------------------------------------#
            #Enlazo y ordeno los nodos por medio de las columnas
            # /*Ahora alineamoso por columna*/

            ecolumna = self.eColumnas.primero

            while ecolumna != None:
                aux = ecolumna.acceso

                dot.write('C'+str(aux.columna)+' -> datoF'+str(aux.fila)+'_C'+str(aux.columna)+'\n')
                while aux != None:
                    if aux.abajo != None:
                        dot.write('datoF'+str(aux.fila)+'_C'+str(aux.columna)+' -> datoF'+str(int(aux.fila)+1)+'_C'+str(aux.columna)+'\n')
                    aux = aux.abajo
                ecolumna = ecolumna.siguiente

            dot.write('}\n')
            dot.write('}')
        system("dot -Tpng graphviz.dot -o graphviz.png")
        startfile("graphviz.png")