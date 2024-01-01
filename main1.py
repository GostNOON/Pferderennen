import pygame
#from pygame.locals import *
from image import *
from random import *
#from einsatz import *

pygame.init()

#Variablen
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
stationen=3
time=0
Station=[]
detektion_station=["Farbe:1:Herz 2:Karo 3:Kreuz 4:Pik",0,0,0,0]
end=False
runde=True

Nachziehstapel_reihenfolge=0
Nachziehstapel_zeit=1
s=0
Karte_nummer=0

for i in range(48-stationen):
    nachziehstappel_auseinander.append([0,0])

"""for i in range(52-stationen):
    s=randint(0,52-stationen-i)
    Nachziehstapel.append(Spielkarten[s])
    Spielkarten.pop(s)"""

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
pygame.display.set_caption("Pferderennen")
clock = pygame.time.Clock()

def Stationen_():
    for i in (1,2,3,4):
        detektion_station[i]-=1
    Farbe=randint(1,4)
    W_ass_position[Farbe]-=120
def Station_():
    x=0
    

def Nachziehstapel_():
    x=0
    if Karte_nummer<1:
        shuffle(Nachziehstapel)
        """for i in range(48):
            Nachziehstapel_reihenfolge=randint(0,48-i)
            #print(Nachziehstapel_reihenfolge)
            #print(Spielkarten_mit_werten_ablage)
            s=Spielkarten_mit_werten_ablage.pop(Nachziehstapel_reihenfolge-1)
            #print(Spielkarten_mit_werten_ablage)
            #print(s)
            Nachziehstapel.append(s)"""        
        for i in range(stationen):
            x=Nachziehstapel.pop(i)
            x[0]=pygame.transform.rotate(x[0],(90))

            Spielkarte_stationen.append(x)
        #Spielkarte_stationen+=Nachziehstapel[0:stationen]
        print(Nachziehstapel,"\n\n",Spielkarte_stationen)
    else:
        shuffle(Nachziehstapel)
        """for i in range(len(Nachziehstapel)):
            y=Nachziehstapel.pop(0)
            zwischenablage.append(y)
        for i in range (len(zwischenablage)):
            o=randint(0,len(zwischenablage))
            Nachziehstapel.append(zwischenablage[o-1])
            l=zwischenablage.pop(o-1)"""
        
    #print(Nachziehstapel,"\n")

def Nachziehstapel_darstellen():
    for i in range(Karte_nummer):
            Nachziehstapel_darstellen_bild=pygame.transform.scale(Nachziehstapel[i][0],(105,150))
            screen.blit(Nachziehstapel_darstellen_bild,(830+nachziehstappel_auseinander[i][0],170+nachziehstappel_auseinander[i][1]))

Nachziehstapel_()

for i in range(stationen):
    Station.append(0)
print(Station)

while spielaktiv:
    
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            spielaktiv = False
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
            """
        if Nachziehstapel[Karte_nummer][1]==1:
            print(Nachziehstapel[Karte_nummer][1])
            Farbe=1

        elif Nachziehstapel[Karte_nummer][1]==2:
            print(Nachziehstapel[Karte_nummer][1])
            Farbe=2

        elif Nachziehstapel[Karte_nummer][1]==3:
             print(Nachziehstapel[Karte_nummer][1])
             Farbe=3

        elif Nachziehstapel[Karte_nummer][1]==4:
             print(Nachziehstapel[Karte_nummer][1])
             Farbe=4
        """

            #Nachziehstapel_darstellen()
            Karte_nummer+=1


            if Karte_nummer>=48-stationen:
                print("Mischen...\n")           
                Nachziehstapel_()
                Karte_nummer=0

            #Farbe=randint(1,4)

            W_ass_position[Farbe]+=160
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
                    """for a in (1,2,3,4):
                    detektion_station[a]-=1"""

                    #Farbe=randint(1,4)
                    Farbe=Spielkarte_stationen[i][1]
                    W_ass_position[Farbe]-=160

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



        """Spielkarte_stationen[0][0]=pygame.transform.scale(Spielkarte_stationen[0][0],(W_karte,H_karte))
        Spielkarte_stationen[0][0]=pygame.transform.rotate(Spielkarte_stationen[0][0],(90))
        Spielkarte_stationen[0][0]=pygame.transform.rotate(Spielkarte_stationen[0][0],(180))

        Station1=pygame.transform.scale(Spielkarte_stationen[1][0],(W_karte,H_karte))
        Station2=pygame.transform.scale(Spielkarte_stationen[2][0],(W_karte,H_karte))
        Station3=pygame.transform.scale(Spielkarte_stationen[3][0],(W_karte,H_karte))
        Station4=pygame.transform.scale(Spielkarte_stationen[4][0],(W_karte,H_karte))
        Station5=pygame.transform.scale(Spielkarte_stationen[5][0],(W_karte,H_karte))
        Station6=pygame.transform.scale(Spielkarte_stationen[6][0],(W_karte,H_karte))
        Station7=pygame.transform.scale(Spielkarte_stationen[7][0],(W_karte,H_karte))
        Station8=pygame.transform.scale(Spielkarte_stationen[8][0],(W_karte,H_karte))
        Station1=pygame.transform.rotate(Spielkarte_stationen[1],(90))
        Station2=pygame.transform.rotate(Spielkarte_stationen[2],(90))
        Station3=pygame.transform.rotate(Spielkarte_stationen[3],(90))
        Station4=pygame.transform.rotate(Spielkarte_stationen[4],(90))
        Station5=pygame.transform.rotate(Spielkarte_stationen[5],(90))
        Station6=pygame.transform.rotate(Spielkarte_stationen[6],(90))
        Station7=pygame.transform.rotate(Spielkarte_stationen[7],(90))
        Station8=pygame.transform.rotate(Spielkarte_stationen[8],(90))"""

        screen.blit(Herz_Ass_größe, (W_ass_position[1],50))
        screen.blit(Karo_Ass_größe, (W_ass_position[2],150))
        screen.blit(Kreuz_Ass_größe, (W_ass_position[3],250))
        screen.blit(Pik_Ass_größe, (W_ass_position[4],350))

        screen.blit(Karte_nachziestapel,(830,374))

        for i in range(200,200+(160*stationen),160):

            if Station[int((i-200)/160)]==1:
                screen.blit(Spielkarte_stationen[int((i-200)/160)][0],(i,425))
            else:

                screen.blit(Karte_rückseite,(i,425))
        Nachziehstapel_darstellen()


    if end==True:
        screen.blit(winner,(W/2,H/4))
        runde=False

        #print(Ass[Farbe+1])
    """screen.blit(Karte_rückseite,(280,425))
    screen.blit(Karte_rückseite,(400,425))"""

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()