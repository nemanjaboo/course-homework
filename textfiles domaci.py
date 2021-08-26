#1. Zadatak

# rezultati = [c.strip() for c in open('rezultati_testa.txt')]
#
# b = open('rezultati_testa1.txt', 'w')
# for i in range(len(rezultati)):
#    b.write(rezultati[i][:-2] + str(int(rezultati[i][-2:]) + 10) + '\n')

###################################################################################################################

#2.Zadatak

# ocene = [i.strip() for i in open('ocene.txt')]
# ocene2 = []
# for i in range(len(ocene)):
#     for b in range(len(ocene[i])):
#         if ocene[i][b].isdigit():
#             broj = ocene[i].index(ocene[i][b])
#             ocene2.append(ocene[i][broj:].split())
#             break
#
# brojac = 0
#
# for i in range(len(ocene2)):
#     if int(ocene2[i][0]) >= 60 and int(ocene2[i][1]) >= 60 and int(ocene2[i][2]) >= 60:
#         brojac +=1
#
# print(ocene2) # radi provere ispravnosti brojaca
# print('Broj studenata koji su polozili sva tri kolokvijuma je {}.'.format(brojac))


###################################################################################################################

#3. Zadatak

# from string import punctuation
#
# log = [i.strip() for i in open('log.txt')]
#
# novi_log = []
#
# for p in punctuation:
#     for i in range(len(log)):
#         log[i] = log[i].replace(p,'')
#
# for i in range(len(log)):
#     novi_log.append(log[i].split())
#
# for i in range(len(novi_log)):
#     novi_log[i][2] = int(novi_log[i][2][:2]) * 60 + int(novi_log[i][2][2:])
#     novi_log[i][3] = int(novi_log[i][3][:2]) * 60 + int(novi_log[i][3][2:])
#     if novi_log[i][3] - novi_log[i][2] >= 60:
#         print('Korisnik {} {} je bio ulogovan {} minuta.'.format(novi_log[i][0], novi_log[i][1],novi_log[i][3] - novi_log[i][2]))


###################################################################################################################

#4. Zadatak

# podaci = [i.strip() for i in open('studenti.txt')]
# nov_fajl = open('studenti1.txt', 'w')
#
# b = []
#
# for i in podaci:
#     b.append(i.split())
#
# for i in range(len(b)):
#     b[i][0] = b[i][0].capitalize()
#     b[i][1] = b[i][1].capitalize()
#     b[i][3] = '011-' + b[i][3]
#
# for i in range(len(b)):
#     nov_fajl.write('{} {}\t\t{} {}\n'.format(b[i][0], b[i][1], b[i][2], b[i][3]))
#
# nov_fajl.close()


###################################################################################################################

#5. Zadatak

# im = [i.strip() for i in open('imena.txt')]
#
# all = []
#
#
# for i in im:
#     all.append(i.split())
#
# test = input('Unesite inicijale da izvrsite proveru:')
# test = test.upper()
#
# print('Pronasli smo sledeca imena sa zadatim inicijalima:')
# for i in range(len(all)):
#     if all[i][0][0] == test[0] and all[i][1][0] == test[1]:
#         print(all[i][0], all[i][1])   #ovde ne koristim break niti stringove zato sto kada koristim ne stampa mi sva imena ( ako neka imena imaju recimo iste inicijale)

###################################################################################################################

#6.Zadatak

reci = [r.strip() for r in open('reci.txt')]        ### ova varijabla se koristi na dalje za svaki zadatak koji ukljucuje listu reci

# #Sve reci koje se zavrsavaju na ime
# for i in range(len(reci)):
#     if reci[i][-3:] == 'ime':
#         print(reci[i])
#
# #Sve reci cije je drugo, trece i cetvrto slovo a v e
# for i in range(len(reci)):
#     if len(reci[i]) > 3:
#         if reci[i][1] == 'a' and reci[i][2] == 'v' and reci[i][3] == 'e':
#             print(reci[i])
#
# #Koliko reci sadrzi bar jedno od sledecih slova r, s, t, l, n, e
# provera = 'rstlne'
# count = set()
# for i in provera:
#     for b in range(len(reci)):
#         if i in reci[b]:
#             count.add(reci[b])
# print(len(count))   # ovde koristim set zato sto u setu ne mogu biti dva ista podatka, nadam se da je to ispranvo
#
# #Procenat reci koje sadrze bar jedno od slova r, s, t, l, n, e
#
# pofset = len(count)/len(reci) * 100
# print('Procenat iznosi {:.2f}'.format(pofset))

