nimet = set()

while True:
    nimi = input("Anna jokin nimi (Enter lopettaa):")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aikaisemmin annettu nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)


print("\nNimet:")
for n in nimet:
    print(n)
