def haneparvenimed():
    arv=1
    nimedeList=list()
    liikmeteArvuList=list()
    while arv-1 != mituParve:   
        print("    Sisestage {0} .haneparve ...".format(arv))
        nimi=input("        ...nimi:    ")
        liikmeteArv=input("        ...liikmete arv:    ")
        nimedeList.append(nimi)
        liikmeteArvuList.append(liikmeteArv)
        arv+=1
    return {'nimedeList':nimedeList, 'liikmeteArvuList':liikmeteArvuList}

def lounasseLahevad():
    print("Lõunasse lähevad järgmised haneparved:")
    arv=0
    while arv != int(mituParve):
        print("    '{0}'({1} hane)".format(nimedeList[arv],liikmeteArvuList[arv]))
        arv+=1
            
def maandumine():
    arv=0
    kokkuMaandubEndla = 0
    kokkuMaandubSaad = 0
    kokkuMaandubRatva = 0
    kokkuLendabEdasi = 0
    while arv != len(nimedeList):
        mituMaandubEndla = input("Mitu hane maandub '{0}' parvest Endla järvele?    ".format(nimedeList[arv]))
        lendabSaad = int(liikmeteArvuList[arv]) - int(mituMaandubEndla)
        kontroll(arv,lendabSaad)
        vastus("x",mituMaandubEndla,lendabSaad)
        mituMaandubSaad = input("Mitu hane maandub '{0}' parvest Saadjärvele?    ".format(nimedeList[arv]))
        lendabRatva = lendabSaad - int(mituMaandubSaad)
        kontroll(arv,lendabRatva)
        vastus("y",mituMaandubSaad,lendabRatva)
        mituMaandubRatva =input("Mitu hane maandub '{0}' parvest Ratva järvele?    ".format(nimedeList[arv]))
        lendabEedasi = lendabRatva - int(mituMaandubRatva)
        kontroll(arv,lendabEedasi)
        vastus("z",mituMaandubRatva,lendabEedasi)
                                
        kokkuMaandubEndla = kokkuMaandubEndla + int(mituMaandubEndla)
        kokkuMaandubSaad = kokkuMaandubSaad + int(mituMaandubSaad)                          
        kokkuMaandubRatva = kokkuMaandubRatva + int(mituMaandubSaad)
        kokkuLendabEdasi +=lendabEedasi
        arv+=1
        
    print('''
Endla järvele on maandunud kokku {0} hane!
Saadjärvele on maandunud kokku {1} hane!
Ratva järvele on maandunud kokku {2} hane!
Eesti järvedel ei peatunud {3} hane!
'''.format(kokkuMaandubEndla,kokkuMaandubSaad,kokkuMaandubRatva,kokkuLendabEdasi))
                                
    return 

def vastus(identifikaator,mituMaandub,lendabEdasi):
    if identifikaator == "x":
        print("Endla järvele maandus {0} hane ja {1} hane lendab edasi!".format(mituMaandub,lendabEdasi))                                            
    if identifikaator == "y":
        print("   Saadjärvele maandus {0} hane ja {1} hane lendab edasi!".format(mituMaandub,lendabEdasi))
    if identifikaator == "z":
        print("        Ratva järvele maandus {0} hane ja {1} hane lendab edasi!".format(mituMaandub,lendabEdasi))

        
def kontroll(arv,alles):
    if  0 > alles:
        print('''        Parves {0} ei ole nii palju hanesid!
        Parves {0} on {1} hane!
        Sisestage väiksem väärtus!'''.format(nimedeList[arv],liikmeteArvuList[arv]))
        kontroll = True
    else: kontroll = False
    return kontroll


def jatkamine():
    sisend = input('Kas te soovite jätkata(jah/ei)?')
    if sisend == 'jah':
        print("")
        edasi = True
    else:
        print("Programm läks kinni!")
        edasi = False
    return edasi


        
a = True
while a == True:
    mituParve = int(input("Mitu haneparve on nähtud?    "))
    listid=haneparvenimed()
    nimedeList=listid['nimedeList']
    liikmeteArvuList=listid['liikmeteArvuList']
    lounasseLahevad()
    maandumine()
    a=jatkamine()

    
      
#Haneparve nimi ei tohi sisaldada tühikuid, ega muid kirjavahemärke (nt !, ?, . jne).
#Parandada tagasisides saadud vead testide lugemise juhendi järgi (vt siia - lisatud Error_OutputIsTooShort ja Error_EOF_InputError veateadete põhjused).
#Error_EOF_InputError -  Punktide arv ei ole kunagi suurem nullist.
#Programmi töö võib lõpetada küsimus "Kas soovite jätkata (jah/ei)? ", mille vastuseks on "ei" ja kõik muud vastused peale "jah".