# Sve reci koje ne sadrze samoglasnike

# for i in range(len(reci)):
#     if 'a' in reci[i]:
#         pass
#     elif 'b' in reci[i]:
#         pass
#     elif 'e' in reci[i]:
#         pass
#     elif 'i' in reci[i]:
#         pass
#     elif 'o' in reci[i]:
#         pass
#     elif 'u' in reci[i]:
#         pass
#     else:
#         print(reci[i])

# Sve reci koje sadrze sve samoglasnike

# samoglasnici = 'aeiou'
#
# for i in range(len(reci)):
#         if samoglasnici[0] in reci[i] and samoglasnici[1] in reci[i] and samoglasnici[2] in reci[i] \
#                 and samoglasnici[3] in reci[i] and samoglasnici[4] in reci[i] :
#             print(reci[i])

#Da li ima vise desetoslovnih ili sedmoslovnih reci
# d = 0
# s = 0
# for i in range(len(reci)):
#     if len(reci[i]) == 7:
#         s +=1
#     if len(reci[i]) == 10:
#         d +=1
#
# if d > s:
#     print('U tekstu vise ima desetoslovnih reci, tacnije {} naspram {} sedmoslovnih.'.format(d, s))
# else:
#     print('U tekstu vise ima sedmoslovnih reci, tacnije {} naspram {} desetoslovnih.'.format(s, d))

#Najveca rec u listi

# najveca = dict()
#
# for i in range(len(reci)):
#     najveca[reci[i]] = len(reci[i])
#
# sortirano = list(najveca.items())
#
# sortirano = [(i[1], i[0]) for i in sortirano]
# sortirano.sort(reverse=True)
# print(sortirano[0][1])

#Sve palindrome

# for i in range(len(reci)):
#     if reci[i][::-1] == reci[i]:
#         print(reci[i])

#Sve reci koje sadrze dupla slova jedno do drugog

# for i in range(len(reci)):
#     for c in range(len(reci[i])):
#         if reci[i][c] == reci[i][c-1] and reci[i][-3:] != 'lly':
#             print(reci[i])

#Sve reci koje sadrze Q iza kog ne sledi u

# for i in range(len(reci)):
#     for c in range(len(reci[i])):
#         if 'q' != reci[i][-1] and 'q' == reci[i][c] and reci[i][c+1] != 'u':
#             print(reci[i])
#         if 'q' == reci[i][-1]:
#             print(reci[i])

#Sve reci koje sadrze zu bilo gde u reci

# for i in reci:
#     if 'zu' in i:
#         print(i)

#Sve reci koje sadrze ab vise puta

# for i in reci:
#     if i.count('ab') > 1:
#         print(i)

#Sve reci cetiri uzastopna samoglasnika

# samoglasnici = 'aeiou'
#
# br = 0
#
# for rec in reci:
#     for slovo in samoglasnici:
#         if slovo in rec:
#             i = rec.index(slovo)
#             if len(rec) - i > 4:
#                 if rec[i+1] in samoglasnici and rec[i+2] in samoglasnici and rec[i+3] in samoglasnici:
#                     print(rec)

#sve reci koje sadrze i slovo z i slovo w

# for rec in reci:
#     if 'z' in rec and 'w' in rec:
#         print(rec)
#
#Sve reci kod kojih je prvo slovo a trece slovo e i peto slovo i

# for i in range(len(reci)):
#     if len(reci[i]) >4:
#         if reci[i][0] == 'a' and reci[i][2] == 'e' and reci[i][4] == 'i':
#             print(reci[i])

#Sve reci sa dva slova

# for i in reci:
#     if len(i) == 2:
#         print(i)

#Sve cetvoroslovne reci koje pocinju i zavrsavaju se istim slovom

# for rec in reci:
#     if len(rec) == 4 and rec[0] == rec[3]:
#         print(rec)

#Sve reci koje sadrze najmanje devet samoglasnika

# devet = []
# samoglasnici = 'aeiou'
#
# for rec in reci:
#     bez = True
#     for slovo in rec:
#         if slovo in samoglasnici:
#             bez = False
#     if bez == True:
#         devet.append(rec)
#
# #ovako sam uspeo da nadjem reci koje nemaju samoglasnike ali nisam uspeo da nadjem sa 9 slova
#
# for rec in devet:
#     if len(rec) >= 9:
#         print(rec)

