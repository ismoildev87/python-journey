# --- ismni qabul qilib salomlashadi---
def salomlash(ism):
    print("Assalomu aleykum", ism)


salomlash("Ismoil")
salomlash("Gul")
print()


# --- sonning kupaytirish jadvalini chiqaradi ---
def kop_aytir(son):
    for i in range(1, 11):
        print(son, "x", i, "=", son * i)


kop_aytir(10)
print()


# --- uch sondan eng kattasini return qiladi ---
def eng_katta(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(eng_katta(5, 5, 6))
print(eng_katta(-1, -2, -3))
print()


# --- son juft bo'lsa True, aks holda False qaytaradi ---
def juftmi(son):
    if son % 2 == 0:
        return True
    else:
        return False


print(juftmi(15))
print(juftmi(10))


# ortacha(sonlar) — ro'yxat qabul qilib, o'rtachasini qaytaradi
def ortacha(sonlar):
    return sum(sonlar) / len(sonlar)


ballar = [1, 5, 5, 15]
print(ortacha(ballar))
print()


# hisobla(a, b, amal) — ikki son va amal belgisini ("+", "-", "*", "/") olib,
# natijani qaytaradi
def hisobla(a, b, amal):
    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        if b == 0:
            return "Nolga bulish mumkin emas"
        return a / b
    else:
        return "Notugri amal kiritildi"


print(hisobla(10, 3, "+"))
print(hisobla(10, 3, "/"))
print(hisobla(10, 0, "*"))
print(hisobla(5, 0, "/"))
