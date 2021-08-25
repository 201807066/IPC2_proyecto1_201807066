"""from os import  sys, startfile, system

def generar():
    graphviz = 
    digraph L{ 

        node[shape=box fontname=courier fillcolor="#FFEDBB" style=filled ]

        #Para decorar       
        subgraph cluster_p{
                root[label = "0,0", fillcolor = "red"]
                label = "MATRIZ DISPERSA"
                bgcolor = "#398D9C"
                edge[dir="both"]
                #dir = none, style = invisible

                /*Aqui creamos las cabeceras de las filas*/
                F1[label = "1", group = 1, fillcolor = "yellow"]
                F2[label = "2", group = 1, fillcolor = "yellow"]
                F3[label = "3", group = 1, fillcolor = "yellow"]
                F4[label = "4", group = 1, fillcolor = "yellow"]
                F5[label = "5", group = 1, fillcolor = "yellow"]

                /*Aqui enlazamos los nodos de las filas*/
                F1 -> F2
                F2 -> F3
                F3 -> F4
                F4 -> F5
                
                /*Se  crean los nodos de las columnas*/
                C1[label = "1", group = 2, fillcolor = "green"]
                C2[label = "2", group = 3, fillcolor = "green"]
                C3[label = "3", group = 4, fillcolor = "green"]
                C4[label = "4", group = 5, fillcolor = "green"]
                C5[label = "5", group = 6, fillcolor = "green"]

                /*Se enlaza las columnas*/
                C1 -> C2
                C2 -> C3
                C3 -> C4
                C4 -> C5

                /*Aqui se une la raiz a las filas y columnas*/
                root -> F1
                root -> C1

                /*rank para que lleve el sentido correcto
                Se alinean los nodos cabeceras de las columnas*/
                {rank = same; root; C1; C2; C3; C4; C5}
                nodoF1_C1[label = "1,1", group = 2]
                nodoF4_C4[label = "4,4", group = 5]
                nodoF5_C3[label = "5,3", group = 4]
                nodoF2_C2[label = "2,2", group = 3]
                nodoF2_C4[label = "2,4", group = 5]
                nodoF3_C4[label = "3,4", group = 5]
                nodoF5_C5[label = "5,5", group = 6]

                /*Ahora alineamoso fila por fila*/
                F1 -> nodoF1_C1
                {rank = same; F1; nodoF1_C1}
                F2 -> nodoF2_C2
                nodoF2_C2 -> nodoF2_C4
                {rank = same; F2; nodoF2_C2; nodoF2_C4}
                F3 -> nodoF3_C4
                {rank = same; F3; nodoF3_C4}
                F4 -> nodoF4_C4
                {rank = same; F4; nodoF4_C4}
                F5 -> nodoF5_C3
                nodoF5_C3 -> nodoF5_C5
                {rank = same; F5; nodoF5_C3; nodoF5_C5}
                
                

                C1 -> nodoF1_C1   
                C2 -> nodoF2_C2  
                C3 -> nodoF5_C3  
                C4 -> nodoF2_C4
                nodoF2_C4 -> nodoF3_C4
                nodoF3_C4 -> nodoF4_C4
                C5 -> nodoF5_C5


                

}
}
    
    miArchivo = open("graphviz.dot", "w")
    miArchivo.write(graphviz)
    miArchivo.close()

    system("dot -Tpng graphviz.dot -o graphviz.png")
    system("cd ./graphviz.png")
    startfile("graphviz.png")




if __name__ == "__main__":
    generar()"""


cont = 10 

x = 1

for i in range(cont):
    print(x)
    x += 1