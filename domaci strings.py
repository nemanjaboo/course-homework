#1. Zadatak

# string = input('Unesite neki tekst: ')
#
# # Ukupan broj znakova u stringu
#
# print('Ukupan broj znakova u vasem tekstu je:', len(string))
# #################################################################
# # String ponovljen 10 puta
#
# print(string * 10)
# ##################################################################
# # Prvi znak u stringu
#
# print(string[0])
# ###################################################################
# #Prva tri znaka stringa
# print(string[0:3])
# ##################################################################
# #Zadnja tri znaka iz stringa
# print(string[-3:])
# #################################################################
# #Ceo string unazad
# print(string[::-1])
# #Sedmi znak u stringu ako string ima dovoljnu duzinu
# if len(string) >=7:
#     print(string[7])
# else:
#     print('Nedovoljan broj karaktera, potrebno sedam karaktera')
# ##################################################################
# #String kod koga su odstranjeni prvi i poslednji znak
# print(string[1:-1])
# ##################################################################
# #String sa svim velikim slovima
# print(string.upper())
# ##################################################################
# #String u kome je svako a zamenjeno sa e
# print(string.replace('a', 'e'))
# ##################################################################
# #String u kome je svako slovo zamenjeno blanko znakom
# for i in range(len(string)):
#     string.replace(string[i], '')
# print(string) #- TREBA ISTRAZITI
# #################################################################


# 2.Zadatak

# string = input('Unesite tekst: ')
# print('Broj reci u vasem tekstu je:', string.count(' ') + 1)

########################################################################################################################

# 3.Zadatak

# formula = input('Molimo unesite formulu')
#
# if formula.count('(') == formula.count(')'):
#     print('Formula je ispravna')
# else:
#     print('Formula je neispravna, molimo vas proverite zagrade')

########################################################################################################################

# 4.Zadatak

# string = input('Molimo unesite tekst')
# provera = 'aeiou'
#
# for i in provera:
#     if i in string:
#         print('Rec sadrzi samoglasnike')
#         break
#     else:
#         print('Rec ne sadrzi samoglasnike')
#         break

########################################################################################################################

# 5.Zadatak

# string = input('Molimo unesite tekst')
# novi_string = string.replace(string[1], '*')
# novi_string += '!!!'
# print(novi_string)

########################################################################################################################

# 6.Zadatak

# s = input('Molimo unesite tekst')
# s = s.lower()
# s = s.replace('.', '')
# s = s.replace(',', '')
# print(s)

########################################################################################################################

# 7.Zadatak

# string = input('Molimo unesite tekst')
#
# if string.lower() == string[::-1].lower():
#     print('Rec koju ste uneli je palindrom')
# else:
#     print('Rec koju ste uneli nije palindrom')

########################################################################################################################

# 8. Zadatak

# broj_adresa = eval(input('Koliko e-mail adresa zelite da unesete: ?'))

# adrese = ''
# for i in range(broj_adresa):
#     unos = input('Unesite e-mail adresu: ')
#     adrese += unos


# print(adrese)
#
# profesorske = adrese.count('@prof.college.edu')
# studentske = adrese.count('@student.college.edu')
#
# if '@prof.college.edu' or '@student.college.edu' in adrese:
#     print('Uneli ste ', profesorske, 'profesorske adrese i', studentske, 'studentske adresa')
# else:
#     print('Niste uneli studentske ili profesorske adrese')

########################################################################################################################

# 9.Zadatak
# 1
#  2
#   3
#    4

# unos = eval(input('Unesite neki broj:'))
#
# for i in range(unos):
#     print(' ' * i, i+1)

########################################################################################################################

# 10 Zadatak

#
# unos = input('Unesite neki tekst:')
#
# for i in range(len(unos)):
#     print(unos[i]*2)

########################################################################################################################

# 11.Zadatak

# unos = input('Unesite neki tekst:').lower()
# lokacija = unos.index('a')
# print(unos[:lokacija+1])
# print(unos[lokacija+1:])

# 12. Zadatak
#
# unos = input('Unesite neki tekst:')
#
# mala = unos[1::2]
# velika = unos[1::2].upper()
#
# for i in range(len(velika)):
#     unos = unos.replace(mala[i],velika[i])
#
# print(unos)

########################################################################################################################

# 13. Zadatak

# print('Unesite dve reci sa identicnim brojem karaktera.')
# prva = input('Vasa prva rec: ')
# druga = input('Vasa druga rec: ')
#
# while len(prva) != len(druga):
#     print('Ove dve reci nisu iste duzine.')
#     break
# else:
#     for i in range(len(prva)):
#         print(prva[i] + druga[i], end='')

########################################################################################################################

# 14. Zadatak

# ime = input('Molimo vas unesite vase ime: ')
# prazno = ime.index(' ')
# ime = ime.replace(ime[0], ime[0].upper())
# ime = ime.replace(ime[prazno+1], ime[prazno+1].upper())

# print(ime)

### Laksi nacin za 14 zadatak koji nismo radili na casu ali sam nasao u dokumentaciji

# ime = input('Molimo vas unesite vase ime: ')
# print(ime.title())

########################################################################################################################

# 15. Zadatak

