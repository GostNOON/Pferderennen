import pygame
from pygame.locals import *


#lädt alle Bilder
class Herz():
    Ass=pygame.image.load("image/Herz/Ass.png")
    zwei=pygame.image.load("image/Herz/2.png")
    drei=pygame.image.load("image/Herz/3.png")
    vier=pygame.image.load("image/Herz/4.png")
    fünf=pygame.image.load("image/Herz/5.png")
    sechs=pygame.image.load("image/Herz/6.png")
    sieben=pygame.image.load("image/Herz/7.png")
    acht=pygame.image.load("image/Herz/8.png")
    neun=pygame.image.load("image/Herz/9.png")
    zehn=pygame.image.load("image/Herz/10.png")
    Bube=pygame.image.load("image/Herz/Bube.png")
    Dame=pygame.image.load("image/Herz/Dame.png")
    König=pygame.image.load("image/Herz/König.png")

class Karo():
    Ass=pygame.image.load("image/Karo/Ass.png")
    zwei=pygame.image.load("image/Karo/2.png")
    drei=pygame.image.load("image/Karo/3.png")
    vier=pygame.image.load("image/Karo/4.png")
    fünf=pygame.image.load("image/Karo/5.png")
    sechs=pygame.image.load("image/Karo/6.png")
    sieben=pygame.image.load("image/Karo/7.png")
    acht=pygame.image.load("image/Karo/8.png")
    neun=pygame.image.load("image/Karo/9.png")
    zehn=pygame.image.load("image/Karo/10.png")
    Bube=pygame.image.load("image/Karo/Bube.png")
    Dame=pygame.image.load("image/Karo/Dame.png")
    König=pygame.image.load("image/Karo/König.png")

class Kreuz():
    Ass=pygame.image.load("image/Kreuz/Ass.png")
    zwei=pygame.image.load("image/Kreuz/2.png")
    drei=pygame.image.load("image/Kreuz/3.png")
    vier=pygame.image.load("image/Kreuz/4.png")
    fünf=pygame.image.load("image/Kreuz/5.png")
    sechs=pygame.image.load("image/Kreuz/6.png")
    sieben=pygame.image.load("image/Kreuz/7.png")
    acht=pygame.image.load("image/Kreuz/8.png")
    neun=pygame.image.load("image/Kreuz/9.png")
    zehn=pygame.image.load("image/Kreuz/10.png")
    Bube=pygame.image.load("image/Kreuz/Bube.png")
    Dame=pygame.image.load("image/Kreuz/Dame.png")
    König=pygame.image.load("image/Kreuz/König.png")

class Pik():
    Ass=pygame.image.load("image/Pik/Ass.png")
    zwei=pygame.image.load("image/Pik/2.png")
    drei=pygame.image.load("image/Pik/3.png")
    vier=pygame.image.load("image/Pik/4.png")
    fünf=pygame.image.load("image/Pik/5.png")
    sechs=pygame.image.load("image/Pik/6.png")
    sieben=pygame.image.load("image/Pik/7.png")
    acht=pygame.image.load("image/Pik/8.png")
    neun=pygame.image.load("image/Pik/9.png")
    zehn=pygame.image.load("image/Pik/10.png")
    Bube=pygame.image.load("image/Pik/Bube.png")
    Dame=pygame.image.load("image/Pik/Dame.png")
    König=pygame.image.load("image/Pik/König.png")


Hintergrund=pygame.image.load("image/Rückseite.png")
bildgroessen = Hintergrund.get_rect()
#print(bildgroessen)
#print(bildgroessen.width)
#print(bildgroessen.height)


Spielkarte=[
Herz.Ass,Herz.zwei,Herz.drei,Herz.vier,Herz.fünf,Herz.sechs,Herz.sieben,Herz.acht,Herz.neun,Herz.zehn,Herz.Bube,Herz.Dame,Herz.König,

Karo.Ass,Karo.zwei,Karo.drei,Karo.vier,Karo.fünf,Karo.sechs,Karo.sieben,Karo.acht,Karo.neun,Karo.zehn,Karo.Bube,Karo.Dame,Karo.König,

Kreuz.Ass,Kreuz.zwei,Kreuz.drei,Kreuz.vier,Kreuz.fünf,Kreuz.sechs,Kreuz.sieben,Kreuz.acht,Kreuz.neun,Kreuz.zehn,Kreuz.Bube,Kreuz.Dame,Kreuz.König,

Pik.Ass,Pik.zwei,Pik.drei,Pik.vier,Pik.fünf,Pik.sechs,Pik.sieben,Pik.acht,Pik.neun,Pik.zehn,Pik.Bube,Pik.Dame,Pik.König
]

