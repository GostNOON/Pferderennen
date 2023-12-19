spieler=3
einsaetz_spiele=[]
ergebniss=0
for i in range(spieler+1):
    einsaetz_spiele.append(0)

while True:
    for i in range(1,spieler+1,1):
        x=int(input(f"einsatz spieler {i}: "))
        einsaetz_spiele[i]=x

    break    
for i in einsaetz_spiele:
    ergebniss+=i
print(ergebniss)