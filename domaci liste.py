#Nemanja Novakovic, liste domaci

# #1. Zadatak
#
# unos = eval(input('Unesite listu celih brojeva( primer [1,2,3]):'))
#
#
# print(len(unos))
# print(unos[-1])
# lista2 = unos.copy()
# unos.sort(reverse=True)
# if 5 in unos:
#     print('Da')
# else:
#     print('Ne')
# print(unos)
# print(unos.count(5))
# del lista2[-1]
# del lista2[1]
# lista2.sort(reverse=True)
# print(lista2)
#
# cb = 0
#
# for i in unos:
#     if i <5:
#         cb +=1
#
# print('Broj celih brojeva manji od 5 u vasoj listi je ', cb)

#######################################################################################################################

#2. Zadatak
#
# from random import randint
#
# lista = []
#
# for i in range(20):
#     lista.append(randint(1, 100))
# print(lista)
#
# sv = sum(lista) / len(lista)
# print('Srednja vrednost liste je :', sv)
#
# print('Najveca vrednost u listi je', max(lista))
# print('Najmanja vrednost u listi je', min(lista))
#
# lista.sort()
#
# print('Druga najveca vrednost u listi je ', lista[-2], ', a druga najmanja je: ', lista[1])
#
# parni = 0
#
# for i in lista:
#     if i % 2 == 0:
#         parni += 1
#
# print('Broj parnih brojeva u listi je: ', parni)

#######################################################################################################################

#3. Zadatak

# lista = [8, 9, 10]
#
# lista[1] = 17
# for i in range(3):
#     lista.append(i+4)
# del lista[0]
# lista.sort()
# lista = lista * 2
# lista.insert(3,25)
#
# print(lista)

#######################################################################################################################

#4.Zadatak

# unos = eval(input('Unesite listu sa brojevima izmedju 1 i 12:'))
#
# for i in range(len(unos)):
#     if unos[i] > 10:
#         unos[i] = 10
#
# print(unos)

#######################################################################################################################

#5. Zadatak


# lista = []
# broj = eval(input('Koliko stringova zelite da unesete ?'))
# for i in range(broj):
#     lista.append(input('Unesite string'))
#
# nova_lista = lista.copy()
#
# for i in range(len(nova_lista)):
#     nova_lista[i] = nova_lista[i][1:]
#
# print(nova_lista)

#######################################################################################################################
#6. Zadatak

# # a)
# lista = []
# for i in range(50):
#     lista.append(i)
#
# print(lista)
#
# # b)
# #
# lista = []
# for i in range(1, 50):
#     lista.append(i*i)
#
# print(lista)
#
# c)
# lista = []
# alfabet = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in range(1, len(alfabet) + 1):
#     lista.append(alfabet[i-1] * i)
#
# print(lista)

#######################################################################################################################

#7. Zadatak

# L = [3, 1, 4]
# M = [1, 5, 9]
# N = []
#
# for i in range(len(L)):
#     N.append(L[i] + M[i])
# print(N)

#######################################################################################################################
#
# 8. Zadatak

# broj = eval(input('Unesite neki ceo broj i dobicete faktore tog broja :'))
# lista = []
#
# if broj % 2 == 0:
#     for i in range(broj):
#         for b in range(broj):
#             if broj % 2 == 0 and i*b == broj:
#                 lista.append(b)
# else:
#     lista.append(broj)
#     lista.append(1)
#
# print(lista)

#######################################################################################################################
#9. Zadatak

# from random import randint
#
# lista = []
#
# for i in range(10000):
#     dice1 = randint(1,6)
#     dice2 = randint(1,6)
#     lista.append(dice1 + dice2)
#
# for i in range(2,13):
#     print('Procenat dobijanja zbira', i, 'je', (lista.count(i) /10000) * 100)



#######################################################################################################################

#10.Zadatak

# lista = ['Nis', 'Bor', 'Pirot', 'Kragujevac', 'Novi Sad', 'Beograd']
#
# lista_2 = ''
#
# for i in range(len(lista)):
#     lista.insert(-i, lista.pop(i))
#
#
# print(lista)

#######################################################################################################################

# 11. Zadatak
#
# lista = []
#
# nule = [0] * 5
#
# for i in range(10):
#     lista.append(1)
#     for i in range(lista.count(1)):
#         lista.append(0)
#
#
# print(lista)

#######################################################################################################################

