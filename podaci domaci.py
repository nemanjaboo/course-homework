# 1. Zadatak

# niz = list()
#
# for i in range(3,101,3):
#     niz.append(i)
#
# print(niz)

# 2.Zadatak

# unos = eval(input('Molimo unesite tezinu u funtama:'))
#
# konverzija = unos / 2.2046
#
# print('Vasa tezina u kg iznosi {:.1f}'.format(konverzija))

# 3.Zadatak
#
# unos = input('Unesite neku rec :')
# lista = list()
#
# for i in unos:
#     lista.append(i)
#
# lista.sort()
# print(lista)
#

# 4.Zadatak

# proizvodi = ['banane','hleb','secer','ulje','so','narandze','kafa','masline','sok','cokolada']
# cene = [110, 50, 105, 140, 98, 130, 120, 150, 99, 116]
#
# for i in range(len(proizvodi)):
#     print('{:9s} RSD {:9.2f}'.format(proizvodi[i], cene[i] - (cene[i] / 11)))

# 5. Zadatak

# boja = ['Herc', 'Karo', 'Tref', 'Pik']
# vrednost = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Žandar', 'Dama', 'Kralj', 'As']

# 6. Zadatak

# from random import randint
#
# lista1 = list(range(0, randint(1, 10)))
# lista2 = list(range(5, randint(10, 15)))
# print(lista1)
# print(lista2)
#
# for i in range(len(lista1)):
#     if lista1[i] in lista2:
#         x = True
#     else:
#         x = False
#
# print(x)


# 7. Zadatak

# lista = [int('1' * i) for i in range(1, 101)]
#
# print(lista)
#

# 8.Zadatak

# lista = []
#
# for i in range(1,101):
#     lista.append(i)
#
# for i in range(len(lista)):
#     if i % 7 ==0 and str(i)[-1] == '6':
#         print(i)

# 9.Zadatak

# brojevi = list(range(1, 10001))
# brojac = 0
#
# for i in brojevi:
#     if '3' in str(i):
#         brojac +=1
#
# print('U listi ima {:d} podataka sa brojem 3 u sebi'.format(brojac))

# 10.Zadatak

# brojac = 0
#
# for i in range(84, 85):
#     x= i + int(str(i)[::-1]
#     if str(x) != str(x)[::-1]:
#
#


# 11.Zadatak

# 12. Zadatak

# 1961


# lista = []
#
# for i in range (1,1000000):
#     lista.append(i)
#
# for i in range(len(lista)):
#     if '2' in str(lista[i]):
#         del lista[i]
#
# print(lista)


#13. Zadatak

# for i in range(90, 10000):
#    if int(str(i)[1]) + int(str(i)[-1]) + (int(str(i)[1]) * int(str(i)[-1])) == i:
#        print(i)

# lista = []
#
# for i in range(90, 101):
#    lista.append(str(i))
#
# for i in range(len(lista)-1):
#     if int(lista[i][1]) * int(lista[i][-1]) + (int(lista[i][1]) + (int(lista[i][-1]))) == lista[i]:
#         print(i)

#14. Zadatak


#15. Zadatak

# broj = 10000000
# broj = str(broj)
# novi = broj[::-1]
# print(novi)
#
# brojac = 0
#
# for i in range(len(novi)):
#     if int(novi[i]) == 0:
#         brojac += 1
# print('Broj nula u zadatom broju je', brojac)

#16.Zadatak

# unos = eval(input('Unesite visinu u feet'))
#
# decimalni = unos - int(unos)
# inches = decimalni * 12
#
# print('To iznosi', unos, 'feets', inches, 'inches' )

#17.Zadatak

