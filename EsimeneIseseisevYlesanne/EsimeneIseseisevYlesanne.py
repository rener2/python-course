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
    if kasKraanid == "jah":
        while kasKraanid == 'jah':                                                                    #and loop lasts as long as the input is 'jah'                                                                                             
            
            if 2.75 <= rohk <= 2.85:pumbaOlek= '[Seisab]'                                               #state of tthe water pump, depending on the level of
            elif 1.75 <= rohk <= 1.85:pumbaOlek= '[Töötab]'                                               #pressure inside the hydrophore
            bar = str('bar')                                                                            
            
          
            while pumbaOlek == '[Seisab]' and 1.80 <= rohk:                                                            #displays log if water pump isn't working and while
                veeTarbimine= random.choice(('[Tarbitakse]', '[Ei tarbita]')) #chooses random value every iteration    #pressure is over 1.80 bar
                if veeTarbimine=='[Tarbitakse]':rohuSuund = '[Alaneb]'
                if veeTarbimine== '[Tarbitakse]'and 1.80<=rohk: rohk -= 0.05
                rohk = round(rohk,2)
                if veeTarbimine== '[Ei tarbita]':rohuSuund = '[Seisab]'
                print('\t',pumbaOlek, veeTarbimine, rohuSuund,':','%.2f' %rohk,bar,)                                             
                #would add time.sleep(1) here and into the other loop, but since it is a simulation, it is not necessary
               
            while pumbaOlek == '[Töötab]' and rohk<= 2.75:              
                veeTarbimine = random.choice(('[Tarbitakse]', '[Ei tarbita]'))
                rohuSuund = '[Tõuseb]'                                                          
                if veeTarbimine== '[Ei tarbita]' and rohk <= 2.70 : rohk += 0.15                                                         
                if veeTarbimine== '[Tarbitakse]'and rohk <= 2.75: rohk += 0.10    
                rohk = round(rohk,2)
                print('\t',pumbaOlek, veeTarbimine, rohuSuund,':','%.2f' %rohk,bar)
        
            kasKraanid = input("\nKas te soovite jätkata (jah/ei)? ")                                  #Second input again with a different message,if it was 'jah' the
