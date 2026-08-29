talabalar = [{"ism": "Ismoil", "ball": [85, 90, 78]}, {"ism": "Vali", "ball": [92, 88]}]


def saqlash(talabalar):
    with open("talabalar.txt", "w") as fayl:
        for talaba in talabalar:
            ballar_matn = ""
            for ball in talaba["ball"]:
                ballar_matn = ballar_matn + str(ball) + ","
            qator = talaba["ism"] + "|" + ballar_matn + "\n"
            fayl.write(qator)


saqlash(talabalar)
