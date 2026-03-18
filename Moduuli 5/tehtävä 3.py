luku = int(input("Anna jokin kokonaisluku: "))

if luku < 2:
    print("Kyseinen luku ei ole alkuluku.")
else:
    alkuluku = True

    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")