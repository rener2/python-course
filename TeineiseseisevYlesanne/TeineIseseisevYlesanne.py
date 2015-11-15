import string


def haneparvenimed():
    arv=1
    nimedeList=list()
    liikmeteArvuList=list()
    while arv-1 != mituParve:   
        print("\tSisestage {0}. haneparve ...".format(arv))
        nimi=input("\t\t... nimi: ")
        while nimi.isdigit() is True or kirjaVaheMark(nimi) is True or " " in nimi:
            nimi=input("\t\t... nimi: ")          
        liikmeteArv=input("\t\t... liikmete arv: ")
        while liikmeteArv.isdigit() is False:
            liikmeteArv=input("\t\t... liikmete arv: ")
        nimedeList.append(nimi)
        liikmeteArvuList.append(liikmeteArv)
        arv+=1
    return {'nimedeList':nimedeList, 'liikmeteArvuList':liikmeteArvuList}


def lounasseLahevad():
    print("Lõunasse lähevad järgmised haneparved:")
    arv=0
    while arv != int(mituParve):
        print("\t'{0}' ({1} hane)".format(nimedeList[arv],liikmeteArvuList[arv]))
        arv+=1

            
def maandumine():
    arv=0
    kokkuMaandubEndla = 0
    kokkuMaandubSaad = 0
    kokkuMaandubRatva = 0
    kokkuLendabEdasi = 0
    while arv != len(nimedeList):
        
        mituMaandubEndla = input("Mitu hane maandub '{0}' parvest Endla järvele? ".format(nimedeList[arv]))
        while mituMaandubEndla.isdigit() is False or int(mituMaandubEndla) > int(liikmeteArvuList[arv]):
            if mituMaandubEndla.isdigit() is True:
                if int(mituMaandubEndla)> int(liikmeteArvuList[arv]):
                    print('''\tParves '{0}' ei ole nii palju hanesid!
\tParves '{0}' on {1} hane!
\tSisestage väiksem väärtus!'''.format(nimedeList[arv],liikmeteArvuList[arv]))
            mituMaandubEndla = input("Mitu hane maandub '{0}' parvest Endla järvele? ".format(nimedeList[arv]))
        lendabSaad = int(liikmeteArvuList[arv]) - int(mituMaandubEndla)
        vastus("x",mituMaandubEndla,lendabSaad)
        
        mituMaandubSaad = input("Mitu hane maandub '{0}' parvest Saadjärvele? ".format(nimedeList[arv]))
        while mituMaandubSaad.isdigit() is False or int(mituMaandubSaad) > lendabSaad :
            if mituMaandubSaad.isdigit() is True:
                if int(mituMaandubSaad)> lendabSaad:
                    print('''\tParves '{0}' ei ole nii palju hanesid!
\tParves '{0}' on {1} hane!
\tSisestage väiksem väärtus!'''.format(nimedeList[arv],lendabSaad))
            mituMaandubSaad = input("Mitu hane maandub '{0}' parvest Saadjärvele? ".format(nimedeList[arv]))
        lendabRatva = lendabSaad - int(mituMaandubSaad)
        vastus("y",mituMaandubSaad,lendabRatva)
        
        mituMaandubRatva =input("Mitu hane maandub '{0}' parvest Ratva järvele? ".format(nimedeList[arv]))
        while mituMaandubRatva.isdigit() is False or int(mituMaandubRatva) > lendabRatva:
            if mituMaandubRatva.isdigit() is True:
                if int(mituMaandubRatva) > lendabRatva:
                    print('''\tParves '{0}' ei ole nii palju hanesid!
\tParves '{0}' on {1} hane!
\tSisestage väiksem väärtus!'''.format(nimedeList[arv],lendabRatva))
            mituMaandubRatva =input("Mitu hane maandub '{0}' parvest Ratva järvele? ".format(nimedeList[arv]))
        lendabEedasi = lendabRatva - int(mituMaandubRatva)
        vastus("z",mituMaandubRatva,lendabEedasi)
                                
        kokkuMaandubEndla = kokkuMaandubEndla + int(mituMaandubEndla)
        kokkuMaandubSaad = kokkuMaandubSaad + int(mituMaandubSaad)                          
        kokkuMaandubRatva = kokkuMaandubRatva + int(mituMaandubRatva)
        kokkuLendabEdasi +=lendabEedasi
        arv+=1
        
    print('''
Endla järvele on maandunud kokku {0} hane!
Saadjärvele on maandunud kokku {1} hane!
Ratva järvele on maandunud kokku {2} hane!
Eesti järvedel ei peatunud {3} hane!
'''.format(kokkuMaandubEndla,kokkuMaandubSaad,kokkuMaandubRatva,kokkuLendabEdasi))
                                
    #return 


def vastus(identifikaator,mituMaandub,lendabEdasi):
    if identifikaator == "x":
        print("\tEndla järvele maandus {0} hane ja {1} hane lendab edasi!".format(mituMaandub,lendabEdasi))                                            
    if identifikaator == "y":
        print("\tSaadjärvele maandus {0} hane ja {1} hane lendab edasi!".format(mituMaandub,lendabEdasi))
    if identifikaator == "z":
        print("\tRatva järvele maandus {0} hane ja {1} hane lendab edasi!".format(mituMaandub,lendabEdasi))


def jatkamine():
    sisend = input("Kas soovite jätkata (jah/ei)? ")
    if sisend == 'jah':
        print("")
        edasi = True
    else:
        print("Programm läks kinni!")
        edasi = False
    return edasi


def kirjaVaheMark(sone):
    arv=0
    value = False
    for char in sone:
        if char in string.punctuation: value = True
    return value
    
        
a = True
while a == True:
    mituParve = input("Mitu haneparve on nähtud? ")
    while mituParve.isdigit() is False:
        mituParve = input("Mitu haneparve on nähtud? ")
    mituParve=int(mituParve)
    listid=haneparvenimed()
    nimedeList=listid['nimedeList']
    liikmeteArvuList=listid['liikmeteArvuList']
    lounasseLahevad()
    maandumine()
    a=jatkamine()

    
