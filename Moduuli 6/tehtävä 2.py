import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan maximi silmäluku: "))

silmäluku = 0

while silmäluku != maksimi:
    silmäluku = heita_noppaa(maksimi)
    print("Heiton tulos on:",silmäluku)