mituParve=input('Mitu haneparve on nähtud? ')
arv=1
nimed=list()
liikmeteList=list()
while int(mituParve) != arv-1:
    nimi=input('''  Sisestage {0}. haneparve...
        ...nimi: '''.format(arv))
    liige=input('        ...liikmete arv: ')
    nimed.append(nimi)
    liikmeteList.append(liige)
    arv+=1
arv=0
print('Lõunasse lähevad järgmised haneparved: ')
while int(mituParve) != arv:
    print("    '{0}' ({1})".format(nimed[arv],liikmeteList[arv]))
    arv+=1
arv=0
kokkuEndla = 0
kokkuSaad = 0
kokkuRatva = 0
while int(mituParve) != arv:
    endlaJarv=input("Mitu hane maandub '{0}' parvest Endla järvele? ".format(nimed[arv]))
    lendabSaad = int(liikmeteList[arv]) - int(endlaJarv)
    print("    Endla järvele maandus {0} hane ja {1} lendab edasi!".format(endlaJarv,lendabSaad))
    saadJarv=input("Mitu hane maandub '{0}' parvest Saadjärvele? ".format(nimed[arv]))
    lendabRatva = lendabSaad - int(saadJarv)
    print("    Saadjärvele maandus {0} hane ja {1} lendab edasi!".format(saadJarv,lendabRatva))
    ratvaJarv=input("Mitu hane maandub '{0}' parvest Ratva järvele? ".format(nimed[arv]))
    lendabEdasi = lendabRatva - int(ratvaJarv)
    print("    Ratva järvele maandus {0} hane ja {1} lendab edasi!".format(ratvaJarv,lendabEdasi))
    arv+=1
    kokkuEndla = kokkuEndla +int(endlaJarv)
    kokkuSaad = kokkuSaad + int(saadJarv)
    kokkuRatva = kokkuRatva + int(ratvaJarv)
liikmeteList = map(int,liikmeteList)
kokkuEdasi = sum(liikmeteList) -(kokkuEndla+kokkuSaad+kokkuRatva)
print('''
Endla järvele on maandunud kokku {0} hane!
Saadjärvele on maandunud kokku {1} hane!
Ratva järvele on maandunud kokku {2} hane!
Eesti järvele ei peatunud {3} hane!'''.format(kokkuEndla,kokkuSaad,kokkuRatva,kokkuEdasi))
sisend=input('Kas te soovite jätkata(jah/ei)? ')