# print('Dobrodosli u igru "Smesna Prica". Pomozite mi sa odabirom nekih reci i zajedno cemo zavrsiti pricu!')
#
# prica = 'Veverica je vozila broj na sat kada ju je pozvala zivotinja.Rekla joj je da kupi proizvod, i da pozuri.Za veceru je spremila jelo.'
#
# zamene = 'broj', 'zivotinja', 'proizvod', 'jelo'
#
# unos1 = input('Unesite dvocifren broj:')
# unos2 = input('Unesite neku zivotinju zenskog roda:')
# unos3 = input('Unesite ime neke namirnice')
# unos4 = input('Unesite ime nekog jela:')
#
#
# prica = prica.replace(zamene[0],  unos1)
# prica = prica.replace(zamene[1],  unos2)
# prica = prica.replace(zamene[2],  unos3)
# prica = prica.replace(zamene[3], unos4)
#
# print(prica)

########################################################################################################################

# 16. Zadatak

# tekst = '''Dear OSOBA,
#
# I am pleased to offer you our new Platinum Plus Rewards
# card at a special introductory APR of 47.99%.  IME,
# an offer like this does not come along every day, so I
# urge you to call now toll-free at 1-800-314-1592. We
# cannot offer such a low rate for long, IME, so call
# right away.
# '''
#
# korisnik = input('Molimo vas unesite vase ime i prezime:')
# prazno_index = korisnik.index(' ')
# ime = korisnik[0:prazno_index]
#
# tekst = tekst.replace('IME', ime)
# tekst = tekst.replace('OSOBA', korisnik)
#
# print(tekst)

########################################################################################################################

# 17.Zadatak

# alfabet = 'abcdefghijklmnopqrstuvwxyz'
# print(alfabet)
# for i in range(20):
#     print(alfabet[i+1]+alfabet)

########################################################################################################################

# 18. a)

# tekst = input('Unesite bilo kakav tekst:')
# tekst_2 = input('Unesite bilo kakav znak: ')
#
# proba = tekst.count(tekst_2)
#
# if proba > 0:
#     print('Vas znak se pojavljuje i u vasem tekstu.')
# else:
#     print('Vas znak se ne pojavljuje u vasem tekstu.')

# b)

# tekst = input('Unesite bilo kakav tekst:')
# tekst_2 = input('Unesite bilo kakav znak: ')
#
# brojac = 0
#
# for i in tekst:
#     if i == tekst_2:
#         brojac +=1
#
# print(brojac)

# c)

# tekst = input('Unesite bilo kakav tekst:')
# tekst_2 = input('Unesite bilo kakav znak: ')
#
# brojac = 0
#
#
# for i in tekst:
#     if tekst_2 not in tekst:
#         print('Vaseg znaka nema u vasem tekstu.')
#         break
#     elif i != tekst_2:
#         brojac +=1
#     elif i == tekst_2:
#         print('Vas znak se prvi put u vasem tekstu pojavljuje na indeksu broj:', brojac)
#         break

########################################################################################################################

# 19.Zadatak

# broj = input('Unesite veliki ceo broj: ')
# print(broj[2::3])
#
# novi_string = ''
#
# novi_string = broj[2::3], sep=','
# print(novi_string)

########################################################################################################################

# 20. Zadatak

# from random import randint
#
# tekst = input('Unesite neku rec:')
# anagram = ''
# broj = len(tekst)
#
# r = randint(0, broj-1)
#
# anagram = tekst[r:] + tekst[:r]
#
# print(anagram)


########################################################################################################################

#21. Zadatak

#ovde imam problem sa desifrovanjem, tj. mislim da sam na pravom putu, ali ne mogu da shvatim kako da namestim da mi
# for petlja dok prelazi poslednji put preko prvi_deo[i] + drugi_deo[i] ignorise to sto ta dva stringa nisu iste duzine

# tekst = input('Unesite neku rec:')
# duzina = len(tekst)
# sifrovana = ''
#
# prvi_deo = tekst[::2]
# drugi_deo = tekst[1::2]
# sifrovana = prvi_deo + drugi_deo
#
#
# print('Vasa poruka je sifrovana, da je vidite iskucajte "sifra"')
# proba = input()
#
# if proba.lower() == 'sifra':
#     print(sifrovana)
#
# for i in range(len(tekst)-1):
#     print(prvi_deo[i] + drugi_deo[i], end='')

########################################################################################################################

#22. Zadatak

#a)


# tekst = input('Unesite neku rec:')
# prvi_deo =tekst[::3]
# drugi_deo =tekst[1::3]
# treci_deo =tekst[2::3]
#
# print(prvi_deo)
# print(drugi_deo)
# print(treci_deo)

#b)

# tekst = input('Unesite neku rec:')
# broj = eval(input('Na koliko delova zelite da podelimo poruku(unesite ceo broj):'))
# podeljeno = ''
#
# for i in range(broj):
#     podeljeno += tekst[i::broj] + ' '
#
#
#
# print(podeljeno)

#c)





########################################################################################################################

# #23. Zadatak

#Ovo nisam znao da resim sam pa sam ga resio preko guglanja "How to convert string into a number". Verovatno to nije
# ono sto si imao na umu, ali drugaciji nacin nisam uspeo da smislim.

# izvod = input('Unesite izvod ciji rezultat zelite da vidite. ( Primer: x3 ili x5:')
#
# novi_izvod = ''
# broj = int(izvod[-1])
# broj = str(broj-1)
#
# novi_izvod = izvod[-1] + 'x' + str(broj)
#
# print(novi_izvod)

########################################################################################################################

# 24. Zadatak

#Nisam uspeo da uradim


########################################################################################################################

#25. Zadatak

# tekst = input('Unesite zeljeni naziv varijable: ')
#
# if tekst.isalnum() and not tekst[0].isdigit() and ' ' not in tekst or '_' in tekst:
#     print('Ispravan naziv varijable')
# else:
#     print('Neispravan naziv varijable.')
