from random import sample
from colorama import Fore, Back
from os import system
import time

class SortAlgorithms:
    def __init__(self):
        self.number_list = range(100)
        self.list_bubble_sort = sample(self.number_list, 8)
        self.list_select_sort = sample(self.number_list, 8)
        self.list_insert_sort = sample(self.number_list, 8)
        self.list_merge_sort = sample(self.number_list, 17)
        self.list_quick_sort = sample(self.number_list, 8)
        self.list_radix_sort = sample(self.number_list, 8)
        self.aux_num = 0
        self.aux_list = []
        self.sum_list = []

    # Ordenamiento butbuja
    def bubble_sort_function(self):
        # Comparación por pares, iniciamos comparando los 2 primeros elementos de la lista
        print("--------------------------------------------")
        print("           Ordenamiento burbuja")
        # Crear un contador para conocer la cantidad de elementos de la lista
        count_item_list = 0
        # Recorremos la lista self.list_burble_sort
        for i in self.list_bubble_sort:
            # al contador de elementos, cada vez que visitemos una posición le sumamos 1
            count_item_list += 1
        
        print(self.list_bubble_sort)
        # Recorremos la lista e imprimimos su contenido en cada iteración
        print("Primer for contador - 1: ", count_item_list-1)
        for j in range(count_item_list-1):
            print(f"     {j}")
            for k in range(count_item_list - j - 1):
                print(f"{k}")
                print(self.prueba(k))
                print(self.list_bubble_sort)
                # Compramos el valor de la posición actual con el valor de la siguiente posicion
                if self.list_bubble_sort[k] > self.list_bubble_sort[k+1]:
                    # Transposición de valores
                    self.list_bubble_sort[k], self.list_bubble_sort[k+1] = self.list_bubble_sort[k+1], self.list_bubble_sort[k]
                
        print(self.list_bubble_sort)

    def bubble_sort_function_refactor(self):
        change_position = True
        print(self.list_bubble_sort)
        while change_position:
            change_position = False
            for i in range(len(self.list_bubble_sort) - 1):
                if self.list_bubble_sort[i] > self.list_bubble_sort[i + 1]:
                    self.list_bubble_sort[i], self.list_bubble_sort[i+1] = self.list_bubble_sort[i+1], self.list_bubble_sort[i]
                    change_position = True
        print(self.list_bubble_sort)


    def select_sort_function(self):
        print("--------------------------------------------")
        print("           Ordenamiento selección")
        count_item_list = 0
        print(self.list_select_sort)
        # Inicializamos el contador
        for i in self.list_select_sort:
            count_item_list += 1
        
        # Recorremos la lista y generamos la comparación de valores entre posiciones:
        for i in range(count_item_list):
            
            min = i
            print(">>> ", i)
            for j in range(min + 1, count_item_list):
                print("> ", j)
                # Comparación de valores
                print("Comparacion: " + str(self.list_select_sort[min]) + " - " + str(self.list_select_sort[j]))
                if self.list_select_sort[min] > self.list_select_sort[j]:
                    min = j
            # Generamos el intercambio, la transposición
            self.list_select_sort[i], self.list_select_sort[min] = self.list_select_sort[min], self.list_select_sort[i]
        print(self.list_select_sort)


    def insert_sort_function(self):
        print("Vector inicial: " + str(self.list_insert_sort))
        # Separar la lista en dos partes (puede o no estar) ordenadas
        for i in range(1, len(self.list_insert_sort)):
            print(f"--------[{i}]--------")
            print("Revisando: " + str(self.list_insert_sort[:i+1]))
            item_visited = self.list_insert_sort[i]
            # Visitamos la posición anterior a la actual
            j = i - 1
            # Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.list_insert_sort[j] > item_visited:
                print(str(self.list_insert_sort[j]) + " > " + str(item_visited))
                self.list_insert_sort[j + 1], self.list_insert_sort[j]  = self.list_insert_sort[j], item_visited
                j -= 1
                print(self.list_insert_sort)
                
        print("Vector final: " + str(self.list_insert_sort))

    def insert_sort_function_v2(self):
        print("Vector inicial: " + str(self.list_insert_sort))
        # Separar la lista en dos partes (puede o no estar) ordenadas
        for i in range(1, len(self.list_insert_sort)):
            print(f"--------[{i}]--------")
            print("Revisando: " + str(self.list_insert_sort[:i+1]))
            item_visited = self.list_insert_sort[i]
            # Visitamos la posición anterior a la actual
            j = i - 1
            # Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.list_insert_sort[j] > item_visited:
                print(str(self.list_insert_sort[j]) + " > " + str(item_visited))
                self.list_insert_sort[j + 1]= self.list_insert_sort[j]
                j -= 1
                print(self.list_insert_sort)
            self.list_insert_sort[j + 1] = item_visited  
            print(self.list_insert_sort)
        print("Vector final: " + str(self.list_insert_sort))

    def merge_sort_function(self, list):
        print(list)
        # En el caso de que el tamaño de la lista sea menor a 2, retornamos la lista (Esto pasa porque ya está ordenada, o se dividió hasta ser sólo 1 elemento)
        if len(list) < 2:
            return list
        # En el caso de que sea 2 o mayor, se divide de nuevo
        else:
            middle = len(list) // 2 # Divide y redondea hacia abajo el resultado
            left = self.merge_sort_function(list[:middle])
            right = self.merge_sort_function(list[middle:])
            return self.merge(left,right)
        
    # Función merge
    def merge(self, list1, list2):
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado
        # Intercalar ordenadamente
        while(i < len(list1) and j < len(list2)):
            if (list1[i] < list2[j]):
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        # Agregamos datos faltantes al resultado
        result += list1[i:]
        result += list2[j:]
    
        # Retornamos el resultados
        return result



    def test_merge_sort_function(self, list):
        self.test_show_data(list)
        """
        Lo primero que se ve en el psudocódigo es un if que
        comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
        ¿Por que? Ya esta ordenada. 
        """
        # En el caso de que el tamaño de la lista sea menor a 2, retornamos la lista (Esto pasa porque ya está ordenada, o se dividió hasta ser sólo 1 elemento)
        if len(list) < 2:
            return list
        # En el caso de que sea 2 o mayor, se divide de nuevo
        else:
            middle = len(list) // 2 # Divide y redondea hacia abajo el resultado
            right = self.test_merge_sort_function(list[:middle])
            left = self.test_merge_sort_function(list[middle:])
            input(Fore.BLACK+"--------------------------------------------------------------"+Fore.RESET)
            return self.test_merge(right, left)

    def test_merge(self, list1, list2):
        print(Fore.RED + "Ordenando subconjuntos" + Fore.RESET)
        print("Lista 1: " + Fore.BLUE + str(list1) + Fore.RESET)
        print("Lista 2: " + Fore.BLUE + str(list2) + Fore.RESET)
        """
        merge se encargara de intercalar los elementos de las dos
        divisiones.
        """
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado

        # Intercalar ordenadamente
        while(i < len(list1) and j < len(list2)):
            if (list1[i] < list2[j]):
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        # Agregamos los resultados a la lista
        result += list1[i:]
        result += list2[j:]
    
        # Retornamos el resultados
        print(Fore.RED + "Resultado: " + Fore.RESET)
        print(Fore.BLUE + str(result) + Fore.RESET)
        #input()
        #self.parcial_result(result)
        return result
    
    def test_show_data(self, list):
        if len(list) == len(self.list_merge_sort):
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(list) + Fore.RESET + "              ")   
        elif len(list) > 1:
            input()
            system("cls")
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(self.list_merge_sort)+ Fore.RESET + "              ")
            print("              "+ Fore.BLUE + str(list) + Fore.RESET + "              ") 
    
    def parcial_result(self, result):
        system("cls")
        # Separar por niveles
        # Nivel 1 (Respueta final)
        if len(result) == len(self.list_merge_sort):
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(self.list_merge_sort)+ Fore.RESET + "              ") 
            print(Fore.RED + "                      Resultado final                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(result) + Fore.RESET + "              ")   
        
        # Nivel 2
        if len(result) < len(self.list_merge_sort):
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(self.list_merge_sort)+ Fore.RESET + "              ")
            if len(result) == self.aux_num or len(result) < self.aux_num: 
                print(Fore.RED + "                     Resultado parcial                   " + Fore.RESET)
                print("              "+ Fore.CYAN + str(self.aux_list) + str(result) + Fore.RESET + "              ")
                self.sum_list = self.aux_list + result
            else:
                self.aux_num = len(result)
                print(Fore.RED + "                     Resultado parcial                   " + Fore.RESET)
                print("              "+ Fore.CYAN + str(result) + Fore.RESET + "              ")
                self.aux_list = result

        input()

    def pruebaBubble(self, k):
        texto = " |    |"
        flechas = " v    v"
        for i in range (k):
            texto = "    " + texto
            flechas = "    " + flechas  
        return texto + "\n"+ flechas