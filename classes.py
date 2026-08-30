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


talaba1 = Talaba("Ismoil")
talaba1.ball_qosh(85)
talaba1.ball_qosh(90)
talaba1.ball_qosh(95)
talaba2 = Talaba("Ali")
talaba2.ball_qosh(80)
talaba2.ball_qosh(85)
talaba2.ball_qosh(88)

print(talaba1.ism)
print(talaba1.ballar)
print(talaba1.ortacha())
print(talaba2.ism)
print(talaba2.ballar)
print(talaba2.ortacha())
