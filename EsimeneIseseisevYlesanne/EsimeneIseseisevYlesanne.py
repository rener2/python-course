rohk =1.65
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
