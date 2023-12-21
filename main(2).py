import pygame,sys
#from pygame.locals import *
from image import *
from random import *
#from einsatz import *
#from main1 import*
pygame.init()
W, H = 1000, 600

class color:
    ORANGE  = ( 255, 140, 0)
    ROT     = ( 255, 0, 0)
    GRUEN_grund= ( 72, 146, 102)
    SCHWARZ = ( 0, 0, 0)
    WEISS   = ( 255, 255, 255)
    GRUEN  = (0,255,0)

skalierung = 0
skalierungswert = 1
W_karte,H_karte=70,100
W_ass_position=[0,40,40,40,40]
spielaktiv = True
Farbe=0 
karte=0
stationen=5
time=0
Station=[]
detektion_station=["Farbe:1:Herz 2:Karo 3:Kreuz 4:Pik",0,0,0,0]
end=False
runde=True

Nachziehstapel_reihenfolge=0
Nachziehstapel_zeit=1
s=0
Karte_nummer=0


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("image/assets/font.ttf", size)

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

screen=pygame.display.set_mode((W,H))
#pygame.display.set_caption("Pferderennen")
clock = pygame.time.Clock()
BG = pygame.image.load("image/assets\Background.png")
pygame.display.set_caption("Menu")

def Stationen_():
    for i in (1,2,3,4):
        detektion_station[i]-=1
    Farbe=randint(1,4)
    W_ass_position[Farbe]-=120

def Nachziehstapel_():
    x=0
    if Karte_nummer<1:
        shuffle(Nachziehstapel)
        for i in range(stationen):
            x=Nachziehstapel.pop(i)
            x[0]=pygame.transform.rotate(x[0],(90))

            Spielkarte_stationen.append(x)
        print(Nachziehstapel,"\n\n",Spielkarte_stationen)
    else:
        shuffle(Nachziehstapel)
     
def Nachziehstapel_darstellen():
    for i in range(Karte_nummer):
        Nachziehstapel_darstellen_bild=pygame.transform.scale(Nachziehstapel[i][0],(105,150))
        screen.blit(Nachziehstapel_darstellen_bild,(830+nachziehstappel_auseinander[i][0],170+nachziehstappel_auseinander[i][1]))


def game_intelation_stations():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("number of Stations ", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 250), 
                            text_input="3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 400), 
                            text_input="4", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 550),
                            text_input="5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return(3)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return(4)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return(5)
                
                

        pygame.display.update()