#Sve reci koje sadrze slova a,b,c,d,e,i,f u bilo kom redosledu
#
# l = ['a', 'b', 'c', 'd', 'e', 'i', 'f']
#
# for rec in reci:
#     ima = True
#     for slovo in l:
#         if slovo not in rec:
#             ima = False
#     if ima ==True:
#         print(rec)

#Sve reci gde su cetiri prva i cetiri poslednja slova ista

# for rec in reci:
#     if len(rec) >= 8:
#         if rec[:4] == rec [-4:]:
#             print(rec)

#Sve reci u obliku abcd*dcba gde je * proizvoljno dugacak niz slova

# for rec in reci:
#     a = rec[:4]
#     b = a[-1:]
#     if a == b:
#         print(rec)

#Rec koja sadrzi najvise slova i

# recnik = dict()
#
# for rec in reci:
#     if 'i' in rec:
#         recnik[rec] = rec.count('i')
#
# lista = list(recnik.items())
# lista = [(i[1], i[0]) for i in lista]
# lista.sort(reverse=True)
# print(lista[0])


###################################################################################################################

#7. Zadatak

# korisnik = input('Unesite rec:').lower()
#
# for i in reci:
#     if korisnik == i:
#         print('Takva rec postoji u listi reci!')
#     else:
#         print('Nazalost, vasa rec ne postoji u listi reci')

###################################################################################################################

# 8. Zadatak

# unazad = []
# for rec in reci:
#     unazad.append(rec[::-1])
# unazad.sort()
# print(unazad[-1])

###################################################################################################################

#9.Zadatak

# provera = input('Unesite neki tekst\n')
#
# sc = provera.split()
# br = 0
#
# for i in sc:
#     if i in reci:
#         print('Rec se nalazi u listi reci'.format(i))
#
# print('Mozda ste mislili na sledece reci:')
# for rec in sc:
#     for word in reci:
#         for slovo in rec:
#             if slovo in word:
#                 br +=1
#             else:
#                 br = 0
#         if br == len(rec) == len(word):
#             print(word)

###################################################################################################################

#10. Zadatak

# pomoc = input('Unesite rec tako sto cete umesto slova koja ne znate ubaciti znak zvezdice *\n').lower
#
# znana = pomoc.split('*')
#
# for rec in reci:
#     ima = True
#     for z in znana:
#         if z not in rec:
#             ima = False
#     if ima == True and len(rec) == len(pomoc):
#         for m in pomoc:
#             if m != '*':
#                 if pomoc.index(m) == rec.index(m):
#                     print(rec)
#                     break

###################################################################################################################

#11. Zadatak

# unos = []
# while 1:
#     m = input('Unesite slovo, da prestanete unesite stop\n').lower()
#     if m == 'stop':
#          break
#     else:
#         unos.append(m)
#
# for i in reci:
#     ima = True
#     for z in unos:
#         if z not in i:
#             ima = False
#     if len(unos) == len(i) and ima == True:
#         print('Reci koje se sastoje od zadatih slova su:\n',(i))

###################################################################################################################

#12. Zadatak

# slova = set()
#
# for i in reci:
#     for b in i:
#         slova.add(b)
#
# alfabet =[]
#
# for c in slova:
#     alfabet.append(c)
#
# alfabet.sort()
# del alfabet[0]
# print(alfabet)
#
# recnik = dict()
#
# for c in alfabet:
#     recnik[c] = 0
#
# for i in alfabet:
#     for b in reci:
#         recnik[i] = recnik[i] + b.count(i)
#
# for key in recnik:
#     recnik[key] = '{:.2f}%'.format(recnik[key] / len(reci) * 100)
#
# print(recnik)

###################################################################################################################

#13. Zadatak

# slova = set()
#
# broj_slova = 0
#
# for rec in reci:
#     for slovo in rec:
#         broj_slova +=1
#
# for i in reci:
#     for b in i:
#         slova.add(b)
#
# alfabet =[]
#
# for c in slova:
#     alfabet.append(c)
#
# alfabet.sort()
# del alfabet[0]
# print(alfabet)
#
# recnik = dict()
#
# for c in alfabet:
#     recnik[c] = 0
#
# for i in alfabet:
#     for b in reci:
#         recnik[i] = recnik[i] + b.count(i)
#
# for key in recnik:
#     recnik[key] = '{:.2f}%'.format(recnik[key] / broj_slova * 100)
# print(recnik)

###################################################################################################################

#14. Zadatak

