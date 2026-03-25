def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    määrä = float(input("Anna bensamäärä gallononina:"))

    if määrä < 0:
        break

    litrat = gallonat_litroiksi(määrä)
    print("Litroina määrä on:",litrat)
