import random

a = []
b = ['kör', 'káró', 'treff', 'pikk']
c = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def pakli_osszeall():
    for szin in b:
        for szam in c:     
            kozos = szin, szam
            a.append(kozos)

        

# def lap_huzas(p):
#     return random.choice(a)


pakli_osszeall()
# print(lap_huzas(a))

print(len(a))
print(a[0])