# unos = input('Unesite rec:\n')
#
# m = set()
# for i in unos:
#     m.add(i)
#
# for rec in reci:
#     ima = True
#     for slovo in rec:
#         if slovo not in m:
#             ima = False
#     for char in unos:
#         if unos.count(char) < rec.count(char):
#             ima = False
#     for s in m:
#         if s not in rec:
#             ima = False
#     if len(rec) < len(unos) and ima == True:
#         print('Manje reci koje se mogu sastaviti od slova zadate reci:\n', rec)

###################################################################################################################

#15.Zadatak

# adrese = [i.strip() for i in open('mail.txt')]
# for i in adrese:
#     print(i)
# s= ''
#
# for i in adrese:
#     if i[-8:] == '@stud.rs':   # za prvi deo zadatka izbaciti ovaj kod
#         s += i + ';'
# print(s)

###################################################################################################################

#16.Zadatak

# t = [i.strip() for i in open('temperature.txt')]
#
# m = dict()
#
# for i in range(1, len(t) - 1):
#     m[t[i][:5]] = int(t[i][-1]) - int(t[i-1][-1])
#
# s = [(i[1], i[0]) for i in m.items()]
# s.sort()
#
# prvi = abs(int(s[0][0]))
# poslednji = abs(int(s[-1][0]))
#
# if prvi > poslednji:
#     print('Najveci skok u temperaturi je bio {} kada je oscilacija u odnosu na predjasnji dan bila -{} stepeni.'.format(s[0][1], s[0][0]))
# else:
#     print('Najveci skok u temperaturi je bio {} kada je oscilacija u odnosu na predjasnji dan bila +{} stepeni.'.format(s[-1][1], s[-1][0]))

###################################################################################################################

#17.Zadatak

# print('Dobrodosli u igru "Smesna Prica". Pomozite mi sa odabirom nekih reci i zajedno cemo zavrsiti pricu!')
#
# prica = open('prica.txt').read()
#
# zamene = 'broj', 'zivotinja', 'proizvod', 'jelo'
#
# unos1 = input('Unesite dvocifren broj:\n')
# unos2 = input('Unesite neku zivotinju zenskog roda:\n')
# unos3 = input('Unesite ime neke namirnice:\n')
# unos4 = input('Unesite ime nekog jela:\n')
#
# prica = prica.replace(zamene[0],  unos1)
# prica = prica.replace(zamene[1],  unos2)
# prica = prica.replace(zamene[2],  unos3)
# prica = prica.replace(zamene[3], unos4)
#
# print(prica)

###################################################################################################################

#18.Zadatak

# from random import randint
#
# akr = input('Unesite akronim').lower()
# l = []
#
# while 1:
#     r = randint(0, len(reci) - 1)
#     if akr[0] == reci[r][0]:
#         l.append(reci[r])
#         break
#
# while 1:
#     r = randint(0, len(reci) - 1)
#     if akr[1] == reci[r][0]:
#         l.append(reci[r])
#         break
#
# while 1:
#     r = randint(0, len(reci) - 1)
#     if akr[2] == reci[r][0]:
#         l.append(reci[r])
#         break
# print(l)

###################################################################################################################

#19.Zadatak

# from random import randint
# print('Dobrodosli u igru Jotto!')
# print('\nProgram je odabrao jednu nasumicnu rec od pet slova, na vama je da tu rec pogodite!')
# print('\nNakon svakog pokusaja videcete recnik prethodnih pokusaja sa brojem poklapanja za tu rec!\n')
#
# tajna_rec = ''
#
# while tajna_rec == '':
#     for i in range(len(reci)):
#         r = randint(0, len(reci) - 1)
#         if len(reci[r]) == 5:
#             pr = set()
#             for c in reci[r]:
#                 pr.add(c)
#             if len(pr) == 5:
#                 tajna_rec = reci[r]
#
# count = 0
# pokusaji = dict()
#
# while count < 6:
#     count += 1
#     if count >= 2:
#         print(pokusaji)
#     guess = input('Probajte da pogodite rec:\n').lower()
#     pogodak = []
#     if guess == tajna_rec:
#         print('Bravo, pogodili ste tajnu rec!Uspeli ste iz {} pokusaja'.format(count))
#         break
#     for f in guess:
#         if f in tajna_rec:
#             pogodak.append(f)
#     print('U reci {} nalaze se {} karaktera koja su i u nasoj tajnoj reci.'.format(guess, len(pogodak)))
#     pokusaji[guess] = len(pogodak)
#
#     if count == 5:
#         print('Nazalost, nemate vise pokusaja, vise srece drugi put, tajna rec je bila {}'.format(tajna_rec))
#         break

