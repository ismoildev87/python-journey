# --- Uch xil tur ---
ism = "Ismoil"        # str  — matn, qo'shtirnoq ichida
yosh = 39             # int  — butun son
boy = 1.78            # float — kasr son, NUQTA bilan

# type() funksiyasi qiymatning turini aytadi
print(type(ism))      # <class 'str'>
print(type(yosh))     # <class 'int'>
print(type(boy))      # <class 'float'>

# --- Son va matnning farqi ---
son = 39              # int
matn = "39"           # str — ichida raqam bor, lekin bu MATN

print(son + 1)        # 40 — matematik qo'shish
print(matn + "1")     # 391 — matn ulanishi! Qo'shish emas

# Matnlarni "qo'shish" — ularni bir-biriga ULASH degani.
# Bu amal concatenation (konkatenatsiya — birlashtirish) deyiladi
ism = "Ismoil"
familiya = "Toshboyev"
toliq_ism = ism + " " + familiya   # orasiga bo'sh joy qo'shdik
print(toliq_ism)                   # Ismoil Toshboyev

# --- int va float aralashsa ---
natija = 10 + 2.5
print(natija)         # 12.5
print(type(natija))   # float — Python "kengroq" turni tanlaydi

# --- Bo'lish har doim float qaytaradi ---
print(10 / 2)         # 5.0 (5 emas!) — / doim float beradi
print(type(10 / 2))   # float