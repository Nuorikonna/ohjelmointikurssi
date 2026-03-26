lista = []

while True:
    luku = int(input("Anna jokin luku:"))

    if luku == 0:
        break

    lista.append(luku)

    print("Lista lisäysjärjestyksessä:", lista)
    print("Lista järjestettynä Suurimmasta pienimpään:", sorted(lista)
          )
