# --- 5. Urinishlar soni cheklangan ---
urinish = 0
kirdi = False                       # bool o'zgaruvchi — holatni saqlaydi

while urinish < 3:
    parol = input("Parol: ")
    if parol == "python123":
        kirdi = True
        break                       # break — siklni DARHOL to'xtatadi
    else:
        urinish = urinish + 1
        print("Xato. Qolgan urinishlar:", 3 - urinish)

if kirdi:
    print("Tizimga kirdingiz")
else:
    print("Urinishlar tugadi. Hisob bloklandi")