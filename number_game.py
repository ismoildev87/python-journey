yashirin_son = 7
javob = 0
urinish = 0
while javob != yashirin_son:
    javob = int(input("Sonni toping: "))
    urinish=urinish+1
    if javob < yashirin_son:
        print("Kattaroq son ayting")
    elif javob > yashirin_son:
        print("Kichikroq son ayting")
    else:
        print("Siz", urinish,"urinishda topdingiz!")
        break

