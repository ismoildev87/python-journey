login = input("Loginingizni kiriting: ")
parol = input("Parolingizni kiriting: ")
if login == "admin" and parol == "12345":
    print("Xush kelibsiz, admin!")
    yosh = int(input("Yoshingizni kiriting: "))
    shahar = input("Shahringizni kiriting: ")
    if (18 <= yosh <= 45) and (shahar == "Toshkent" or shahar == "Quqon"):
        print("Siz vakansiyaga mos keldingiz")
    else:
        print("Afsuski, talablarga javob bermaysiz")
else:
    print("parol yoki login xato")