#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog
import tkMessageBox
import os
import getpass
#import FitxersIguals.py

dir_font=None
dir_desti=None


class Interficie(object): 
	def __init__(self, parent):
		self.finestra = parent
		finestra.resizable(width=False, height=False) #Fem que no es pugui canviar la mida de la finestra
		self._primeraFila()
		self._segonaFila()
		self._ultimesFiles()
		self._llistes()

#WIDGETS

	def _primeraFila(self):
		'''Creem el frame que contindra els elements de la primera fila (dir font)'''
		self.dirfont = Frame(self.finestra)
		self.dirfont.pack(side=TOP, fill=X, padx=3)
		
		#Afegim el boto per escollir el directori font
		self.boto_dirfont = Button (self.dirfont, text = 'Escolliu el directori font', command=self._obrirDirectoriFont)
		self.boto_dirfont.pack(side=LEFT)
		self.boto_dirfont.config(width = 16)

		#Afegim el quadre de text on apareix el directori
		self.txt_dirfont = Label(self.dirfont, relief="sunken")
		self.txt_dirfont.pack(side=LEFT, expand=TRUE, fill=X)

	def _segonaFila(self):
		'''Creem el frame que contindra els elements de la segona fila (dir desti) '''
		self.dirdesti = Frame(self.finestra)
		self.dirdesti.pack(side=TOP, fill=X, padx=3)

		#Afegim el boto per escollir el directori desti 
		self.b_dirdesti = Button (self.dirdesti, text = 'Escolliu directori destí', command=self._obrirDirectoriDesti)
		self.b_dirdesti.pack(side=LEFT)
		self.b_dirdesti.config(width = 16)

		#Afegim el quadre de text on apareix el directori
		self.txt_dirdesti = Label(self.dirdesti, relief="sunken")
		self.txt_dirdesti.pack(side=LEFT)
		self.txt_dirdesti.config(width=47)

		#Afegim el boto per cercar
		self.cerca = Button (self.dirdesti, text='Cerca', command=self._cercar)
		self.cerca.pack(side=RIGHT)

	def _llistes(self):
		'''Creem un frame per als elements que queden '''
		self.inferior = Frame(self.finestra)
		self.inferior.pack(side=LEFT)

		self._fitxersOriginals()
		
		''' Creem un frame per a fitxers iguals i semblants'''
		self.iguals_semblants = Frame(self.inferior)
		self.iguals_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)
		
		self._fitxersIguals()
		self._fitxersSemblants()

	def _fitxersOriginals(self): 
		'''Creem un frame per a la part de fitxers originals '''
		self.originals = Frame(self.inferior)
		self.originals.pack(side=LEFT, expand=TRUE, fill=Y, padx=8)

		#Afegim el text superior
		self.text_orig = Label(self.originals, text='Fitxers Originals:', anchor="w")
		self.text_orig.pack(side=TOP, fill=X)

		#Afegim la llista dels fitxers originals
		self.scroll_orig = Scrollbar(self.originals, orient=VERTICAL)
		self.llista_orig = Listbox(self.originals, yscrollcommand=self.scroll_orig.set, selectmode=MULTIPLE)

		self.llista_orig.pack(side=LEFT, expand=TRUE, fill=Y)
		self.llista_orig.config(width=29)

		self.scroll_orig.config(command=self.llista_orig.yview)
		self.scroll_orig.pack(side=RIGHT, fill=Y)

	def _fitxersIguals(self):
		'''#Creem un frame per als elements de fitxers iguals '''
		self.iguals = Frame(self.iguals_semblants)
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
		self.llista_iguals = Listbox(self.iguals_interior, yscrollcommand=self.scroll_iguals.set, selectmode=MULTIPLE)
		self.llista_iguals.pack(side=LEFT, expand=TRUE, fill=BOTH)
		self.scroll_iguals.config(command=self.llista_iguals.yview)
		self.llista_iguals.config(width=22)

		self._botons_iguals()

	def _botons_iguals(self):
		self.iguals_botons = Frame(self.iguals_interior)
		self.iguals_botons.pack(side=RIGHT)

		self.ig_esborra = Button(self.iguals_botons, text='Esborra')	#Boto esborra
		self.ig_esborra.pack(side=TOP, anchor="w")
		self.ig_hl = Button(self.iguals_botons, text='Hard Link') 	#Boto hard link
		self.ig_hl.pack(side=TOP, anchor="w")
		self.ig_sl = Button(self.iguals_botons, text='Soft Link') 	#Boto soft link
		self.ig_sl.pack(side=TOP, anchor="w")
		self.ig_st = Button(self.iguals_botons, text='Selec Tots') 	#Boto Seleccionar tots
		self.ig_st.bind("<Button-1>", lambda event: self._seleccionarTot(self.llista_iguals))
		self.ig_st.pack(side=TOP, anchor="w")
		self.ig_sc = Button(self.iguals_botons, text='Selec Cap') 	#Boto selecciona cap
		self.ig_sc.pack(side=TOP, anchor="w")
		self.ig_sc.bind("<Button-1>", lambda event: self._seleccionarCap(self.llista_iguals))

	def _fitxersSemblants(self):
		'''Creem un frame per als elements de fitxers semblants '''
		self.semblants = Frame(self.iguals_semblants)
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
		self.llista_semblants = Listbox(self.semblants_interior, yscrollcommand=self.scroll_semblants.set, selectmode=MULTIPLE)
		self.scroll_semblants.config(command=self.llista_semblants.yview)
		self.llista_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)

		self._botons_semblants()

	def _botons_semblants(self):
		self.semblants_botons = Frame(self.semblants_interior)
		self.semblants_botons.pack(side=RIGHT)

		self.se_compara = Button(self.semblants_botons, text='Compara') 	#Boto compara
		self.se_compara.pack(side=TOP, anchor="w")
		self.se_renombra = Button(self.semblants_botons, text='Renombra') 	#Boto renombra
		self.se_renombra.pack(side=TOP, anchor="w")
		self.se_esborra = Button(self.semblants_botons, text='Esborra') 	#Boto esborra
		self.se_esborra.pack(side=TOP, anchor="w")
		self.se_st = Button(self.semblants_botons, text='Selec Tots') 	#Boto Seleccionar tots
		self.se_st.bind("<Button-1>", lambda event: self._seleccionarTot(self.llista_semblants))
		self.se_st.pack(side=TOP, anchor="w")
		self.se_sc = Button(self.semblants_botons, text='Selec Cap') 	#Boto selecciona cap
		self.se_sc.bind("<Button-1>", lambda event: self._seleccionarCap(self.llista_semblants))
		self.se_sc.pack(side=TOP, anchor="w")

	def _ultimesFiles(self):
		'''Creem frame per als botons de sota''' 
		self.seleccionar = Frame(self.finestra)
		self.seleccionar.pack(side=BOTTOM, anchor="w")

		#Boto de sortir
		self.sortir = Button(self.seleccionar, text='Sortir', command=self._tancarFinestra)
		self.sortir.pack(side=BOTTOM, anchor="w")

		#Boto de selecciona tots
		self.selec_tots = Button(self.seleccionar, text = 'Selecciona Tots')
		self.selec_tots.bind("<Button-1>", lambda event: self._seleccionarTot(self.llista_orig))
		self.selec_tots.pack(side=LEFT)

		#Boto de selecciona cap
		self.selec_cap = Button(self.seleccionar, text = 'Selecciona Cap')
		self.selec_cap.bind("<Button-1>", lambda event: self._seleccionarCap(self.llista_orig))
		self.selec_cap.pack(side=LEFT)

	
