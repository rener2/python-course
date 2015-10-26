import string
#import sys
#---------------------------------------------------------------------------------------------
def kirjavahemargid(x):
    a=bool()
    for char in x:
        if char in string.punctuation: a=True
    return a
def haneparvedjaliikmed(x1,x2,x3,x4,x5,x6):
    while x1 != x2-1:
        x6=input('''    Sisestage {0}. haneparve...
        ...nimi: '''.format(x2))
        while kirjavahemargid(x6)==True or x6.isdigit() == True or x6 == '':
            x6=input('''    Sisestage {0}. haneparve...
        ...nimi: '''.format(x2))
        while x4.isdigit()==False or x4=='0':
            x4=input('        ...liikmete arv: ')
        x5.append(x6)
        x3.append(x4)
        x2+=1
        x4=''
def parveLend(y1,y2,y3,y4,y5):
    while y1.isdigit() is False or int(y1)>int(y2):
        y1=input("Mitu hane maandub '{0}' parvest {1}? ".format(y3[indeks],y5))
        if y1.isdigit() is True:
            if int(y1)> int(y2):
                print('''}\n    Parves '{0}' ei ole nii palju hanesid!
    Parves '{0}' on {1} hane!
    Sisestage väiksem väärtus!'''.format(y3[indeks],y2))
    return y1
def kokkuvote(x,y,z,t):
    t=map(int,t)
    eiPeatunud=sum(t)-(x+y+z)
    c=print('''Endla järvele on maandunud kokku {0} hane!
Saadjärvele on maandunud kokku {1} hane!
Ratva järvele on maandunud kokku {2} hane!
Eesti järvedel ei peatunud {3} hane!'''.format(x,y,z,eiPeatunud))
    return c
#----------------------------------------------------------------------------------------------    
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
    
    haneparvedjaliikmed(mituParve,arv,liikmeteArv,LiikmeteArvuList,nimed,nimedeList)
    
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
        lendabSaad=0
        lendabRatva=0
        lendabEdasi=0

        endlaJarv=parveLend(endlaJarv,liikmeteArv[indeks],nimed,lendabSaad,'Endla järvele')
        lendabSaad=int(liikmeteArv[indeks])-int(endlaJarv)
        print('    Endla järvele maandus {0} hane ja {1} lendab edasi!'.format(endlaJarv,lendabSaad))
        
        saadJarv=parveLend(saadJarv,lendabSaad,nimed,lendabRatva,'Saadjärvele')
        lendabRatva=int(lendabSaad)-int(saadJarv)
        print('    Saadjärvele maandus {0} hane ja {1} lendab edasi!'.format(saadJarv,lendabRatva))
        
        ratvaJarv=parveLend(ratvaJarv,lendabRatva,nimed,lendabEdasi,'Ratva järvele')
        lendabEdasi=int(lendabRatva)-int(ratvaJarv)
        print('    Ratva järvele maandus {0} hane ja {1} hane lendab edasi!'.format(ratvaJarv,lendabEdasi))

        indeks+=1
        kokkuRatva=kokkuRatva+int(ratvaJarv)
        kokkuSaad=kokkuSaad+int(saadJarv)
        kokkuEndla=kokkuEndla+int(endlaJarv)
    kokkuvote(kokkuEndla,kokkuSaad,kokkuRatva,liikmeteArv)

    sisend = input('Kas the soovite jätkata(jah/ei)? ')
    if sisend == 'jah':
        print('')
print('Programm läks kinni!')
sys.exit

    
    
    

 
           
        


        



    


