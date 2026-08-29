def hisobla(a, b, amal):
    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        return a / b


while True:
    try:
        a = int(input("birinchi sonni kiriting: "))
        b = int(input("ikkinchi sonni kiriting: "))
        amal = input("amalni kiriting: ")
        natija = hisobla(a, b, amal)
        print("Natija: ", natija)
        break
    except ValueError:
        print("Son emas, qaytadan urining")
    except ZeroDivisionError:
        print("Nolga bo'lib bo'lmaydi!")
