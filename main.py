import os, sys, time
from listaTerreno.listaTerrenos import ListaTerreno
import xml.etree.ElementTree as ET

def cls():
    os.system("cls")

def cargar(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        print("Terreno: ", elemento.attrib["nombre"], "ha sido insertado")


        for subelemento in elemento.iter("posicioninicio"):
            print("Posicion de Inicio")
            for inicioX in subelemento.iter("x"):
                x = inicioX.text
                print("Corrdenada X:", x)
            for inicioY in subelemento.iter("y"):
                y = inicioY.text
                print("Corrdenada Y:", y, "\n")

    


def menu():
    cls()
    while True:
        print("""\n          ***   Menú Principal   ***\n          
        1. Cargar archivo
        2. Procesar archivo
        3. Escribir archivo salida
        4. Mostrar datos del estudiante
        5. Generar gráfica
        6. Salir""")

        opc = input("\nOpción a realizar: ")

        if opc == "1": 
            cls()
            print("   --- Cargar Archivo ---   \n")
            try:
                archivo = input("Ingrese nombre del archivo '.xml': ") 
                file = 'D:/Users/Yayan/OneDrive/Escritorio/Desarrollo/Python/IPC2/Proyecto1/extras/' + archivo + '.xml'
                cargar(file)
                input("\n--> Archivo cargado exitosamente...")
                menu()
            except:
                input("El nombre del archivo no se ha encontrado...")
                menu()
            break
        elif opc == "2":
            break
        elif opc == "3":
            break
        elif opc == "4":
            cls()      
            print("\n           Datos del estudiante            \n")     
            print("**********************************************")
            print("****                IPC 2                 ****")
            print("****              Sección D               ****")
            print("****                                      ****")
            print("****            Ciencias y sistemas       ****")
            print("****      Brayan Andrés Cholotio Tum      ****")
            print("****              201807066               ****")
            print("**********************************************\n")

            input("Presione cualquier tecla para continuar...")
            menu()
            break
        elif opc == "5":
            break
        elif opc == "6":
            cls()
            print("Saliendo del sistema...")
            time.sleep(0.5)
            os.system("exit")
            break

menu()