#COMANDES

	def _obrirDirectoriFont(self):
		global dir_font		
		dir_font = tkFileDialog.askdirectory(initialdir='/home/%s' %getpass.getuser(), title='Escolliu un directori font')
		self.txt_dirfont.config(text=dir_font)

	def _obrirDirectoriDesti(self):
		global dir_desti		
		dir_desti = tkFileDialog.askdirectory(initialdir='/home/%s' %getpass.getuser(), title='Escolliu un directori destí')
		self.txt_dirdesti.config(text=dir_desti)
		
	def _tancarFinestra(self):
		self.finestra.destroy()	

	def _cercar(self):	
		if(dir_font==None or dir_desti==None):
			self.error = tkMessageBox.showerror("Error","S'han d'escollir els dos directoris")
		elif(dir_font==dir_desti):
			self.error = tkMessageBox.showerror("Error", "El directori font i el directori destí no poden ser el mateix")
		else:	
			lista = ['holi', 'holi2', 'dw']
			self._afegirFitxers(self.llista_orig, lista)
			lista1 = ['a','b','c','d']
			self._afegirFitxers(self.llista_iguals, lista1)
			lista2 = ['1','2','3','4']
			self._afegirFitxers(self.llista_semblants, lista2)

	def _afegirFitxers(self, llista, fitxers):
		i=0		
		for f in fitxers:
			llista.insert(i, f)
			i+=1

	def _seleccionarTot(event, llista):
		llista.select_set(0,END)

	def _seleccionarCap(event, llista):
		llista.selection_clear(0,END)

if __name__ == '__main__':
    finestra = Tk()
    finestra.title("Cerca Fitxers Redundants")
    app = Interficie(finestra)
    finestra.mainloop()


