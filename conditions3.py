# --- If ichida if (nested ichma isch) ---
yosh = int(input("Yoshingiz:"))

if yosh >= 18:
    guvohnoma = input("Haydovchilik guvohnomangiz bormi? (ha / yoq):")

    if guvohnoma == "ha":
        print("Siz mashina hayday olasiz")
    else:
        print("Avval guvohnoma olishingiz kerak")

else:
    print("Yoshingiz yetmagan")