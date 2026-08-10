#---"O`rganilganlarni savol javob orqali takrorlash"---
ism = input("Ismingizni kiriting: ")
print("Salom",ism, "sizga beshta savollar beriladi, javoblarga qarab ball beriladi")
print("Savollarni boshlaymiz unda")
ball = 0
#1-savol
print("1-Savol: input() qanday turdagi qiymat qaytaradi?")
javob = input("javobingiz: ")
if javob == "str" or javob == "STR" or javob == "Str":
    print("tugri")
    ball = ball+1
else:
    print("notugri. tugri javob: str")
print()
#2-savol
print("2-Savol: pythondagi kasr sonli o`zgaruvchilarni ko`rsating")
javob = input("javobingiz: ")
if javob == "float" or javob == "FLOAT" or javob == "Float":
    print("tugri")
    ball = ball+1
else:
    print("notugri. tugri javob: float")
print()
#3-savol
print("3-Savol: Matnni songa aylantiruvchi funksiya nomi?")
javob = input("javobingiz: ")
if javob == "int" or javob == "INT" or javob == "Int":
    print("tugri")
    ball = ball+1
else:
    print("notugri. tugri javob: int")
print()
#4-savol
print("4-Savol: Sonni matnga aylantiruvchi funksiya nomi?")
javob = input("javobingiz: ")
if javob == "str" or javob == "STR" or javob == "Str":
    print("tugri")
    ball = ball+1
else:
    print("notugri. tugri javob: str")
print()
#5-savol
print("5-Savol: 100/24 natijasi qanday turda buladi?")
javob = input("javobingiz: ")
if javob == "float" or javob == "FLOAT" or javob == "Float":
    print("tugri")
    ball = ball+1
else:
    print("notugri. tugri javob: float")
print()
print("Sizning tuplagan ballingiz:",ball)
foiz = ball/5*100
print("Sizning natijangiz:", ball, "/ 5")
print("Foiz:", foiz, "%")
if foiz>=100:
    print("Zo'r! Siz mutaxassissiz!")
elif foiz>=80:
    print("Yaxshi natija!")
elif foiz>=60:
    print("Qoniqarli, yana o'rganish kerak")
else:
    print("Ko'proq mashq qiling") 
 