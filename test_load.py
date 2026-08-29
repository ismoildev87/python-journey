def yuklash():
    talabalar = []
    try:
        with open("talabalar.txt", "r") as fayl:
            for qator in fayl:
                qismlar = qator.strip().split("|")
                ism = qismlar[0]
                ballar_matn = qismlar[1]

                ballar_royxat = ballar_matn.split(",")
                ballar = []
                for ball_matn in ballar_royxat:
                    if ball_matn != "":
                        ballar.append(int(ball_matn))

                talabalar.append({"ism": ism, "ball": ballar})
    except FileNotFoundError:
        pass
    return talabalar


natija = yuklash()
print(natija)
