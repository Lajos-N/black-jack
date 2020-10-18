
import random


#   váltózok

pakli_lapjai = ['kör 2', 'kör 3', 'kör 4', 'kör 5', 'kör 6', 'kör 7', 'kör 8', 'kör 9', 'kör 10', 'kör j', 'kör q', 'kör k', 'kör a',
'káró 2', 'káró 3', 'káró 4', 'káró 5', 'káró 6', 'káró 7', 'káró 8 ', 'káró 9', 'káró 10', 'káró j', 'káró q', 'káró k', 'káró a',
'treff 2', 'treff 3', 'treff 4', 'treff 5', 'treff 6', 'treff 7', 'treff 8', 'treff 9', 'treff 10', 'treff j', 'treff q', 'treff k', 'treff a',
'pikk 2', 'pikk 3', 'pikk 4', 'pikk 5', 'pikk 6', 'pikk 7', 'pikk 8', 'pikk 9', 'pikk 10', 'pikk j', 'pikk q', 'pikk k', 'pikk a']


lap = 0
jatekos = 0
gep = 0 

#   metodusok / függvények



def lap_huzas(kihuzott_lap):
    lap = random.choice(pakli_lapjai)
    i = random.choice(pakli_lapjai)
    #del pakli_lapjai[i]
    return lap
    



def jatek_menete():
    jatekos = lap_huzas(lap) + " "
    gep = lap_huzas(lap) + " "
    jatekos += lap_huzas(lap)
    gep += lap_huzas(lap)


    print("Játékos:", jatekos)
    print("Gép    :", gep)


# def lap_erteke(jatekos):
#     if jatekos[:-1] == figurak:   # ez in figurak     valami szerepel-e a figurák változóban? Értékként igaz / hamis-at ad vissza
#         szamlalao = "igen"

#     return szamlalao




jatek_menete() 
# print(lap_erteke(szamlalo))



















### egyébb
