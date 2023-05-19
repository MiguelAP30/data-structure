from Botones.TextButton import TextButton
class MenuPanel:

    def __init__(self):
        boton_sll = TextButton("Single Linked List",28,(30,10))
        Boton_cartas = TextButton("Double Linked List",28,(275, 10))
        boton_pyl = TextButton("Pilas y Colas",28,(530, 10))
        boton_arb = TextButton("Arboles",28,(710, 10))
        boton_grf = TextButton("Grafos",28,(830, 10))
        self.lista_botones = [boton_sll,Boton_cartas,boton_pyl,boton_arb,boton_grf]

    def draw_menu_panel(self, screen, mouse_pos):
        for button in self.lista_botones:
            button.draw(screen,mouse_pos)

    def click_event(self, mouse_pos):
        for button in self.lista_botones:
            if button.is_mouse_contained(mouse_pos):
                return button.text
