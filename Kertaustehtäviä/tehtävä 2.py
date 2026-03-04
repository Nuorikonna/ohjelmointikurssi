tuntipalkka = float(input("Anna tuntipalkka:"))
tunnit = float(input("Anna tehdyt tunnit:"))
paiva = input("Mikä viikonpäivä on kyseessä:")

if paiva == "sunnuntai":
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print(f"Päiväpalkka on {paivapalkka:.2f}euroa. ")