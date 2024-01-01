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


def Back():

       OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
       OPTIONS_BACK = Button(image=None, pos=(850, 550), 
                           text_input="Zurück", font=get_font(45), base_color="Black", hovering_color="Green")
       
       OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
       
       for event in pygame.event.get():
           if event.type == pygame.MOUSEBUTTONDOWN:
               if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                   main_menu()

def Stationen_():
    for i in (1,2,3,4):
        detektion_station[i]-=1
    Farbe=randint(1,4)
    W_ass_position[Farbe]-=120

def Nachziehstapel_(Stationen):
    x=0
    if Karte_nummer<1:
        shuffle(Nachziehstapel)
        for i in range(Stationen):
            x=Nachziehstapel.pop(-1)
            x[0]=pygame.transform.rotate(x[0],(90))
            print(i)

            Spielkarte_stationen.append(x)
        print(Nachziehstapel,"\n\n",Spielkarte_stationen)
    else:
        shuffle(Nachziehstapel)
     
def Nachziehstapel_darstellen():
    for i in range(Karte_nummer):
        Nachziehstapel_darstellen_bild=pygame.transform.scale(Nachziehstapel[i][0],(105,150))
        screen.blit(Nachziehstapel_darstellen_bild,(830+nachziehstappel_auseinander[i][0],170+nachziehstappel_auseinander[i][1]))


def game_intelation_stations():
    f=open("txt/Stations.txt","r")
    lines=f.readlines()
    f.close()
    while True:
        screen.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("Anzahl Stationen", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 80))

        PLAY_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 200), 
                            text_input=str(int(lines[0])), font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 350), 
                            text_input=str(int(lines[1])), font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 500),
                            text_input=str(int(lines[2])), font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(850, 550), 
                            text_input="Zurück", font=get_font(45), base_color="Black", hovering_color="Green")
        
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON,OPTIONS_BACK]:
            button.changeColor(MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    return(int(lines[0]))
                if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                    return(int(lines[1]))
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    return(int(lines[2]))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(MOUSE_POS):
                        main_menu()
                

        pygame.display.update()
def game_intelation_horse_betting_stake(p):
    player_betting_stake=[]
    for i in range(p):
        player_betting_stake.append(game_intelation_horse_betting_stake_pbg(i))
    return(player_betting_stake)

def Horse(i):
    h=0
    player=True
    while player:
        screen.blit(BG, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render(f"Horse of player {i+1}", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))
        
        one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 250),
                            text_input="Herz", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 400), 
                            text_input="Karo", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 250),
                            text_input="Kreuz", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 400),
                            text_input="Pik", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(800, 550), 
                            text_input="Zurück", font=get_font(60), base_color="Black", hovering_color="Green")
        screen.blit(MENU_TEXT, MENU_RECT)
        
        for button in [one_BUTTON, two_BUTTON, three_BUTTON, four_BUTTON,OPTIONS_BACK]:
            button.changeColor(MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_BUTTON.checkForInput(MOUSE_POS):
                    h=1
                    player=False
                if two_BUTTON.checkForInput(MOUSE_POS):
                    h=2
                    player=False
                if three_BUTTON.checkForInput(MOUSE_POS):
                    h=3
                    player=False
                if four_BUTTON.checkForInput(MOUSE_POS):
                    h=4
                    player=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(MOUSE_POS):
                        play()
        pygame.display.update()
    print(h)
    return(h)

def Betting_stake(i):
    BT=0
    player=True
    while player:
        screen.blit(BG, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(35).render(f"Einsatz Spieler {i+1}", True, "#b68f40")
        #MENU_TEXT2 = get_font(35).render(f"Horse {}", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))
        #MENU_RECT2 = MENU_TEXT2.get_rect(center=(500, 100))

        one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 250),
                            text_input="5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 400), 
                            text_input="10", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 250),
                            text_input="15", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 400),
                            text_input="20", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(850, 550), 
                            text_input="BACK", font=get_font(45), base_color="Black", hovering_color="Green")
        
        screen.blit(MENU_TEXT, MENU_RECT)
        #screen.blit(MENU_TEXT2, MENU_RECT2)

        for button in [one_BUTTON, two_BUTTON, three_BUTTON, four_BUTTON,OPTIONS_BACK]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_BUTTON.checkForInput(MOUSE_POS):
                    BT=5
                    player=False
                if two_BUTTON.checkForInput(MOUSE_POS):
                    BT=10
                    player=False
                if three_BUTTON.checkForInput(MOUSE_POS):
                    BT=15
                    player=False
                if four_BUTTON.checkForInput(MOUSE_POS):
                    BT=20
                    player=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(MOUSE_POS):
                        play()
        pygame.display.update()
    return(BT)

