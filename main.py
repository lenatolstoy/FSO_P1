#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog

#MAIN

#Inicialitzem la finestra principal
finestra=Tk()
finestra.title('Cerca Fitxers redundants')

'''Creem el frame del directori font '''
fdirfont = Frame(finestra)
fdirfont.pack(side=TOP, expand=TRUE, fill=X)

#Afegim el boto per escollir el directori font
escollirdfont = Button (fdirfont, text = 'Escollir directori font')
escollirdfont.pack(side=LEFT)

#Afegim el quadre de text on apareix el directori
dfont = Label(fdirfont, text='prova1', relief="sunken")
dfont.pack(side=LEFT, expand=TRUE, fill=X)

'''Creem el frame del directori desti '''
fdirdesti = Frame(finestra)
fdirdesti.pack(side=TOP, fill=X)

#Afegim el boto per escollir el directori desti 
escollirddesti = Button (fdirdesti, text = 'Escollir directori desti')
escollirddesti.pack(side=LEFT)

#Afegim el quadre de text on apareix el directori
ddesti = Label(fdirdesti, text='prova2', relief="sunken")
ddesti.pack(side=LEFT, expand=TRUE, fill=X)

#Afegim el boto per cercar
cerca = Button (fdirdesti, text='Cerca')
cerca.pack(side=RIGHT)

finestra.mainloop()

