#   imprortált modulok

import random

#   globális változók

pakli = []
pakli_szin = ['kör', 'káró', 'treff', 'pikk']
pakli_szam = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

lap = 0



#   függvények / metodusok

# összeállítja a paklit
def pakli_osszeall():
    for szin in pakli_szin:
        for szam in pakli_szam:     
            kozos = szin, szam
            pakli.append(kozos)

# a pakliból kihúz egy lapot amit átad a lap változónak
def lap_huzas(kihuzott_lap):
    lap = random.choice(pakli)
    #print(lap)
    return lap
	
def lap_eltavolito(lap):
	pakli.remove(lap_huzas(pakli))
	

# for ciklussal kihúzott lapok törlése a pakliból
def pakli_tesztelö_ciklus():
	for i in range(len(pakli)-1):
		pakli.remove(lap_huzas(pakli))
		print(len(pakli))


pakli_osszeall()
#pakli_tesztelö_ciklus()


#	föprogram

# pakli lapjainak számolása
print(len(pakli))
print(lap_huzas(lap))
lap_eltavolito(lap)
print()


print(len(pakli))
print(lap_huzas(lap))
lap_eltavolito(lap)
print()

print(len(pakli))
print(lap_huzas(lap))
lap_eltavolito(lap)
print()

print()
print()
print(len(pakli))
print(pakli)