def game_intelation_Player():
    player_sheet= open("txt/player.txt")
    player_button_lines=player_sheet.readlines()
    
    while True:
        screen.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("Spieleranzahl", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 250),
                            text_input=player_button_lines[0], font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 400), 
                            text_input=player_button_lines[1], font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 250),
                            text_input=player_button_lines[2], font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(750, 400),
                            text_input=player_button_lines[3], font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(850, 550), 
                            text_input="zurück", font=get_font(45), base_color="Black", hovering_color="Green")
        
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [one_BUTTON, two_BUTTON, three_BUTTON,four_BUTTON,OPTIONS_BACK]:
            button.changeColor(MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_BUTTON.checkForInput(MOUSE_POS):
                    player_sheet.close()
                    return(int(player_button_lines[0]))
                if two_BUTTON.checkForInput(MOUSE_POS):
                    player_sheet.close()
                    return(int(player_button_lines[1]))
                if three_BUTTON.checkForInput(MOUSE_POS):
                    player_sheet.close()
                    return(int(player_button_lines[2]))
                if four_BUTTON.checkForInput(MOUSE_POS):
                    player_sheet.close()
                    return(int(player_button_lines[3]))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(MOUSE_POS):
                        player_sheet.close()
                        game_intelation_stations()
        pygame.display.update()

def game_intelation_Player_keybord_input():
    base_font=pygame.font.Font(None,32*6)
    user_text=''

    input_rect=pygame.Rect(350,200,140,32*4)
    

    color_active = pygame.Color('Green')
    color_passiv= pygame.Color('white')
    color=color_passiv

    active=False

    while True:
        MENU_TEXT = get_font(50).render("Spieleranzahl", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))
        screen.fill((0,0,0))
        forward_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 500),
                                text_input="Weiter", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        forward_BUTTON.changeColor(pygame.mouse.get_pos())
        forward_BUTTON.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                
                if input_rect.collidepoint(event.pos):
                    active=True
                    user_text=""
                else:
                    active=False
                    if len(user_text)<1:
                            user_text="1"

                if forward_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    try:
                        return(int(user_text))
                    except:
                         pass

            if event.type==pygame.KEYDOWN:
                if active==True:
                    if event.key==pygame.K_BACKSPACE:
                        user_text =user_text[:-1]
                    elif event.key==pygame.K_RETURN:
                        active=False
                        if len(user_text)<1:
                            user_text="1"
                        try:
                            return(int(user_text))
                        except:
                            pass
                    else:
                        try:
                            input_=int(event.unicode)
                            user_text+=str(input_)
                        except:
                            pass
                
        if active:
            color=color_active
        else:
            color=color_passiv

        pygame.draw.rect(screen,color,input_rect,2)
        
        screen.blit(MENU_TEXT, MENU_RECT)
        text_surface=base_font.render(user_text,True,(255,255,255))
        try:
            screen.blit(text_surface,(input_rect.x+(100/len(user_text)),input_rect.y+5))
        except:
            screen.blit(text_surface,(input_rect.x+100,input_rect.y+5))
        input_rect.w=max(140*2,text_surface.get_width()+70)

        pygame.display.update()
