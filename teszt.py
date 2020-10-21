#   imprortált modulok

import random

#   globális változók

a = []
b = ['kör', 'káró', 'treff', 'pikk']
c = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

lap = 0
index = None


#   függvények / metodusok

def pakli_osszeall():
    for szin in b:
        for szam in c:     
            kozos = szin, szam
            a.append(kozos)

def lap_huzas(kihuzott_lap):
    lap = random.choice(a)
    print(lap)
    return lap
        
# def kihuzott_lap_indexe(lap):
#     index = a.index(lap)
#     return index

# print(kihuzott_lap_indexe(lap))

pakli_osszeall()


for i in range(len(a)-1):
    a.remove(lap_huzas(a))
    print(len(a))
    # if len(a) <= 0:
    #     break

# pakli lapjainak számolása
print(len(a))
print(lap_huzas(lap))

# print(lap)



