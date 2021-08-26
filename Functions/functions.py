from random import randint


# 1. Zadatak
def pravougaonik(m, n):
    '''Na osnovu zadatih vrednosti
    stampa pravougaonik.
    :returns None
    :parameter m : visina n: duzina
    '''
    for i in range(m):
        print('*' * n)

#2.Zadatak

def dodaj_uzvicnik(lista):
    '''Dodaje uzvicnik na postojece
    elemente liste
    :returns None
    :param lista: lista
    '''
    for i in range(len(lista)):
        lista[i] = lista[i] + '!'

# 3.Zadatak

def dodaj_uzvicnik2(lista):
    '''
    Uzima elemente iz liste
    a zatim im dodaje uzvicnik i vraca
    ih kao elemente nove liste
    :param lista:  lista
    :return: nova lista
    '''
    nova = [i + '!' for i in lista]
    return nova

#4. Zadatak

def suma_cifara(broj):
    '''Sabira cifre zadatog broja
    i vraca rezultat
    :parameter broj: broj u int formatu
    returns : sum cifara zadatog broja
    '''
    broj = str(broj)
    z = 0
    for i in range(len(broj)):
        z += int(broj[i])
    return z

#5. Zadatak

def digitalni_koren(n):
    '''Racuna i vraca digitalni
    koren zadatog broja
    :parameter n: int broj
    :returns digitalni koren broja
    '''
    n = str(n)
    zbir = 0
    for i in range(len(str(n))):
        zbir += int(n[i])
    if len(str(zbir)) == 1:
        return zbir
    else:
        return digitalni_koren(zbir)


#6. Zadatak

def prva_razlika(string1, string2):
    '''Funkcija prihvata dva striga
     i vraca prvu poziciju na kojoj se razlikuju
     :parameter string1: prvi string, string2: drugi string
     :returns pozicija na kojoj se stringovi razlikuju
     '''
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return string1.index(string1[i])
        if string1 == string2:
            return -1

# 7.Zadatak

def binom(n, k):
    '''Funkcija vraca binomijalni koeficijent n C k
    :parameter n: int k: int
    :returns binomijalni koeficijent
    '''
    r = n - k
    f = list(range(r+1, n))
    f1 = list(range(1, k))
    for i in f:
        n *= i
    for c in f1:
        k *= c
    if 0 <= k <= n:
        return n/k
    else:
        return 'Neispravan uslov'


# 8.Zadatak

def vraca_broj(n):
    '''
    Funkcija vraca slucajan broj sa
    brojem cifara jednakom vrednosti zadatog broja
    :param n: int
    :return: slucajan broj
    '''
    l = [i for i in range(0, 10)]
    z = ''
    for i in range(n):
        if n == 1:
            r = randint(0, len(l) - 1)
            z += str(l[r])
        else:
            r = randint(1, len(l) - 1)
            z += str(l[r])
    return z

#9.Zadatak

def broj_faktora(broj):
    '''
    Funkcija izracunava koliko faktora ima broj
    :param broj:
    :return: broj faktora
    '''
    lista = []
    if broj % 2 == 0:
        for i in range(broj + 1):
            for b in range(broj + 1):
                if broj % 2 == 0 and i * b == broj:
                    lista.append(b)
    else:
        lista.append(broj)
        lista.append(1)
    return len(lista)


# 10.Zadatak

def faktori(broj):
    '''
    Funkcija izracunava faktore broja
    i vraca ih kao vrednosti liste
    :param broj: int
    :return: list: faktori zadatog int
    '''
    lista = []
    if broj % 2 == 0:
        for i in range(broj + 1):
            for b in range(broj + 1):
                if broj % 2 == 0 and i * b == broj:
                    lista.append(b)
    else:
        lista.append(broj)
        lista.append(1)
    return (lista)

# 11.Zadatak

def najveci(L, n):
    '''
    Funkcija uzima broj i listu, i vraca prvi broj manji od uzetog iz liste
    :param L: lista
    :param n: int
    :return: prvi broj manji od int
    '''
    z = []
    for i in range(len(L)):
        if L[i] - n < 0:
            z.append(L[i] - n)
    z.sort()
    return z[-1] + n


# 12.Zadatak

def poklapanja(s1, s2):
    '''
    Funkcija trazi broj poklapanja izmedju dva stringa
    :param s1: string
    :param s2: string
    :return: int poklapanja
    '''
    counter = 0
    if len(s1) < len(s2):
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                counter += 1
        return counter
    else:
        for i in range(len(s2)):
            if s2[i] == s1[i]:
                counter += 1
        return counter

# 13.Zadatak

def findall(tekst, slovo):
    '''
    Funkcija za dati string i dato slovo trazi svaki index tog slova u stringu
    :param tekst: string
    :param slovo: slovo
    :return: svaki indeks tog slova u stringu
    '''
    l = [i.lower() for i in tekst]
    indeksi = []
    for i in range(len(l)):
        if l[i] == slovo.lower():
            indeksi.append(i)
    if len(indeksi) >= 1:
        return indeksi
    else:
        return []

# 14.Zadatak

def promeni_velicinu(s):
    '''
    Funkcija menja velika u mala slova iz stringa i obratno
    :param s: string
    :return: promenjeni string
    '''
    mala = ''
    velika = ''

    for i in range(len(s)):
        if s[i] != s[i].lower():
            s = s.replace(s[i], s[i].lower())
        else:
            s = s.replace(s[i], s[i].upper())

    return s


# 15.Zadatak

