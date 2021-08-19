from matrizTerreno.matriz import Matriz
class Nodo():

    def __init__(self, nombre, columna, fila, inicioX, inicioY, finX, finY):
        self.nombre = nombre
        self.columna = columna
        self.fila = fila
        self.inicioX = inicioX
        self.inicioY = inicioY
        self.finX = finX
        self.finY = finY
        self.matriz = Matriz()
        #Aqui instanciamos la matriz donde va el terreno
        self.siguiente = None

    def getTerreno(self):
        return self.matriz
