from listaTerreno.nodoTerreno import Nodo

class ListaTerreno():
    
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def vacia(self):
        return self.inicio == None
    
    def agregar(self, nombre, inicioX, inicioY, finX, finY):
        terreno = Nodo(nombre, inicioX, inicioY, finX, finY)
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
            aux = aux.siguiente

    def buscarTerrenos(self, nombre):
        aux = self.inicio

        while  aux != None:
            if aux.nombre == nombre:
                print("Si se encontro: ", aux.nombre)
                return True
            aux = aux.siguiente

x = ListaTerreno()
x.agregar("hola", 3, 2, 5, 1)
x.agregar("hola32", 3, 2, 5, 1)

x.mostrarTerrenos()