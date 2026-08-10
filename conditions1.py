# --- if / elif / else : bir necha variant ---
ball = int(input("Imtihon balingizni kiriting(0-100):"))

if ball >= 90:
    baho = "A`lo"
elif ball >= 70:
    baho = "Yaxshi"
elif ball >= 50:
    baho = "qoniqarli"
else :
    baho = "Qoniqarsiz"
print ("Sizning bahoingiz:", baho)

print ()