#   imprortált modulok

import random

#   globális változók

#pakli = []
#pakli_szin = ['kör', 'káró', 'treff', 'pikk']
pakli = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

lap = None

elso_lap_jatekos = 0
masodik_lap_jatekos = 0
elso_lap_gep = 0
masodik_lap_gep = 0

jatekos_lapok_osszege = 0
gep_lapok_osszege = 0




#   függvények / metodusok

# összeállítja a paklit
#def pakli_osszeall():
#    for szin in pakli_szin:
#        for szam in pakli_szam:     
#            kozos = szin, szam
#            pakli.append(kozos)

# a pakliból kihúz egy lapot amit átad a lap változónak
def lap_huzas(kihuzott_lap):
	lap = random.choice(pakli)
	pakli.remove(lap)
	return lap

#def lap_eltavolito(lap):
#	pakli.remove(lap_huzas(pakli))
	

# for ciklussal kihúzott lapok törlése a pakliból
'''
def pakli_tesztelö_ciklus():
	for i in range(52):
		#pakli.remove(lap_huzas(pakli))
		print()
		print('lapok szama')
		print(len(pakli))
		print()
		print('kihuzott lap')
		print(lap_huzas(lap))
		print()
		print('pakli:')
		print(pakli)
'''

def jatek(lap):
	print('ez az elsö valtozo')
	elso_lap_jatekos = lap
	print(elso_lap_jatekos)
	
	




#							a gép lapot kér függvény (még nincs befejezve!!!)

#def gep_lapot_ker(lap):
#	if gep_lapok_osszege < 16:
#		pass # a gép kap még egy lapot
#	
#	else: 
#		pass # a gép már nem kap több lapot
#	
def eredmeny_szamlalo():
	if elso_lap_jatekos == 'J' or 'Q' or 'K':
		jatekos_lapok_osszege = 10
		
	#jatekos_lapok_osszege = int(elso_lap_jatekos) + int(masodik_lap_jatekos)
	print(jatekos_lapok_osszege)
	gep_lapok_osszege = int(elso_lap_gep) + int(masodik_lap_gep)
	print(gep_lapok_osszege)




#	föprogram


elso_lap_jatekos = lap_huzas(lap)
print(elso_lap_jatekos)

elso_lap_gep = lap_huzas(lap)
print(elso_lap_gep)

masodik_lap_jatekos = lap_huzas(lap)
print(masodik_lap_jatekos)

masodik_lap_gep = lap_huzas(lap)
print(masodik_lap_gep)

eredmeny_szamlalo()






