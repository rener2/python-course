__author__ = 'Rene Räkk'
# -*- coding: utf-8 -*-


from tkinter import *
from turtle import *
import random


def reklaam_start(taust):
    """Sulgeb eelmise akna, loob ühtlasi ka uue akna,
    milles reklaam käivitub ja loob ka jõuluvana, lume ja kingi pildid"""
    taust.destroy()
    aken = Tk()
    aken.title("Reklaam")
    aken.geometry("720x480")
    aken["bg"] = "Blue"
    vana_pilt = PhotoImage(file="jouluvana_saanis.png")
    vana_pilt = vana_pilt.subsample(4, 4)
    lume_pilt = PhotoImage(file="snowflake.png")
    lume_pilt = lume_pilt.subsample(25, 25)
    kingi_pilt = PhotoImage(file="gift.png")
    kingi_pilt = kingi_pilt.subsample(15, 15)
    aken.grid()
    pilve_list = pilve_pildid()
    loo_pilv(aken, pilve_list, 7)
    jouluvana(aken, vana_pilt)
    loo_lumi(aken, lume_pilt, kingi_pilt)
    aken.mainloop()


def pilve_pildid():
    """Laeb alla kaks erinevat pildi pilvede jaoks ja väljastab need pildid"""
    pilve_pilt = PhotoImage(file="vihmaPilv.png")
    pilve_pilt = pilve_pilt.subsample(4, 4)
    teine_pilv = PhotoImage(file="tavalinePilv.png")
    teine_pilv = teine_pilv.subsample(7, 7)
    return pilve_pilt, teine_pilv


def loo_pilv(aken, pildi_list, mitu_pilve):
    """Loob soovitud arvu pilvi ja lõpus käivitab pilvede
    liikuma panemiseks vastava funktsiooni"""
    arv = 0
    pilve_koht_x = 0
    while mitu_pilve != arv:
        kiirus = 30
        pilt = random.choice(pildi_list)
        pilv = Canvas(aken, width=100, height=55, bg="blue", highlightthickness=0)
        pilv.create_image(50, 30, image=pilt)
        pilv.place(x=pilve_koht_x, y=0)
        pilv.pack()
        pilve_koht_y = random.randint(0, 85)
        liiguta_pilve(pilv, pilve_koht_x, pilve_koht_y, kiirus, aken, pildi_list)
        pilve_koht_x += 100
        arv += 1


def liiguta_pilve(pilv, positsioon_x, positsioon_y, kiirus, aken, pildi_list):
    """Liigutab pilvi vasakult paremale ja kui pilv kaob vaateväljast
    siis käivitab uue pilve loomise funktsiooni"""
    pilv.place(x=positsioon_x, y=positsioon_y)
    if positsioon_x < 800:
        pilv.after(kiirus, liiguta_pilve, pilv, positsioon_x+1, positsioon_y, kiirus, aken, pildi_list)
    if positsioon_x == 800:
        pilv.delete("all")
        loo_pilv(aken, pildi_list, 1)


def jouluvana(aken, vana_pilt):
    """Loob jõuluvana ja teksti, mida jõuluvana hiljem saaniga veab,
    ühtlasi käivitab ka fukntsiooni, mis jõuluvana liikuma paneb tekstiga"""
    vana = Canvas(aken, width=90, height=70, bg="blue", highlightthickness=0)
    vana.create_image(45, 35, image=vana_pilt)
    vana.pack()
    tekst = Label(aken, text="Osta kingid tervele perele meie poest!", bg="blue")
    tekst.pack()
    vana_liikuma(vana, 650, 200, tekst)


def vana_liikuma(vana, positsioon_x, positsioon_y, tekst):
    """Paneb jõuluvana saaniga liikuma ja teksti lohistama tema taga"""
    vana.place(x=positsioon_x, y=positsioon_y)
    if 200 <= positsioon_x:
        tekst.place(x=positsioon_x+100, y=positsioon_y+40)
    vana.after(15, vana_liikuma, vana, positsioon_x-1, positsioon_y, tekst)


def loo_lumi(aken, lume_pilt, kingi_pilt):
    """Loob lume helbeid ja käivitab lumesaju funktsiooni"""
    lumi = Canvas(aken, bg="Blue", highlightthickness=0, width=20, height=20)
    pilt = [lume_pilt, kingi_pilt]
    pilt = random.choice(pilt)
    positsioon_x = random.randint(0, 780)
    lumi.create_image(9, 9, image=pilt)
    lumi.pack()
    lumi.after(250, loo_lumi, aken, lume_pilt, kingi_pilt)
    lumesadu(aken, lumi, positsioon_x, 120)


def lumesadu(aken, lumi, positsioon_x, positsioon_y):
    """Paneb lume sadama"""
    lumi.place(x=positsioon_x, y=positsioon_y)
    if positsioon_y <= 520:
        lumi.after(50, lumesadu, aken, lumi, positsioon_x, positsioon_y+1)
    if 520 <= positsioon_y:
        lumi.delete("all")


def nupp_start():
    """Loob nupu ja akna, millest saab käivitada reklaami"""
    taust = Tk()
    taust.title("Click me!")
    taust["bg"] = "Blue"
    button = Button(taust, text="Tasuta reklaam!", relief="raised", command=lambda:reklaam_start(taust))
    button.flash()
    button.pack()
    taust.mainloop()


nupp_start()
