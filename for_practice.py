# Oddiy sonlar qatori
for i in range(20):
    print(i)
# 1 dan 50 gacha faqat 5 ga karrali sonlar
for son in range(0, 50, 5):
    print(son)
# % bilan 5 ga karralini chiqarish
for son in range(0,50):
    if son % 5 == 0:
        print(son)
# foktarialni hisoblash
foktarial = 1
son = int(input("Qaysi sonning foktariali kerak? "))
for i in range(1, son+1):
    foktarial = foktarial * i
print(son,"foktarial:", foktarial)
# kiritgan songacha juft sonlar yig'indisi
son = int(input("sonni kiriting: "))
yigindi = 0
for i in range(0, son+1, 2):
    yigindi = yigindi + i
print(yigindi)
# harflar ketma ketligi
soz = input("so`zni kiriting: ")
for harf in soz:                
    print(harf)
# harflar yonma yon
soz = input("so`zni kiriting: ")
for harf in soz:                
    print(harf, end="    ")