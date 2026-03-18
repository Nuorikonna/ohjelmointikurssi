luvut = []

while True:
    syöte = input("Anna jokin luku:")

    if syöte == "":
        break

    luku = float(syöte)
    luvut.append(luku)

luvut.sort(reverse=True)

print("Viisi suurinta lukua on:")
for luku in luvut [:5]:
    print(luku)
    