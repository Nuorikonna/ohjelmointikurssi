sanat = ["koira", "kissa", "puu", "kello", "lautanen", "kuha", "lentokone"]

laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1


print("Listan sanat joissa on enemmän kuin 5 kirjainta:", laskuri)


