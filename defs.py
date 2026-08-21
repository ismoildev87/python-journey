def salomlash(ism):
    print("Assalomu alaykum,", ism)

salomlash("Ismoil")      # Assalomu alaykum, Ismoil
salomlash("Vali")        # Assalomu alaykum, Vali
# --- 1. Eng oddiy funksiya ---
def salomlash():
    print("Assalomu alaykum!")

salomlash()          # chaqirish
salomlash()          # yana
print()
# --- 2. Parametr bilan ---
def salomlash_ism(ism):
    print("Salom,", ism)

salomlash_ism("Ismoil")
salomlash_ism("Vali")
print()
# --- 3. Bir nechta parametr ---
def tanishtir(ism, yosh, shahar):
    print(ism, "—", yosh, "yosh,", shahar)

tanishtir("Ismoil", 39, "Qo'qon")
print()
# --- 4. return bilan ---
def kvadrat(son):
    return son * son
natija = kvadrat(6)
print(natija)              # 36
print(kvadrat(10) + kvadrat(11))   # 100 + 121 = 221
print()
# --- 5. print va return farqi ---
def yigindi_print(a, b):
    print(a + b)

def yigindi_return(a, b):
    return a + b

x = yigindi_print(2, 3)    # 5 chiqadi
print("x =", x)            # x = None — hech narsa qaytarmadi!

y = yigindi_return(2, 3)   # hech narsa chiqmaydi
print("y =", y)            # y = 5
def yigindi_return (5, 2):
    print (5)