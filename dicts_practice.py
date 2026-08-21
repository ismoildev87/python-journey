# --- ruyxat yaratish ---
uzim = {
    "ism": "Abdu",
    "familiya": "Sher",
    "yosh": "30",
    "shahar": "Quqon",
    "kasb": "admin"
}
print(uzim["ism"])
print(uzim["familiya"])
print(uzim["yosh"])
print(uzim["shahar"])
print(uzim["kasb"])
print()
narxlar = {
    "gusht": 150000,
    "sabzi": 8000,
    "yog`": 20000,
    "gurunch": 25000,
    "non": 5000
}
for mahsulot in narxlar.keys():
    print(mahsulot)
print (sum(narxlar.values()))
print (max(narxlar.values()))
print (min(narxlar.values()))
mahsulot = input("Mahsulot nomini kiriting: ")
print (narxlar.get(mahsulot, "Bunday mahsulot yuq"))
print ()
talabalar = [
    {"ism": "Nosir", "ball": 90},
    {"ism": "Abror", "ball": 85},
    {"ism": "Abbos", "ball": 90} 
]
for t in talabalar:
    print (t["ism"], "-", t["ball"])
jami_ball = 0
for t in talabalar:
    jami_ball =jami_ball + t["ball"]
urtacha = jami_ball / len(talabalar)
print ("Urtacha ball: ",urtacha)
print ()