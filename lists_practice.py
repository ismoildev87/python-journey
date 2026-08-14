# 5 ta shahar nomidan iborat ro'yxat yarat va har birini alohida qatorda chiqar
shaharlar = ["Yaypan", "Quqon", "Fargona", "Toshkent", "Navoiy"]
for shahar in shaharlar:
    print(shahar)
# 8 ta sondan iborat ro'yxat yarat. Uning yig'indisi, o'rtachasi, eng katta va eng kichik elementini chiqar
sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
print("yigindi: ",sum(sonlar))
print("urtachasi: ", sum(sonlar)/len(sonlar))
print("eng kattasi: ", max(sonlar))
print("eng kichigi: ", min(sonlar))
print()
# Foydalanuvchidan 5 ta son so'ra, ularni ro'yxatga yig' va saralangan holda chiqar
# (maslahat: for sikli + append())
sonlar = []
for i in range(5):
    son = int(input("Son kiriting: "))
    sonlar.append(son)
sonlar.sort()
print(sonlar)
juft_sonlar = []
#juft sonlarni aniqlash va alohida ruyhat qilish
for son in sonlar:
    if son % 2 == 0:
        juft_sonlar.append(son)
print("Juft sonlar: ",juft_sonlar)
print()
# Foydalanuvchidan shahar nomi so'ra va u 1-banddagi ro'yxatda bor-yo'qligini tekshir (in ishlat)
shahar = input("shahrni kiriting: ")
if shahar in shaharlar:
    print(shahar, "ruyxatda bor")
else:
    print(shahar, "ruyxatda yuq")