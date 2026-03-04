import math
while True:
    luku = int(input("Anna kokonaisluku:"))

    if luku == 0:
        print("Ohjelma lopetetaan.")
        break
    elif luku < 0:
        print("Virheellinen numero.")
    else:
        juuri = math.sqrt(luku)
        print("Neliöjuuri on:", juuri)