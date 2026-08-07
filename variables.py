# O`zgaruvchi yaratish: nom=qiymat
ism="Ismoil" #matn qiymati qo`shtirnoq ichida yoziladi
yosh=40 #son qo`shtirnoqsiz yoziladi
oylik=35000
#print bilan o`zgaruvchi qiymatini ekranga chiqaramiz
print(ism)
print(yosh)
# Bir nechta qiymatni vergul bilan ajratib chiqarish mumkin.
# Python ular orasiga avtomatik bo'sh joy qo'yadi.
print("Mening ismim:", ism)
print("Yoshim:", yosh)

# O'zgaruvchi qiymatini o'zgartirish mumkin — eski qiymat o'chadi
yosh = 29
print("Yangi yosh:", yosh)   # 29 chiqadi, 28 emas

# O'zgaruvchilar ustida amal bajarish
oylik_yillik = oylik * 12    # * — ko'paytirish belgisi
print("Yillik daromad:", oylik_yillik)

# Bir o'zgaruvchini boshqasiga ham berish mumkin
dostim_yoshi = yosh
print("Do'stim yoshi:", dostim_yoshi)