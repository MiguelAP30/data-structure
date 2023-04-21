from random import sample
from colorama import ansi,Fore,init
init()

class SortAlgoritmo:
    def __init__(self):
        self.NumeroLista=range(100)
        self.Lista_Burble_Sort = sample(self.NumeroLista,8)
        self.Lista_Selec_Sort = sample(self.NumeroLista,8)
        self.Lista_Insert_Sort = sample(self.NumeroLista,8)
        self.Lista_Marge_Sort = sample(self.NumeroLista,8)
        self.Lista_Quick_Sort = sample(self.NumeroLista,8)
        self.Lista_Radix_Sort = sample(self.NumeroLista,8)

    #ordenamiento burbuja
    def burble_sort_funcion(self):
        #comprobacion por pares, iniciamos comparando los 2 primeros elementos
        print(ansi.Fore.CYAN+"--------------------------------"+ansi.Fore.RESET)
        print(ansi.Fore.GREEN+"          Ordenamiento Burbuja"+ansi.Fore.RESET)
        #crear una contador para conocer la cantidad de elementos de la lista
        cont_lista=0
        #Recorremos la lista self.Lista_Burble_Sort
        for i in self.Lista_Burble_Sort:
            #al contador del elementos, cada ves que visitemos una posicion le sumamos 1:
            cont_lista += 1
        print(self.Lista_Burble_Sort)

        #Recorremos la lista e iniciamos la comparacion del valor
        print("Primer contador - 1: ", cont_lista)
        print(ansi.Fore.LIGHTMAGENTA_EX+"                >>> Interaccion Externa: <<<"+ansi.Fore.RESET)
        for j in range(cont_lista-1):
            print(ansi.Fore.RED + str(j) + ansi.Fore.RESET)
            for k in range(cont_lista-j-1):
                print(Fore.LIGHTCYAN_EX + str(k)+ "-"+ str(k+1) + ansi.Fore.RESET)
                #comparamos el valor de la posicion actual con el valor de la sgte
                if self.Lista_Burble_Sort[k] > self.Lista_Burble_Sort[k+1]:
                    #transposicion de valores
                    self.Lista_Burble_Sort[k], self.Lista_Burble_Sort[k+1]= self.Lista_Burble_Sort[k+1], self.Lista_Burble_Sort[k]
        print(self.Lista_Burble_Sort)

    def Burble_Sort_Funcion_Refactorizar(self):
        Cambio_posicion= False
        while Cambio_posicion:
            Cambio_posicion = False
            for i in range(len(self.Lista_Burble_Sort)-1):
                if self.Lista_Burble_Sort[i] > self.Lista_Burble_Sort[i+1]:
                    self.Lista_Burble_Sort[i], self.Lista_Burble_Sort[i+1]= self.Lista_Burble_Sort[i+1], self.Lista_Burble_Sort[i]
                    Cambio_posicion = True
        print(Fore.LIGHTRED_EX+ str(self.Lista_Burble_Sort) +Fore.RESET) 

    def select_Sort_Funcion(self):
        print(ansi.Fore.CYAN+"--------------------------------"+ansi.Fore.RESET)
        print(ansi.Fore.GREEN+"          Ordenamiento Seleccion"+ansi.Fore.RESET) 
        cont_lista=0
        # inicializamos el contador
        for i in self.Lista_Selec_Sort:
            cont_lista += 1    
        
        #recorremos la lista y generamos la comparacion de valores entre posiciones
        for i in range(cont_lista):
            min=i
            print(Fore.RED+ str(i) + Fore.RESET)
            for j in range( min + 1 , cont_lista):
                print(Fore.CYAN+ str(j) + Fore.RESET)
                #comparacion de valores
                print("Comparacion: "+Fore.BLUE+ str(self.Lista_Selec_Sort[min])+"-"+str(self.Lista_Selec_Sort[j])+ Fore.RESET)
                if self.Lista_Selec_Sort[min]> self.Lista_Selec_Sort[j]:
                    min=j
            #generamos el intercambio, la transposicion
            #generamos el elemneto de menor valor de la lista con el primero
            self.Lista_Selec_Sort[i],self.Lista_Selec_Sort[min]=self.Lista_Selec_Sort[min],self.Lista_Selec_Sort[i]
        print(self.Lista_Selec_Sort)

    def Insert_sort_Funtion(self):
        print(Fore.CYAN+"----------------------------------------------------------"+Fore.RESET)
        print(Fore.GREEN+"             Ordenamiento de insercion"+Fore.RESET)
        # separamos la lista en dos partes (puede o no estar) ordenados
        print(self.Lista_Insert_Sort)
        for i in range(1, len(self.Lista_Insert_Sort)):
            item_visited = self.Lista_Insert_Sort[i]
            #visitamos la posicion anterior a la actual
            j=i-1
            #todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.Lista_Insert_Sort[j]> item_visited:
                print(Fore.CYAN+ str(self.Lista_Insert_Sort[j])+Fore.RESET+">"+str(item_visited))
                self.Lista_Insert_Sort[j+1]=self.Lista_Insert_Sort[j]
                j-=1
                #transposicion            
            self.Lista_Insert_Sort[j+1]=item_visited
        print(self.Lista_Insert_Sort)

    def Marge_Sort_funcion(self, Lista):
        print(self.Lista_Marge_Sort)
        if len(Lista)>1:
            mitad = len(Lista)//2
            primera_mitad= Lista[:mitad]
            segunda_mitad= Lista[mitad:]

            self.Marge_Sort_funcion(primera_mitad)
            self.Marge_Sort_funcion(segunda_mitad)

            i=0
            j=0
            K=0
            while i < len(primera_mitad) and j < len(segunda_mitad):
                if primera_mitad[i] < segunda_mitad[i]:
                    Lista[k]= primera_mitad[i]
                    i += 1
                else:
                    Lista[k] = segunda_mitad[j]
                    j += 1
                k += 1
            while i < len(primera_mitad):
                Lista[k]= primera_mitad[i]
                i += 1
                k += 1
            while j < len(segunda_mitad):
                Lista[k]= segunda_mitad[j]
                j += 1
                k += 1
        print(self.Lista_Marge_Sort)

