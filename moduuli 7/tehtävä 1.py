kuukausi = int(input("Anna kuukauden numero väliltä (1-12):"))

vuodenajat = (
    "talvi",
    "talvi",
    "kevät",
    "kevät",
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy",
    "talvi"
)

if 1 <= kuukausi <= 12:
    print("Kyseisen kuukauden vuodenaika on", vuodenajat[kuukausi- 1])

else:
    print("Et antanut numeroa väliltä (1-12)!")