# skorovi = list()
# skorovi_2 = list()
# najveci = list()
# najmanji = list()
#
# while 1:
#     unos = input('Unesite skorove(npr: 33-12):')
#     if unos.lower() == 'kraj':
#         break
#     skorovi.append(unos)
#
# for i in range(len(skorovi)):
#     skorovi_2.append((str(skorovi[i])))
#
# for i in range(len(skorovi_2)):
#     x = skorovi_2[i].index('-')
#     najveci.append(int(skorovi_2[i][:x]))
#     najmanji.append(int(skorovi_2[i][x+1:]))
#
# print(max(najveci),'je najveci skor')
# print(min(najmanji),'je najmanji skor')
#

#18.Zadatak

# lista = []
# februar = 0
# dvapet = 0
# while 1:
#     unos = input('Unesite datum rodjenja u formatu mesec/dan:')
#     if unos == 'kraj':
#         break
#     lista.append(unos)
#
# print(lista)
#
#
# for i in range(len(lista)):
#     x = lista[i].index('/')
#     if lista[i][:x] == '04' or  lista[i][:x] == '4':
#         februar +=1
#     if lista[i][x+1:] == '25':
#         dvapet +=1
#
# print('Unetih rodjendana koji su u februaru bilo je {:d}'.format(februar))
# print('Unetih rodjendana koji su 25og u mesecu bilo je {:d}'.format(dvapet))

#19.Zadatak

# unos = input('Unesite datum rodjenja u formatu mm/dd/yy :')
#
# #02/04/77  Februar 4, 1977
#
# meseci = ['Januar', 'Februar', 'Mart', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar', 'Januar']
#
# for i in range(len(unos)):
#     unos = unos.replace('/', ' ')
#     msc = int(unos[:2])
#     dan = str(int(unos[3:6]))
#     god = '19' + str(int(unos[6:]))
#
# print('Konvertovani datum je: ', str(meseci[msc]) + dan + ', ' + god + '.')

#20.Zadatak

# unos = input('Unosite razlomak koji zelite da skratite:')
#
# prvi = int(unos[:unos.index('/')])
# drugi = int(unos[unos.index('/')+1:])
#
# nzd = 0
#
# i = prvi
# b = drugi
#
# while 1:
#     if i > b:
#         b = b -1
#     if prvi % b == 0 and drugi % b == 0:
#         print(i)
#     if i < b:
#         i = i -1
#     if prvi % i == 0 and drugi % i == 0:
#         nzd = i
#         break
#
# skraceni = str(prvi//nzd) + '/' + str(drugi//nzd)
#
# print('Najmanji zajednicki sadrzalac je {:d}'.format(nzd))
# print('Vas skraceni razlomak je {:s}'.format(skraceni))

#21.Zadatak

# mango = 5
# grejp = 3
# triJabuke = 1
#
# m = (100 // 3) // 5
# g = (100//3) // 3
# j = (100//3) // 3
#
# print(m)
# print(g)
# print(j)

#22.Zadatak

# izraz = '43 + 57 = 207'
#
# deo1 = list(izraz[:2])
# deo2 = list(izraz[5:7])
# deo3 = list(izraz[-3:])
#
#
#
# while int(str(deo1)) + int(str(deo2)) != int(str(deo3)):
#     for i in range(len(deo1+deo2+deo3)):
#         deo1[i] = int(deo1[i]) +1

#23.Zadatak

from random import randint

# x = 0
# y = 0
#
# pell = x * 2 - 2 * y * 2


#24. Zadatak


#25. Zadatak

# prva = [i for i in range(1, 7)]
# druga = [i for i in range(1, 7)]
# treca = [i for i in range(1, 7)]
# cetvrta = [i for i in range(1, 7)]
#
# bacanja = []
#
# for i in prva:
#     for b in druga:
#         for c in treca:
#             for d in cetvrta:
#                 bacanja.append([i,b,c,d])
#
# rezultati = []
#
# for i in range(len(bacanja)):
#     for b in range(len(bacanja[i])):
#         rezultati.append(bacanja[b] + bacanja[b+1])
#         rezultati.append(bacanja[b] + bacanja[b + 2])
#         rezultati.append(bacanja[b] + bacanja[b + 3])

#26.Zadatak