def game_intelation_Player():
     while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("number of players ", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 250),
                            text_input="1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 400), 
                            text_input="2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 250),
                            text_input="3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 400),
                            text_input="4", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [one_BUTTON, two_BUTTON, three_BUTTON,four_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return(1)
                if two_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return(2)
                if three_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return(3)
                if four_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return(4)
                
        pygame.display.update()

def game_intelation_einsatz(p):
    einsatz=[]
    for i in range(p+1):
        einsatz.append(0)
    
    for i in range(1,p+1,1):
        player=True
        while player:
            screen.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = get_font(35).render(f"Betting stake of player {i}", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

            one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 250),
                                text_input="5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 400), 
                                text_input="10", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 250),
                                text_input="15", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 400),
                                text_input="20", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            screen.blit(MENU_TEXT, MENU_RECT)
            for button in [one_BUTTON, two_BUTTON, three_BUTTON, four_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if one_BUTTON.checkForInput(MENU_MOUSE_POS):
                        einsatz[i]=5
                        player=False
                    if two_BUTTON.checkForInput(MENU_MOUSE_POS):
                        einsatz[i]=10
                        player=False
                    if three_BUTTON.checkForInput(MENU_MOUSE_POS):
                        einsatz[i]=15
                        player=False
                    if four_BUTTON.checkForInput(MENU_MOUSE_POS):
                        einsatz[i]=20
                        player=False

            pygame.display.update()
    return(einsatz)
def game_intrlation_horse(p):
    horse=[]
    for i in range(p+1):
        horse.append(0)
    
    
    for i in range(1,p+1,1):
        player=True
        while player:
            screen.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = get_font(50).render(f"Horse of player {i}", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

            one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 250),
                                text_input="Herz", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 400), 
                                text_input="Karo", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 250),
                                text_input="Kreuz", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 400),
                                text_input="Pik", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            screen.blit(MENU_TEXT, MENU_RECT)
            for button in [one_BUTTON, two_BUTTON, three_BUTTON, four_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if one_BUTTON.checkForInput(MENU_MOUSE_POS):
                        horse[i]=1
                        player=False
                    if two_BUTTON.checkForInput(MENU_MOUSE_POS):
                        horse[i]=2
                        player=False
                    if three_BUTTON.checkForInput(MENU_MOUSE_POS):
                        horse[i]=3
                        player=False
                    if four_BUTTON.checkForInput(MENU_MOUSE_POS):
                        horse[i]=4
                        player=False

            pygame.display.update()
    return(horse)


def play():
    W_karte,H_karte=70,100
    W_ass_position=[0,40,40,40,40]
    spielaktiv = True
    Farbe=0 
    karte=0
    stationen=game_intelation_stations()
    player=game_intelation_Player()
    einsatz=game_intelation_einsatz(player)
    horse=game_intrlation_horse(player)
    print(horse)
    time=0
    detektion_station=["Farbe:1:Herz 2:Karo 3:Kreuz 4:Pik",0,0,0,0]
    end=False
    runde=True

    Nachziehstapel_zeit=1
    Karte_nummer=0

    Station=[]
    for i in range(stationen):
        Station.append(0)
    nachziehstappel_auseinander=[]
    for i in range(48-stationen):
        nachziehstappel_auseinander.append([0,0])

    Nachziehstapel_()
    while True:

        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                print("down")
                if event.key==pygame.K_c:
                    #karte=randint(0,48)
                    #print (karte)
                    print("c Down")
                elif event.key ==pygame.K_UP:
                    #distance=-20
                    print(Farbe)
                    W_ass_position[Farbe]+=-20
            if event.type==pygame.KEYUP:
                print("UP")
                if event.key == pygame.K_c:
                    print("c UP")
                elif event.key ==pygame.K_UP:
                    distance=0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Spiellogik hier integrieren
        
        if runde==True:
            time+=1
            if time>=int(Nachziehstapel_zeit*60) and end==False :
                for i in (0,1):
                    nachziehstappel_auseinander[Karte_nummer][i]=randint(-7,7)

                for i in (1,2,3,4):
                     if Nachziehstapel[Karte_nummer][1]==i:
                        print(Nachziehstapel[Karte_nummer][1])
                        Farbe=i

                #Nachziehstapel_darstellen()
                Karte_nummer+=1


                if Karte_nummer>=48-stationen:
                    print("Mischen...\n")           
                    Nachziehstapel_()
                    Karte_nummer=0

                #Farbe=randint(1,4)

                W_ass_position[Farbe]+=120
                time=0

                if W_ass_position[Farbe]> 51+(120*stationen):
                    print("End")
                    winner=Ass[Farbe]
                    winner=pygame.transform.rotate(winner,(0))
                    winner=pygame.transform.scale(winner,(W_karte*3,H_karte*3))
                    end=True

                    print(Ass[Farbe],Farbe)

                for i in range(160,160+(120*stationen),120):
                    if W_ass_position[Farbe]==i:
                        detektion_station[Farbe]+=1
                        break
                print(detektion_station, Station)
                for i in range(stationen):
                    print(i)
                    if detektion_station[1] >=i+1 and detektion_station[2] >=i+1 and detektion_station[3] >=i+1 and detektion_station[4] >=i+1 and Station[i]!=1:

                        #Farbe=randint(1,4)
                        Farbe=Spielkarte_stationen[i][1]
                        W_ass_position[Farbe]-=120

                        if detektion_station[Farbe]!=0:
                            detektion_station[Farbe]-=1
                        Station[i]+=1

                        print(Farbe," Ass")

        # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)
        screen.fill(color.GRUEN_grund)
        if runde==True:
            Karte_größe=pygame.transform.scale(Spielkarte[karte], (140,200))
            Karte_rückseite=pygame.transform.scale(Hintergrund,(W_karte,H_karte))
            Karte_nachziestapel=pygame.transform.scale(Hintergrund,(105,150))
            Karte_rückseite=pygame.transform.rotate(Karte_rückseite,(90))
            Herz_Ass_größe=pygame.transform.scale(Herz.Ass, (W_karte,H_karte))
            Herz_Ass_größe=pygame.transform.rotate(Herz_Ass_größe,(90))
            Karo_Ass_größe=pygame.transform.scale(Karo.Ass, (W_karte,H_karte))
            Karo_Ass_größe=pygame.transform.rotate(Karo_Ass_größe,(90))
            Kreuz_Ass_größe=pygame.transform.scale(Kreuz.Ass, (W_karte,H_karte))
            Kreuz_Ass_größe=pygame.transform.rotate(Kreuz_Ass_größe,(90))
            Pik_Ass_größe=pygame.transform.scale(Pik.Ass, (W_karte,H_karte))
            Pik_Ass_größe=pygame.transform.rotate(Pik_Ass_größe,(90))

            for i in range(stationen):
                Spielkarte_stationen[i][0]=pygame.transform.scale(Spielkarte_stationen[i][0],(H_karte,W_karte))
                #Spielkarte_stationen[i][0]=pygame.transform.rotate(Spielkarte_stationen[i][0],(90))

            screen.blit(Herz_Ass_größe, (W_ass_position[1],50))
            screen.blit(Karo_Ass_größe, (W_ass_position[2],150))
            screen.blit(Kreuz_Ass_größe, (W_ass_position[3],250))
            screen.blit(Pik_Ass_größe, (W_ass_position[4],350))

            screen.blit(Karte_nachziestapel,(830,374))

            for i in range(160,160+(120*stationen),120):

                if Station[int((i-160)/120)]==1:
                    screen.blit(Spielkarte_stationen[int((i-160)/120)][0],(i,425))
                else:

                    screen.blit(Karte_rückseite,(i,425))
            for i in range(Karte_nummer):
                Nachziehstapel_darstellen_bild=pygame.transform.scale(Nachziehstapel[i][0],(105,150))
                screen.blit(Nachziehstapel_darstellen_bild,(830+nachziehstappel_auseinander[i][0],170+nachziehstappel_auseinander[i][1]))

        if end==True:
            screen.blit(winner,(W/2,H/4))
            runde=False
            main_menu()

        # Fenster aktualisieren
        pygame.display.flip()

        # Refresh-Zeiten festlegen
        clock.tick(60)

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("image/assets/Play Rect.png"), pos=(500, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("image/assets/Options Rect.png"), pos=(500, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #options()
                    pass
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()