def game_intelation_horse_betting_stake_pbg(i):
    
    h=0
    player=True
    base_font=pygame.font.Font(None,32*6)
    user_text=''

    input_rect=pygame.Rect(550,200,140,32*4)
    

    color_active = pygame.Color('Green')
    color_passiv= pygame.Color('white')
    color=color_passiv

    active=False
    while player:
        screen.blit(BG, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(45).render(f"Einsatz für Spieler {i+1}", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 75))
        einsatz_TEXT = get_font(25).render("Anzahl Schlücke:", True, "#b68f40")
        einsatz_RECT = MENU_TEXT.get_rect(center=(970, 190))

        if h==1: one_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 170),
                            text_input="Herz", font=get_font(75), base_color="#d7fcd4", hovering_color="Blue")
        else: one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 170),
                            text_input="Herz", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        if h==2: two_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 290),
                            text_input="Karo", font=get_font(75), base_color="#d7fcd4", hovering_color="Blue")
        else:two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 290), 
                            text_input="Karo", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        if h==3: three_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 410),
                            text_input="Kreuz", font=get_font(65), base_color="#d7fcd4", hovering_color="Blue")
        else:three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 410),
                            text_input="Kreuz", font=get_font(65), base_color="#d1fcd4", hovering_color="White")
        if h==4: four_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 530),
                            text_input="Pik", font=get_font(75), base_color="#d7fcd4", hovering_color="Blue")
        else:four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 530),
                            text_input="Pik", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(800, 550), 
                            text_input="Zurück", font=get_font(60), base_color="Black", hovering_color="Green")
        OPTIONS_FORWARD = Button(image=None, pos=(800, 470),
                            text_input="weiter", font=get_font(60), base_color="Black", hovering_color="Green")

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(einsatz_TEXT,einsatz_RECT)

        for button in [one_BUTTON, two_BUTTON, three_BUTTON, four_BUTTON,OPTIONS_BACK,OPTIONS_FORWARD]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if active==True:
                    if event.key==pygame.K_BACKSPACE:
                        user_text =user_text[:-1]
                    elif event.key==pygame.K_RETURN:
                        active=False
                        if len(user_text)<1:
                            user_text="1"
                        try:
                            return([h,int(user_text)])
                        except:
                             pass
                        
                            
                    else:
                        try:
                            input_=int(event.unicode)
                            user_text+=str(input_)
                        except:
                            pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active=True
                    user_text=""
                else:
                    active=False
                    if len(user_text)<1:
                        user_text="1"
                
                if one_BUTTON.checkForInput(MOUSE_POS):
                    if h==1:
                        one_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 200),
                            text_input="Herz", font=get_font(75), base_color="#d7fcd4", hovering_color="Blue")
                    h=1

                if two_BUTTON.checkForInput(MOUSE_POS):
                    h=2

                if three_BUTTON.checkForInput(MOUSE_POS):
                    h=3

                if four_BUTTON.checkForInput(MOUSE_POS):
                    h=4

                if OPTIONS_BACK.checkForInput(MOUSE_POS):
                    play()

                if OPTIONS_FORWARD.checkForInput(MOUSE_POS):
                    player=False
                    try:
                        return([h,int(user_text)])
                    except:
                         player=True

                #play()
        if active:
            color=color_active
        else:
            color=color_passiv

        pygame.draw.rect(screen,color,input_rect,2)
        
        
        text_surface=base_font.render(user_text,True,(255,255,255))
        try:
            screen.blit(text_surface,(input_rect.x+(100/len(user_text)),input_rect.y+5))
        except:
            screen.blit(text_surface,(input_rect.x+100,input_rect.y+5))
        input_rect.w=max(140*2,text_surface.get_width()+70)
        pygame.display.update()

