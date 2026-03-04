nimi = input("Anna nimesi:")

if nimi != "Matti":
    annokset = int(input("Montako keittoannosta?"))
    hinta_annos = 5.90
    kokonaishinta = annokset * hinta_annos
    print(f"Kokonaishinta on {kokonaishinta:.2f}euroa.")
    print("Seuraava,kiitos!")
else:
    print("Tervetuloa Matti!")
    print("Seuraava,kiitos!")
