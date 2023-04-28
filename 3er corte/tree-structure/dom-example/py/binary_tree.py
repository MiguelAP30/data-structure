class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def insert(self,root,node):
        #si no existe raiz en el arbol
        if root is None:
            root = node
        else:
            #(20, 16)
            #si el valor es menor que la raiz
            if root.value > node.value:
                #si no existe nodo izquierdo
                if root.left_node is None:
                    root.left_node = node
                else:
                    #si existe nodo izquierdo, se inserta el nodo en el subarbol izquierdo
                    self.insert(root.left_node,node)
            else:
                #(20 , 21)
                #si no existe nodo derecho
                if root.right_node is None:
                    root.right_node = node
                else:
                    #si existe nodo derecho, se inserta el nodo en el subarbol derecho
                    self.insert(root.right_node, node)

    def print_tree(self, root):
        if root is not None:
            self.print_tree(root.left_node)
            print(root.value)
            self.print_tree(root.right_node)
