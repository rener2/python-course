import string
import datetime
import sys


def valikvastus():
    """Funktsioon laseb kasutajal valida 4 sisendi vahel ja 
    tagastab sisestatud väärtuse"""
    valikud=("L","M","P","E")        
    valik =""
    valik = input("Sisestage soovitud valik (L, M, P, E): ")
    if valik not in valikud:
        valik=valikvastus()
    return valik


def lisa_salvesta():
    """Funktsioon lisab anbmebaasi faili kasutaja sisestatud andmed, kui andmed
    on sisestatud nõutud kujul. Lõpus käivitab uuesti valivkastus() funktsiooni"""
    sisend=input("\tFikseerige sade kujul [Identifikaator] [20] (C):")
    aeg=current_time()
    if sisend == 'C':return sisend
    if check_brackets(sisend)==False: valik=lisa_salvesta()
    fail=open("andmebaasid.txt","a",encoding="utf-8")
    fail.write(aeg+" "+sisend+"\n")
    fail.close()
    print("\tSade fikseeritud")
    valik=valikvastus()
    return valik

def muuda(muudetava_indeks):
    """Muudab andmebaasi sisu antud indeksi ja uue sisu järgi"""
    sisend=input("Fikseerige sade kujul [Identifikaator] [20] (C): ")
    if sisend == "C": return sisend
    if check_brackets(sisend) == False: muuda(muudetava_indeks)
    aeg=current_time()
    sisend=aeg+" "+sisend+"\n"
    fail=open("andmebaasid.txt","r",encoding="utf-8")
    sisu=fail.readlines()
    sisu.pop(muudetava_indeks)
    sisu.insert(muudetava_indeks,sisend)
    sisu="".join(sisu)
    fail.close()
    fail=open("andmebaasid.txt","w",encoding="utf-8")
    fail.write(sisu)
    print("Sademe kirje on uuendatud!")
    fail.close()

def muuda_sadet():
    """Funktsioon kuvab kasutajale andmebaasi sisu indeksi järgi ja
    laseb kasutajal indeksi järgi andmebaasi sisu muuta muuda() funktsiooni
    välja kutsudes. Lõpus käivitab uuesti valikvastus() funktsiooni"""
    fail = open("andmebaasid.txt","r+",encoding="utf-8")
    sisu=fail.readlines()
    arv=1
    for i in sisu:
        print("{0}. {1}".format(arv,i[20:]))
        arv+=1
    fail.close()
    sisend=""
    while sisend.isdigit() == False or int(sisend)> arv or int(sisend) < 1:
        sisend=input("Sisestage sademe indeks, mida soovite muuta (C): ")
        if sisend =='C': return valikvastus()
        elif int(sisend) < 1 or int(sisend) > arv:
            print("Sisestatud sademe indeksit ei eksisteeri andmebaasis!")
    valjund=muuda(int(sisend)-1)
    if valjund == "C": return valikvastus()
    valik=valikvastus()
    return valik


        
def kuva_sademeid():
    """Funktsioon avab faili ja kuvab selle sisu ridade kaupa, lõpus läheb
    uuesti valikvastus() funktsiooni"""
    fail=open("andmebaasid.txt","r",encoding="utf-8")
    print("\tAndmebaasi sisu:")
    sisu=fail.readlines()
    for i in sisu:
        print("\t\t",i)
    fail.close()
    valik=valikvastus()
    return valik

    
def sulge_programm():
    """Funktsioon sulgeb programmi, juhul kui kasutaja seda soovib,
    kui ei soovi siis läheb uuesti valikvastus() funktsiooni"""
    sisend=input("\tKas olete kindel, et soovite programmi sulgeda ('jah')? ")
    if sisend=="jah" or "JAH":
        print("\tProgramm läks kinni!")
        sys.exit()
    else:
        valik=valikvastus()
        return valik

    
def current_time():
    """Funktsioon võtab antud aja
    kasutan sisendi aja võtmiseks"""
    aeg=datetime.datetime.now().isoformat()
    aeg=str(aeg)
    aeg=aeg[0:19]
    aeg=aeg.replace("-",".")
    aeg=aeg.replace("T","-")
    return aeg


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
    teineP=esimeneV+1 #kui vahepeal on tühik siis muuta +2'ks ehk [](kui siin on tühik vahel)[]
    teineV=sentence[esimeneV+1:].index(']')+teineP
    if teineV < teineP: return False
    if teineV+1 != len(sentence) or esimeneP != 0: return False
    for i in sentence[esimeneP+1:esimeneV]:
        if i not in string.ascii_letters:
            a = False
    b=sentence[teineP+1:teineV].isdigit()
    if a == True and b == True:
        return True    
    else:
        return False
    
    
    

#
 #fail=open("andmebaasid.txt","w",encoding="utf-8")
 #fail.close()
#def salvesta():


    
print("""L - Sademete lisamine andmebaasi.
M - Andmebaasis oleva sademe muutmine.
P - Andmebaasis asuvate sademete kuvamine.
E - Programmi sulgemine.""")
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
