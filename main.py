'''
5. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! 
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvénynek, amely a lista legkisebb elemével tér vissza. 
A program írja ki, hogy melyik volt a megadott legkisebb szám!
'''

lista = []
while True:
    beker = int(input('Számok: (negatív szám esetén kilépsz): \t'))
    if beker > 0:
        lista.append(beker)
    else:
        break


def legkisebb(lista):
    return f'Legkisebb érték: {min(lista)}'

print(legkisebb(lista))