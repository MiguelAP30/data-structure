import pygame
from Botones.TextButton import TextButton


class SllActionPanel:

    def __init__(self, font, singlell):
        self.font = font
        self.sll = singlell
        self.selected_figure = None
        self.labelPosicion = font.render("POSICION",True,(14,14,14))
        Boton1 = TextButton("Agregar elemento al inicio", 24,(35,30))
        Boton2 = TextButton("Agregar elemento al final", 24,(35, 90))
        Boton3 = TextButton("Eliminar elemento al inicio", 24,(35, 150))
        Boton4 = TextButton("Eliminar elemento al final", 24,(35, 210))
        Boton5 = TextButton("Invertir la lista enlazada", 24,(35, 270))
        Boton6 = TextButton("Eliminar todos los elementos", 24,(35, 330))
        Boton7 = TextButton("Eliminar elemento en la posicion", 24,(35, 390))
        Boton8 = TextButton("Agregar elemento a la posicion", 24,(35, 450))
        Boton9 = TextButton("Editar elemento a la posicion",24,(35, 510))
        Boton10 = TextButton("Eliminar Duplicados",24,(35, 570))
        Boton11 = TextButton("Unir elementos Duplicados",24,(35, 630))

        self.lista_acciones=[Boton1,Boton2,Boton3,Boton4,Boton5,Boton6,Boton7,Boton8,Boton9,Boton10,Boton11]

    def draw(self,screen):
        run = True
        user_number = 0
        user_numberd = self.font.render("0",False,(14,14,14)) 
        while run:
            screen.fill((250,0,10))
            pygame.draw.rect(screen,(10,0,250), pygame.Rect(0, 0, 500, 1000))
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN: 
                    if event.unicode.isnumeric():
                        user_numberd = self.font.render(event.unicode,True,(255,255,255))
                        user_number = int(event.unicode)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for boton in self.lista_acciones:
                        if boton.is_mouse_contained(mouse_pos):
                            self.edit_singlell(boton.text,user_number)
                            run = False
            for button in self.lista_acciones:
                button.draw(screen,mouse_pos)
            screen.blit(user_numberd,(750,270))
            screen.blit(self.labelPosicion,(685,200))
            pygame.display.update()
        return

    def set_selected_figure(self,figure):
        self.selected_figure = figure
    
    def edit_singlell(self, boton_text, user_number):
        if boton_text == "Agregar elemento al inicio":
            self.sll.create_node_sll_unshift(self.selected_figure) 
        elif boton_text == "Agregar elemento al final":
            self.sll.create_node_sll_ends(self.selected_figure)  
        elif boton_text == "Eliminar elemento al inicio":
            self.sll.shift_node_sll()
        elif boton_text == "Eliminar elemento al final":
            self.sll.delete_node_sll_pop()
        elif boton_text == "Invertir la lista enlazada":
            self.sll.reverse_sll()  
        elif boton_text == "Eliminar todos los elementos":
            self.sll.remove_all_nodes()  
        elif boton_text == "Eliminar elemento en la posicion":
            self.sll.remove_node(user_number)   
        elif boton_text == "Agregar elemento a la posicion":
            self.sll.insert_value_at_index( self.selected_figure,user_number)   
        elif boton_text == "Editar elemento a la posicion":
            self.sll.update_node_value(user_number,self.selected_figure)
        elif boton_text == "Eliminar Duplicados":
            self.sll.Eliminar_duplicados()
        elif boton_text == "Unir elementos Duplicados":
            self.sll.Mostrar_continuo_dup()
