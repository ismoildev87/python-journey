matn = "Ismoil|85,90,78"
qismlar = matn.split("|")
print(qismlar)
print(qismlar[0])
print(qismlar[1])
print()
ballar_matn = "85,90,78"
ballar_royxat = ballar_matn.split(",")
print(ballar_royxat)
print(type(ballar_royxat[0]))
print()
ballar_royxat = ["85", "90", "78"]

ballar = []
for ball_matn in ballar_royxat:
    ballar.append(int(ball_matn))

print(ballar)
print(type(ballar[0]))
