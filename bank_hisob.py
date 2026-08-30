class Hisob:
    def __init__(self, egasi):
        self.egasi = egasi
        self.balans = 0

    def pul_qoshish(self, summa):
        self.balans = self.balans + summa

    def pul_yechish(self, summa):
        if summa > self.balans:
            print("Balansda yetarli mablag' yo'q")
        else:
            self.balans = self.balans - summa


hisob1 = Hisob("Ismoil")
print(hisob1.egasi)
hisob1.pul_qoshish(100000)
print(hisob1.balans)

hisob1.pul_qoshish(50000)
hisob1.pul_qoshish(75000)
hisob1.pul_qoshish(5000)
print(hisob1.balans)

hisob1.pul_yechish(300000)
print(hisob1.balans)
hisob1.pul_yechish(200000)
print(hisob1.balans)
