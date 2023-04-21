'''
    List methos
    Date: 27/01/23
'''
class ListMethos:
    #1 Metodo inicializador de la clase
    def __init__(self):
        # Definimos una lista vacia
        self.pets=[]
        self.vehicles = list()

    #2 Metodo para añadir elementos en la lista
    def add_list_elements(self):
        #["dog","cat"]
        self.pets.append("Dog")
        self.pets.append("Cat")
        print(self.pets)
    
    #3 Metodo que solicita valores al usuario
    def input_data_vehicles_list(self):
        # Variables locales: vehicles_number , vehicle_type
        vehicles_number = int(input("cuantos vehiculos tiene: "))
        # Recorrer una lista
        for vehicle_item in range(vehicles_number):
            vehicle_type = input("Tipo de vehiculo: ")
            #añadimos el vehiculo a la lista
            self.vehicles.append(vehicle_type)
        # Imprimir toda la lista
        print(self.vehicles)
        # Imprimir ultimo elemento de la lista
        print(self.vehicles[-1],self.vehicles[-2],self.vehicles[-3])

    #4 Extraer subconjuntoa de una lista
    def show_collection_data_list(self):
        # Desde posicion 2 hasta 4-1
        print(self.vehicles[2:4])
        # Todos los elementos de la lista 
        print(self.vehicles[:])
        # Elementos desde un indice especifico: 2 [2,3,4....]
        print(self.vehicles[2:])
        # Elementos hasta un indice especifico: 2 [0,1,2]
        print(self.vehicles[:2])
        # Acceder a los elementos de 2 en 2
        print(self.vehicles[::2])
        # Acceder a un subconjunto de elementos de 2 en 2
        print(self.vehicles[1:5:2])

    #5 Iterar los elementos de una lista con fr
    def iterar_list(self):
        for item in self.vehicles:
            print(item)
        # Validar si la lista contiene un valor especifico
        if "CARRo".capitalize() in self.vehicles:
            print("si se encontro valor")
        else:
            print("No se entontro el valor")

    #6 Añadir varios elementos al final de la lista
    def add_elements(self):
        self.vehicles.extend("Avion","Tractomula","Otro medio")
        print(self.vehicles)

    #7 Añadir un elemento en posicion especifica de la lista
    def add_specific_elements(self):
        self.vehicles.insert(0,"Moto")
        print(self.vehicles)
    
    #8 Eliminar ultimo elemento de la lista
    def remove_last_element(self):
        self.vehicles.pop()
        print(self.vehicles)

    #9 Eliminar elemento de posicion especifica
    def remove_specific_elements(self):
        #primer elemento
        self.vehicles.pop(0)
        print(self.vehicles)

    #10 Eliminar todos los elementos de la lista
    '''def remove_all_elements(self):
        self.vehicles.clear()'''

    #11 Eliminar de la lista un valor especifico
    def remove_element_by_name(self):
        self.vehicles.remove("tractomula".capitalize)
        print(self.vehicles)
    
    #12 Eliminar todas las coincidencias de valor en la lista
    def remove_all_match_elements(self):
        new_list= list(filter("Tractomula".__ne__,self.vehicles))
        print(new_list)