import random                                                                                           #Importing random module for later use 

sisend1 = input("Süsteem on ülesse seatud - kas käivitada süsteem (jah/ei)? ")                     #First input
                                                                                                        
if sisend1 == "ei":                                                                                #Depending on the input (jah/ei) the program will either
    print("Süsteemi ei võeta tööle!")                                                                   #continue or shut down               
rohk = 1.80                             
if sisend1 == "jah":                
    print('''                           
\tSüvaveepump käivitus! 
\t\tHüdrofoorirõhk: ''')                                                                                    #If first input was 'jah', then program the continues and
    while rohk<=2.75 and rohk<=2.85:                                                                    #displays pressure change in hydrophore until it reaches
        if rohk == 1.80:print('\t\t\t%.2f' %rohk , str('bar'))                                                #maximum pressure(2.8 +/-0.05)
        rohk += 0.15                                                                                     
        print('\t\t\t%.2f' %rohk , str('bar'))                                                                
        
    print('\tSüvaveepump seiskus!\n')    
    rohk='%.2f' %rohk                                                                                   #2 digits after decimal point                                                                  
    rohk = float(rohk)                                                                                  #Float value to rohk again
    sisend2 = input('Kas keerata kraanid lahti (jah/ei)? ')                                    #Second input
    if sisend2 == 'ei':                                                                            #If 'ei' program quits and prints a message
        print('Kraane lahti ei keeratud.')
    elif sisend2 == 'jah':                                                                         #if 'jah' then program goes into a while loop
        while sisend2 == 'jah':                                                                    #and loop lasts as long as the input is 'jah'                                                                                             
            
            if 2.75 <= rohk <= 2.85:pumbaOlek= '[Seisab]'                                               #state of tthe water pump, depending on the level of
            elif 1.75 <= rohk <= 1.85:pumbaOlek= '[Töötab]'                                               #pressure inside the hydrophore
            bar = str('bar')                                                                            
            
          
            while pumbaOlek == '[Seisab]' and 1.80 <= rohk:                                                            #displays log if water pump isn't working and while
                veeTarbimine= random.choice(('[Tarbitakse]', '[Ei tarbita]')) #chooses random value every iteration    #pressure is over 1.80 bar
                if veeTarbimine=='[Tarbitakse]':rohuSuund = '[Alaneb]'
                if veeTarbimine== '[Tarbitakse]'and 1.80<=rohk: rohk -= 0.05
                rohk = round(rohk,2)
                if veeTarbimine== '[Ei tarbita]':rohuSuund = '[Seisab]'
                print('\t',pumbaOlek, veeTarbimine, rohuSuund,'%.2f' %rohk,bar,)                                             
                #would add time.sleep(1) here and into the other loop, but since it is a simulation, it is not necessary
               
            while pumbaOlek == '[Töötab]' and rohk<= 2.75:              
                veeTarbimine = random.choice(('[Tarbitakse]', '[Ei tarbita]'))
                rohuSuund = '[Tõuseb]'                                                          
                if veeTarbimine== '[Ei tarbita]' and rohk <= 2.70 : rohk += 0.15                                                         
                if veeTarbimine== '[Tarbitakse]'and rohk <= 2.75: rohk += 0.10    
                rohk = round(rohk,2)
                print('\t',pumbaOlek, veeTarbimine, rohuSuund,'%.2f' %rohk,bar)
                
                

                            
            sisend2 = input("\nKas te soovite jätkata(jah/ei)?")                                  #Second input again with a different message,if it was 'jah' the
            if sisend2=="jah":print("") 
            elif sisend2 == str("ei"):                                                                    #first time
                print("Süsteem suleti!")
              
