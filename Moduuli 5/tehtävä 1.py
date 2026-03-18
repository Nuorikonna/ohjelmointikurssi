import random

määrä = int(input("Kuinka monta arpakuutiota heitetään?"))

summa = 0

for i in range(määrä):
    heitto = random.randint(1,6)
    print(f"heitto {i+1}: {heitto}")
    summa += heitto

print("Arpakuution silmälukujen summa on:", summa)
