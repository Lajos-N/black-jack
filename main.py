
import random


#   váltózok

pakli_lapjai = ['kör 2', 'kör 3', 'kör 4', 'kör 5', 'kör 6', 'kör 7', 'kör 8', 'kör 9', 'kör 10', 'kör J', 'kör Q', 'kör K', 'kör A',
'káró 2', 'káró 3', 'káró 4', 'káró 5', 'káró 6', 'káró 7', 'káró 8 ', 'káró 9', 'káró 10', 'káró J', 'káró Q', 'káró K', 'káró A',
'treff 2', 'treff 3', 'treff 4', 'treff 5', 'treff 6', 'treff 7', 'treff 8', 'treff 9', 'treff 10', 'treff J', 'treff Q', 'treff K', 'treff A',
'pikk 2', 'pikk 3', 'pikk 4', 'pikk 5', 'pikk 6', 'pikk 7', 'pikk 8', 'pikk 9', 'pikk 10', 'pikk J', 'pikk Q', 'pikk K', 'pikk A']

pakli_szinei = ['kör', 'káró', 'treff', 'pikk']


lap = 0


#   metodusok / függvények



def lap_huzas(kihuzott_lap):
    lap = random.choice(pakli_lapjai)
    return lap
    



print(lap_huzas(lap))








'''
for j in pakli_szinei:			# nem tudom, hogy kell egy tömböt feltölteni egy ciklussal
	for i in range(2, 11):
		pass
		
'''








### egyébb