def is_sorted(lista):
    '''
    Funkcija vraca zadatu listu kao sortiranu
    :param lista:lista
    :return:sortirana lista
    '''
    p = [i for i in lista]
    p.sort()
    if lista == p:
        return True
    else:
        return False


# 16.Zadatak

def root(x, n = 2):
    '''
    Za dati broj x funkcija izracunava x na 1/n
    :param x: int
    :param n: int
    :return: x na 1/n
    '''
    y = 1 / n
    return x ** y

# 17.Zadatak

def one_away(s1, s2):
    '''
    Meri da li su stringovi iste duzine i da li se razlikuju samo po jednom slovu
    :param s1:string
    :param s2:string
    :return:True or False
    '''
    isti = True
    counter = 0
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
                if counter != 1:
                    isti = False
    return isti

#
# 18.Zadatak

def primes(start = 2, n = 100):
    '''
    Uzima zadati broj i vraca listu prvih prostih brojeva
    :param start: minimalni pocetak liste
    :param n: int
    :return: lista
    '''
    brojevi = [i for i in range(start, 9999999)]
    p = 0
    pl = []
    for i in range(len(brojevi)):
        if brojevi[i] % 2 != 0:
            p += 1
            pl.append(brojevi[i])
        if p == n:
            return pl


# 19.Zadatak

def naziv_broja(n):
    '''
    Funkcija vraca naziv zadatog broja na engleskom jeziku
    :param n: int
    :return: string naziv broja
    '''
    n = str(n)
    jednocifreni = ['one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine']
    dva = ['ten', 'eleven', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    dvocifreni = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    vise = ['hundred', 'thousand']
    if len(n) == 1:
        return str(jednocifreni[int(n)-1])
    elif len(n) == 2 and n[0] == '1':
        return str(dva[int(n[1])-1])
    elif len(n) == 2 and n[0] != '1':
        d = dvocifreni[int(n[0])-2]
        j = jednocifreni[int(n[1])-1]
        return '{} {}'.format(d, j)
    elif len(n) == 3:
        j = jednocifreni[int(n[0])-1]
        h = vise[0]
        d = dvocifreni[int(n[1])-2]
        z = jednocifreni[int(n[2])-1]
        return '{} {} {} {}'.format(j, h, d, z)
    elif len(n) == 4:
        j = jednocifreni[int(n[0]) - 1]
        h = vise[1]
        s = jednocifreni[int(n[1]) - 1]
        h1 = vise[0]
        d = dvocifreni[int(n[2])-2]
        j1 = jednocifreni[int(n[-1]) - 1]
        return '{} {} {} {} {} {} '.format(j, h, s, h1, d, j1)

#
# 20.Zadatak

def merger(l1, l2):
    '''
    Spaja dve sortirane liste u novu sortiranu listu
    :param l1: lista
    :param l2:lista
    :return:nova lista
    '''
    l3 = l1 + l2
    l3.sort()
    print(l3)
    l4 = l1 + l2
    l5 = []
    for i in range(len(l4)):
        l5.append(min(l4))
        m = l4.index(min(l4))
        del l4[m]
    print(l5)

#
# 21.Zadatak

def binarno(lista, rec):
    '''
    binarno pretrazivanje liste za zadatu rec
    :param lista: lista
    :param rec: string
    :return: True or False
    '''
    d = False
    for i in range(len(lista)):
        R = lista.index(rec)
        sredina = len(lista) // 2
        if lista[sredina] == lista[R]:
            d = True
            return d
        elif R > sredina:
            lista = lista[sredina+1:]
        elif R < sredina:
            lista = lista[:sredina]
        else:
            return d
#
# 22.Zadatak

def oks(igra):
    '''
    Provera pobednika u igri iks oks
    :param igra: lista
    :return: True or False
    '''
    l = randint(0,2)
    p = randint(0,2)
    oks = False
    for i in range(len(igra)):
        for j in range(len(igra[i])):
            if igra[i][j] == '':
                oks = True
            else:
                oks = False
    if oks == True:
        igra[l][p] = 'O'
    print(igra[0])
    print(igra[1])
    print(igra[2])

def pobednik(igra):
    pobeda = False
    for l in range(len(igra)):
        if igra[l].count('o') == 3 or igra[l].count('x') == 3:
            pobeda = True
            return pobeda
    if igra[0][0] == igra[1][0] == igra[2][0] != '':
        pobeda = True
        return pobeda
    elif igra[0][1] == igra[1][1] == igra[2][1] != '':
        pobeda = True
        return pobeda
    elif igra[0][2] == igra[1][2] == igra[2][2] != '':
        pobeda = True
        return pobeda
    elif igra[0][0] == igra[1][1] == igra[2][2] != '':
        pobeda = True
        return pobeda
    elif igra[0][2] == igra[1][1] == igra[2][0] != '':
        pobeda = True
        return pobeda
    else:
        return pobeda



#23.Zadatak

def sudoku(game):
    '''
    Provera ispravno popunjene sudoku igre
    :param game: lista
    :return: True or False
    '''
    resen = False
    brojevi = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
    provera = []
    p1 = 0
    for i in range(len(game)):
        for b in range(len(game[i])):
            if b in brojevi:
                pass
            else:
                resen = False

    for i in range(len(game)):
        for b in range(len(game[i])):
            provera.append(game[i][b])

    for i in range(len(provera)):
        if provera.count(i) == 9:
            p1 +=1

    if p1 == 9:
        return True
    else:
        return False



