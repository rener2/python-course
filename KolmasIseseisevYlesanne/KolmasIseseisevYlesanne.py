import string
import sys
from time import localtime, strftime


def valikvastus():
    """Funktsioon laseb kasutajal valida 4 sisendi vahel ja 
    tagastab sisestatud väärtuse"""
    valikud=("L","M","P","E")        
    valik = input("Sisestage soovitud valik (L, M, P, E): ")
    valik=valik.upper()
    if valik not in valikud: return valikvastus()
    elif valik in valikud: print("")
    return valik


def lisa_salvesta():
    """Funktsioon lisab anbmebaasi faili kasutaja sisestatud andmed, kui andmed
    on sisestatud nõutud kujul. Lõpus käivitab uuesti valivkastus() funktsiooni"""
    sisend,aeg=input("\tFikseerige sade kujul [Identifikaator] [20] (C): "),strftime("%d.%m.%Y %H:%M:%S", localtime())
    if sisend == 'C' or sisend == 'c':
        print("")
        return valikvastus()
    if check_brackets(sisend)==False: return lisa_salvesta()
    fail=open("andmebaas.txt","a",encoding="utf-8")
    fail.write(aeg+" - "+sisend+"\n")
    fail.close()
    print("\tSade fikseeritud!\n")
    valik=valikvastus()
    return valik


def muuda(muudetava_indeks):
    """Muudab andmebaasi sisu antud indeksi ja uue sisu järgi"""
    sisend,aeg=input("\tFikseerige sade kujul [Identifikaator] [20] (C): "),strftime("%d.%m.%Y %H:%M:%S", localtime())
    if sisend == "C" or sisend == "c": return sisend
    if check_brackets(sisend) == False: return muuda(muudetava_indeks)
    sisend=aeg+" - "+sisend+"\n"
    fail=open("andmebaas.txt","r",encoding="utf-8")
    sisu=fail.readlines()
    sisu.pop(muudetava_indeks)
    sisu.insert(muudetava_indeks,sisend)
    sisu="".join(sisu)
    fail.close()
    fail=open("andmebaas.txt","w",encoding="utf-8")
    fail.write(sisu)
    print("\tSademe kirje on uuendatud!\n")
    fail.close()
    valik=valikvastus()
    return valik


def muuda_sadet(): 
    """Funktsioon kuvab kasutajale andmebaasi sisu indeksi järgi ja
    laseb kasutajal indeksi järgi andmebaasi sisu muuta muuda() funktsiooni
    välja kutsudes. Lõpus käivitab uuesti valikvastus() funktsiooni"""
    fail = open("andmebaas.txt","r+",encoding="utf-8")
    sisu=fail.readlines()
    arv=1
    print("\tAndmebaasis olevad andmed:")
    for i in sisu:
        print("\t\t{0}. {1}".format(arv,i[22:-1])) 
        arv+=1
    print("")
    fail.close()
    sisend=""
    while sisend.isdigit() == False or int(sisend)> len(sisu) or int(sisend) < 1:
        sisend=input("\tSisestage sademe indeks, mida soovite muuta (C): ")
        if sisend =='C' or sisend == 'c':
            print("")
            return valikvastus()
        if sisend.isdigit() == True:
            if int(sisend) < 1 or int(sisend) > len(sisu):
                print("\t\tSisestatud sademe indeksit ei eksisteeri andmebaasis!")
    valjund=muuda(int(sisend)-1)
    return valjund


def kuva_sademeid():
    """Funktsioon avab faili ja kuvab selle sisu ridade kaupa, lõpus läheb
    uuesti valikvastus() funktsiooni"""
    fail=open("andmebaas.txt","r",encoding="utf-8")
    print("\tAndmebaasi sisu:")
    print("")
    sisu=fail.readlines()
    for i in sisu:
        print("\t\t",i[:-1])
    fail.close()
    valik=valikvastus()
    return valik

    
def sulge_programm():
    """Funktsioon sulgeb programmi, juhul kui kasutaja seda soovib,
    kui ei soovi siis läheb uuesti valikvastus() funktsiooni"""
    sisend=input("\tKas olete kindel, et soovite programmi sulgeda ('jah')? ")
    if sisend.upper()=="JAH":
        print("\tProgramm läks kinni!")
        sys.exit()
    else:
        print("")
        valik=valikvastus()
        return valik


def check_brackets(sentence):
    """Checks if given sentence consists of values inside two
    brackets if not, returns False. Function returns true if inside
    of the first bracket consists of letters and the inside of the second
    bracket consists only of numbers.Furthermore functions returns false
    if there is anything outside the brackets"""
    a=True
    b=True
    if sentence.count('[')<2 or sentence.count(']')<2:return False    
    esimeneP=sentence.index('[')
    esimeneV=sentence.index(']')
    if esimeneV<esimeneP:return False
    if sentence[esimeneV+1] != ' ': return False
    teineP=esimeneV+2
    teineV=sentence[esimeneV+2:].index(']')+teineP
    if teineV < teineP: return False
    if teineV+1 != len(sentence) or esimeneP != 0: return False   
    for i in sentence[esimeneP+1:esimeneV]:
        if i not in string.ascii_letters:
            a = False
    b=sentence[teineP+1:teineV].isdigit()
    if a == True and b == True:return True    
    else:return False
    
    


    
print("""L - Sademete lisamine andmebaasi.
M - Andmebaasis oleva sademe muutmine.
P - Andmebaasis asuvate sademete kuvamine.
E - Programmi sulgemine.\n""")
valik=valikvastus()
while True:    
    if valik == 'L':
        valik=lisa_salvesta()
    elif valik == 'M':
        valik=muuda_sadet()
    elif valik == 'P':
        valik=kuva_sademeid()
    elif valik == 'E':
        valik=sulge_programm()