def play():
    pygame.display.set_caption("Game")
    W_karte,H_karte=70,100
    W_ass_position=[0,40,40,40,40]
    spielaktiv = True
    Farbe=0 
    karte=0
    stationen=game_intelation_stations()
    stationen_abstand=600//stationen
    stationen_H,stationen_W=10,10
    print (stationen_abstand)

    player=game_intelation_Player_keybord_input()
    horse_betting_skake=game_intelation_horse_betting_stake(player)
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

    Nachziehstapel_(stationen)
    time_txt=open("txt/zeit.txt","r")
    x=int(time_txt.read())
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
                if end==True:
                    if event.key==pygame.K_SPACE:
                        main_menu()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        main_menu()
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
            
            
            if time>=x*60 and end==False :
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

                W_ass_position[Farbe]+=stationen_abstand
                time=0

                if W_ass_position[Farbe]> 51+(stationen_abstand*stationen):
                    print("End")
                    time_txt.close()
                    winner=Ass[Farbe]
                    winner=pygame.transform.rotate(winner,(0))
                    winner=pygame.transform.scale(winner,(W_karte*3,H_karte*3))
                    end=True
                    

                    print(Ass[Farbe],Farbe)

                for i in range(stationen):
                    if W_ass_position[Farbe]==(i*stationen_abstand)+(stationen_abstand+40):
                        detektion_station[Farbe]+=1
                        break
                print(detektion_station, Station)
                for i in range(stationen):
                    print(i)
                    if detektion_station[1] >=i+1 and detektion_station[2] >=i+1 and detektion_station[3] >=i+1 and detektion_station[4] >=i+1 and Station[i]!=1:

                        #Farbe=randint(1,4)
                        Farbe=Spielkarte_stationen[i][1]
                        W_ass_position[Farbe]-=stationen_abstand

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

            for i in range(stationen_abstand+40,stationen_abstand+40+(stationen_abstand*stationen),stationen_abstand):

                if Station[int((i-(stationen_abstand+40))/stationen_abstand)]==1:
                    screen.blit(Spielkarte_stationen[int((i-(stationen_abstand+40))/stationen_abstand)][0],(i,425))
                else:

                    screen.blit(Karte_rückseite,(i,425))
            
            for i in range(Karte_nummer):
                Nachziehstapel_darstellen_bild=pygame.transform.scale(Nachziehstapel[i][0],(105,150))
                screen.blit(Nachziehstapel_darstellen_bild,(830+nachziehstappel_auseinander[i][0],170+nachziehstappel_auseinander[i][1]))

        if end==True:
            screen.blit(winner,(W/2+200,H/4))
            runde=False
            swallowes=0
            for i in range(player):
                if horse_betting_skake[i][0]==Farbe:
                    TEXT = get_font(40).render(f"Spieler {i+1} hat gewonnen!!!", True, "#b68f40")
                    RECT = TEXT.get_rect(center=(300, 50+50*i))
                    screen.blit(TEXT,RECT)
                
                swallowes+=horse_betting_skake[i][1]
                    
            TEXT2 = get_font(40).render(f"schlücke: {swallowes} ", True, "#b68f40")
            RECT2 = TEXT2.get_rect(center=(300,300))
            screen.blit(TEXT2,RECT2)



        # Fenster aktualisieren
        pygame.display.flip()

        # Refresh-Zeiten festlegen
        clock.tick(60)
