kerrat = int(input("Montako kertaa spammataan: "))
tehdyt = 0
while tehdyt < kerrat:
    print("Wazzuuuup")
    tehdyt = tehdyt + 1

komento = input("Anna komento: ")
while komento != "lopeta":
    print("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
print("Toiminnot lopetettu.")