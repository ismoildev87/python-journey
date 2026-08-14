#---"O`rganilganlarni savol javob orqali takrorlash"---
savollar = [
    "input() qanday turdagi qiymat qaytaradi?",
     "pythondagi kasr sonli o`zgaruvchilarni ko`rsating",
     "Matnni songa aylantiruvchi funksiya nomi?",
     "Sonni matnga aylantiruvchi funksiya nomi?",
     "100/24 natijasi qanday turda buladi?",
     "print(True and False)da nima chiqadi?",
      "b*3 nima chiqadi?"
      ]
javoblar = ["str", "float", "int", "str", "float", "True", "bbb"]
ball = 0
ism = input("Ismingizni kiriting: ")
print("Salom",ism, "-sizga", len(savollar),"ta savol beriladi, javoblarga qarab ball beriladi")
print("Savollarni boshlaymiz unda")
for i in range(len(savollar)):
    print(i+1, "-savol:", savollar[i])
    javob = input("Javobingiz: ")
    if javob == javoblar[i]:
        print("tugri")
        ball = ball+1
    else:
        print("notugri, tugri javob:", javoblar[i]) 
foiz = ball / len(savollar) * 100
print("Sizning natijangiz:", ball, "/",len(savollar))
print("Foiz:", foiz, "%")
if foiz>=100:
    print("Zo'r! Siz mutaxassissiz!")
elif foiz>=80:
    print("Yaxshi natija!")
elif foiz>=60:
    print("Qoniqarli, yana o'rganish kerak")
else:
    print("Ko'proq mashq qiling") 
 