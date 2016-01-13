import random
import sys

def algus():
    fail = open("Vaatamisvaarsused.txt", "r")
    failisisu = fail.readlines()
    vaatamise_list = list()
    vaatamisvaarsus = ""
    ei_tohi = [0]
    kas_uus = dict()
    for i in failisisu:
        indeks = i.index("\t")
        indeks2 = i[indeks+1:].index("\t") + indeks + 1
        vaatamisvaarsus = i[indeks+1:indeks2]
        kas_lubada = i[indeks2+1:]
        if "\n" in kas_lubada:
            kas_lubada = kas_lubada[:-1]
        kas_uus[vaatamisvaarsus] = kas_lubada
    return failisisu, vaatamise_list, vaatamisvaarsus, ei_tohi, kas_uus
        

def taringu_vise(failisisu, vaatamise_list, ei_tohi, kas_lubada):
    jah = ["Jah", "jah"]
    if kas_lubada == "1":
        kas_visata = input("Kas soovite täringuid visata (Jah/Ei)? ")
        if kas_visata not in jah:
            return kuva(vaatamise_list)
    suvaline = random.randint(2,12)
    while suvaline in ei_tohi:
        suvaline = random.randint(2,12)
    for i in failisisu:
        indeks = i.index("\t")
        if int(i[:indeks]) == suvaline:
            indeks = i.index("\t")
            indeks2 = i[indeks+1:].index("\t")
            vaatamisvaarsus = i[indeks+1:indeks2+indeks+1]
    if kas_uus[vaatamisvaarsus] == "0":
        ei_tohi.append(suvaline)
        print("""\tViske tulemus: {0}
\tVaatamisväärsus: {1}""".format(suvaline, vaatamisvaarsus))
        if len(ei_tohi) == 12:
            return kuva(vaatamise_list)
        else:
            return taringu_vise(failisisu, vaatamise_list, ei_tohi, "0")
    
    print("""\tViske tulemus: {0}
\tVaatamisväärsus: {1}""".format(suvaline, vaatamisvaarsus))
    kas_sobib = input("Kas sihtkoht sobib (Jah/Ei)? ")
    if kas_sobib in jah:
        vaatamise_list.append(vaatamisvaarsus)
        ei_tohi.append(suvaline)
        if len(ei_tohi) == 12:
            return kuva(vaatamise_list)
        else:
            return taringu_vise(failisisu, vaatamise_list, ei_tohi, "1")
    elif kas_sobib not in jah:
        return taringu_vise(failisisu, vaatamise_list, ei_tohi, "1")
    

def kuva(vaatamise_list):
    if len(vaatamise_list) == 0:
        sys.exit()
    number = 1
    print("Reisi marsruut: ")
    for i in vaatamise_list:
        print("\t{0}.".format(number),i)
        number += 1
        
failisisu, vaatamise_list, vaatamisvaarsus, ei_tohi, kas_uus = algus()
taringu_vise(failisisu, vaatamise_list, ei_tohi, "1")
        
        
    

