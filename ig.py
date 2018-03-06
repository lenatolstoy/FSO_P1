#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog

class PrimeraFila(Frame):
	def __init__(self, finestra):
		'''Creem el frame que contindra els elements de la primera fila (dir font)'''
		self.dirfont = Frame(finestra)
		self.dirfont.pack(side=TOP, fill=X, padx=3)
		#Afegim el boto per escollir el directori font
		self.boto_dirfont = Button (self.dirfont, text = 'Esculli el directori font', command=self.obrir_directori)
		self.boto_dirfont.pack(side=LEFT)
		self.boto_dirfont.config(width = 16)
		#Afegim el quadre de text on apareix el directori
		self.text_dirfont = Label(self.dirfont, text='prova1', relief="sunken")
		self.text_dirfont.pack(side=LEFT, expand=TRUE, fill=X)
	
	def obrir_directori(self):
		self.directory = tkFileDialog.askdirectory(title='Esculli un directori font')		

class SegonaFila(Frame):
	def __init__(self, finestra):
		'''Creem el frame que contindra els elements de la segona fila (dir desti) '''
		self.dirdesti = Frame(finestra)
		self.dirdesti.pack(side=TOP, fill=X, padx=3)
		#Afegim el boto per escollir el directori desti 
		self.boto_dirdesti = Button (self.dirdesti, text = 'Escolliu directori destí', command=self.obrir_directori)
		self.boto_dirdesti.pack(side=LEFT)
		self.boto_dirdesti.config(width = 16)
		#Afegim el quadre de text on apareix el directori
		self.text_dirdesti = Label(self.dirdesti, text='prova2', relief="sunken")
		self.text_dirdesti.pack(side=LEFT)
		self.text_dirdesti.config(width=47)
		#Afegim el boto per cercar
		self.cerca = Button (self.dirdesti, text='Cerca')
		self.cerca.pack(side=RIGHT)

	def obrir_directori(self):
		self.directory = tkFileDialog.askdirectory(title='Esculli un directori destí')

class Llistes(Frame):
	def __init__(self, finestra):
		'''Creem un frame per als elements que queden '''
		self.inferior = Frame(finestra)
		self.inferior.pack(side=LEFT)

		self.fitx_originals = FitxersOriginals(self.inferior)
		
		'''Creem un frame per a fitxers iguals i semblants'''
		self.iguals_semblants = Frame(self.inferior)
		self.iguals_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)
		
		self.fitx_iguals = FitxersIguals(self.iguals_semblants)
		self.fitx_semblants = FitxersSemblants(self.iguals_semblants)

class FitxersOriginals(Frame):
	def __init__(self, finestra): 
		'''Creem un frame per a la part de fitxers originals '''
		self.originals = Frame(finestra)
		self.originals.pack(side=LEFT, expand=TRUE, fill=Y, padx=8)
		#Afegim el text superior
		self.text_orig = Label(self.originals, text='Fitxers Originals:', anchor="w")
		self.text_orig.pack(side=TOP, fill=X)
		#Afegim la llista dels fitxers originals
		self.scroll_orig = Scrollbar(self.originals, orient=VERTICAL)
		self.llista_orig = Listbox(self.originals, yscrollcommand=self.scroll_orig.set)

		self.llista_orig.pack(side=LEFT, expand=TRUE, fill=Y)
		self.llista_orig.config(width=29)

		self.scroll_orig.config(command=self.llista_orig.yview)
		self.scroll_orig.pack(side=RIGHT, fill=Y)

