# --- oddiy if / else ---
yosh = int(input("Yoshingizni kiriting:"))
if yosh >= 18:
    print("Siz voyaga yetgansiz")
else :
    print ("Siz hali voyaga yetmagansiz")

    print()
# --- if / elif / else : bir necha variant ---
ball = int(input("Imtihon balingizni kiriting(0-100):"))

if ball >= 90:
    baho = "A`lo"
elif ball >= 70:
    baho = "Yaxshi"
elif ball >= 50:
    baho = "qoniqarli"
else :
    baho = "Qoniqarsiz"
print ("Sizning bahoingiz:", baho)

print ()

# --- Matn solishtirish ---

parol = Input("Parolni kiriting:")

if parol == "pyton123":
    print("Xush kelibsiz!")

else:
    print("PArol noto`g`ri!")

    print()

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
    

