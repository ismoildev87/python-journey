class Talaba:
    def __init__(self, ism):
        self.ism = ism
        self.ballar = []

    def ball_qosh(self, ball):
        self.ballar.append(ball)

    def ortacha(self):
        if len(self.ballar) == 0:
            return 0
        return round(sum(self.ballar) / len(self.ballar), 2)

    def __str__(self):
        return self.ism + " (o'rtacha: " + str(self.ortacha()) + ")"


class Guruh:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []

    def talaba_qosh(self, talaba):
        self.talabalar.append(talaba)


guruh1 = Guruh("Python-101")

talaba1 = Talaba("Ismoil")
talaba1.ball_qosh(85)
talaba1.ball_qosh(90)

talaba2 = Talaba("Vali")
talaba2.ball_qosh(70)
talaba2.ball_qosh(75)

guruh1.talaba_qosh(talaba1)
guruh1.talaba_qosh(talaba2)

print("Guruh:", guruh1.nomi)
for talaba in guruh1.talabalar:
    print(talaba)