Spielkarte_ohne_ass={
Herz.zwei:2,Herz.drei:3,Herz.vier:4,Herz.fünf:5,Herz.sechs:6,Herz.sieben:7,Herz.acht:8,Herz.neun:9,Herz.zehn:10,Herz.Bube:11,Herz.Dame:12,Herz.König:13,

Karo.zwei:2,Karo.drei:3,Karo.vier:4,Karo.fünf:5,Karo.sechs:6,Karo.sieben:7,Karo.acht:8,Karo.neun:9,Karo.zehn:10,Karo.Bube:11,Karo.Dame:12,Karo.König:13,

Kreuz.zwei:2,Kreuz.drei:3,Kreuz.vier:4,Kreuz.fünf:5,Kreuz.sechs:6,Kreuz.sieben:7,Kreuz.acht:8,Kreuz.neun:9,Kreuz.zehn:10,Kreuz.Bube:11,Kreuz.Dame:12,Kreuz.König:13,

Pik.zwei:2,Pik.drei:3,Pik.vier:4,Pik.fünf:5,Pik.sechs:6,Pik.sieben:7,Pik.acht:8,Pik.neun:9,Pik.zehn:10,Pik.Bube:11,Pik.Dame:12,Pik.König:13
}

Spielkarten=[
Herz.zwei,Herz.drei,Herz.vier,Herz.fünf,Herz.sechs,Herz.sieben,Herz.acht,Herz.neun,Herz.zehn,Herz.Bube,Herz.Dame,Herz.König,
Karo.zwei,Karo.drei,Karo.vier,Karo.fünf,Karo.sechs,Karo.sieben,Karo.acht,Karo.neun,Karo.zehn,Karo.Bube,Karo.Dame,Karo.König,
Kreuz.zwei,Kreuz.drei,Kreuz.vier,Kreuz.fünf,Kreuz.sechs,Kreuz.sieben,Kreuz.acht,Kreuz.neun,Kreuz.zehn,Kreuz.Bube,Kreuz.Dame,Kreuz.König,
Pik.zwei,Pik.drei,Pik.vier,Pik.fünf,Pik.sechs,Pik.sieben,Pik.acht,Pik.neun,Pik.zehn,Pik.Bube,Pik.Dame,Pik.König
]

Spielkarte_list=[]
nachziehstappel_auseinander=[]
Spielkarte_stationen=[]
#print(Spielkarte)
#print(Spielkarte_ohne_ass)
Ass=[
    0,
    Herz.Ass,
    
    Karo.Ass,
    
    Kreuz.Ass,
    
    Pik.Ass,
    
]

Karten_detecktion={
    "Herz1":0,
    "Kreu1":0,
    "Karo1":0,
    "Pik1":0,
    "Herz2":0,
    "Kreu2":0,
    "Karo2":0,
    "Pik2":0,
    "Herz3":0,
    "Kreu3":0,
    "Karo3":0,
    "Pik3":0,
}

Nachziehstapel=[
[Herz.zwei,1],[Herz.drei,1],[Herz.vier,1],[Herz.fünf,1],[Herz.sechs,1],[Herz.sieben,1],[Herz.acht,1],[Herz.neun,1],[Herz.zehn,1],[Herz.Bube,1],[Herz.Dame,1],[Herz.König,1],

[Karo.zwei,2],[Karo.drei,2],[Karo.vier,2],[Karo.fünf,2],[Karo.sechs,2],[Karo.sieben,2],[Karo.acht,2],[Karo.neun,2],[Karo.zehn,2],[Karo.Bube,2],[Karo.Dame,2],[Karo.König,2],

[Kreuz.zwei,3],[Kreuz.drei,3],[Kreuz.vier,3],[Kreuz.fünf,3],[Kreuz.sechs,3],[Kreuz.sieben,3],[Kreuz.acht,3],[Kreuz.neun,3],[Kreuz.zehn,3],[Kreuz.Bube,3],[Kreuz.Dame,3],[Kreuz.König,3],

[Pik.zwei,4],[Pik.drei,4],[Pik.vier,4],[Pik.fünf,4],[Pik.sechs,4],[Pik.sieben,4],[Pik.acht,4],[Pik.neun,4],[Pik.zehn,4],[Pik.Bube,4],[Pik.Dame,4],[Pik.König,4]

]