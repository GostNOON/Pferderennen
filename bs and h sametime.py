import pygame,sys

pygame.init()

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

screen=pygame.display.set_mode((1000,600))
#pygame.display.set_caption("Pferderennen")
clock = pygame.time.Clock()
BG = pygame.image.load("image/assets\Background.png")			

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

        if h==1: one_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 180),
                            text_input="Herz", font=get_font(75), base_color="#d7fcd4", hovering_color="Blue")
        else: one_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 180),
                            text_input="Herz", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        if h==2: two_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 300),
                            text_input="Karo", font=get_font(75), base_color="#d7fcd4", hovering_color="Blue")
        else:two_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 300), 
                            text_input="Karo", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        if h==3: three_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 420),
                            text_input="Kreuz", font=get_font(65), base_color="#d7fcd4", hovering_color="Blue")
        else:three_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 420),
                            text_input="Kreuz", font=get_font(65), base_color="#d1fcd4", hovering_color="White")
        if h==4: four_BUTTON= Button(image=pygame.image.load("image/assets/Quit Rect select.png"), pos=(250, 540),
                            text_input="Pik", font=get_font(75), base_color="#d7fcd4", hovering_color="Blue")
        else:four_BUTTON = Button(image=pygame.image.load("image/assets/Quit Rect.png"), pos=(250, 540),
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
                    pass
                if active==True:
                    if event.key==pygame.K_BACKSPACE:
                        user_text =user_text[:-1]
                    elif event.key==pygame.K_RETURN:
                        active=False
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
                else:
                    active=False
                
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
                    pass

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
        screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
        input_rect.w=max(140*2,text_surface.get_width()+10)
        pygame.display.update()
    
    
print(bg(0))
