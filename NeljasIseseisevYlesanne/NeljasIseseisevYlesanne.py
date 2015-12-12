__author__ = 'Rene Räkk'
# -*- coding: utf-8 -*-


from tkinter import *
from turtle import *
import time
import random


def reklaam_start():
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
    pilve_pilt = PhotoImage(file="vihmaPilv.png")
    pilve_pilt = pilve_pilt.subsample(4, 4)
    teine_pilv = PhotoImage(file="tavalinePilv.png")
    teine_pilv = teine_pilv.subsample(7, 7)
    return pilve_pilt, teine_pilv


def loo_pilv(aken, pildi_list, mitu_pilve):
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
    pilv.place(x=positsioon_x, y=positsioon_y)
    if positsioon_x < 720:
        pilv.after(kiirus, liiguta_pilve, pilv, positsioon_x+1, positsioon_y, kiirus, aken, pildi_list)
    if positsioon_x == 720:
        loo_pilv(aken, pildi_list, 1)


def jouluvana(aken, vana_pilt):
    vana = Canvas(aken, width=90, height=70, bg="blue", highlightthickness=0)
    vana.create_image(45, 35, image=vana_pilt)
    vana.pack()
    tekst = Label(aken, text="Osta kingid tervele perele meie poest!", bg="blue")
    tekst.pack()
    vana_liikuma(vana, 650, 200, tekst)


def vana_liikuma(vana, positsioon_x, positsioon_y, tekst):
    vana.place(x=positsioon_x, y=positsioon_y)
    if 200 <= positsioon_x:
        tekst.place(x=positsioon_x+100, y=positsioon_y+40)
    vana.after(15, vana_liikuma, vana, positsioon_x-1, positsioon_y, tekst)


def loo_lumi(aken, lume_pilt, kingi_pilt):
    lumi = Canvas(aken, bg="Blue", highlightthickness=0, width=20, height=20)
    pilt = [lume_pilt, kingi_pilt]
    pilt = random.choice(pilt)
    positsioon_x = random.randint(0, 780)
    lumi.create_image(9, 9, image=pilt)
    lumi.pack()
    lumi.after(250, loo_lumi, aken, lume_pilt, kingi_pilt)
    lumesadu(aken, lumi, positsioon_x, 120)


def lumesadu(aken, lumi, positsioon_x, positsioon_y):
    lumi.place(x=positsioon_x, y=positsioon_y)
    lumi.after(50, lumesadu, aken, lumi, positsioon_x, positsioon_y+1)


def nupp(aken):
    button = Button(aken, text="Tasuta reklaam!", relief="raised", command=reklaam_start)
    button.place(x=360, y=240)


def nupp_start():
    aken = Tk()
    aken.title("Click me!")
    aken.geometry("720x480")
    aken["bg"] = "Blue"
    aken.grid()
    nupp(aken)
    aken.mainloop()

reklaam_start()