class FitxersIguals(Frame):
	def __init__(self, finestra):
		'''Creem un frame per als elements de fitxers iguals '''
		self.iguals = Frame(finestra)
		self.iguals.pack(side=TOP, expand=TRUE, fill=BOTH)
		#Afegim text superior
		self.text_iguals = Label(self.iguals, text='Fitxers Iguals:', anchor="w")
		self.text_iguals.pack(side=TOP, expand=TRUE, fill=X, padx=11)
		#Creem un frame per a afegir la llista de fitxers iguals i els seus botons
		self.iguals_interior = Frame(self.iguals)
		self.iguals_interior.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
		#Afegim la llista dels fitxers iguals
		self.scroll_iguals = Scrollbar(self.iguals_interior, orient=VERTICAL)
		self.scroll_iguals.pack(side=LEFT, fill=Y)
		self.llista_iguals = Listbox(self.iguals_interior, yscrollcommand=self.scroll_iguals.set)
		self.llista_iguals.pack(side=LEFT, expand=TRUE, fill=BOTH)
		self.scroll_iguals.config(command=self.llista_iguals.yview)
		self.llista_iguals.config(width=22)

		self.botons_iguals()

	def botons_iguals(self):
		self.iguals_botons = Frame(self.iguals_interior)
		self.iguals_botons.pack(side=RIGHT)

		self.ig_esborra = Button(self.iguals_botons, text='Esborra')	#Boto esborra
		self.ig_esborra.pack(side=TOP, anchor="w")
		self.ig_hl = Button(self.iguals_botons, text='Hard Link') 	#Boto hard link
		self.ig_hl.pack(side=TOP, anchor="w")
		self.ig_sl = Button(self.iguals_botons, text='Soft Link') 	#Boto soft link
		self.ig_sl.pack(side=TOP, anchor="w")
		self.ig_st = Button(self.iguals_botons, text='Selec Tots') 	#Boto Seleccionar tots
		self.ig_st.pack(side=TOP, anchor="w")
		self.ig_sc = Button(self.iguals_botons, text='Selec Cap') 	#Boto selecciona cap
		self.ig_sc.pack(side=TOP, anchor="w")

class FitxersSemblants(Frame): 
	def __init__(self, finestra):
		'''Creem un frame per als elements de fitxers semblants '''
		self.semblants = Frame(finestra)
		self.semblants.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
		#Afegim text superior
		self.text_semblants = Label(self.semblants, text='Fitxers Semblants:', anchor="w")
		self.text_semblants.pack(side=TOP, expand=TRUE, fill=X, padx=11)
		#Creem un frame per a afegir la llista de fitxers iguals i els seus botons
		self.semblants_interior = Frame(self.semblants)
		self.semblants_interior.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
		#Afegim la llista dels fitxers iguals
		self.scroll_semblants = Scrollbar(self.semblants_interior, orient=VERTICAL)
		self.scroll_semblants.pack(side=LEFT, fill=Y)
		self.llista_semblants = Listbox(self.semblants_interior, yscrollcommand=self.scroll_semblants.set)
		self.scroll_semblants.config(command=self.llista_semblants.yview)
		self.llista_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)

		self.botons_semblants()


	def botons_semblants(self):
		self.semblants_botons = Frame(self.semblants_interior)
		self.semblants_botons.pack(side=RIGHT)

		self.se_compara = Button(self.semblants_botons, text='Compara') 	#Boto compara
		self.se_compara.pack(side=TOP, anchor="w")
		self.se_renombra = Button(self.semblants_botons, text='Renombra') 	#Boto renombra
		self.se_renombra.pack(side=TOP, anchor="w")
		self.se_esborra = Button(self.semblants_botons, text='Esborra') 	#Boto esborra
		self.se_esborra.pack(side=TOP, anchor="w")
		self.se_st = Button(self.semblants_botons, text='Selec Tots') 	#Boto Seleccionar tots
		self.se_st.pack(side=TOP, anchor="w")
		self.se_sc = Button(self.semblants_botons, text='Selec Cap') 	#Boto selecciona cap
		self.se_sc.pack(side=TOP, anchor="w")

class UltimesFiles(Frame):
	def __init__(self, finestra):
		'''Creem frame per als botons de sota '''
		self.seleccionar = Frame(finestra)
		self.seleccionar.pack(side=BOTTOM, anchor="w")
		#Boto de sortir
		self.sortir = Button(self.seleccionar, text='Sortir', command=self.tancar_finestra)
		self.sortir.pack(side=BOTTOM, anchor="w")
		#Boto de selecciona tots
		self.selec_tots = Button(self.seleccionar, text = 'Selecciona Tots')
		self.selec_tots.pack(side=LEFT)
		#Boto de selecciona cap
		self.selec_cap = Button(self.seleccionar, text = 'Selecciona Cap')
		self.selec_cap.pack(side=LEFT)
	
	def tancar_finestra(self):
		finestra.destroy()


class Interficie(object): 
	def __init__(self, parent):
		self.finestra = parent
		finestra.resizable(width=False, height=False) #Fem que no es pugui canviar la mida de la finestra
		
		self.primera_fila = PrimeraFila(self.finestra)
		self.segona_fila = SegonaFila(self.finestra)
		self.ultimes_files = UltimesFiles(self.finestra)
		self.llistes = Llistes(self.finestra)
		

		
	

if __name__ == '__main__':
    finestra = Tk()
    finestra.title = ('Cerca Fitxers Redundants')
    app = Interficie(finestra)
    finestra.mainloop()


