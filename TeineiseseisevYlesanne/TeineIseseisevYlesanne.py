def kirjavahemargid(x):
    a=False
    for char in x:
        if char in string.punctuation: a=True
    return a
def taisarvulinevaartus(y):
    b=False
    if y.isdigit()==True: b=True
    return b
def kokkuvote(x,y,z,t):
    t=map(int,t)
    eiPeatunud=sum(t)-(x+y+z)
    c=print('''Endla järvele on maandunud kokku {0} hane!
    Saadjärvele on maandunud kokku {1} hane!
    Ratva järvele on maandunud kokku {2} hane!
    Eesti järvedel ei peatunud {3} hane!'''.format(x,y,z,eiPeatunud))
    return c
def sisendkunitaisarv(nimi,kysimus):
    while taisarvulinevaartus(nimi) != True:
        nimi=input(kysimus)
    nimi = int(nimi)
    return nimi
    
    
sisend = 'jah'
while sisend == 'jah':
    import string

    nimi=''
    mituParve=sisendkunitaisarv(nimi,'Mitu haneparve on nähtud?: ')
    
    arv=1
    nimed=list()
    liikmeteArv=list()
    nimedeList='1'
    LiikmeteArvuList=''
    while mituParve != arv-1:
        nimedeList=input('''\nSisestage {0}.
haneparve nimi:'''.format(arv))  
        while kirjavahemargid(nimedeList)==True or taisarvulinevaartus(nimedeList)==True:
            nimedeList=input('''\nSisestage {0}.
haneparve nimi:'''.format(arv))
        while taisarvulinevaartus(LiikmeteArvuList)==False:
            LiikmeteArvuList=input('Liikmete arv: ')
        nimed.append(nimedeList)
        liikmeteArv.append(LiikmeteArvuList)
        arv+=1
        LiikmeteArvuList=''
    arv=len(nimed)
    indeks=0
    print('\nLõunasse lähevad järgmised haneparved: ')
    while arv != indeks:
        print('{0} ({1} hane)'.format(nimed[indeks],liikmeteArv[indeks]))
        indeks+=1
	
    indeks=0	
    kokkuRatva=0
    kokkuEndla=0
    kokkuSaad=0
    while len(nimed) != indeks:
        endlaJarv=''
        saadJarv=''
        ratvaJarv=''

        while taisarvulinevaartus(endlaJarv) is False or endlaJarv > liikmeteArv[indeks]: 
            endlaJarv=input('\nMitu hane maandub {0} parvest Endla järvele? '.format(nimed[indeks]))
            if taisarvulinevaartus(endlaJarv) is True:
                if int(endlaJarv) > int(liikmeteArv[indeks]):
                    print('''\nParves {0} ei ole nii palju hanesid!
Parves {0} on {1} hane!
Sisestage väiksem väärtus!'''.format(nimed[indeks],liikmeteArv[indeks]))
        lendabSaad=int(liikmeteArv[indeks])-int(endlaJarv)
        print('Endla järvele maandus {0} hane ja {1} lendab edasi.\n'.format(endlaJarv,lendabSaad))
        
        
        while taisarvulinevaartus(saadJarv) is False or int(saadJarv)>lendabSaad:
            saadJarv=input('Mitu hane maandub {0} parvest Saadjärvele? '.format(nimed[indeks]))
            if taisarvulinevaartus(saadJarv) is True:
                if int(saadJarv) > lendabSaad:
                    print('''\nParves {0} ei ole nii palju hanesid!
Parves {0} on {1} hane!
Sisestage väiksem väärtus!'''.format(nimed[indeks],lendabSaad))
        lendabRatva=lendabSaad-int(saadJarv)
        print('Saadjärvele maandus {0} hane ja {1} lendab edasi.\n'.format(saadJarv,lendabRatva))
        
        while taisarvulinevaartus(ratvaJarv) is False or int(ratvaJarv)>lendabSaad:
            ratvaJarv=input('Mitu hane maandub {0} parvest Ratva järvele? '.format(nimed[indeks]))
            if taisarvulinevaartus(ratvaJarv) is True:
                if int(ratvaJarv) > lendabRatva:
                    print('''\nParves {0} ei ole nii palju hanesid!
Parves {0} on {1} hane!
Sisestage väiksem väärtus!'''.format(nimed[indeks],lendabRatva))
        lendabEdasi=lendabRatva-int(ratvaJarv)
        print('Ratvajärvele maandus {0} hane ja {1} hane lendab edasi.\n'.format(ratvaJarv,lendabEdasi))
        
        indeks+=1
        kokkuRatva+=int(ratvaJarv)
        kokkuSaad+=int(saadJarv)
        kokkuEndla+=int(endlaJarv)
    kokkuvote(kokkuRatva,kokkuSaad,kokkuEndla,liikmeteArv)
	
    sisend=input('\nKas te soovite jätkata(jah/ei)? \n')
print('\nSüsteem läks kinni!')
exit



    


