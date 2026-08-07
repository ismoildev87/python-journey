# --- Oddiy input ---
ism = input("Ismingizni kiriting: ")
print("Salom,", ism + "!")

# --- input() matn qaytarishini isbotlaymiz ---
yosh_matn = input("Yoshingizni kiriting: ")
print("Siz kiritgan qiymat turi:", type(yosh_matn))   # <class 'str'> chiqadi

# Matn ustida hisob ishlab ko'ramiz
print("Ikki barobari:", yosh_matn * 2)   # 39 kiritsang: 3939 chiqadi!

# --- Endi to'g'ri usul: songa aylantiramiz ---
yosh = int(yosh_matn)                    # str -> int
print("Endi turi:", type(yosh))          # <class 'int'>
print("Ikki barobari:", yosh * 2)        # 78 — mana bu to'g'ri

# --- Qisqa yozuv: aylantirishni darhol qilamiz ---
tugilgan_yil = 2026 - int(input("Yana yoshingizni kiriting: "))
print("Siz", tugilgan_yil, "yilda tug'ilgansiz")

# --- Kasr son uchun float() ---
narx = float(input("Mahsulot narxini kiriting: "))
soni = int(input("Nechta olasiz: "))
jami = narx * soni
print("Jami to'lov:", jami, "so'm")