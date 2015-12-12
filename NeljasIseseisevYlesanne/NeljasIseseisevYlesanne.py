__author__ = 'Rene Räkk'
# -*- coding: utf-8 -*-


from tkinter import *
from turtle import *
import random


def reklaam_start(taust):
    """Closes the previous window and creates a new one for the commercial,
    also creates pictures of santa, snow and gifts.
    """
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
    """Load two pictures of clouds and return them."""
    pilve_pilt = PhotoImage(file="vihmaPilv.png")
    pilve_pilt = pilve_pilt.subsample(4, 4)
    teine_pilv = PhotoImage(file="tavalinePilv.png")
    teine_pilv = teine_pilv.subsample(7, 7)
    return pilve_pilt, teine_pilv


def loo_pilv(aken, pildi_list, mitu_pilve):
    """Create desired amount of clouds and make them move
    by calling out another function.
    """
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
    """Move clouds and create new clouds if they have moved
    out of sight.
    """
    pilv.place(x=positsioon_x, y=positsioon_y)
    if positsioon_x < 800:
        pilv.after(kiirus, liiguta_pilve, pilv, positsioon_x+1, positsioon_y, kiirus, aken, pildi_list)
    if positsioon_x == 800:
        pilv.delete("all")
        loo_pilv(aken, pildi_list, 1)


def jouluvana(aken, vana_pilt):
    """Create santa and a message, initiate a function that makes
    santa's sleigh move with a message behind him.
    """
    vana = Canvas(aken, width=90, height=70, bg="blue", highlightthickness=0)
    vana.create_image(45, 35, image=vana_pilt)
    vana.pack()
    tekst = Label(aken, text="Osta kingid tervele perele meie poest!", bg="blue")
    tekst.pack()
    vana_liikuma(vana, 650, 200, tekst)


def vana_liikuma(vana, positsioon_x, positsioon_y, tekst):
    """Make santa's sleigh move and a message move behind him."""
    vana.place(x=positsioon_x, y=positsioon_y)
    if 200 <= positsioon_x:
        tekst.place(x=positsioon_x+100, y=positsioon_y+40)
    vana.after(15, vana_liikuma, vana, positsioon_x-1, positsioon_y, tekst)


def loo_lumi(aken, lume_pilt, kingi_pilt):
    """Create new snow, gifts and make it snow by calling
    out snowing function.
    """
    lumi = Canvas(aken, bg="Blue", highlightthickness=0, width=20, height=20)
    pilt = [lume_pilt, kingi_pilt]
    pilt = random.choice(pilt)
    positsioon_x = random.randint(0, 780)
    lumi.create_image(9, 9, image=pilt)
    lumi.pack()
    lumi.after(250, loo_lumi, aken, lume_pilt, kingi_pilt)
    lumesadu(aken, lumi, positsioon_x, 120)


def lumesadu(aken, lumi, positsioon_x, positsioon_y):
    """Make it snow snowflakes and gifts."""
    lumi.place(x=positsioon_x, y=positsioon_y)
    if positsioon_y <= 520:
        lumi.after(50, lumesadu, aken, lumi, positsioon_x, positsioon_y+1)
    if 520 <= positsioon_y:
        lumi.delete("all")


def nupp_start():
    """Create a button which will start the commercial and a window,
     for the button.
     """
    taust = Tk()
    taust.title("Click me!")
    taust["bg"] = "Blue"
    button = Button(taust, text="Tasuta reklaam!", relief="raised", command=lambda:reklaam_start(taust))
    button.flash()
    button.pack()
    taust.mainloop()


nupp_start()
