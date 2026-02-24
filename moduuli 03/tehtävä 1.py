pituus = float(input("Anna kuhan pituus senttimetreinä"))
alamitta = 30

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print("Kuha on alamittainen")
    print(f"Alimmasta sallitusta pituudesta puuttuu {puuttuu:.1f} cm.")
    print("Laske Kuha takaisin järveen.")

else:
    print("Kuha on tarpeeksi pitkä. Voit pitää sen.")
