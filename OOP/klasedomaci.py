from random import *

# 1.Zadatak
class Investicija:
    def __init__(self, glavnica, kamata):
        self.glavnica = glavnica
        self.kamata = kamata

    def vrednost_posle(self, n):
        self.vrednost = self.glavnica * (1 + self.kamata) ** n
        return self.vrednost

    def __str__(self):
        return 'Glavnica - {:.2f}, Kamatna stopa - {:.2f}%'.format(self.glavnica, self.kamata)


# 2.Zadatak

class Proizvod:
    def __init__(self, naziv, kolicina, cena):
        self.naziv = naziv
        self.kolicina = kolicina
        self.cena = cena

    def __str__(self):
        return '{} {} {}'.format(self.naziv, self.kolicina, self.cena)

    def daj_cenu(self, n):
        if n < 10:
            return self.cena * n
        elif n > 10 <= 100:
            return self.cena * n / 10
        else:
            return self.cena * n / 5

    def napravi_prodaju(self, brojproizvoda):
        return self.kolicina - brojproizvoda


# 3. Zadatak

class Password_manager:
    def __init__(self, lista):
        self.lista = lista

    def get_password(self):
        return self.lista[-1]

    def set_password(self, unos):
        if unos not in self.lista:
            self.lista.append(unos)
        else:
            print('Vec ste koristili taj password')

    def is_correct(self, unos):
        if unos == self.lista[-1]:
            return True
        else:
            return False


# 4. Zadatak

