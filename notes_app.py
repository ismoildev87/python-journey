while True:
    print("1. Eslatma qo'shish")
    print("2. Eslatmalarni ko'rish")
    print("3. Chiqish")
    tanlov = input("Tanlovingiz: ")

    if tanlov == "1":
        eslatma = input("Eslatmangizni yozing: ")
        with open("notes.txt", "a") as fayl:
            fayl.write(eslatma + "\n")
        print("Saqlandi!")

    elif tanlov == "2":
        try:
            with open("notes.txt", "r") as fayl:
                raqam = 0
                for qator in fayl:
                    raqam = raqam + 1
                    print(raqam, qator.strip())
        except FileNotFoundError:
            print("Hali eslatma yo'q")

    elif tanlov == "3":
        break
