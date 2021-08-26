# 1 Zadatak

# proizvodi = list()
# cene = list()
# print('Da izadjete iz programa unesite "kraj"')
# while 1:
#     proizvod = input('Unesite ime proizvoda\n').lower()
#     if proizvod == 'kraj':
#         break
#     proizvodi.append(proizvod)
#     cena = eval(input('Unesite cenu proizvoda\n'))
#     cene.append(cena)
#
# cenovnik = dict()
#
# for i in range(len(proizvodi)):
#     cenovnik[proizvodi[i]] = cene[i]
#
# print(cenovnik)
#
# while 1:
#     unos = input('Unesite ime proizvoda ciju cenu zelite da vidite').lower()
#     if unos == 'kraj':
#         break
#     if unos in cenovnik:
#         print('Cena za {:s} je {:d}'.format(unos, cenovnik[unos]))
#     else:
#         print('Proizvod koji ste uneli ne postoji u cenovniku')

#####################################################################################################################
#
# #2.Zadatak
#     provera = eval(input('Unesite cenu\n'))
#     for i in cenovnik:
#         if provera > cenovnik[i]:
#             print(i)
#         else:
#             print('Ne postoji toliko niska cena u ovom cenovniku')
#

#####################################################################################################################


#3-4.Zadatak(kombinovano)

# dana = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# meseci = {'Januar':31, 'Februar':28, 'Mart':31, 'April':30,
#         'Maj':31, 'Jun':30, 'Jul':31, 'Avgust':31,
#         'Septembar':30, 'Oktobar':31, 'Novembar':30, 'Decembar':31}
#
# while 1:
#     test = input('Unesite mesec da vidite broj dana u tom mesecu. Da izadjete iz programa unesite "kraj"\n')
#     if test == 'kraj':
#         break
#
#     if test in meseci:
#         print('Broj dana u mesecu koji ste uneli je: {:d}'.format(meseci[test]))
#         print('')
#     if test not in meseci:
#         print('Uneli ste mesec koji ne postoji, pazite da prvo slovo meseca bude veliko slovo, probajte ponovo')
#     redosled = []
#
#     for i in meseci:
#         redosled.append(i)
#     redosled.sort()
#     print(redosled)
#     print('')
#     print('Meseci koji imaju 31 dan su sledeci:')
#
#
#     for i in meseci:
#         if meseci[i] == 31:
#             print(i)
#     print('Kljuc-vrednost parovi sortirani po danima u mesecu')
#     for i in meseci:
#         if meseci[i] == 30:
#             print(i, meseci[i])
#     for i in meseci:
#         if meseci[i] == 31:
#             print(i, meseci[i])



# DODATAK ZA 4 ZADATAK ( •	Modifikujte program tako da korisnik može da unese samo prva tri znaka iz naziva meseca.)

#     if len(test) == 3:
#         for k in meseci.keys():
#             if test == k[0:3]:
#                 print('Broj dana u mesecu koji ste uneli je: {:d}'.format(meseci[k]))
#

#####################################################################################################################


#5.Zadatak

# usernames = {'zoran': 'fff1', 'gojko': '2222a', 'marko32':'geaafeafae', 'stefan777':'ddddd5', 'mitar':'123', 'volimpfc':'pfc', 'volimrsfc':'rsfc', 'borbor':'nijebor', 'pirotpirot':'nijepirot', 'babusnica':'jestebabusnica'}
#
# korisnickoime = input('Unesite korisnicko ime\n')
# sifra = input('Unesite password\n')
#
# if korisnickoime not in usernames:
#     print('Takvo korisnicko ime ne postoji.')
# elif korisnickoime in usernames and sifra != usernames[korisnickoime]:
#     print('Vas password nije ispravan.')
# elif korisnickoime in usernames and sifra == usernames[korisnickoime]:
#     print('Ulogovani ste u sistem.')

#####################################################################################################################

#6.Zadatak

