from colorama import Fore,init,ansi
init()
class super_Heros:
    def __init__(self):
        self.ListaSuperheroesMarvel=[]
        self.ListaSuperheroesDC= []
        self.MenuO= 0
        self.SuperHeroes=[]
        self.MenuO2= 0
    
    def MenuT(self):
        while True:
            try:
                self.MenuO2= int(input(ansi.Fore.BLUE+"\n       1. Nuevo superhéroe\n         2. Buscar superhéroe\n           3. Eliminar superhéroe\n             4. Mas superpoderes\n               5. Menos superpoderes\n                 6. Marvel y DC\n                   7. Salir\n->"+ansi.Fore.RESET))
                if self.MenuO2 < 1 or self.MenuO2 > 7:
                    print(ansi.Fore.GREEN+"\nOpcion inválida, ingrese un numero del menú"+ansi.Fore.RESET)
                
                elif self.MenuO2 == 1:
                    print(ansi.Fore.CYAN+"<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"+ansi.Fore.RESET)
                    print(ansi.Fore.LIGHTMAGENTA_EX+"\n <<<<<Crear un Superheroe>>>>> "+ansi.Fore.RESET)
                    self.MenuIni()
                
                elif self.MenuO2 == 2:
                    print(ansi.Fore.CYAN+"<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"+ansi.Fore.RESET)
                    print(ansi.Fore.LIGHTMAGENTA_EX+"\n <<<<< Buscar Superheroe >>>>> "+ansi.Fore.RESET)
                    self.EncontrarSuperheroe()
                
                elif self.MenuO2 == 3:
                    print(ansi.Fore.CYAN+"<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"+ansi.Fore.RESET)
                    print(ansi.Fore.LIGHTMAGENTA_EX+"\n <<<<< Eliminar Superheroe >>>>> "+ansi.Fore.RESET)
                    self.EliminarSuperheroe()
                
                elif self.MenuO2 == 4:
                    print(ansi.Fore.CYAN+"<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"+ansi.Fore.RESET)
                    print(ansi.Fore.LIGHTMAGENTA_EX+"\n <<<<< Mas Poderes >>>>> "+ansi.Fore.RESET)
                    self.SuperHeroePoderoso()
                
                elif self.MenuO2 == 5:
                    print(ansi.Fore.CYAN+"<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"+ansi.Fore.RESET)
                    print(ansi.Fore.LIGHTMAGENTA_EX+"\n <<<<< Menos Poderes >>>>> "+ansi.Fore.RESET)
                    self.SuperHeroeDevil()
                
                elif self.MenuO2 == 6:
                    print(ansi.Fore.CYAN+"<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"+ansi.Fore.RESET)
                    print(ansi.Fore.LIGHTMAGENTA_EX+"\n <<<<< Toda La Lista >>>>> "+ansi.Fore.RESET)
                    self.MARVELyDC()
                
                else:
                    print(ansi.Fore.CYAN+"<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"+ansi.Fore.RESET)
                    break
            except ValueError:
                print(ansi.Fore.GREEN+"\nOpción inválida, ingrese un numero del menú"+ansi.Fore.RESET)
    
    def MenuIni(self):
        NumeroDeSuperheroes= 0
        NombreDelSuperheroe= " "
        NumeroDePoderes= 0
        PoderDelSuperheroe= ""
        Poder= ""
        NumeroDeCreadores= 0
        Creador= ""

        print(ansi.Fore.RED+"\n---------------Seleccione una opcion--------------"+ansi.Fore.RESET)
        while True:
            try:
                self.MenuO= int(input(ansi.Fore.BLUE+"\n      1. Marvel\n        2. DC\n          3. Salir\n\n ->"+ansi.Fore.RESET))
                if self.MenuO < 1 or self.MenuO > 3:
                    print(ansi.Fore.GREEN+"\nOpcion inválida, ingrese un numero del 1 al 3"+ansi.Fore.RESET)

                elif self.MenuO == 1:
                    print(ansi.Fore.CYAN+"\nMarvel:"+ansi.Fore.RESET)
                    NumeroDeSuperheroes= int(input(ansi.Fore.LIGHTMAGENTA_EX+"\nCantidad de superheroes:\n>"))
                    for i in range(0, NumeroDeSuperheroes):
                        ListaDeSuperPoderes=[]
                        ListaDeCreadores= []
                        NombreDelSuperheroe= input(f"Nombre del superheroe: {i+1}\n").upper()
                        NumeroDePoderes= int(input("Numero de poderes: \n"))
                        for i in range(0,NumeroDePoderes):
                            Poder=input("Nombre del poder: \n")
                            ListaDeSuperPoderes.append(Poder)
                        NumeroDeCreadores=int(input("Cantidad de creadores: \n"))
                        for i in range(0, NumeroDeCreadores):
                            Creador=input("Nombre del creador\n")
                            ListaDeCreadores.append(Creador)
                        
                        self.ListaSuperheroesMarvel.append((NombreDelSuperheroe, ListaDeSuperPoderes, ListaDeCreadores))
                        self.SuperHeroes.append((NombreDelSuperheroe, ListaDeSuperPoderes, ListaDeCreadores))
                    print(self.ListaSuperheroesMarvel)

                elif self.MenuO == 2:
                    print(ansi.Fore.CYAN+"\nDC:"+ansi.Fore.RESET)
                    NumeroDeSuperheroes= int(input(ansi.Fore.LIGHTMAGENTA_EX+"\nCantidad de superheroes:\n>"))
                    for i in range(0, NumeroDeSuperheroes):
                        ListaDeSuperPoderes=[]
                        ListaDeCreadores= []
                        NombreDelSuperheroe= input(f"Nombre del superheroe: {i+1}\n").upper()
                        NumeroDePoderes= int(input("Numero de poderes: \n"))
                        for i in range(0,NumeroDePoderes):
                            Poder=input("Nombre del poder: \n")
                            ListaDeSuperPoderes.append(Poder)
                        NumeroDeCreadores=int(input("Cantidad de creadores: \n"))
                        for i in range(0, NumeroDeCreadores):
                            Creador=input("Nombre del creador\n")
                            ListaDeCreadores.append(Creador)
                        
                        self.ListaSuperheroesDC.append((NombreDelSuperheroe, ListaDeSuperPoderes, ListaDeCreadores))
                        self.SuperHeroes.append((NombreDelSuperheroe, ListaDeSuperPoderes, ListaDeCreadores))
                    print(self.ListaSuperheroesDC)

                else:
                    break

            except ValueError:
                print(ansi.Fore.GREEN+"\nError"+ansi.Fore.RESET)

    def EncontrarSuperheroe(self):
        Nombre=input(ansi.Fore.CYAN+"nombre del superhéroe que quiere buscar:\n"+ansi.Fore.RESET)
        Buscar= False
        for i in self.SuperHeroes:
            if Nombre.upper() in i[0]:
                print(i[1])
                Buscar= True
        if not Buscar:
            print(ansi.Fore.GREEN+"No está el superhéroe"+ansi.Fore.RESET)
            AñadirSuperheroe=int(input(ansi.Fore.LIGHTMAGENTA_EX+"quiere añadirlo?\n \n1. Si\n2. No\n\n"+ansi.Fore.RESET))
            if(AñadirSuperheroe==1):
                self.initial_menu()
            else:
                print(ansi.Fore.GREEN+"\nNo añadido\n"+ansi.Fore.RESET)
    
    def EliminarSuperheroe(self):
        Nombre=input(ansi.Fore.CYAN+"\n Nombre del superhéroe que va a eliminar\n"+ansi.Fore.RESET)
        Buscar= False
        for hero in self.ListaSuperheroesMarvel:
            if Nombre.upper() in hero[0]:
                self.ListaSuperheroesMarvel.remove(hero)
                print(self.ListaSuperheroesMarvel)
        for hero in self.ListaSuperheroesDC:
            if Nombre.upper() in hero[0]:
                self.ListaSuperheroesDC.remove(hero)
                print(self.ListaSuperheroesDC)
        for hero in self.SuperHeroes:
            if Nombre.upper() in hero[0]:
                self.SuperHeroes.remove(hero)
                Buscar=True
        if not Buscar:
            print(ansi.Fore.GREEN+"No está el superhéroe"+ansi.Fore.RESET)
    
    def SuperHeroePoderoso(self):
        mayor= -999
        
        for hero in self.SuperHeroes:
            if len(hero[1])>mayor:
                mayor=len(hero[1])
                cont=hero
        print(ansi.Fore.CYAN+ f"El superhéroe con mayor cantidad de poderes {cont[0]}"+ansi.Fore.RESET)
    
    def SuperHeroeDevil(self):
        menor= 999
        for hero in self.SuperHeroes:
            if len(hero[1])<menor:
                menor=len(hero[1])
                cont=hero
        print(ansi.Fore.CYAN+ f"El superhéroe con menos cantidad de poderes {cont[0]}"+ansi.Fore.RESET)
    
    def MARVELyDC(self):
        print(self.SuperHeroes)