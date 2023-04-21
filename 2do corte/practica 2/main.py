from double_linked_list import DoublyLinkedList
inst_dll = DoublyLinkedList()

'''
inst_dll.add_node_at_end("A")
inst_dll.add_node_at_end('B')
inst_dll.add_node_at_start('C')
inst_dll.add_node_at_end('D')
inst_dll.add_node_at_end('E')
inst_dll.add_node_at_start('NewA')
inst_dll.print_list()
inst_dll.add_node_in_position(1,"primero")
inst_dll.print_list()



#eliminacion
print("<<<<<<<<<>>>>>>>>>")
print("Eliminar por posicion del nodo 7")
inst_dll.remove_node_by_position(7)
inst_dll.print_list()
print("<<<<<<<<<>>>>>>>>>")
print("Eliminar por posicion del nodo 6")
inst_dll.remove_node_by_position(6)
inst_dll.print_list()
print("<<<<<<<<<>>>>>>>>>")
print("Eliminar por posicion del nodo 1")
inst_dll.remove_node_by_position(1)
inst_dll.print_list()
print("<<<<<<<<<>>>>>>>>>")
print("Eliminar por posicion del nodo 2")
inst_dll.remove_node_by_position(2)
inst_dll.print_list()
print("<<<<<<<<<>>>>>>>>>")
print("Eliminar por valor del nodo A")
inst_dll.remove_node_by_value("A")
inst_dll.print_list()


print("<<<<<<<<<>>>>>>>>>")
print("imprimir lista invertida")
inst_dll.reverse()
inst_dll.print_list()
'''

inst_dll.add_node_at_end(-6)
inst_dll.add_node_at_end(5)
inst_dll.add_node_at_start(3)
inst_dll.add_node_at_end(0)
inst_dll.add_node_at_end(-6)
inst_dll.print_list()
inst_dll.has_duplicates_with_information_v2()
inst_dll.reverse()
inst_dll.print_list()
inst_dll.sort_asc()
inst_dll.print_list()



#inst_dll.calculate_complexity(inst_dll.add_node_at_end)




