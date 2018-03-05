#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog

#Inicialitzem la finestra principal
self.finestra=Tk()
self.finestra.title('Cerca Fitxers Redundants')
self.finestra.resizable(width=False, height=False) #Fem que no es pugui canviar la seva mida
'''Creem el frame del directori font '''
dirfont = Frame(finestra)
dirfont.pack(side=TOP, fill=X, padx=3)
#Afegim el boto per escollir el directori font
boto_dirfont = Button (dirfont, text = 'Escolliu directori font')
boto_dirfont.pack(side=LEFT)
boto_dirfont.config(width = 16)
#Afegim el quadre de text on apareix el directori
text_dirfont = Label(dirfont, text='prova1', relief="sunken")
text_dirfont.pack(side=LEFT, expand=TRUE, fill=X)

'''Creem el frame del directori desti '''
dirdesti = Frame(finestra)
dirdesti.pack(side=TOP, fill=X, padx=3)
#Afegim el boto per escollir el directori desti 
boto_dirdesti = Button (dirdesti, text = 'Escolliu directori destí')
boto_dirdesti.pack(side=LEFT)
boto_dirdesti.config(width = 16)
#Afegim el quadre de text on apareix el directori
text_dirdesti = Label(dirdesti, text='prova2', relief="sunken")
text_dirdesti.pack(side=LEFT)
text_dirdesti.config(width=47)
#Afegim el boto per cercar
cerca = Button (dirdesti, text='Cerca')
cerca.pack(side=RIGHT)


'''Creem un frame per als elements que queden '''
inferior = Frame(finestra)
inferior.pack(side=LEFT)

'''Creem frame per als botons de sota '''
seleccionar = Frame(inferior)
seleccionar.pack(side=BOTTOM, anchor="w")
#Boto de sortir
sortir = Button(seleccionar, text='Sortir')
sortir.pack(side=BOTTOM, anchor="w")
#Boto de selecciona tots
selec_tots = Button(seleccionar, text = 'Selecciona Tots')
selec_tots.pack(side=LEFT)
#Boto de selecciona cap
selec_cap = Button(seleccionar, text = 'Selecciona Cap')
selec_cap.pack(side=LEFT)

'''Creem un frame per a la part de fitxers originals '''
originals = Frame(inferior)
originals.pack(side=LEFT, expand=TRUE, fill=Y, padx=8)
#Afegim el text superior
text_orig = Label(originals, text='Fitxers Originals:', anchor="w")
text_orig.pack(side=TOP, fill=X)
#Afegim la llista dels fitxers originals
scroll_orig = Scrollbar(originals, orient=VERTICAL)
llista_orig = Listbox(originals, yscrollcommand=scroll_orig.set)

llista_orig.pack(side=LEFT, expand=TRUE, fill=Y)
llista_orig.config(width=29)

scroll_orig.config(command=llista_orig.yview)
scroll_orig.pack(side=RIGHT, fill=Y)


'''Creem un frame per a fitxers iguals i semblants'''
iguals_semblants = Frame(inferior)
iguals_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)

'''Creem un frame per als elements de fitxers iguals '''
iguals = Frame(iguals_semblants)
iguals.pack(side=TOP, expand=TRUE, fill=BOTH)
#Afegim text superior
text_iguals = Label(iguals, text='Fitxers Iguals:', anchor="w")
text_iguals.pack(side=TOP, expand=TRUE, fill=X, padx=11)
#Creem un frame per a afegir la llista de fitxers iguals i els seus botons
iguals_interior = Frame(iguals)
iguals_interior.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
#Afegim la llista dels fitxers iguals
scroll_iguals = Scrollbar(iguals_interior, orient=VERTICAL)
scroll_iguals.pack(side=LEFT, fill=Y)
llista_iguals = Listbox(iguals_interior, yscrollcommand=scroll_iguals.set)
llista_iguals.pack(side=LEFT, expand=TRUE, fill=BOTH)
scroll_iguals.config(command=llista_iguals.yview)
llista_iguals.config(width=22)
#Afegim els botons dels fitxers originals (amb un frame nou)
iguals_botons = Frame(iguals_interior)
iguals_botons.pack(side=RIGHT)

ig_esborra = Button(iguals_botons, text='Esborra')	#Boto esborra
ig_esborra.pack(side=TOP, anchor="w")
ig_hl = Button(iguals_botons, text='Hard Link') 	#Boto hard link
ig_hl.pack(side=TOP, anchor="w")
ig_sl = Button(iguals_botons, text='Soft Link') 	#Boto soft link
ig_sl.pack(side=TOP, anchor="w")
ig_st = Button(iguals_botons, text='Selec Tots') 	#Boto Seleccionar tots
ig_st.pack(side=TOP, anchor="w")
ig_sc = Button(iguals_botons, text='Selec Cap') 	#Boto selecciona cap
ig_sc.pack(side=TOP, anchor="w")

'''Creem un frame per als elements de fitxers semblants '''
semblants = Frame(iguals_semblants)
semblants.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
#Afegim text superior
text_semblants = Label(semblants, text='Fitxers Semblants:', anchor="w")
text_semblants.pack(side=TOP, expand=TRUE, fill=X, padx=11)
#Creem un frame per a afegir la llista de fitxers iguals i els seus botons
semblants_interior = Frame(semblants)
semblants_interior.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
#Afegim la llista dels fitxers iguals
scroll_semblants = Scrollbar(semblants_interior, orient=VERTICAL)
scroll_semblants.pack(side=LEFT, fill=Y)
llista_semblants = Listbox(semblants_interior, yscrollcommand=scroll_iguals.set)
scroll_semblants.config(command=llista_semblants.yview)
llista_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)
#Afegim els botons dels fitxers originals (amb un frame nou)
semblants_botons = Frame(semblants_interior)
semblants_botons.pack(side=RIGHT)

se_compara = Button(semblants_botons, text='Compara') 	#Boto compara
se_compara.pack(side=TOP, anchor="w")
se_renombra = Button(semblants_botons, text='Renombra') #Boto renombra
se_renombra.pack(side=TOP, anchor="w")
se_esborra = Button(semblants_botons, text='Esborra') 	#Boto esborra
se_esborra.pack(side=TOP, anchor="w")
se_st = Button(semblants_botons, text='Selec Tots') 	#Boto Seleccionar tots
se_st.pack(side=TOP, anchor="w")
se_sc = Button(semblants_botons, text='Selec Cap') 	#Boto selecciona cap
se_sc.pack(side=TOP, anchor="w")



