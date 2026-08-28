print("Hei, Oskari.")

while True:
    komento = input("Anna komento (lopetus / kiitos /  / sammuta: ").lower().strip()
    
    if komento == "hei":
        print("Hei, kuinka voin auttaa sinua?")
        break  
        
        
    elif komento == "kiitos":
        print("Ole hyvä!")
        #break
        
    elif komento == "sulje":
        print("Suljetaan ohjelma...")
        break
        
        
    else:
        print("Tuntematon komento, anna uusi")

print("Ohjelma suljettu")