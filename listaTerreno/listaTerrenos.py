from listaTerreno.nodoTerreno import Nodo

class ListaTerreno():
    
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def vacia(self):
        return self.inicio == None
    
    def agregarTerreno(self, nombre, columna, fila, inicioX, inicioY, finX, finY):
        terreno = Nodo(nombre, columna, fila, inicioX, inicioY, finX, finY)
        self.size += 1
        
        if self.vacia():
            self.inicio = self.fin = terreno
        else:
            aux = self.fin
            self.fin = aux.siguiente = terreno
        
    def mostrarTerrenos(self):
        aux = self.inicio

        while aux != None:
            print("Nombre: ", aux.nombre)
            print("Dimensiones del terreno: ", aux.columna, "x", aux.fila)
            print("Coordenada de Inicio --> Fila/Columna: ", "(", aux.inicioX, ",", aux.inicioY , ")")
            print("Coordenada de Fin --> Fila/Columna: ", "(", aux.finX, ",", aux.finY , ")")
            print("\n")
            aux = aux.siguiente

    def buscarTerrenos(self, nombre):
        aux = self.inicio

        while  aux != None:
            if aux.nombre == nombre:
                print("Si se encontro: ", aux.nombre)
                return True
            aux = aux.siguiente