# recnik = dict()
# print('Da izadjete iz programa unesite "kraj"')
#
# while 1:
#     tim = input('Unesite ime tima\n')
#     if tim == 'kraj':
#         break
#     skor = input('Unesite broj pobeda i poraza tima(u formatu: 30-15, 23-20)\n')
#     recnik[tim] = skor
#
# print(recnik)
# procenti = input('Unesite tim iz tabele iznad za koji zelite da vidite procenat pobeda\n')
#
#
# for i in recnik:
#     if procenti in recnik:
#         x = recnik[procenti].index('-')
#         y = int(recnik[procenti][:x]) / ((int(recnik[procenti][:x]) + int(recnik[procenti][x+1:])))
#         print('{:.2f} je procenat pobede tima koji ste uneli'.format(y*100))
#
#
# pobede = []
# for i in recnik:
#     x = recnik[i].index('-')
#     pobede.append(recnik[i][:x])
# print('Pobede svih timova', pobede)
#
# konacno = []
# for i in recnik:
#     x = recnik[i].index('-')
#     if int(recnik[i][:x]) > int(recnik[i][x+1:]):
#         konacno.append(i)
#
# print('Svi timovi koji imaju vise pobeda nego poraza:')
# print(konacno)
#
#####################################################################################################################
# 7. Zadatak
# skor = dict()
# while 1:
#     unos = input('Unesite rezultate utakmica\n( u formatu: Srbija5-Brazil2)\nDa izadjete unesite "kraj"\n')
#     if unos == 'kraj':
#         break
#     x = unos.index('-')
#     tim1 = unos[:x-1]
#     tim2 = unos[x+1:-1]
#
#     score = ''
#     for i in unos:
#         if i.isdigit():
#             score += str(i)
#
#     if tim1 not in skor:
#         skor[tim1] = [0, 0]
#         if int(score[0]) > int(score[1]):
#             skor[tim1][0] += 1
#         if int(score[0]) < int(score[1]):
#             skor[tim1][1] += 1
#     else:
#         if int(score[0]) > int(score[1]):
#             skor[tim1][0] += 1
#         if int(score[0]) < int(score[1]):
#             skor[tim1][1] += 1
#
#     if tim2 not in skor:
#         skor[tim2] = [0, 0]
#         if int(score[0]) > int(score[1]):
#             skor[tim2][1] += 1
#         if int(score[0]) < int(score[1]):
#             skor[tim2][1] += 1
#     else:
#         if int(score[0]) > int(score[1]):
#             skor[tim2][1] += 1
#         if int(score[0]) < int(score[1]):
#             skor[tim2][0] += 1
#
# print(skor)

#####################################################################################################################

#8.Zadatak
#
# from random import randint
# lista = list()
#
# for i in range(5):
#     lista.append([randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)])
#
# recnik = dict()
# print(lista)
#
# for i in range(len(lista)):
#     for x in lista[i]:
#         if x in lista[i]:
#             if x in recnik:
#                 recnik[x] = recnik[x] + 1
#             else:
#                 recnik[x] = 1
#
# print(recnik)

#####################################################################################################################

#9.Zadatak

# from random import randint
#
# spil = [{'vrednost': i, 'boja' : c}
#
#         for c in ['pik', 'tref', 'herc', 'karo']
#         for i in range(2,15)]
#
# igrac1 = []
# igrac2 = []
#
# for i in range(3):
#     r = randint(0, 51)
#     igrac1.append(spil[r])
#
# for i in range(3):
#     r = randint(0, 51)
#     igrac2.append(spil[r])
#
# igrac1jacina = []
# igrac2jacina = []
#
# for i in range(len(igrac1)):
#     if 'vrednost' in igrac1[i]:
#         igrac1jacina.append(igrac1[i]['vrednost'])
#     if 'vrednost' in igrac2[i]:
#         igrac2jacina.append(igrac2[i]['vrednost'])
#
# igrac1jacina.sort(reverse=True)
# igrac2jacina.sort(reverse=True)
#
# while 1:
#
#     if igrac1jacina[0] > igrac2jacina[0]:
#         print('Pobedio je igrac1, sa rukom', igrac1[0]['vrednost'])
#         break
#     else:
#         print('Pobedio je igrac2 sa rukom', igrac2[0]['vrednost'])
#         break
#
#     if igrac1jacina[0] == igrac2jacina[0]:
#         if igrac1jacina[1] > igrac2jacina[1]:
#             print('Pobedio je igrac1, sa rukom', igrac1[1]['vrednost'])
#             break
#         else:
#             print('Pobedio je igrac2, sa rukom', igrac2[1]['vrednost'])
#             break
#
#     if igrac1jacina[1] == igrac2jacina[1]:
#         if igrac1jacina[2] > igrac2jacina[2]:
#             print('Pobedio je igrac1, sa rukom', igrac1[2]['vrednost'])
#             break
#         else:
#             print('Pobedio je igrac1, sa rukom', igrac2[2]['vrednost'])
#             break
#
#     if igrac1jacina[1] == igrac2jacina[1]:
#         print('Oba igraca imaju ruke iste jacine')
#         break
#
# print(igrac1)
# print(igrac2)

