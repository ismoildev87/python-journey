def menyu_korsat():
    print("=== TALABALAR BAHOLASH TIZIMI ===")
    print("1. Talaba qo'shish")
    print("2. Talabani baholash")
    print("3. Barcha talabalarni ko'rish")
    print("4. Statistikani ko'rish")
    print("5. Chiqish")


def saqlash(talabalar):
    with open("talabalar.txt", "w") as fayl:
        for talaba in talabalar:
            ballar_matn = ""
            for ball in talaba["ball"]:
                ballar_matn = ballar_matn + str(ball) + ","
            qator = talaba["ism"] + "|" + ballar_matn + "\n"
            fayl.write(qator)


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


def ball_qoshish(talabalar):
    ism = input("Kimga ball qo'yasiz: ")
    for talaba in talabalar:
        if talaba["ism"] == ism:
            ball = int(input("Ball: "))
            talaba["ball"].append(ball)
            print("Qo'shildi")
            return
    print("Bunday talaba topilmadi")


def royxatni_korsat(talabalar):
    if len(talabalar) == 0:
        print("Hali talaba yo'q")
        return
    for talaba in talabalar:
        ortacha = ortacha_hisobla(talaba["ball"])
        print(talaba["ism"], "- o'rtacha ball:", ortacha)


def ortacha_hisobla(ballar):
    if len(ballar) == 0:
        return 0
    return round(sum(ballar) / len(ballar), 2)


def statistika_korsat(talabalar):
    if len(talabalar) == 0:
        print("Hali talaba yo'q")
        return

    eng_yaxshi_ism = ""
    eng_yaxshi_ortacha = 0

    for talaba in talabalar:
        ortacha = ortacha_hisobla(talaba["ball"])
        if ortacha > eng_yaxshi_ortacha:
            eng_yaxshi_ortacha = ortacha
            eng_yaxshi_ism = talaba["ism"]

    print("Eng yaxshi natija:", eng_yaxshi_ism, "-", eng_yaxshi_ortacha)


talabalar = yuklash()
while True:
    menyu_korsat()
    tanlov = input("Tanlovingizni kiriting (1-5): ")
    if tanlov == "1":
        ism = input("Talabaning ismini yozing: ")

        mavjud = False
        for talaba in talabalar:
            if talaba["ism"] == ism:
                mavjud = True

        if mavjud:
            print("Bu ism allaqachon mavjud!")
        else:
            yangi_talaba = {"ism": ism, "ball": []}
            talabalar.append(yangi_talaba)
            print(ism, "muvaffaqiyatli qo'shildi!")
    elif tanlov == "2":
        ball_qoshish(talabalar)
    elif tanlov == "3":
        royxatni_korsat(talabalar)
    elif tanlov == "4":
        statistika_korsat(talabalar)

    elif tanlov == "5":
        saqlash(talabalar)
        print("Dastur yopildi")
        break
    else:
        print("Noto'g'ri tanlov, 1-5 orasida kiriting")
