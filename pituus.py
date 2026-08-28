pituus = int(input("Anna pituutesi cm: "))
if pituus >= 252:
    print("Olet Thanos.")
elif pituus >= 218:
    print("Olet Shaq.")
elif pituus >= 200:
    print("Olet Brian Shaw.")
elif pituus >= 190:
    print("Olet Tom Ellis.")
elif pituus >= 185:
    print("Oot Jensen Ackles.")
elif pituus >= 180:
    print("Olet Jon Bernthal.")
elif pituus >= 175:
    print("Olet Tom hardy")
elif pituus >= 170:
    print("Olet Mark Wahlberg.")
elif pituus >= 165:
    print("olet Josh Hutcherson.")
elif pituus >= 160:
    print("olet Kai Cenat.")
elif pituus >= 155:
    print("Olet Kevin hart.")
elif pituus >= 145:
    print("Olet danny DeVito.")
else:
    print("Olet Peter Dinklage.")


komento = input("Anna komento: ")
while komento != "lopeta":
    print("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
print("Toiminnot lopetettu.")