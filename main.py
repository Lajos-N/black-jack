
import random

pakli_lapjai = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
pakli_szinei = ['kör', 'káró', 'treff', 'pikk']


def lap_huzas(p):   # probléma van, ha szám és szöveg kerül kihúzásra
    return random.choice(pakli_lapjai) + random.choice(pakli_szinei)
    



print(lap_huzas(pakli_lapjai))







### egyébb


# def dontes(nev):
    # return 'A neved: ' + nev


# def osszead(a, b):
    # return a + b


# nev = input('Név ')
# print(dontes(nev))
