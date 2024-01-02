spieler=3
einsaetz_spiele=[]
pferd_spieler=[]

def einsatz():
    
    einsaetz_spiele=[]
    pferd_spieler=[]
    for i in range(spieler+1):
        einsaetz_spiele.append(0)
        pferd_spieler.append(0)


    for i in range(1,spieler+1,1):
        try:
            print(f"Spiler {i}:")
            pferd_spieler[1]=int(input("Pferd (1,2,3,4): "))
            einsaetz_spiele[i]=int(input(f"einsatz spieler {i}: "))
        except:
            einsatz()



einsatz()
def rechnung_gewinn():
    ergebniss=0
    for i in einsaetz_spiele:
        ergebniss+=i
    return(ergebniss)

print(rechnung_gewinn())