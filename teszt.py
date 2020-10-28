#   imprortált modulok

import random

#   globális változók

pakli = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
pakli_figuras_lapok = ['J', 'Q', 'K']

lap = None

elso_lap_jatekos = 0
masodik_lap_jatekos = 0
haramdik_lap_jatekos = 0
elso_lap_gep = 0
masodik_lap_gep = 0
harmadik_lap_gep = 0

jatekos_lapok_osszege_1 = 0
jatekos_lapok_osszege_2 = 0
jatekos_lapok_osszege_3 = 0

gep_lapok_osszege_1 = 0
gep_lapok_osszege_2 = 0
gep_lapok_osszege_3 = 0

jatekos_vegeredmeny = 0
gep_vegeredmeny = 0



#   függvények / metodusok

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


	
	




#							a gép lapot kér függvény (még nincs befejezve!!!)

#def gep_lapot_ker(lap):
#	if gep_lapok_osszege < 16:
#		pass # a gép kap még egy lapot
#	
#	else: 
#		pass # a gép már nem kap több lapot
#	


# a figurás lapokat értékkel látja el (jákékos)

def eredmeny_szamlalo_jatekos():
	
	if elso_lap_jatekos in pakli_figuras_lapok:
		jatekos_lapok_osszege_1 = 10
		print('jatékos elsö változó', jatekos_lapok_osszege_1)
		
	elif elso_lap_jatekos == 'A':
		jatekos_lapok_osszege_1 = 11
		print('jatékos elsö változó', jatekos_lapok_osszege_1)
		
	else:
		jatekos_lapok_osszege_1 = elso_lap_jatekos
		print('jatékos elsö változó', jatekos_lapok_osszege_1)
		
	
	if masodik_lap_jatekos in pakli_figuras_lapok:
		jatekos_lapok_osszege_2 = 10
		print('játékos második változó', jatekos_lapok_osszege_2)

	elif masodik_lap_jatekos == 'A':
		jatekos_lapok_osszege_2 = 11
		print('jatékos masodik változó', jatekos_lapok_osszege_2)
	
	else:
		jatekos_lapok_osszege_2 = masodik_lap_jatekos
		print('játékos második változó', jatekos_lapok_osszege_2)

	jatekos_vegeredmeny = jatekos_lapok_osszege_1 + jatekos_lapok_osszege_2
	print('játékos végeredmény', jatekos_vegeredmeny)



# a figurás lapokat értékkel látja el (gép)

def eredmeny_szamlalo_gep():
	
	if elso_lap_gep in pakli_figuras_lapok:
		gep_lapok_osszege_1 = 10
		print('gép elsö változó', gep_lapok_osszege_1)
	
	elif elso_lap_gep == 'A':
		gep_lapok_osszege_1 = 11
		print('gép elsö változó', gep_lapok_osszege_1)

	else:
		gep_lapok_osszege_1 = elso_lap_gep
		print('gép elsö változó', gep_lapok_osszege_1)
		
	
	if masodik_lap_gep in pakli_figuras_lapok:
		gep_lapok_osszege_2 = 10
		print('gép második változó', gep_lapok_osszege_2)

	elif masodik_lap_gep == 'A':
		gep_lapok_osszege_2 = 11
		print('gép masodik változó', gep_lapok_osszege_2)

	
	else:
		gep_lapok_osszege_2 = masodik_lap_gep
		print('gép masodik változó', gep_lapok_osszege_2)
		

	gep_vegeredmeny = gep_lapok_osszege_1 + gep_lapok_osszege_2
	print('gép végeredmény', gep_vegeredmeny)
	

def lap_keres():
	while True:
		i = input('Kérsz még lapot? (i/n)')
		if i == 'n':			
			break
		haramdik_lap_jatekos = lap_huzas(lap)
		print('jatékos harmadik lap: ', haramdik_lap_jatekos)
		


#	föprogram

elso_lap_jatekos = lap_huzas(lap)
print(elso_lap_jatekos)

elso_lap_gep = lap_huzas(lap)
print(elso_lap_gep)

masodik_lap_jatekos = lap_huzas(lap)
print(masodik_lap_jatekos)

masodik_lap_gep = lap_huzas(lap)
print(masodik_lap_gep)

eredmeny_szamlalo_jatekos()
eredmeny_szamlalo_gep()

lap_keres()





