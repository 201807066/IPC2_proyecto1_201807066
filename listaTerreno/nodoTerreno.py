class Nodo():

    def __init__(self, nombre, inicioX, inicioY, finX, finY):
        self.nombre = nombre
        self.inicioX = inicioX
        self.inicioY = inicioY
        self.finX = finX
        self.finY = finY
        #Aqui instanciamos la matriz donde va el terreno
        self.siguiente = None
        
