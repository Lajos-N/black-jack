#   imprortált modulok

import random

#   globális változók

pakli = []
pakli_szin = ['kör', 'káró', 'treff', 'pikk']
pakli_szam = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

lap = 0
index = None


#   függvények / metodusok

def pakli_osszeall():
    for szin in pakli_szin:
        for szam in pakli_szam:     
            kozos = szin, szam
            pakli.append(kozos)

def lap_huzas(kihuzott_lap):
    lap = random.choice(pakli)
    print(lap)
    return lap


pakli_osszeall()


for i in range(len(pakli)-1):
    pakli.remove(lap_huzas(pakli))
    print(len(pakli))


#	föprogram

# pakli lapjainak számolása
print(len(pakli))
print(lap_huzas(lap))





