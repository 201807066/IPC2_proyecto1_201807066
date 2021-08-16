from nodoT import NodoTerreno, NodoEncabezado

#Se crea las listas doblemente enlazadas el
class ListaEncabezado():
    def __init__(self, primero=None):
        self.primero = primero

    def vacia(self):
        return self.primero == None

    # nuevo hace refrenecia a un nuevo nodo de las listas de encabezados
    def setEncabezado(self, nuevo):
        if self.vacia():
            self.primero = nuevo
        #Ordenamos el nodo de la lista doblemente enlazada 
        elif nuevo.id < self.primero.id:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo  
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente != None:
                if nuevo.id < aux.siguiente.id:
                    nuevo.siguiente = aux.siguiente
                    aux.siguiente.anterior = nuevo
                    nuevo.anterior = aux
                    aux.siguiente = nuevo
                    break
                aux = aux.siguiente
            if aux.siguiente == None:
                aux.siguiente = nuevo
                nuevo.anterior = aux

                

    def getEncabezado(self, id):
        aux = self.primero

        while aux != None:
            if aux.id == id:
                return aux
            aux = aux.siguiente
        return None
