nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
nimet.append(nimi)
while nimi != "":
    nimet.append(nimi)
    valinta = input("haluatko lisätä vai poistaa (l tai p)")
    if(valinta=="l"):
        nimi = input("Anna seuraava nimi tai lopeta painamalla Enter")
        nimet.append(nimi)
    else:
        nimi = input("Anna poistettava nimi tai lopeta painamalala Enter: ")
        nimi.remove(nimi) 

print(nimet)