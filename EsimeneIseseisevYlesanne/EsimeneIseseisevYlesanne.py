rohk =1.65
import random
kasKaivitada = input("Süsteem on ülesse seatud - kas käivitada süsteem (jah/ei)? ")
if kasKaivitada != "jah":
    print("Süsteemi ei võta tööle!")
if kasKaivitada == "jah":
    print("\n\tSüvaveepump käivitus!")
    print("\t\tHüdrofoori rõhk:")
    while rohk <= 2.75:
        rohk += 0.15
        rohk = "%.2f"%rohk
        print("\t\t\t {0} bar".format(rohk))
        rohk = float(rohk)
    print("\tSüvaveepump seiskus!")
    kasKraanid = input("\nKas keerata kraanid lahti (jah/ei)? ")
    if kasKraanid != "jah":
        print("Kraane lahti ei keeratud!")
    while kasKraanid == 'jah':                                                                                                                                                                 
            
        if 2.75 <= rohk <= 2.85:pumbaOlek= "[Seisab]"                                 
        if 1.75 <= rohk <= 1.85:pumbaOlek= "[Töötab]"                                               
        bar = str("bar")
        while 1.80 <= rohk:     
            veeTarbimine= random.choice(('[Tarbitakse]', '[Ei tarbita]')) 
            if veeTarbimine=='[Tarbitakse]':rohuSuund = '[Alaneb]'
            if veeTarbimine== '[Tarbitakse]'and 1.80<=rohk: rohk -= 0.05
            rohk = round(rohk,2)
            if veeTarbimine== '[Ei tarbita]':rohuSuund = '[Seisab]'
            print('\t',pumbaOlek, veeTarbimine, rohuSuund,':','%.2f' %rohk,bar,)
 
            
    
        
        kasKraanid = input("\nKas te soovite jätkata (jah/ei)? ")           