class Time:
    def __init__(self, vreme):
        self.vreme = vreme
        self.minut = 60
        self.sat = 3600

    def convert_to_minutes(self):
        return '{}:{}'.format(self.vreme // 60, self.vreme % self.minut)

    def convert_to_hours(self):
        return '{}:{}:{}'.format(self.vreme // self.sat, int(self.vreme % self.sat / 60), self.vreme % self.minut)


# 5. Zadatak

class Wordplay:
    def __init__(self, reci):
        self.reci = reci

    def words_with_lenght(self, n):
        lenght = []
        for rec in self.reci:
            if len(rec) == n:
                lenght.append(rec)

        return lenght

    def starts_with(self, s):
        sw = []
        for rec in self.reci:
            if rec[0] == s:
                sw.append(rec)
        return sw

    def ends_with(self, s):
        ew = []
        for rec in self.reci:
            if rec[-1] == s:
                ew.append(rec)
        return ew

    def palindromes(self):
        p = []
        for rec in self.reci:
            if rec[::-1] == rec:
                p.append(rec)
        return p

    def only(self, L):
        o = []
        for rec in self.reci:
            if len(rec) == len(L):
                broj = 0
                for slovo in L:
                    if slovo in rec:
                        broj += 1
                    else:
                        broj = 0
                    if broj == len(L):
                        o.append(rec)
        return o

    def avoids(self, L):
        a = []
        for rec in self.reci:
            broj = 0
            for slovo in L:
                if slovo not in rec:
                    broj += 1
                    if broj == len(L):
                        a.append(rec)
        return a


# 6. Zadatak

class Converter:
    def __init__(self, d, j):
        self.d = d
        self.j = j
        self.inc = 'inc'
        self.fit = 'feet'
        self.jard = 'jard'
        self.milja = 'milja'
        self.km = 'km'
        self.m = 'm'
        self.cm = 'cm'
        self.mm = 'mm'

    def c_inc(self):
        if self.j == self.inc:
            return self.d
        if self.j == self.fit:
            return self.d * 12
        if self.j == self.jard:
            return self.d / 36
        if self.j == self.milja:
            return self.d / 63360
        if self.j == self.km:
            return self.d / 39370
        if self.j == self.m:
            return self.d / 39.37
        if self.j == self.cm:
            return self.d * 2.54
        if self.j == self.mm:
            return self.d * 25.4

    def c_fit(self):
        if self.j == self.fit:
            return self.d
        if self.j == self.inc:
            return self.d / 12
        if self.j == self.jard:
            return self.d * 36
        if self.j == self.milja:
            return self.d * 5280
        if self.j == self.km:
            return self.d * 3281
        if self.j == self.m:
            return self.d * 3281
        if self.j == self.cm:
            return self.d / 30.48
        if self.j == self.mm:
            return self.d / 305

    def c_jard(self):
        if self.j == self.jard:
            return self.d
        if self.j == self.inc:
            return self.d / 36
        if self.j == self.milja:
            return self.d * 1760
        if self.j == self.km:
            return self.d * 1094
        if self.j == self.m:
            return self.d * 1094
        if self.j == self.cm:
            return self.d / 91.44
        if self.j == self.mm:
            return self.d / 914

    def c_milja(self):
        if self.j == self.milja:
            return self.d
        if self.j == self.inc:
            return self.d / 63360
        if self.j == self.fit:
            return self.d / 5280
        if self.j == self.jard:
            return self.d / 1760
        if self.j == self.km:
            return self.d / 1.609
        if self.j == self.m:
            return self.d / 1609
        if self.j == self.cm:
            return self.d / 160934
        if self.j == self.mm:
            return self.d / 1.609e+6

    def c_km(self):
        if self.j == self.km:
            return self.d
        if self.j == self.inc:
            return self.d / 39370
        if self.j == self.fit:
            return self.d / 3281
        if self.j == self.jard:
            return self.d / 1094
        if self.j == self.milja:
            return self.d * 1609
        if self.j == self.m:
            return self.d / 1000
        if self.j == self.cm:
            return self.d / 100000
        if self.j == self.mm:
            return self.d / 1e+6

    def c_m(self):
        if self.j == self.m:
            return self.d
        if self.j == self.inc:
            return self.d / 39.37
        if self.j == self.fit:
            return self.d / 3281
        if self.j == self.jard:
            return self.d / 1094
        if self.j == self.milja:
            return self.d / 1609
        if self.j == self.km:
            return self.d * 1000
        if self.j == self.cm:
            return self.d / 100
        if self.j == self.mm:
            return self.d / 1000

    def c_cm(self):
        if self.j == self.cm:
            return self.d
        if self.j == self.inc:
            return self.d * 2.54
        if self.j == self.fit:
            return self.d * 30.48
        if self.j == self.jard:
            return self.d * 91.44
        if self.j == self.milja:
            return self.d * 160934
        if self.j == self.km:
            return self.d * 100000
        if self.j == self.m:
            return self.d * 100
        if self.j == self.mm:
            return self.d / 10

    def c_mm(self):
        if self.j == self.mm:
            return self.d
        if self.j == self.inc:
            return self.d * 25.4
        if self.j == self.fit:
            return self.d * 305
        if self.j == self.jard:
            return self.d * 914
        if self.j == self.milja:
            return self.d * 1.609e+6
        if self.j == self.km:
            return self.d * 1e+6
        if self.j == self.m:
            return self.d * 1000
        if self.j == self.cm:
            return self.d * 10

# 7.Zadatak

class Standard_deck():
    def __init__(self):
        self.cards = []
        for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for v in range(2, 15):
                self.cards.append([v, s])
        self.prvi = self.cards[:len(self.cards) // 2]
        self.drugi = self.cards[len(self.cards) // 2:]

    def deljenje(self):
        shuffle(self.prvi)
        shuffle(self.drugi)
        return 'Spil je podeljen'

    def okreni_kartu(self):
        print(self.prvi[0])
        print(self.drugi[0])
        if self.prvi[0][0] > self.drugi[0][0]:
            self.prvi.append(self.drugi.pop(0))
            self.prvi.append(self.prvi.pop(0))
        elif self.prvi[0][0] < self.drugi[0][0]:
            self.drugi.append(self.prvi.pop(0))
            self.drugi.append(self.drugi.pop(0))
        elif self.prvi[0][0] == self.drugi[0][0]:
            self.prvi.pop(0)
            self.drugi.pop(0)
        print(self.prvi)
        print(self.drugi)

    def igraj_sam(self):
        while len(self.prvi) != 0 or len(self.drugi) != 0:
            print(self.prvi[0])
            print(self.drugi[0])
            if self.prvi[0][0] > self.drugi[0][0]:
                self.prvi.append(self.drugi.pop(0))
                self.prvi.append(self.prvi.pop(0))
                print('Ovu rundu dobija PRVI igrac!')
            elif self.prvi[0][0] < self.drugi[0][0]:
                self.drugi.append(self.prvi.pop(0))
                self.drugi.append(self.drugi.pop(0))
                print('Ovu rundu dobija DRUGI igrac!')
            elif self.prvi[0][0] == self.drugi[0][0]:
                self.prvi.pop(0)
                self.drugi.pop(0)
                print('U ovoj rundi rezultat je neresen!')

            if len(self.prvi) == 0:
                return 'Igra je gotova, pobedio je igrac broj DVA!', self.prvi
            elif len(self.drugi) == 0:
                return 'Igra je gotova, pobedio je igrac broj JEDAN!', self.drugi



# 8.Zadatak

class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards

    def nextCard(self):
        return self.cards.pop(0)

    def hasCard(self):
        return len(self.cards)>0

    def size(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)

class Herc_pik(Card_group):
    def __init__(self, cards=[]):
        super().__init__(cards)
        for s in ['Heart', 'Spade']:
            for b in range(2, 11):
                self.cards.append([b, s])


    def next2(self):
        return self.cards[0], self.cards[1]

#9. Zadatak

class Rock_paper_scissors:
    def __init__(self, ime, runde=3):
        self.runde = runde
        self.ime = ime
        self.komp = 'DEEP BLUE RPS'
        self.tekuca = 0
        self.covekwins = 0
        self.kompwins = 0
        self.potezcovek = ''
        self.potezkomp = ''
        self.potezi = ['papir', 'kamen', 'makaze']

    def pobednik_runde(self):
        if self.potezcovek == self.potezi[0]:
            if self.potezkomp == self.potezcovek:
                print('Nereseno je!')
            elif self.potezkomp == self.potezi[1]:
                self.covekwins += 1
                print('Bravo {}, pobedio si ovu rundu!'.format(self.ime))
            elif self.potezkomp == self.potezi[2]:
                self.kompwins += 1
                print('Izgubio si, sto je naravno apsolutno ocekivano.')
        elif self.potezcovek == self.potezi[1]:
            if self.potezkomp == self.potezcovek:
                print('Nereseno je!')
            elif self.potezkomp == self.potezi[0]:
                self.kompwins += 1
                print('Izgubio si, sto je naravno apsolutno ocekivano.')
            elif self.potezkomp == self.potezi[2]:
                self.covekwins += 1
                print('Bravo {}, pobedio si ovu rundu!'.format(self.ime))
        elif self.potezcovek == self.potezi[2]:
            if self.potezkomp == self.potezcovek:
                print('Nereseno je!')
            elif self.potezkomp == self.potezi[0]:
                print('Bravo {}, pobedio si ovu rundu!'.format(self.ime))
            elif self.potezkomp == self.potezi[1]:
                self.kompwins += 1
                print('Izgubio si, sto je naravno apsolutno ocekivano.')

    def deepblue(self):
        self.potezkomp = self.potezi[randint(0, 2)]
        print('Ja sam spreman!Da prekines igru unesi "izlaz"')


    def igra(self):
        for i in range(self.runde):
            self.kasparov()
            self.deepblue()
            self.potezcovek = input('Unesite vas potez, papir, makaze ili kamen. Uostalom nije ni bitno, ja sigurno pobedjujem...\n')
            self.potezcovek = self.potezcovek.lower()
            if self.potezcovek == 'izlaz':
                print('Gde ode?')
                return
            self.tekuca += 1
            self.pobednik_runde()
            print('\nDEEP BLUE RPS je odigrao {}, dok je '.format(self.potezkomp) + '{} je odigrao {}'.format(self.ime, self.potezcovek))
            self.trenutnirezultat()
            if self.runde == self.tekuca:
                self.pobednik()


    def trenutnirezultat(self):
        print('\n{} trenutno ima {:d} poena'.format(self.ime, self.covekwins) + ', dok DEEP BLUE RPS ima {:d} poena'.format(self.kompwins) + ' Do kraja je ostalo jos {:d}\n\n\n'.format(self.runde - self.tekuca))


    def pobednik(self):
            if self.covekwins > self.kompwins:
                print('\n\nIgra je gotova, cestitam {}, ali sam poprilicno siguran da si varao...'.format(self.ime))
            elif self.kompwins > self.covekwins:
                print('\n\nJos jedna pobeda, ovo postaje dosadno...hoces partiju Saha?')
            elif self.covekwins == self.covekwins:
                print('\n\nNereseno. Blah. Bravo.')

    def kasparov(self):
        if self.ime == 'Kasparov':
            print('Ti bas ne odustajes Garry.')

#10. Zadatak

class Poker_hand(Standard_deck):
    def __init__(self):
        super().__init__()
        self.ruka = []


    def hand(self):
        shuffle(self.cards)
        for k in range(5):
            self.ruka.append(self.cards[randint(0, len(self.cards) -1)])
        print(self.ruka)

    def has_straight_flush(self):
        znak = self.ruka[0][1]
        boja = 0
        kenta = False
        suit = False
        flush = set()

        if self.ruka[-1][0] - self.ruka[-2][0] == 1:
            if self.ruka[-2][0] - self.ruka[-3][0] == 1:
                if self.ruka[-3][0] - self.ruka[-4][0] == 1:
                    if self.ruka[-4][0] - self.ruka[-5][0] == 1:
                        kenta = True


        for k in range(len(self.ruka)):
            flush.add(self.ruka[k][1])

        if len(flush) == 0:
                suit = True
        if kenta and suit == True:
            return 'Dobili ste Straight Flush!'

    def has_royal_flush(self):
        znak = self.ruka[0][1]
        royal = ['10', '11', '12', '13', '14']
        check = []
        r = False
        suit = False
        flush = set()

        for k in range(len(self.ruka)):
            check.append(self.ruka[k][0])
        check.sort()
        if check == royal:
            r = True

        for k in range(len(self.ruka)):
            flush.add(self.ruka[k][1])

        if len(flush) == 0:
                suit = True

        if r and suit == True:
            print('Dobili ste Straight Flush!')

    def has_four_of_a_kind(self):
        poker = set()
        for k in range(len(self.ruka)):
            poker.add(self.ruka[k][0])

        if len(poker) == 1:
            print('Dobili ste poker!')

    def has_full_house(self):
        fh = set()
        for k in range(len(self.ruka)):
            fh.add(self.ruka[k][0])

        if len(fh) == 0:
            print('Dobili ste poker!')

    def has_flush(self):
        flush = set()
        for k in range(len(self.ruka)):
            flush.add(self.ruka[k][1])

        if len(flush) == 0:
            print('Dobili ste boju!')

    def has_straight(self):
        znak = self.ruka[0][1]
        kenta = False
        if self.ruka[-1][0] - self.ruka[-2][0] == 1:
            if self.ruka[-2][0] - self.ruka[-3][0] == 1:
                if self.ruka[-3][0] - self.ruka[-4][0] == 1:
                    if self.ruka[-4][0] - self.ruka[-5][0] == 1:
                        kenta = True

        if kenta == True:
            print('Dobili ste kentu!')

    def has_three_of_a_kind(self):
        triling = set()
        for k in range(len(self.ruka)):
            triling.add(self.ruka[k][0])

        if len(triling) == 2:
            print('Dobili ste triling!')

    def has_two_pair(self):
        dvapara = []
        par = 0
        for b in range(len(self.ruka)):
            dvapara.append(self.ruka[b][0])
        for z in dvapara:
            if dvapara.count(z) == 2:
                par += 1
        if par == 4:
            print('Dobili ste dva para!')

    def has_pair(self):
        pair = []
        par = 0
        for b in range(len(self.ruka)):
            pair.append(self.ruka[b][0])
        for z in pair:
            if pair.count(z) == 2:
                par += 1
        if par == 2:
            print('Dobili ste par')

    def Play_poker(self):
        self.hand()
        self.has_pair()
        self.has_two_pair()
        self.has_three_of_a_kind()
        self.has_straight()
        self.has_flush()
        self.has_four_of_a_kind()
        self.has_straight_flush()
        self.has_royal_flush()