#12. Zadatak

# from random import randint
# lista = []
#
# for i in range(100):
#     lista.append(randint(0,1))
#
# ukupno = []
# brojac = 0
#
# for i in range(1, len(lista)):
#     if lista[i-1] == 0 and lista[i-1] == lista[i]:
#         brojac +=1
#     elif lista[i-1] != lista[i]:
#         ukupno.append(brojac)
#         brojac = 0
#
# print(lista)
# print('Maksimalni broj ponovljenih nula je ', max(ukupno)+1)
#######################################################################################################################
#13.Zadatak

# lista = [1, 1, 2, 3, 4, 3, 0, 0]
#
# for i in range(len(lista)):
#     if lista.count(i) > 1:
#         del lista[lista.index(i)]
#
# print(lista)

#######################################################################################################################
#14.Zadatak

# unos = eval(input('Unesite duzinu u feets:'))
#
# print('''Iaberite konverziju:
#     1. Za Inches kucajte 0
#     2. Za Centimetre kucajte 1
#     3. Za metre kucajte 2
#     4. Za kilometre kucajte 3
# ''')
#
# broj = eval(input('Unesite zeljeni broj:'))
#
# konverzija = ['inches', 'cm.', 'm.', 'km.']
# formule = [unos * 12, unos*30.48, unos / 3.281, unos / 3281]
#
# print(unos, 'feets iznosi', formule[broj], konverzija[broj])

#######################################################################################################################

#15.Zadatak

# from random import randint
#
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# brojevi = []
# lokacija = []
# poruka = input('Unesite poruku koju zelite da sifrujete: ')
# sifrovana = ''
#
#
# for i in range(6):
#     brojevi.append(randint(1,25))
#
#
#
# for i in poruka:
#     lokacija.append(alphabet.index(i))
#
#
#
# for i in range(len(poruka)):
#     if lokacija[i] + brojevi[i] <26:
#         sifrovana += alphabet[lokacija[i] + brojevi[i]]
#     else:
#         sifrovana += alphabet[lokacija[i] - (lokacija[i] -brojevi[i])]
#
#
# print('Sifrovali smo vasu poruku, ona je sada:', sifrovana)
#######################################################################################################################
#16. Zadatak

# from random import randint
#
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# brojevi = []
# lokacija = []
# interpunkcija = ',.!'
# poruka = input('Unesite poruku koju zelite da sifrujete: ')
# poruka = poruka.lower()
# sifrovana = ''
# znaci = ''
#
# for i in range(6):
#     brojevi.append(randint(1,25))
#
# for i in poruka:
#     lokacija.append(alphabet.index(i))
#
#
# for i in range(len(poruka)):
#     if lokacija[i] + brojevi[i] <26:
#         sifrovana += alphabet[lokacija[i] + brojevi[i]]
#     else:
#         sifrovana += alphabet[lokacija[i] - (lokacija[i] -brojevi[i])]
#
# print('Sifrovali smo vasu poruku, ona je sada:', sifrovana)

#Ovde nisam znao kako da zadrzim znake interpunkcije

#######################################################################################################################
#17.Zadatak
#
# from random import randint

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# brojevi = []
# lokacija = []
# interpunkcija = ',.!'
# poruka = input('Unesite poruku koju zelite da sifrujete: ')
# poruka = poruka.lower()
# sifrovana = ''
# znaci = ''
# desifrovana = ''
# lokacija_2 = []
#
# for i in range(len(poruka)):
#     brojevi.append(randint(1,25))
#
# print(brojevi)
#
# for i in poruka:
#     lokacija.append(alphabet.index(i))
# print(lokacija)
#
# for i in range(len(poruka)):
#     if lokacija[i] + brojevi[i] <26:
#         sifrovana += alphabet[lokacija[i] + brojevi[i]]
#     else:
#         sifrovana += alphabet[lokacija[i] - (lokacija[i] -brojevi[i])]
#
# print('Sifrovali smo vasu poruku, ona je sada:', sifrovana)
#
# for i in sifrovana:
#     lokacija_2.append(alphabet.index(i))
# print(lokacija_2)
#
#
#
# for i in range(len(sifrovana)):
#     if brojevi[i] - (brojevi[i] - lokacija[i]) >= 0:
#         desifrovana += alphabet[brojevi[i] - (brojevi[i] - lokacija[i])]

#
# print(desifrovana)
