# ---yaratish va o`qish---
talabalar = ["Ali", "Vali", "Soli", "Guli"]
print(talabalar)
print(talabalar[0])
print(talabalar[1])
print(talabalar[2])
print(talabalar[3])
print(talabalar[-2])
print(talabalar[-3])
print(talabalar[-1])
print(len(talabalar))
#uzgartirish
talabalar[1] = "Bobur"
print(talabalar)
talabalar.append("Doniyor")
print(talabalar)
talabalar.insert(0, "Anvarboy")
print(talabalar)
talabalar.insert(3, "Anvarboy")
print(talabalar)
talabalar.remove("Anvarboy")
print(talabalar)
talabalar.remove("Anvarboy")
print(talabalar)
talabalar.pop()
print(talabalar)
#---Buylab yurish---
sonlar = [10, 15, 25, 30, 35, 40, 45]
for son in sonlar:
    print(son, end="")
print()
# indeks bilan
for i in range (len(sonlar)):
    print(i, "->", sonlar[i])
print()
#---foydali funksiyalar---
print("yig`indi: ",sum(sonlar))
print("Eng katta:", max(sonlar))
print("Eng kichik:", min(sonlar))
print("O'rtacha:", sum(sonlar) / len(sonlar))
print()
#---ruyxat ichida qidirish---
if "Ali" in talabalar:
    print("Ali talabar ruyxatida bor")
print()
#---saralash---
sonlar.sort()
print(sonlar)
print()
sonlar.sort(reverse=True)
print(sonlar)
print()
sonlar.sort(reverse=False)
print(sonlar)
print()
#---ikki ruyxatni paralel ishlatish---
savollar = ["2+2=?", "5*3=?", "10-4=?"]
javoblar = ["4", "15", "6"]
for i in range(len(savollar)):
    print(savollar[i], "->", javoblar[i])
print()