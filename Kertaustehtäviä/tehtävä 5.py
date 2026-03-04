while True:
    print("Valitse jokin seuraavista:")
    print("1 = yhteenlasku")
    print("2 = vähennyslasku")
    print("3 = jakolasku")
    print("4 = kertolasku")
    print("L = lopeta ")

    valinta = input("Anna valinta:")

    if valinta == "L":
        print("Ohjelma lopetetaan.")
        break

    elif valinta in ["1", "2", "3", "4"]:
        luku1 = float(input("Anna ensimmäinen luku:"))
        luku2 = float(input("Anna toinen luku:"))

        if valinta == "1":
            tulos = luku1 + luku2
            print("Tulos on:",tulos)

        elif valinta == "2":
            tulos = luku1 - luku2
            print("Tulos on:",tulos)

        elif valinta == "3":
            tulos = luku1 / luku2
            print("Tulos on:",tulos)

        elif valinta == "4":
            tulos = luku1 * luku2
            print("Tulos on:",tulos)

    else:
        print("Valinta on virheellinen, kokeile uudestaan!")