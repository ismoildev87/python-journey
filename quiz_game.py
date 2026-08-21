#---"O`rganilganlarni savol javob orqali takrorlash"---
savollar = {
    "input() qanday turdagi qiymat qaytaradi?": "str",
     "pythondagi kasr sonli o`zgaruvchilarni ko`rsating": "float",
     "Matnni songa aylantiruvchi funksiya nomi?": "int",
     "Sonni matnga aylantiruvchi funksiya nomi?": "str",
     "100/24 natijasi qanday turda buladi?": "float",
     "print(True and False)da nima chiqadi?": "True",
     "b*3 nima chiqadi?": "bbb"
}
ball = 0
ism = input("Ismingizni kiriting: ")
print("Salom",ism, "-sizga", len(savollar),"ta savol beriladi, javoblarga qarab ball beriladi")
print("Savollarni boshlaymiz unda")
raqam = 0
for savol, tugri_javob in savollar.items():
    raqam = raqam+1
    print(raqam, "-savol: ", savol)
    javob = input("Javobingiz: ")
    if javob == tugri_javob:
        print("tugri")
        ball = ball+1
    else:
        print("notugri, tugri javob:", tugri_javob) 
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
 