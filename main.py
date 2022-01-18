'''
1.1 Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!
'''

import random 

lista = []

for _ in range(5):
   veletlen = random.randint(1,10)
   lista.append(veletlen)
 

osszeg = 0
for szam in lista:
  osszeg += szam 
print(osszeg)
print(lista)