#####################################################################################################################

#10. Zadatak

# from random import randint
#
# spil = [{'vrednost': i, 'boja' : c}
#
#         for c in ['pik', 'tref', 'herc', 'karo']
#         for i in range(2, 15)]
#
# ruka = []
#
# for i in range(3):
#     r = randint(0, 51)
#     ruka.append(spil[r])
#
# print(ruka)
#
# for i in range(1):
#     if ruka[0]['boja'] == ruka[1]['boja'] == ruka[2]['boja']:
#         print('Sve tri karte su istog znaka, imate boju!')
#
# for i in range(1):
#     if ruka[0]['vrednost'] == ruka[1]['vrednost'] == ruka[2]['vrednost']:
#         print('Sve tri karte su iste, imate triling!')
#
# for i in range(1):
#     if ruka[0]['vrednost'] == ruka[1]['vrednost'] or  ruka[0]['vrednost'] == ruka[2]['vrednost'] or ruka[1]['vrednost'] == ruka[2]['vrednost']:
#         print('Dve karte su vam iste, imate par!')
#
# for i in range(1):
#     if ruka[2]['vrednost'] - ruka[1]['vrednost'] ==1 and  ruka[1]['vrednost'] - ruka[0]['vrednost'] == 1:
#         print('Karte su vam u nizu, imate liniju(kentu)!')

#####################################################################################################################

#11.Zadatak

# from random import randint
#
# spil = [{'vrednost': i, 'boja' : c}
#
#         for c in ['pik', 'tref', 'herc', 'karo']
#         for i in range(2, 15)]
#
# flush_counter = 0
# for b in range(100000):
#     ruka = []
#     for i in range(3):
#         r = randint(0,51)
#         ruka.append(spil[r])
#
#     if ruka[0]['boja'] == ruka[1]['boja'] == ruka[2]['boja']:
#         flush_counter +=1
#
# print('Procenat dobijanja boje u 100 000 deljenja je {:.2f}%'.format((flush_counter / 100000) * 100))

#####################################################################################################################

#12.Zadatak

# recnik = dict()
#
# rec_1 = input('Unesite prvu rec')
# rec_2 = input('Unesite drugu rec')
#
# for i in range(len(rec_1)):
#     recnik[rec_1[i]] = rec_2[i]
#
# for k,v in recnik.items():
#     if k == v:
#         print('Rec 2 ne moze biti sifrovana verzija od rec 1')
#
# broj = 0
#
# for i in range(len(rec_1)):
#     if rec_1.count(rec_1[i]) > 1:
#         broj += 1
#
# broj2 = 0
#
# for i in range(len(rec_2)):
#     if rec_2.count(rec_2[i]) > 1:
#         broj2 += 1
#
# if broj != broj2 :
#     print('Rec 2 ne moze biti sifrovana verzija od reci 1')

#####################################################################################################################

#13.Zadatak

# L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
#
# mustra = input('Unesite mustru')
#
# proba = dict()
#
# for i in range(len(mustra)):
#     if mustra[i].isalpha() == True:
#         proba[i] = mustra[i]\
#
# nadjeni = []
#
# for k,v in proba.items():
#         for i in range(len(L)):
#             if L[i][k] == v:
#                 nadjeni.append(i)
#
# ns = set()
#
# for i in nadjeni:
#     if nadjeni.count(i) == len(proba):
#         ns.add(i)
#
# for i in ns:
#     print(L[i])

#####################################################################################################################
#14.Zadatak

# d=[{'ime':'Janko', 'telefon':'555-1414', 'email':'janko@mail.net'},
#    {'ime':'Marko', 'telefon':'555-1618', 'email':'marko@mail.net'},
#    {'ime':'Ana', 'telefon':'555-3141', 'email':''},
#    {'ime':'Jovana', 'telefon':'555-2718', 'email':'jovana@mail.net'}]
#
#
# for recnik in d:
#     if recnik['telefon'][-1] == '8':
#         print(recnik['ime'], recnik['telefon'])
# for recnik in d:
#     if recnik['email'] == '':
#         print(recnik['ime'], 'nema email adresu')

#####################################################################################################################

#16.Zadatak

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
#
# C = A.union(B)
# D = A & B
# print('Unija skupova {1, 2, 3, 4, 5} i {4, 5, 6, 7, 8}   je', C)
# print('Presek skupova {1, 2, 3, 4, 5} i {4, 5, 6, 7, 8}   je', D)