import string
import sys
from time import localtime, strftime


def valikvastus():
    """Funktsioon laseb kasutajal valida 4 sisendi vahel ja 
    tagastab sisestatud väärtuse.
    """
    valikud = ("L", "M", "P", "E")
    valik = input("\nSisestage soovitud valik (L, M, P, E): ").upper()
    while valik not in valikud: valik = input("Sisestage soovitud valik (L, M, P, E): ").upper()

    if valik in valikud:
        print()
    return valik


def lisa_salvesta():
    """Funktsioon lisab anbmebaasi faili kasutaja sisestatud andmed, kui andmed
    on sisestatud nõutud kujul. Lõpus käivitab uuesti valivkastus() funktsiooni.
    """
    sisend, aeg = input("\tFikseerige sade kujul [Identifikaator] [20] (C): "), strftime("%d.%m.%Y %H:%M:%S", localtime())
    if check_brackets(sisend) is False:
        return lisa_salvesta()
    if sisend.lower() == 'c':
        return valikvastus()
    fail = open("andmebaas.txt", "a", encoding="utf-8")
    fail.write(aeg+" - "+sisend+"\n")
    fail.close()
    print("\tSade fikseeritud!")
    return valikvastus()


def muuda(muudetava_indeks):
    """Muudab andmebaasi sisu antud indeksi ja uue sisu järgi."""
    sisend, aeg = input("\t\nFikseerige sade kujul [Identifikaator] [20] (C): "), strftime("%d.%m.%Y %H:%M:%S", localtime())
    if check_brackets(sisend) is False:
        return muuda(muudetava_indeks)
    if sisend.lower() == 'c':
        return valikvastus()
    sisend = aeg+" - "+sisend+"\n"
    fail = open("andmebaas.txt", "r", encoding="utf-8")
    sisu = fail.readlines()
    sisu.pop(muudetava_indeks)
    sisu.insert(muudetava_indeks, sisend)
    sisu = "".join(sisu)
    fail.close()
    fail = open("andmebaas.txt", "w", encoding="utf-8")
    fail.write(sisu)
    print("\tSademe kirje on uuendatud!")
    fail.close()
    return valikvastus()


def muuda_sadet(): 
    """Funktsioon kuvab kasutajale andmebaasi sisu indeksi järgi ja
    laseb kasutajal indeksi järgi andmebaasi sisu muuta muuda() funktsiooni
    välja kutsudes. Lõpus käivitab uuesti valikvastus() funktsiooni.
    """
    fail = open("andmebaas.txt", "r+", encoding="utf-8")
    sisu = fail.readlines()
    arv = 1
    print("\tAndmebaasis olevad andmed:")
    for i in sisu:
        print("\t\t{0}.{1}".format(arv, i[21:-1]))
        arv += 1
    print()
    fail.close()
    sisend = ""
    while sisend.isdigit() is False or int(sisend) > len(sisu) or int(sisend) < 1:
        sisend = input("\tSisestage sademe indeks, mida soovite muuta (C): ")
        if sisend.lower() == 'c':
            return valikvastus()
        if sisend.isdigit() is True:
            if int(sisend) < 1 or int(sisend) > len(sisu):
                print("\t\tSisestatud sademe indeksit ei eksisteeri andmebaasis!")
    valjund = muuda(int(sisend)-1)
    return valjund


def kuva_sademeid():
    """Funktsioon avab faili ja kuvab selle sisu ridade kaupa, lõpus läheb
    uuesti valikvastus() funktsiooni.
    """
    fail = open("andmebaas.txt", "r", encoding="utf-8")
    print("\tAndmebaasi sisu:")
    sisu = fail.readlines()
    for i in sisu:
        print("\t\t"+i[:-1])
    fail.close()
    return valikvastus()

    
def sulge_programm():
    """Funktsioon sulgeb programmi, juhul kui kasutaja seda soovib,
    kui ei soovi siis läheb uuesti valikvastus() funktsiooni.
    """
    sisend = input("\tKas olete kindel, et soovite programmi sulgeda ('jah')? ")
    if sisend.upper() == "JAH":
        print("\tProgramm läks kinni!")
        sys.exit()
    else:
        return valikvastus()


def check_brackets(sentence):
    """Check if given sentence consists of values inside two
    brackets, if not, return False. Returns true, if inside
    of the first bracket consists of letters and the inside of the second
    bracket consists only of numbers.Furthermore return false
    if there is anything outside the brackets.
    """
    if sentence.lower() == 'c':
        return True
    a = True
    if sentence.count('[') != 2 or sentence.count(']') != 2:
        return False
    esimene_p = sentence.index('[')
    esimene_v = sentence.index(']')
    if esimene_v < esimene_p:
        return False
    if sentence[esimene_v+1] != ' ':
        return False
    teine_p = esimene_v+2
    teine_v = sentence[esimene_v+2:].index(']')+teine_p
    if teine_v < teine_p:
        return False
    if teine_v+1 != len(sentence) or esimene_p != 0:
        return False
    for i in sentence[esimene_p+1:esimene_v]:
        if i not in string.ascii_letters:
            a = False
    b = sentence[teine_p+1:teine_v].isdigit()
    if a is True and b is True:
        return True
    else:
        return False


print("""L - Sademete lisamine andmebaasi.
M - Andmebaasis oleva sademe muutmine.
P - Andmebaasis asuvate sademete kuvamine.
E - Programmi sulgemine.""")
valik = valikvastus()

while True:    
    if valik == 'L':
        valik = lisa_salvesta()
    elif valik == 'M':
        valik = muuda_sadet()
    elif valik == 'P':
        valik = kuva_sademeid()
    elif valik == 'E':
        valik = sulge_programm()
