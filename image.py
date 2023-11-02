import pygame
from pygame.locals import *


#lädt alle Bilder
class Herz():
    Ass=pygame.image.load("Pferderennen/image/Herz/Ass.png")
    zwei=pygame.image.load("Pferderennen/image/Herz/2.png")
    drei=pygame.image.load("Pferderennen/image/Herz/3.png")
    vier=pygame.image.load("Pferderennen/image/Herz/4.png")
    fünf=pygame.image.load("Pferderennen/image/Herz/5.png")
    sechs=pygame.image.load("Pferderennen/image/Herz/6.png")
    sieben=pygame.image.load("Pferderennen/image/Herz/7.png")
    acht=pygame.image.load("Pferderennen/image/Herz/8.png")
    neun=pygame.image.load("Pferderennen/image/Herz/9.png")
    zehn=pygame.image.load("Pferderennen/image/Herz/10.png")
    Bube=pygame.image.load("Pferderennen/image/Herz/Bube.png")
    Dame=pygame.image.load("Pferderennen/image/Herz/Dame.png")
    König=pygame.image.load("Pferderennen/image/Herz/König.png")

class Karo():
    Ass=pygame.image.load("Pferderennen/image/Karo/Ass.png")
    zwei=pygame.image.load("Pferderennen/image/Karo/2.png")
    drei=pygame.image.load("Pferderennen/image/Karo/3.png")
    vier=pygame.image.load("Pferderennen/image/Karo/4.png")
    fünf=pygame.image.load("Pferderennen/image/Karo/5.png")
    sechs=pygame.image.load("Pferderennen/image/Karo/6.png")
    sieben=pygame.image.load("Pferderennen/image/Karo/7.png")
    acht=pygame.image.load("Pferderennen/image/Karo/8.png")
    neun=pygame.image.load("Pferderennen/image/Karo/9.png")
    zehn=pygame.image.load("Pferderennen/image/Karo/10.png")
    Bube=pygame.image.load("Pferderennen/image/Karo/Bube.png")
    Dame=pygame.image.load("Pferderennen/image/Karo/Dame.png")
    König=pygame.image.load("Pferderennen/image/Karo/König.png")

class Kreuz():
    Ass=pygame.image.load("Pferderennen/image/Kreuz/Ass.png")
    zwei=pygame.image.load("Pferderennen/image/Kreuz/2.png")
    drei=pygame.image.load("Pferderennen/image/Kreuz/3.png")
    vier=pygame.image.load("Pferderennen/image/Kreuz/4.png")
    fünf=pygame.image.load("Pferderennen/image/Kreuz/5.png")
    sechs=pygame.image.load("Pferderennen/image/Kreuz/6.png")
    sieben=pygame.image.load("Pferderennen/image/Kreuz/7.png")
    acht=pygame.image.load("Pferderennen/image/Kreuz/8.png")
    neun=pygame.image.load("Pferderennen/image/Kreuz/9.png")
    zehn=pygame.image.load("Pferderennen/image/Kreuz/10.png")
    Bube=pygame.image.load("Pferderennen/image/Kreuz/Bube.png")
    Dame=pygame.image.load("Pferderennen/image/Kreuz/Dame.png")
    König=pygame.image.load("Pferderennen/image/Kreuz/König.png")

class Pik():
    Ass=pygame.image.load("Pferderennen/image/Pik/Ass.png")
    zwei=pygame.image.load("Pferderennen/image/Pik/2.png")
    drei=pygame.image.load("Pferderennen/image/Pik/3.png")
    vier=pygame.image.load("Pferderennen/image/Pik/4.png")
    fünf=pygame.image.load("Pferderennen/image/Pik/5.png")
    sechs=pygame.image.load("Pferderennen/image/Pik/6.png")
    sieben=pygame.image.load("Pferderennen/image/Pik/7.png")
    acht=pygame.image.load("Pferderennen/image/Pik/8.png")
    neun=pygame.image.load("Pferderennen/image/Pik/9.png")
    zehn=pygame.image.load("Pferderennen/image/Pik/10.png")
    Bube=pygame.image.load("Pferderennen/image/Pik/Bube.png")
    Dame=pygame.image.load("Pferderennen/image/Pik/Dame.png")
    König=pygame.image.load("Pferderennen/image/Pik/König.png")

#Größe der Bilder
class Herz_Größe:
    Ass=Herz.Ass.get_rect()
    zwei=Herz.zwei.get_rect()
    drei=Herz.drei.get_rect()
    vier=Herz.vier.get_rect()
    fünf=Herz.fünf.get_rect()
    sechs=Herz.sechs.get_rect()
    sieben=Herz.sieben.get_rect()
    acht=Herz.acht.get_rect()
    neun=Herz.neun.get_rect()
    zehn=Herz.zehn.get_rect()
    Bube=Herz.Bube.get_rect()
    Dame=Herz.Dame.get_rect()
    König=Herz.König.get_rect()

class Pik_Größe:
    Ass=Karo.Ass.get_rect()
    zwei=Karo.zwei.get_rect()
    drei=Karo.drei.get_rect()
    vier=Karo.vier.get_rect()
    fünf=Karo.fünf.get_rect()
    sechs=Karo.sechs.get_rect()
    sieben=Karo.sieben.get_rect()
    acht=Karo.acht.get_rect()
    neun=Karo.neun.get_rect()
    zehn=Karo.zehn.get_rect()
    Bube=Karo.Bube.get_rect()
    Dame=Karo.Dame.get_rect()
    König=Karo.König.get_rect()
class Kreuz_Größe:
    Ass=Kreuz.Ass.get_rect()
    zwei=Kreuz.zwei.get_rect()
    drei=Kreuz.drei.get_rect()
    vier=Kreuz.vier.get_rect()
    fünf=Kreuz.fünf.get_rect()
    sechs=Kreuz.sechs.get_rect()
    sieben=Kreuz.sieben.get_rect()
    acht=Kreuz.acht.get_rect()
    neun=Kreuz.neun.get_rect()
    zehn=Kreuz.zehn.get_rect()
    Bube=Kreuz.Bube.get_rect()
    Dame=Kreuz.Dame.get_rect()
    König=Kreuz.König.get_rect()
class Pik_Größe:
    Ass=Pik.Ass.get_rect()
    zwei=Pik.zwei.get_rect()
    drei=Pik.drei.get_rect()
    vier=Pik.vier.get_rect()
    fünf=Pik.fünf.get_rect()
    sechs=Pik.sechs.get_rect()
    sieben=Pik.sieben.get_rect()
    acht=Pik.acht.get_rect()
    neun=Pik.neun.get_rect()
    zehn=Pik.zehn.get_rect()
    Bube=Pik.Bube.get_rect()
    Dame=Pik.Dame.get_rect()
    König=Pik.König.get_rect()

Hintergrund=pygame.image.load("Pferderennen/image/Rückseite.png")
bildgroessen = Hintergrund.get_rect()
print(bildgroessen)
print(bildgroessen.width)
print(bildgroessen.height)


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
#print(Spielkarte)
#print(Spielkarte_ohne_ass)
Ass=[
    0,
    Herz.Ass,
    "Herz Ass",
    Karo.Ass,
    "Karo Ass",
    Kreuz.Ass,
    "Kreuz Ass",
    Pik.Ass,
    "Pik Ass"
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