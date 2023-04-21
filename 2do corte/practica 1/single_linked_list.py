class SingleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    '''por fuera de la clase nodo'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def show_list(self):
        #1 declarar una array(lista) vacia que contendrá los vlores de los nodos de sll
        # array whith nodes 
        array_whith_nodes_value = list()
        current_node = self.head
        # mientras que el nodo actual que estoy visitando sea diferente de None
        while(current_node != None):
            # añado al final de la lista el valor extraido del nodo
            array_whith_nodes_value.append(current_node.value)
            #incrementamos en 1 el valor del nodo visitado
            #current_node +=1 NO SIRVE PARA PASAR AL SIGUIENTE NODO DE UNA SLL
            # pasamos del nodo actual al siguiente nodo mediante el puntero
            current_node = current_node.next
        #imprimimos los valores de la lista
        print(f"los valores de los nodos de la SLL son:\n {array_whith_nodes_value}")

# EJERCICIO 2
    def create_node_sll_ends(self, value):
        # creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        #validar si la SLL tiene nodos o no
        '''
        if self.length == 0:
            print("La lista simplemente enlazada no tiene nodos")
        else:
            print("La lista simplemente enlazada si tiene nodos")
        if self.head == None and self.tail == None:
            print("La lista simplemente enlazada no tiene nodos")
        else:
            print("La lista simplemente enlazada si tiene nodos")
        '''
        if self.head == None:
            #al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            #si ingresa en esta condicion, es porque ya existe al menos un nodo
            # 1. debemos relacionar al nuevo nodo con la cola de la lista
            # 2. convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        # incrementamos en 1 el tamaño de la lista
        self.length +=1
    
# EJERCICIO 1
    def create_node_SLL_unshift(self,value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

# EJERCICIO 4
    def delete_node_SLL_pop(self):
        # 1. validar si la lista está vacía
        # 2. Validar si la lista tiene un único nodo        
        # 3. Si tiene más de un nodo eliminar el nodo que es la cola de la lista         
        # 4. Asignar al nodo anterior como la nueva cola de la lista
        if self.length == 0:
            print(">> Lista vacia no hay nodos por eliminar <<")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            current_node = self.head
            # 1. recorrer la lista para identificar la cola
            new_tail = current_node
            # 2. validar mediante el enlace del nodo actual que haya un nodo
            while current_node.next != None:
                # 3. convertimos en la cola de la lista el nodo que actualmente visitamos en la iteracion
                new_tail = current_node
                # 4. pasamos al siguiente nodo antes de salir del while
                current_node = current_node.next
            # 5. actualizamos la cola de la lista
            self.tail = new_tail
            self.tail.next = None
            # 6. restamos 1 en el tamaño de la lista
            self.length -=1

# EJERCICIO 3
    def shift_node_SLL(self):
        print(self.length)
        if self.length == 0:
            print(">> Lista vacia no hay nodos por eliminar <<")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            remove_node = self.head
            print(f"Valor del nodo a eliminar es: [{remove_node.value}]")
            self.head = remove_node.next
            self.length -=1

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node

# EJERCICIO 7
    def get_node_value(self, index):
            if index < 1 or index> self.length:
                print("No se encontró")
            elif index == 1:
                print(self.head.value)
            elif index == self.head:
                print(self.tail.value)
            else:
                current_node = self.head
                node_counter = 1
                while(index != node_counter):
                    current_node = current_node.next
                    node_counter +=1
                print(current_node.value)

# EJERCICIO 13
    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            #Encontró el nodo y se puede actualizar
            print(f'Actualizando el valor del nodo ...\n>>{search_node.value}<< por >>{new_value}<<')
            search_node.value= new_value
        else:
            #Si no se encuentra el nodo pos nada
            print("No se encontró el nodo")

# EJERCICIO 11
    def remove_node(self, index):
        if index == 1:
            self.shift_node_SLL()
        elif index == self.length:
            self.delete_node_SLL_pop()
        else:
            remove_node_SLL = self.get_node(index)
            if remove_node_SLL != None:
                previous_node = self.get_node(index - 1)
                previous_node.next = remove_node_SLL.next
                remove_node_SLL.next = None
            else:
                print(" No se encuentra el nodo")

# EJERCICIO 5
    def show_length(self):
        array_whith_nodes_value = list()
        current_node = self.head
        while(current_node != None):
            array_whith_nodes_value.append(current_node.value)
            current_node = current_node.next
        print(len(array_whith_nodes_value))

# EJERCICIO 6
    def posicion_de_un_elemento(self, valor):
        if valor == self.head.value:
            return print("1")
        elif valor == self.tail.value:
            return print(self.length)
        else:
            current_node = self.head
            node_counter = 1
            while(valor != current_node.value):
                print(current_node.value)
                current_node = current_node.next
                node_counter += 1
            return print(node_counter)

# EJERCICIO 9
    def eliminar_todos_los_elementos(self):
            while self.head != None:
                remove_node = self.head
                self.head = remove_node.next
                self.length -=1

# EJERCICIO 10
    def ordenar_la_lista(self):
        array_whith_nodes_value = list()
        new_list = list()
        current_node = self.head
        while(current_node != None):
            array_whith_nodes_value.append(current_node.value)
            current_node = current_node.next
        new_list = array_whith_nodes_value
        new_list.sort()
        return print(new_list)    

# EJERCICIO 12 
    def insertar_en_posicion(self, value, index):
        nuevo_nodo = self.Node(value)
        if not self.head:  # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.head = nuevo_nodo
            return
        if index == 1:  # Si la posición es cero, el nuevo nodo se inserta al principio
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
            return
        actual = self.head
        anterior = None
        contador = 1
        while actual and contador != index:  # Se recorre la lista hasta llegar a la posición deseada
            anterior = actual
            actual = actual.next
            contador += 1
        if contador == index:  # Se inserta el nuevo nodo en la posición deseada
            anterior.next = nuevo_nodo
            nuevo_nodo.next = actual
        else:  # Si la posición es mayor que la longitud de la lista, se inserta al final
            anterior.next = nuevo_nodo

# EJERCICIO 14
    def comprobar_si_esta_vacia(self):
        if self.head == None:
            return(print("La Lista esta vacia"))
        else:
            return(print("La Lista tiene elementos"))

# EJERCICIO 8
    def reverse_sll(self):
        if self.length == 2:
            self.head=self.tail
            self.tail=self.head
        if self.length>2:
            previus_node=None
            next_node=None
            current_node=self.head
            while current_node:
                next_node=current_node.next
                current_node.next=previus_node
                previus_node=current_node
                current_node=next_node
            self.head=previus_node
