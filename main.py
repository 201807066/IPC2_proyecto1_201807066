import os, sys, time
from listaTerreno.listaTerrenos import ListaTerreno
import xml.etree.ElementTree as ET

ListaTerreno = ListaTerreno()

def cls():
    os.system("cls")

def cargar(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        print("Terreno: ", elemento.attrib["nombre"], "ha sido insertado")
        #Almaceno el nombre del nodo
        nombre = elemento.attrib["nombre"]

        #Almaceno la dimension del nodo mxn
        for dimension in elemento.iter("dimension"):
            print("Dimensiones del terreno")
            for columna in dimension.iter("m"):
                tamM = columna.text
                print("Dimensiones de las filas: ", tamM)
            for fila in dimension.iter("n"):
                tamN = fila.text
                print("Dimensiones de las columnas: ", tamN)

        #Almaceno la posicion de inicio del nodo
        for subelemento in elemento.iter("posicioninicio"):
            print("Posicion de inicio")
            for inicioX in subelemento.iter("x"):
                xInicio = inicioX.text
                print("Corrdenada X:", xInicio)
            for inicioY in subelemento.iter("y"):
                yInicio = inicioY.text
                print("Corrdenada Y:", yInicio)

        #Almaceno la posicion de fin del nodo
        for subelemento in elemento.iter("posicionfin"):
            print("Posicion de finalizacion")
            for finx in subelemento.iter("x"):
                xFin = finx.text
                print("Corrdenada X:", xFin)
            for finy in subelemento.iter("y"):
                yFin = finy.text
                print("Corrdenada Y:", yFin)

                ListaTerreno.agregarTerreno(nombre, tamM, tamN, xInicio , yInicio, xFin, yFin)

        #Agregamos la matriz a la lista de Terrenos
        for subelemento in elemento.iter("posicion"):
            print("x:", subelemento.attrib['x'], " y:",  subelemento.attrib['y'], " dato:", subelemento.text)
            terreno = ListaTerreno.buscarTerreno(elemento.attrib["nombre"])
            terreno.matriz.insertar(subelemento.attrib['x'], subelemento.attrib['y'], subelemento.text)
            



def menu():
    cls()
    while True:
        print("""\n          ***   Men?? Principal   ***\n          
        1. Cargar archivo
        2. Mostrar Terrenos
        3. Generar gr??fica
        4. Mostrar datos del estudiante
        5. Salir""")

        opc = input("\nOpci??n a realizar: ")

        if opc == "1": 
            cls()
            print("   --- Cargar Archivo ---   \n")
            try:
                archivo = input("Ingrese nombre del archivo '.xml': ") 
                Filename = 'D:/Users/Yayan/OneDrive/Escritorio/Desarrollo/Python/IPC2/Proyecto1/extras/' + archivo + '.xml'
                # Filename = 'D:/Users/Yayan/OneDrive/Escritorio/Desarrollo/Python/IPC2/Proyecto1/extras/test.xml'
                cargar(Filename)
                input("\n--> Archivo cargado exitosamente...")
                cls()
                menu()
            except:
                input("El nombre del archivo no se ha encontrado...")
                menu()
            break
        elif opc == "2":
            cls()
            input("--> Listado de Terrenos agregados: \n")
            ListaTerreno.mostrarTerrenos()
            input()
            menu()
            break
        elif opc == "3":
            cls()
            nombre = input("Ingrese el nombre del terreno: \n")
            # nombre = "terreno1"
            terreno = ListaTerreno.buscarTerreno(nombre)

            if terreno == None:
                input("Terreno no ingresado aun...")
            else:
                print("Terreno: ", terreno.nombre)
                terreno.matriz.recorrerFilas()
                print("Imagen generada...\n")
                terreno.matriz.reporte(nombre)
                input("Presione para continuar")
            
            menu()
            break
        elif opc == "4":
            cls()      
            print("\n           Datos del estudiante            \n")     
            print("**********************************************")
            print("****                IPC 2                 ****")
            print("****              Secci??n D               ****")
            print("****                                      ****")
            print("****            Ciencias y sistemas       ****")
            print("****      Brayan Andr??s Cholotio Tum      ****")
            print("****              201807066               ****")
            print("**********************************************\n")

            input("Presione cualquier tecla para continuar...")
            menu()
            break
        elif opc == "5":
            cls()
            print("Saliendo del sistema...")
            time.sleep(0.5)
            os.system("exit")
            break

menu()