import pygame
from pygame.locals import *
from image import *
from random import randint

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
stationen=5
time=0
Station=[]
detektion_station=["Farbe:1:Herz 2:Karo 3:Kreuz 4:Pik",0,0,0,0]
Nachziehstapel=[]
Nachziehstapel_reihenfolge=0
Nachziehstapel_zeit=120

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

for i in range(48-stationen):
    Nachziehstapel_reihenfolge=randint(0,48-stationen)
    Nachziehstapel.append(Spielkarten[Nachziehstapel_reihenfolge])
print(Nachziehstapel)
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
    time+=1
    if time>=Nachziehstapel_zeit:

        Farbe=randint(1,4)

        W_ass_position[Farbe]+=120
        time=0
        if W_ass_position[Farbe]> 51+(120*stationen):
            print("End")
            
            spielaktiv=False
            print(Ass[Farbe+1],Farbe)
            
            break
        for i in range(160,160+(120*stationen),120):
            if W_ass_position[Farbe]==i:
                detektion_station[Farbe]+=1
                break
        print(detektion_station, Station)
        for i in range(stationen):
            if detektion_station[1] >=i+1 and detektion_station[2] >=i+1 and detektion_station[3] >=i+1 and detektion_station[4] >=i+1 and Station[i]!=1:
                for a in (1,2,3,4):
                    detektion_station[a]-=1
                Farbe=randint(1,4)
                W_ass_position[Farbe]-=120
                if detektion_station[Farbe]!=0:
                    detektion_station[Farbe]-=1
                Station[i]+=1
                
                print(Farbe," Ass")
                
            

    # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)
    screen.fill(color.GRUEN_grund)

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

    screen.blit(Herz_Ass_größe, (W_ass_position[1],50))
    screen.blit(Karo_Ass_größe, (W_ass_position[2],150))
    screen.blit(Kreuz_Ass_größe, (W_ass_position[3],250))
    screen.blit(Pik_Ass_größe, (W_ass_position[4],350))

    screen.blit(Karte_nachziestapel,(830,374))

    for i in range(160,160+(120*stationen),120):
        
        screen.blit(Karte_rückseite,(i,425))
    
    if spielaktiv==False:
        print(Ass[Farbe+1])
    """screen.blit(Karte_rückseite,(280,425))
    screen.blit(Karte_rückseite,(400,425))"""

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()