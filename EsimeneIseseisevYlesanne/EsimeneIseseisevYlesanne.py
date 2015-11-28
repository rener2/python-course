rohk =1.65
import random
arv=2

kasKaivitada = input("Süsteem on ülesse seatud - kas käivitada süsteem (jah/ei)? ")
if kasKaivitada != "jah":
    print("Süsteemi ei võta tööle!")
elif kasKaivitada == "jah":
    print("\n\t Süvaveepump käivitus!\n\t\tHüdrofoori rõhk:")
    
    while rohk <= 2.80:
        rohk += 0.15
        rohk = "%.2f"%rohk
        print("\t\t\t{0} bar".format(rohk))
        rohk = float(rohk)
    print("\tSüvaveepump seiskus!")
    kasKraanid = input("\nKas keerata kraanid lahti (jah/ei)? ")
    
    if kasKraanid != "jah":
        print("Kraane lahti ei keeratud!")
        
    while kasKraanid == "jah":
        
        if arv % 2 == 0:
            while 1.85<=rohk:
                veeTarbimine= random.choice(("[Tarbitakse]", "[Ei tarbita]"))
                if veeTarbimine=="[Tarbitakse]":rohuSuund = "[Alaneb]"
                if veeTarbimine== "[Tarbitakse]"and 1.80<=rohk: rohk -= 0.05
                rohk = round(rohk,2)
                if veeTarbimine== "[Ei tarbita]":rohuSuund = "[Seisab]"
                print("\t[Seisab]", veeTarbimine, rohuSuund,": %.2f bar"%rohk)
                
        if arv % 2 != 0:
            while rohk <= 2.75:
                veeTarbimine = random.choice(("[Tarbitakse]", "[Ei tarbita]"))                                                        
                if veeTarbimine== '[Ei tarbita]' and rohk <= 2.70 : rohk += 0.15                                                         
                if veeTarbimine== '[Tarbitakse]'and rohk <= 2.75: rohk += 0.10    
                rohk = round(rohk,2)
                print("\t[Töötab]", veeTarbimine,"[Tõuseb] : %.2f bar"%rohk)
        arv +=1
        kasKraanid = input("\nKas te soovite jätkata (jah/ei)? ")           
        if kasKraanid != "jah":
            print("Süsteem suleti!")
