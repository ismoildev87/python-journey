print("===Tanishuv boti===")  # tanishuv boshlanadi
print()
ism = input("Ismingiz nima? ")  # ismini kiritadi
familiya = input("Familiyangiz nima? ")  # familiyasini kiritadi
tuliq_ism = ism + " " + familiya
tugilgan_yil = int(input("Tugilgan yilingizni kiriting: "))  # tugilgan yilini kiritadi
yosh = 2026 - tugilgan_yil
yashagan_kunlar = yosh * 365
un_yildan_keyin_yosh = yosh + 10
shahar = input("Shahringizni kiriting: ")
oylik_daromad = float(input("Oylik daromadingizni kiriting: "))
yillik_daromad = oylik_daromad * 12
print()
print("---Natija---")  # natijani chiqarishni boshlaydi
print("To`liq ismingiz", tuliq_ism)
print("Sizning yoshingiz", yosh)
print("Sizning shahringiz", shahar)
print("Sizning yashagan kunlaringiz", yashagan_kunlar)
print("Sizning yillik daromadingiz", yillik_daromad)
print("Sizning o`n yildan keyin yoshingiz", un_yildan_keyin_yosh)
print("Tanishganimdan xursandman", ism)
