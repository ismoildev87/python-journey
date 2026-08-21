# --- Yaratish va uqish ---
talaba = {"ism": "Abduraxmon",
          "yosh": "30",
          "tuman": "Beshariq"
          }
print (talaba)
print (talaba["ism"])
print(len(talaba))
print()
# --- qo`shish va o`zgartirish ---
talaba["kasb"] = "adminstrator" # yangi kalit - qo`shiladi
talaba["yosh"] = 40 # mavjud kalit - o`zgaradi
print(talaba)
print()
# --- o`chirish ---
del talaba["tuman"]
print (talaba)
print()
# --- Kalit bor yuqligini tekshirish ---
if "ism" in talaba:
    print ("Ism kaliti bor")
if "email" not in talaba:
    print("Email kaliti yuq")
print()
# --- get() - xavfsiz o`qish ---
print (talaba.get("ism"))   # Ismoil
print (talaba.get("email")) # None - xato bermaydi
print (talaba.get("email", "ko`rsatilmagan")) # standart qiymat
print ()
# --- Bo`ylab yurish ---
narxlar = {
    "non": 5000,
    "sut": 12000,
    "gurunch": 18000
}
# faqat kalitlar
for mahsulot in narxlar:
    print (mahsulot)
print ()
# kalit va qiymat birga
for mahsulot, narx in narxlar.items():
    print (mahsulot, "-", narx, "so`m")
print ()
# foydali metodlar
print (narxlar.keys()) #kalitlar ruyxati
print (narxlar.values()) #qiymatlar ruyxati
print (sum(narxlar.values())) #qiymatlar yig`indisi
print()
# --- lug`at ichida ro`xat ---
talaba = {
    "ism": "Abduraxmon",
    "tillar": ["Python", "SQL"]
}
print (talaba["tillar"][0]) # python
print (talaba["tillar"][1])
print(talaba["ism"])
print()
# --- lug`atlar ro`xati (juda keng tarqalgan) ---
talabalar = [
    {"ism": "Ali", "ball": 85},
    {"ism": "Vali", "ball": 92},
    {"ism": "Guli", "ball": 78}
]
for t in talabalar: 
    print (t["ism"], "->", t["ball"])


