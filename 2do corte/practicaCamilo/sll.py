class SingleLinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None

    def __init__(self):
        self.Head=None
        self.Tail=None
        self.lenght=0
    
    def add_final(self,value):
        update=value*2
        new_node=self.Node(update)
        if self.lenght==0:
            self.Head=new_node
            self.Tail=new_node
            self.lenght += 1
        else:
            self.Tail.next=new_node
            self.Tail=new_node
            self.lenght +=1

    def show_list(self):
        lista = list()
        current_node=self.Head
        while current_node != None:
            lista.append(current_node.value)
            current_node = current_node.next
        print(lista)