def options():
    pygame.display.set_caption("Optionen")
    file=open("txt/Stations.txt","r")
    inhalt=file.readlines()

    base_font=pygame.font.Font(None,32*4)
    user_text1=str(int(inhalt[0]))
    user_text2=str(int(inhalt[1]))
    user_text3=str(int(inhalt[2]))
    
    file=open("txt/Stations.txt","w")
    file2=open("txt/zeit.txt","r")
    user_text_time=file2.read()
    file2=open("txt/zeit.txt","w")

    input_rect1=pygame.Rect(150,150,140,31*3)
    input_rect2=pygame.Rect(150,300,140,31*3)
    input_rect3=pygame.Rect(150,450,140,31*3)
    input_rect_time=pygame.Rect(580,150,140,32*3)

    color_active = pygame.Color('Green')
    color_passiv= pygame.Color('white')
    color1=color_passiv
    color2=color_passiv
    color3=color_passiv
    color_time=color_passiv

    active1=False
    active2=False
    active3=False
    active_time=False

    while True:
        screen.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(60).render("Optionen", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 80))

        OPTIONS_BACK = Button(image=None, pos=(850, 550),
                            text_input="BACK", font=get_font(45), base_color="Black", hovering_color="Green")
        
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [OPTIONS_BACK]:
            button.changeColor(MOUSE_POS)
            button.update(screen)
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file.write(f"{user_text1}\n{user_text2}\n{user_text3}")
                file2.write(f"{user_text_time}")
                file.close(),file2.close()
                pygame.quit()
                sys.exit()
            
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if input_rect_time.collidepoint(event.pos):
                    active_time=True
                    user_text_time=""
                else:
                    if len(user_text_time)<1:
                        user_text_time="1"
                    active_time=False

                if input_rect1.collidepoint(event.pos):
                    active1=True
                    user_text1=""
                else:
                    active1=False
                    if len(user_text1)<1:
                        user_text1="1"
                    

                if input_rect2.collidepoint(event.pos):
                    active2=True
                    user_text2=""
                else:
                    active2=False
                    if len(user_text2)<1:
                        user_text2="1"
                                   
                if input_rect3.collidepoint(event.pos):
                    active3=True
                    user_text3=""
                else:
                    active3=False
                    if len(user_text3)<1:
                        user_text3="1"

                if OPTIONS_BACK.checkForInput(MOUSE_POS):
                    
                    file.write(f"{user_text1}\n{user_text2}\n{user_text3}")
                    file2.write(f"{user_text_time}")
                    file.close(),file2.close()
                    main_menu()

            if event.type==pygame.KEYDOWN:
                #Einstellung1
                if active1==True:
                    if event.key==pygame.K_BACKSPACE:
                        user_text1 =user_text1[:-1]
                    elif event.key==pygame.K_RETURN:
                        active1=False
                        if len(user_text1)<1:
                            user_text1="1"
                    else:
                        try:
                            input_=int(event.unicode)
                            user_text1+=str(input_)
                        except:
                            pass
                #Einstellung2
                if active2==True:
                    if event.key==pygame.K_BACKSPACE:
                        user_text2 =user_text2[:-1]
                    elif event.key==pygame.K_RETURN:
                        active2=False
                        if len(user_text2)<1:
                            user_text2="1"
                    else:
                        try:
                            input_=int(event.unicode)
                            user_text2+=str(input_)
                        except:
                            pass
            #einstellung3
                if active3==True:
                    if event.key==pygame.K_BACKSPACE:
                        user_text3 =user_text3[:-1]
                    elif event.key==pygame.K_RETURN:
                        active3=False
                        if len(user_text3)<1:
                            user_text3="1"
                    else:
                        try:
                            input_=int(event.unicode)
                            user_text3+=str(input_)
                        except:
                            pass

                if active_time==True:
                    if event.key==pygame.K_BACKSPACE:
                        user_text_time =user_text_time[:-1]
                    elif event.key==pygame.K_RETURN:
                        active_time=False
                        if len(user_text_time)<1:
                            user_text_time="1"
                    else:
                        try:
                            input_=int(event.unicode)
                            user_text_time+=str(input_)
                        except:
                            pass
        if active1:color1=color_active
        else:color1=color_passiv

        if active2:color2=color_active
        else:color2=color_passiv

        if active3:color3=color_active
        else:color3=color_passiv

        if active_time:color_time=color_active
        else:color_time=color_passiv

        pygame.draw.rect(screen,color1,input_rect1,2)
        pygame.draw.rect(screen,color2,input_rect2,2)
        pygame.draw.rect(screen,color3,input_rect3,2)
        pygame.draw.rect(screen,color_time,input_rect_time,2)
        

        station1_TEXT = get_font(20).render("Station Option Nr.1", True, "#b68f40")
        station1_RECT = station1_TEXT.get_rect(center=(220, 130))
        screen.blit(station1_TEXT, station1_RECT)

        text_surface=base_font.render(user_text1,True,(255,255,255))
        screen.blit(text_surface,(input_rect1.x+15,input_rect1.y+5))
        input_rect1.w=max(80,text_surface.get_width()+20)

        station2_TEXT = get_font(20).render("Station Option Nr.2", True, "#b68f40")
        station2_RECT = station2_TEXT.get_rect(center=(220, 270))
        screen.blit(station2_TEXT, station2_RECT)

        text_surface=base_font.render(user_text2,True,(255,255,255))
        screen.blit(text_surface,(input_rect2.x+15,input_rect2.y+5))
        input_rect2.w=max(80,text_surface.get_width()+20)

        station3_TEXT = get_font(20).render("Station Option Nr.3", True, "#b68f40")
        station3_RECT = station3_TEXT.get_rect(center=(220, 420))
        screen.blit(station3_TEXT, station3_RECT)

        text_surface=base_font.render(user_text3,True,(255,255,255))
        screen.blit(text_surface,(input_rect3.x+15,input_rect3.y+5))
        input_rect3.w=max(80,text_surface.get_width()+20)


        station_time_TEXT = get_font(25).render("Zeiteinstellung:", True, "#b68f40")
        station_time_RECT = station_time_TEXT.get_rect(center=(700, 130))
        screen.blit(station_time_TEXT, station_time_RECT)

        text_surface=base_font.render(f"{user_text_time} sek",True,(255,255,255))
        screen.blit(text_surface,(input_rect_time.x+15,input_rect_time.y+5))
        input_rect_time.w=max(80,text_surface.get_width()+25)

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")
    while True:
        screen.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("image/assets/Play Rect.png"), pos=(500, 250), 
                            text_input="SPIEL", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("image/assets/Options Rect.png"), pos=(500, 400), 
                            text_input="OPTIONEN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(500, 550), 
                            text_input="ENDE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                    options()
                    
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()