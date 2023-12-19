spieler=3
einsaetz_spiele=[]

def einsatz():
    for i in range(spieler+1):
        einsaetz_spiele.append(0)

    for i in range(1,spieler+1,1):
        x=int(input(f"einsatz spieler {i}: "))
        einsaetz_spiele[i]=x

def rechnung_gewinn():
    ergebniss=0
    for i in einsaetz_spiele:
        ergebniss+=i
    return(ergebniss)

print(rechnung_gewinn())