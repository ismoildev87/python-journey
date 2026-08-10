# yoshga qarab davrni belgilash
ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
if yosh < 0:
    print(ism,"notugri yosh kiritdingiz")
elif yosh >= 150:
    print(ism,"notugri yosh kiritdingiz")
elif yosh <= 6:
    print(ism,"siz bolalik davridasiz")
elif yosh <= 17:
    print(ism,"siz maktab davridasiz")
elif yosh <= 35:
    print(ism,"siz yoshlik davridasiz")
elif yosh <= 60:
    print(ism,"siz yetuklik davridasiz")
else:
    print(ism,"siz keksalik davridasiz")


    

