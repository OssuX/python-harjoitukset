import random

# Alustetaan muuttujat
heitot = 0
silmäluku = 0

# Heitetään noppaa niin kauan, kunnes saadaan 6
while silmäluku != 6:
    silmäluku = random.randint(1, 6)  # Arvotaan luku väliltä 1-6
    heitot += 1                       # Lisätään heittomäärään 1
    print(f"Heitit: {silmäluku}")

# Tulostetaan lopputulos (sinun korjattu koodisi)
print(f"Tarvittiin {heitot:d} heittoa.")
