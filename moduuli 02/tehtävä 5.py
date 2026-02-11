a=int(input("Anna leiviskät"))
b=int(input("Anna naulat"))
c=int(input("Anna luodit"))

luodit_yhteensa = (
    a * 20 * 32 +
    b * 32 +
    c
)
grammat = luodit_yhteensa * 13.3
kilot = int(grammat// 1000)
jaljella_grammat = grammat % 1000

print(f"Massa on {kilot} kilogrammaa ja {jaljella_grammat:.2f} grammaa")


