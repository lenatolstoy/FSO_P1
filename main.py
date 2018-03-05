#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog

#MAIN

#Inicialitzem la finestra principal
finestra=Tk()
finestra.title('Cerca Fitxers redundants')

'''Creem el frame del directori font '''
dirfont = Frame(finestra)
dirfont.pack(side=TOP, fill=X, padx=4)

#Afegim el boto per escollir el directori font
boto_dirfont = Button (dirfont, text = 'Escolliu directori font')
boto_dirfont.pack(side=LEFT)
boto_dirfont.config(width = 17)

#Afegim el quadre de text on apareix el directori
text_dirfont = Label(dirfont, text='prova1', relief="sunken")
text_dirfont.pack(side=LEFT, expand=TRUE, fill=X)

'''Creem el frame del directori desti '''
dirdesti = Frame(finestra)
dirdesti.pack(side=TOP, fill=X, padx=4)

#Afegim el boto per escollir el directori desti 
boto_dirdesti = Button (dirdesti, text = 'Escolliu directori desti')
boto_dirdesti.pack(side=LEFT)
boto_dirdesti.config(width = 17)

#Afegim el quadre de text on apareix el directori
text_dirdesti = Label(dirdesti, text='prova2', relief="sunken")
text_dirdesti.pack(side=LEFT, expand=TRUE, fill=X)

#Afegim el boto per cercar
cerca = Button (dirdesti, text='Cerca')
cerca.pack(side=RIGHT)

'''Creem frame general per a tots els elements de fitxers '''
fitxers = Frame(finestra)
fitxers.pack(side=TOP, expand=TRUE, fill=BOTH)

'''Creem un frame per a la part de fitxers originals '''
originals = Frame(fitxers)
originals.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=8)

#Afegim el text superior
text_orig = Label(originals, text='Fitxers Originals:', anchor="w")
text_orig.pack(side=TOP, expand=TRUE, fill=X)

#Afegim la llista dels fitxers originals
scroll_orig = Scrollbar(originals, orient=VERTICAL)
llista_orig = Listbox(originals, yscrollcommand=scroll_orig.set)
llista_orig.pack(side=LEFT, expand=TRUE, fill=BOTH)
scroll_orig.config(command=llista_orig.yview)
scroll_orig.pack(side=RIGHT, fill=Y)

'''Creem un frame per a fitxers iguals i semblants'''
iguals_semblants = Frame(fitxers)
iguals_semblants.pack(side=RIGHT, expand=TRUE, fill=BOTH)

'''Creem un frame per als elements de fitxers iguals '''
iguals = Frame(iguals_semblants)
iguals.pack(side=TOP, expand=TRUE, fill=BOTH)

#Afegim text superior
text_iguals = Label(iguals, text='Fitxers Iguals:', anchor="w")
text_iguals.pack(side=TOP, expand=TRUE, fill=X)

#Creem un frame per a afegir la llista de fitxers iguals i els seus botons
iguals_interior = Frame(iguals)
iguals_interior.pack(side=BOTTOM, expand=TRUE, fill=BOTH)

#Afegim la llista dels fitxers iguals
scroll_iguals = Scrollbar(iguals_interior, orient=VERTICAL)
scroll_iguals.pack(side=LEFT, fill=Y)
llista_iguals = Listbox(iguals_interior, yscrollcommand=scroll_iguals.set)
llista_iguals.pack(side=LEFT, expand=TRUE, fill=BOTH)
scroll_iguals.config(command=llista_iguals.yview)

#Afegim els botons dels fitxers originals (amb un frame nou)
iguals_botons = Frame(iguals_interior)
iguals_botons.pack(side=RIGHT)

ig_esborra = Button(iguals_botons, text='Esborra') #Boto esborra
ig_esborra.pack(side=TOP, anchor="w")

ig_hl = Button(iguals_botons, text='Hard Link') #Boto hard link
ig_hl.pack(side=TOP, anchor="w")

ig_sl = Button(iguals_botons, text='Soft Link') #Boto soft link
ig_sl.pack(side=TOP, anchor="w")

ig_st = Button(iguals_botons, text='Selec Tots') #Boto Seleccionar tots
ig_st.pack(side=TOP, anchor="w")

ig_sc = Button(iguals_botons, text='Selec Cap') #Boto selecciona
ig_sc.pack(side=TOP, anchor="w")


finestra.mainloop()

