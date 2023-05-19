import pygame, sys, webbrowser
from crupier import crupier
from player import playerx
class Pilas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100,700))
        #colores
        self.negro = (0,0,0)
        self.blanco = (255,255,255)
        self.gris = (155,155,155)
        self.verde = (0,187,45)
        self.verdeoscuro = (0,207,46)
        self.azul = (0,26,255)
        self.rojoclaro = (226,65,65)
        self.cafe = (101,30,30)
        self.morado = (128, 0, 128)
        
        #imagenes
        self.persona1= pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/tanjiro.png")
        self.persona1= pygame.transform.scale(self.persona1,(680,680))
        self.persona2= pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/naruto.png")
        self.persona2= pygame.transform.scale(self.persona2,(500,500))
        self.persona3= pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/eren.png")
        self.persona3= pygame.transform.scale(self.persona3,(600,984))
        self.fondo= pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/fondoblackjack2.jpg")
        self.fondo= pygame.transform.scale(self.fondo,(1100,700))
        self.crupier= pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/baraja3.jpg")
        self.crupier=pygame.transform.scale(self.crupier,(1200,600))
        self.cartaas=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/as.jpg")
        self.cartaas=pygame.transform.scale(self.cartaas,(120,120))
        self.carta2=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta2.jpg")
        self.carta2=pygame.transform.scale(self.carta2,(120,120))
        self.carta3=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta3.jpg")
        self.carta3=pygame.transform.scale(self.carta3,(120,120))
        self.carta4=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta4.jpg")
        self.carta4=pygame.transform.scale(self.carta4,(120,120))
        self.carta5=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta5.jpg")
        self.carta5=pygame.transform.scale(self.carta5,(120,120))
        self.carta6=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta6.jpg")
        self.carta6=pygame.transform.scale(self.carta6,(120,120))
        self.carta7=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta7.jpg")
        self.carta7=pygame.transform.scale(self.carta7,(120,120))
        self.carta8=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta8.jpg")
        self.carta8=pygame.transform.scale(self.carta8,(120,120))
        self.carta9=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta9.jpg")
        self.carta9=pygame.transform.scale(self.carta9,(120,120))
        self.carta10=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/carta10.jpg")
        self.carta10=pygame.transform.scale(self.carta10,(120,120))
        self.j=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/j.jpg")
        self.j=pygame.transform.scale(self.j,(120,120))
        self.q=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/q.jpg")
        self.q=pygame.transform.scale(self.q,(120,120))
        self.k=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/k.jpg")
        self.k=pygame.transform.scale(self.k,(120,120))
        self.alrevez=pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/alrevez.jpg")
        self.alrevez=pygame.transform.scale(self.alrevez,(120,120))
        self.flecha= pygame.image.load("C:/Users/migue/OneDrive/Documentos/UAM/SEMESTRE #3/TAD/1sem tad/2do corte/RetoPyGame/Reto/pilas/flecha.png")
        self.flecha=pygame.transform.scale(self.flecha,(86,49))
        #booleanos
        self.verificar=False
        self.clickinicio=False
        self.clickstart=False
        self.empezar=False
        self.click_pedir=False
        self.boolplantar1=False
        self.boolplantar2=False
        self.boolplantar3=False
        self.clickrestar=False
        self.turno_jugador=0
        self.booleanosplantarse=[self.boolplantar1,self.boolplantar2,self.boolplantar3]
        #lista
        self.instcrupier = crupier()
        self.player1= playerx(45,215,20,403)
        self.player2= playerx(376,381,325,574)
        self.player3= playerx(733,214,699,400)
        self.players= [self.player1,self.player2,self.player3]
        #plantarse
        self.plantar1= pygame.Rect(207,350,137,36)
        self.plantar2= pygame.Rect(551,523,137,36)
        self.plantar3= pygame.Rect(887,349,137,36)
        self.botones_plantarse=[self.plantar1,self.plantar2,self.plantar3]

    def run(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.principal()
            inicio=pygame.draw.rect(self.screen,self.rojoclaro,(930,30,128,38))
            self.boton("inicio",self.rojoclaro,inicio,0, 16, 25,self.negro,930,30,128,38)
            pygame.display.flip()
            if self.clickbotones(inicio,self.clickinicio):
                self.restart()
                return True
                from MainWindow import Window



    def principal(self):
        self.screen.blit(self.fondo,(0,0))        
        pedircartas=pygame.draw.rect(self.screen,self.azul,(450,217,180,36))
        self.imagen(440,130,self.crupier,100,200)#self.imagen(360,35,self.crupier,230,300)
        self.boton("PEDIR",self.azul,pedircartas,0, 16, 25,self.negro,450,217,180,36)

        self.imagen(100,350,self.persona1,200,200)
        self.texto("Tanjiro",self.blanco,20,160,377)
        jugador1=pygame.draw.rect(self.screen,self.negro,(207,350,137,36))       
        self.boton("PLANTAR",self.negro,jugador1,0, 16, 25,self.blanco,207,350,137,36)
        self.imagen(360,490,self.persona2,200,200)
        self.texto("Naruto",self.blanco,20,425,523)
        jugador2=pygame.draw.rect(self.screen,self.negro,(551,523,137,36))
        self.boton("PLANTAR",self.negro,jugador2,0, 16, 25,self.blanco,551,523,137,36)
        self.imagen(680,340,self.persona3,200,165)
        self.texto("Eren",self.blanco,20,780,349)
        jugador3=pygame.draw.rect(self.screen,self.negro,(887,349,137,36))
        self.boton("PLANTAR",self.negro,jugador3,0, 16, 25,self.blanco,887,349,137,36)
        self.texto("presione INICIAR para comenzar",self.blanco,20,15,32)
        start=pygame.draw.rect(self.screen,self.morado,(312,30,128,38))
        self.boton("INICIAR",self.morado,start,0, 16, 25,self.negro,312,30,128,38)
        restart=pygame.draw.rect(self.screen,self.morado,(312,90,128,38))
        self.boton("RESET",self.morado,restart,0, 16, 25,self.negro,312,90,128,38)
        if self.clickbotones(start,self.clickstart) and not self.empezar:
            self.instcrupier.barajar()
            print(self.instcrupier.baraja)
            self.repartir_cartas()
            self.actualizar_cartas_jugadores()
            self.empezar=True
        if self.empezar:
            self.empezar_partida(pedircartas,self.click_pedir)
            self.saber_turno()
            self.winer()
        if self.clickbotones(restart,self.clickrestar):
            self.restart()
        self.poner_cartas_pantalla()
        self.poner_cartas_crupier()

    def inicio(self):
        if self.clickinicio:
            return True
        else:
            return False
            
    def imagen(self,x,y,img,alto,ancho):
        img= pygame.transform.scale(img,(ancho,alto))
        self.screen.blit(img,(x,y))


    def boton(self, text, button_color, background_rect, border, border_radius, text_size, text_color,x,y,w,h):
        boton=pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Arial", text_size,True)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))
        if boton.collidepoint(pygame.mouse.get_pos()):
            boton= pygame.draw.rect(self.screen,self.verdeoscuro,(x,y,w,h),5,0)

    def texto(self, text, color, dimensiones,x,y):
        fuente=pygame.font.SysFont("Impact",dimensiones)
        superficie= fuente.render(text,True,(color))
        self.screen.blit(superficie,(x,y))

    def clickbotones(self,cuadradoboton,clickboton):
        if cuadradoboton.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not clickboton and self.verificar:
                clickboton=True
                self.verificar = False
                return True
        if not pygame.mouse.get_pressed()[0]:
            clickboton=False
            self.verificar = True
            return False
        
    def repartir_cartas(self):
        for player in self.players:
            for i in range(0,2):
                player.cartas.append(self.instcrupier.baraja.pop())
        self.instcrupier.cartas=[self.instcrupier.baraja.pop(),self.instcrupier.baraja.pop()]

    def actualizar_cartas_jugadores(self):
        for player in self.players:
            player.actualizar_cartas()
            player.actualizar_score()
        self.instcrupier.actualizar_cartas()
        self.instcrupier.actualizar_score()


    def poner_cartas_pantalla(self):
        for player in self.players:
            gap= player.x
            for carta in player.cartas:
                if carta == "as":
                    self.imagen(gap,player.y,self.cartaas,120,120)
                elif carta == "2":
                    self.imagen(gap,player.y,self.carta2,120,120)
                elif carta == "3":
                    self.imagen(gap,player.y,self.carta3,120,120)
                elif carta == "4":
                    self.imagen(gap,player.y,self.carta4,120,120)
                elif carta == "5":
                    self.imagen(gap,player.y,self.carta5,120,120)
                elif carta == "6":
                    self.imagen(gap,player.y,self.carta6,120,120)
                elif carta == "7":
                    self.imagen(gap,player.y,self.carta7,120,120)
                elif carta == "8":
                    self.imagen(gap,player.y,self.carta8,120,120)
                elif carta == "9":
                    self.imagen(gap,player.y,self.carta9,120,120)
                elif carta == "10":
                    self.imagen(gap,player.y,self.carta10,120,120)
                elif carta == "j":
                    self.imagen(gap,player.y,self.j,120,120)
                elif carta == "q":
                    self.imagen(gap,player.y,self.q,120,120)
                elif carta == "k":
                    self.imagen(gap,player.y,self.k,120,120)
                gap+=38

    def poner_cartas_crupier(self):
        gap=600
        count=1
        for carta in self.instcrupier.cartas:
            if count != len(self.instcrupier.cartas) or self.turno_jugador>2:
                if carta == "as":
                    self.imagen(gap,68,self.cartaas,120,120)
                elif carta == "2":
                    self.imagen(gap,68,self.carta2,120,120)
                elif carta == "3":
                    self.imagen(gap,68,self.carta3,120,120)
                elif carta == "4":
                    self.imagen(gap,68,self.carta4,120,120)
                elif carta == "5":
                    self.imagen(gap,68,self.carta5,120,120)
                elif carta == "6":
                    self.imagen(gap,68,self.carta6,120,120)
                elif carta == "7":
                    self.imagen(gap,68,self.carta7,120,120)
                elif carta == "8":
                    self.imagen(gap,68,self.carta8,120,120)
                elif carta == "9":
                    self.imagen(gap,68,self.carta9,120,120)
                elif carta == "10":
                    self.imagen(gap,68,self.carta10,120,120)
                elif carta == "j":
                    self.imagen(gap,68,self.j,120,120)
                elif carta == "q":
                    self.imagen(gap,68,self.q,120,120)
                elif carta == "k":
                    self.imagen(gap,68,self.k,120,120)
            else:
                self.imagen(gap,68,self.alrevez,120,120)
            gap+=38
            count+=1
        
    def empezar_partida(self,cuadradopedir,boolpedir):
        if not self.turno_jugador>2:
            player=self.players[self.turno_jugador]
            if self.clickbotones(cuadradopedir,boolpedir) and not player.score > 21:
                player.cartas.append(self.instcrupier.baraja.pop())
                player.actualizar_cartas()
                player.actualizar_score()
                self.poner_cartas_pantalla()
            elif self.clickbotones(self.botones_plantarse[self.turno_jugador],self.booleanosplantarse[self.turno_jugador]) or player.score>=21:
                self.poner_cartas_pantalla()
                self.turno_jugador +=1 
            elif self.players[2].score>=21:
                self.turno_crupier()
        else:
            self.turno_crupier()

    def turno_crupier(self):
        while self.instcrupier.score < 17:
            self.instcrupier.cartas.append(self.instcrupier.baraja.pop())
            self.instcrupier.actualizar_cartas()
            self.instcrupier.actualizar_score()
            
    
    def saber_turno(self):
        if self.turno_jugador==0:
            self.imagen(2,349,self.flecha,49,86)
        elif self.turno_jugador==1:
            self.imagen(315,510,self.flecha,49,86)
        elif self.turno_jugador==2:
            self.imagen(688,377,self.flecha,49,86)

    def winer(self):
        for player in self.players:
            if player.score>21:
                self.texto("superaste los 21, perdiste",self.azul,20,player.textox,player.textoy)
            elif player.score==self.instcrupier.score and self.turno_jugador>2:
                self.texto("tu puntaje es igual al del crupier, empataste",self.azul,20,player.textox,player.textoy)
            elif player.score>self.instcrupier.score and self.turno_jugador>2 and self.instcrupier.score<21:
                self.texto("tu puntaje es superior al del crupier, WINER",self.verde,20,player.textox,player.textoy)
            elif player.score==21:
                self.texto("Blackjack, WINER",self.verde,20,player.textox,player.textoy)
            elif self.turno_jugador>2 and player.score<self.instcrupier.score and self.instcrupier.score<=21:
                self.texto("tu puntaje es inferior al del crupier, perdiste",self.azul,20,player.textox,player.textoy)
            elif player.score<=21 and self.instcrupier.score>21:
                self.texto("el crupier paso los 21, WINER",self.verde,20,player.textox,player.textoy)

    def restart(self):
        for player in self.players:
            player.cartas.clear()
            player.score=0
        self.instcrupier.baraja.clear()
        self.instcrupier.cartas.clear()
        self.instcrupier.score=0
        self.empezar=False
        self.turno_jugador=0
        print(self.instcrupier.baraja)

init = Pilas()
init.run()