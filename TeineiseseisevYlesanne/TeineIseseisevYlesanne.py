import string
def kirjavahemargid(x):
    a=bool()
    for char in x:
        if char in string.punctuation: a=True
    return a
 
sisend = 'jah'
while sisend == 'jah':
    mituParve=''
    while not mituParve.isdigit():
        mituParve = input('Mitu haneparve on nähtud? ')
    mituParve=int(mituParve)
    arv=1
    nimed=list()
    liikmeteArv=list()
    nimedeList='1'
    LiikmeteArvuList=''
    while mituParve != arv-1:
        nimedeList=input('''    Sisestage {0}. haneparve...
        ...nimi: '''.format(arv))
        while kirjavahemargid(nimedeList)==True or nimedeList.isdigit() == True:
            nimedeList=input('''    Sisestage {0}. haneparve...
        ...nimi: '''.format(arv))
        while LiikmeteArvuList.isdigit()==False:
            LiikmeteArvuList=input('        ...liikmete arv: ')
        nimed.append(nimedeList)
        liikmeteArv.append(LiikmeteArvuList)
        arv+=1
        LiikmeteArvuList=''
    arv=len(nimed)
    indeks=0
    print('Lõunasse lähevad järgmised haneparved: ')
    while arv != indeks:
        print("    '{0}' ({1})".format(nimed[indeks],liikmeteArv[indeks]))
        indeks+=1
	
    indeks=0
	
    kokkuRatva=0
    kokkuEndla=0
    kokkuSaad=0
    while len(nimed) != indeks:
        endlaJarv=''
        saadJarv=''
        ratvaJarv=''
        while endlaJarv.isdigit() is False or int(endlaJarv) > int(liikmeteArv[indeks]): 
            endlaJarv=input("Mitu hane maandub '{0}' parvest Endla järvele? ".format(nimed[indeks]))
            if endlaJarv.isdigit() is True:
                if int(endlaJarv) > int(liikmeteArv[indeks]):
                    print('''    Parves '{0}' ei ole nii palju hanesid!
    Parves '{0}' on {1} hane!
    Sisestage väiksem väärtus!'''.format(nimed[indeks],liikmeteArv[indeks]))
        lendabSaad=int(liikmeteArv[indeks])-int(endlaJarv)
        print('    Endla järvele maandus {0} hane ja {1} lendab edasi'.format(endlaJarv,lendabSaad))
        while saadJarv.isdigit() is False or int(saadJarv) > lendabSaad:
            saadJarv=input("Mitu hane maandub '{0}' parvest Saadjärvele? ".format(nimed[indeks]))
            if saadJarv.isdigit() is True:
                if int(saadJarv) > lendabSaad:
                    print('''    Parves '{0}' ei ole nii palju hanesid!
    Parves '{0}' on {1} hane!
    Sisestage väiksem väärtus!'''.format(nimed[indeks],lendabSaad))
        lendabRatva=lendabSaad-int(saadJarv)
        print('    Saadjärvele maandus {0} hane ja {1} lendab edasi'.format(saadJarv,lendabRatva))
        while ratvaJarv.isdigit() is False or int(ratvaJarv) > lendabRatva:
            ratvaJarv=input("Mitu hane maandub'{0}'parvest Ratva järvele? ".format(nimed[indeks]))
            if ratvaJarv.isdigit() is True:
                if int(ratvaJarv) > lendabRatva:
                    print('''    Parves '{0}' ei ole nii palju hanesid!
    Parves '{0}' on {1} hane!
    Sisestage väiksem väärtus!'''.format(nimed[indeks],lendabRatva))
        lendabEdasi=lendabRatva-int(ratvaJarv)
        print('    Ratvajärvele maandus {0} hane ja {1} hane lendab edasi'.format(ratvaJarv,lendabEdasi))
        indeks+=1
        kokkuRatva=kokkuRatva+int(ratvaJarv)
        kokkuSaad=kokkuSaad+int(saadJarv)
        kokkuEndla=kokkuEndla+int(endlaJarv)
    liikmeteArv=map(int,liikmeteArv)
    eiPeatunud=sum(liikmeteArv)-(kokkuRatva+kokkuSaad+kokkuEndla)
    print('''
Endla järvele on maandunud kokku {0} hane!
Saadjärvele on maandunud kokku {1} hane!
Ratva järvele on maandunud kokku {2} hane!
Eesti järvedel ei peatunud {3} hane!
'''.format(kokkuEndla,kokkuSaad,kokkuRatva,eiPeatunud))

    sisend = input('Kas the soovite jätkata(jah/ei)? ')
    if sisend != 'jah':
        print('Programm läks kinni!')
        exit
    

 
           
        


        



    


