#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog
import os
import getpass
import Exceptions as ex
import Funcions as funct
#import FitxersIguals

dir_font=None
dir_desti=None


class Interficie(object):

	# Inicialització de la interfície gràfica. S'inicialitzen 4 blocs 
	# de manera separada: la primera fila de la IG, la segona fila, les 
	# últimes files i la part central on trobem totes les llistes de fitxers.
	def __init__(self, parent):
		self.finestra = parent
		finestra.resizable(width=False, height=False) #Fem que no es pugui canviar la mida de la finestra
		self._primeraFila()
		self._segonaFila()
		self._ultimesFiles()
		self._llistes()


	'''--------------------------------------------------------------------

	Inicialització, col.locació i assignació d'events de tots els widgets de la IG

	--------------------------------------------------------------------'''

	# Creació de la primera fila que trobem a la IG, on es pot seleccionar
	# el directori font. 
	def _primeraFila(self):
		self.dirfont = Frame(self.finestra)
		self.dirfont.pack(side=TOP, fill=X, padx=3)
		
		#Afegim el boto per escollir el directori font
		self.boto_dirfont = Button (self.dirfont, text = 'Escolliu el directori font', command=self._obrirDirectoriFont)
		self.boto_dirfont.pack(side=LEFT)
		self.boto_dirfont.config(width = 16)

		#Afegim el quadre de text on apareix el directori
		self.txt_dirfont = Label(self.dirfont, relief="sunken")
		self.txt_dirfont.pack(side=LEFT, expand=TRUE, fill=X)


	# Creació de la segona fila de la IG, on es permet a l'usuari
	# cercar un directori destí i fer una cerca als dos directoris.
	def _segonaFila(self):
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


	# Inicialitzem la part central de la IG, on hi ha les llistes
	# de fitxers i els botons de la llista de fitxers iguals i semblants.
	def _llistes(self):
		#Creem un frame per a totes les llistes
		self.centre = Frame(self.finestra)
		self.centre.pack(side=LEFT)

		self._fitxersOriginals()	#Creem la llista de fitxers originals
		
		#Creem un frame per a fitxers iguals i semblants
		self.iguals_semblants = Frame(self.centre)
		self.iguals_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)
		
		self._fitxersIguals()		#Creem la llista de fitxers iguals
		self._fitxersSemblants()	#Creem la llista de fitxers semblants


	# Creem una listbox per als fitxers originals amb la seva
	# scrollbar i un títol a la part superior per a fer saber
	# a l'usuari que conté aquest contenidor.
	def _fitxersOriginals(self): 
		#Creem un frame per a la part de fitxers originals
		self.originals = Frame(self.centre)
		self.originals.pack(side=LEFT, expand=TRUE, fill=Y, padx=8)

		#Afegim el text superior
		self.text_orig = Label(self.originals, text='Fitxers Originals:', anchor="w")
		self.text_orig.pack(side=TOP, fill=X)

		#Afegim la llista dels fitxers originals
		self.scroll_orig = Scrollbar(self.originals, orient=VERTICAL)	#Inicialitzem la scrollbar
		self.llista_orig = Listbox(self.originals, yscrollcommand=self.scroll_orig.set, selectmode=MULTIPLE)
		self.llista_orig.bind("<<ListboxSelect>>", lambda event: self._detectarSeleccio())
	
		self.llista_orig.pack(side=LEFT, expand=TRUE, fill=Y)
		self.llista_orig.config(width=29)

		self.scroll_orig.config(command=self.llista_orig.yview)
		self.scroll_orig.pack(side=RIGHT, fill=Y)


	# Creem una listbox per als fitxers iguals amb la seva
	# scrollbar i un títol a la part superior per a fer saber
	# a l'usuari que conté aquest contenidor. A més creem els
	# botons laterals.
	def _fitxersIguals(self):
		#Creem un frame per als elements de fitxers iguals 
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

		self._botons_iguals()	#Creem els botons dels fitxers iguals

	# Inicialitzem els botons que trobem al lateral de la listbox
	# de fitxers iguals.
	def _botons_iguals(self):
		self.iguals_botons = Frame(self.iguals_interior)
		self.iguals_botons.pack(side=RIGHT)

		self.ig_esborra = Button(self.iguals_botons, text='Esborra', command = lambda: self._esborrarFitxers(self.llista_iguals))	#Boto esborra
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


	# Creem una listbox per als fitxers semblants amb la seva
	# scrollbar i un títol a la part superior per a fer saber
	# a l'usuari que conté aquest contenidor. A més creem els
	# botons laterals.
	def _fitxersSemblants(self):
		#Creem un frame per als elements de fitxers semblants
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

	# Inicialitzem els botons que trobem al lateral de la listbox
	# de fitxers semblants.
	def _botons_semblants(self):
		self.semblants_botons = Frame(self.semblants_interior)
		self.semblants_botons.pack(side=RIGHT)

		self.se_compara = Button(self.semblants_botons, text='Compara') 	#Boto compara
		self.se_compara.pack(side=TOP, anchor="w")

		self.se_renombra = Button(self.semblants_botons, text='Renombra') 	#Boto renombra
		self.se_renombra.pack(side=TOP, anchor="w")

		self.se_esborra = Button(self.semblants_botons, text='Esborra', command = lambda: self._esborrarFitxers(self.llista_semblants)) 	#Boto esborra
		self.se_esborra.pack(side=TOP, anchor="w")

		self.se_st = Button(self.semblants_botons, text='Selec Tots') 	#Boto Seleccionar tots
		self.se_st.bind("<Button-1>", lambda event: self._seleccionarTot(self.llista_semblants))
		self.se_st.pack(side=TOP, anchor="w")

		self.se_sc = Button(self.semblants_botons, text='Selec Cap') 	#Boto selecciona cap
		self.se_sc.bind("<Button-1>", lambda event: self._seleccionarCap(self.llista_semblants))
		self.se_sc.pack(side=TOP, anchor="w")


	# Afegim els botons finals, els de selecciona tots i selecciona
	# cap fan referència a la listbox de fitxers originals.
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

	
	'''--------------------------------------------------------------------

	Implementació de tots els events

	--------------------------------------------------------------------'''
	# Al fer clic en el botó d'escollir directori font, obrim
	# un tkFileDialog i emmagatzemem el path a dir_font.
	def _obrirDirectoriFont(self):
		global dir_font		
		dir_font = tkFileDialog.askdirectory(initialdir='/home/%s' %getpass.getuser(), title='Escolliu un directori font')
		self.txt_dirfont.config(text=dir_font)
		self._eliminarTotsFitxersLlista(self.llista_orig)		#Si canviem de directori eliminarem la llista 
		self._eliminarTotsFitxersLlista(self.llista_iguals)		# de fitxers que hi havia anteriorment
		self._eliminarTotsFitxersLlista(self.llista_semblants) 	


	# Al fer clic en el botó d'escollir directori destí, obrim
	# un tkFileDialog.
	def _obrirDirectoriDesti(self):
		global dir_desti		
		dir_desti = tkFileDialog.askdirectory(initialdir='/home/%s' %getpass.getuser(), title='Escolliu un directori destí')
		self.txt_dirdesti.config(text=dir_desti)
		self._eliminarTotsFitxersLlista(self.llista_orig)		#Si canviem de directori eliminarem la llista 
		self._eliminarTotsFitxersLlista(self.llista_iguals)	# de fitxers que hi havia anteriorment
		self._eliminarTotsFitxersLlista(self.llista_semblants) 	
		
	# Funcionalitat per al botó sortir.
	def _tancarFinestra(self):
		self.finestra.destroy()	


	# Funció que crida a les funcions llistaFitxersOriginals,
	# llistaFitxersIguals i llistaFitxersSemblants del fitxer FitxersIguals.
	# També comprova que els directoris tinguin emmagatzemada alguna cosa i 
	# que no siguin iguals; en cas de no sigui així fa saltar una exception.
	def _cercar(self):
		self._eliminarTotsFitxersLlista(self.llista_orig)		#Si cerquem eliminarem la llista 
		self._eliminarTotsFitxersLlista(self.llista_iguals)	# de fitxers que hi havia anteriorment
		self._eliminarTotsFitxersLlista(self.llista_semblants) 	
	
		if(dir_font==None or dir_desti==None):
			raise ex.errorCerca("S'han d'escollir els dos directoris")
		elif(dir_font==dir_desti):
			raise ex.errorCerca("El directori font i el directori destí no poden ser el mateix")
		else:	
			#self.f_origin = llistaFitxersOriginals(dir_font)		
			self.f_origin = ['holi', 'holi2', 'dw']
			self._afegirFitxers(self.llista_orig, self.f_origin)
			
			#self._actualitzarSemblantsIguals(f_origin)
			#self.f_iguals = llistaFitxersIguals(dir_desti, f_origin)	
			self.f_iguals = ['a','b','c','d']
			self._afegirFitxers(self.llista_iguals, self.f_iguals)
			
			#self.f_semblants = llistaFitxersSemblants(dir_desti, f_origin)
			self.f_semblants = ['1','2','3','4']
			self._afegirFitxers(self.llista_semblants, self.f_semblants)


	def _actualitzarSemblantsIguals(self, fitxersorigen):
		#self.f_iguals = llistaFitxersIguals(dir_desti, fitxersorigen)	
		self.f_iguals = ['a','b']
		self._afegirFitxers(self.llista_iguals, self.f_iguals)

		#self.f_semblants = llistaFitxersSemblants(dir_desti, fitxersorigen)
		self.f_semblants = ['1','3','4']
		self._afegirFitxers(self.llista_semblants, self.f_semblants)
		

	# Mètode que rep una listbox i una llista que conté el nom o el path
	# relatiu dels fitxers. Afegeix els fitxers a la listbox.
	def _afegirFitxers(self, llista, fitxers):	
		i=0		
		for f in fitxers:
			llista.insert(i, f)
			i+=1
	

	# Mètode que donada una listbox ens permet esborrar tots els elements
	# que té afegits.
	def _eliminarTotsFitxersLlista(self, llista):
		llista.delete(0, END)
	
	# Mètode que ens permet eliminar una sèrie d'elements d'una listbox
	# donada la listbox i la posicio dels elements a eliminar
	def _eliminarAlgunsFitxersLlista(self, llista, posicions):
		for i in posicions[::-1]:
			llista.delete(i)	

	# Funció per a seleccionar tots els elements de la listbox. A més
	# actualitza els elements de la listbox de fitxers semblants i iguals
	# si la llista en la que fem la desel.lecció és la listbox d'originals
	def _seleccionarTot(self, llista):
		llista.select_set(0,END)

		if (llista is self.llista_orig):
			self._detectarSeleccio()


	# Mètode que deselecciona tots els elements de la listbox. A més
	# actualitza els elements de la listbox de fitxers semblants i iguals
	# si la llista en la que fem la desel.lecció és la listbox d'originals
	def _seleccionarCap(self, llista):
		llista.selection_clear(0,END)

		if (llista is self.llista_orig):
			self._eliminarTotsFitxersLlista(self.llista_iguals)		#Esborrem els elements que hi hagi a la llista de fitxers
			self._eliminarTotsFitxersLlista(self.llista_semblants)	# iguals i de fitxers semblants
			self._actualitzarSemblantsIguals(self.f_origin)


	# Event de la listbox que conté els fitxers originals. Detecta quins
	# elements estan pressionats i actualitza les llistes de fitxers originals 
	def _detectarSeleccio(self):
		self._eliminarTotsFitxersLlista(self.llista_iguals)		#Esborrem els elements que hi hagi a la llista de fitxers
		self._eliminarTotsFitxersLlista(self.llista_semblants)	# iguals i de fitxers semblants
		selec = [self.llista_orig.get(i) for i in self.llista_orig.curselection()] #Obtenim el nom dels fitxers seleccionats
		self._actualitzarSemblantsIguals(selec)


	# Mètode que permet esborrar els fitxers seleccionats, ja sigui
	# a la llista de fitxers iguals o semblants. Si no hi ha cap fitxer
	# seleccionat però hi ha elements a la listbox llençarem una exception.
	def _esborrarFitxers(self, llista):
		#Obtenim el nom dels elements seleccionats		
		selec = llista.curselection()
		#Si hi ha elements, però no s'ha seleccionat cap llencem una exception
		if (llista.size()!=0 and not selec):	
			raise ex.resSeleccionat()
			return
		elif (selec):
			fitxers = [llista.get(i) for i in selec]
			#funct.eliminarFitxers(dir_desti, fitxers)
			self._eliminarAlgunsFitxersLlista(llista, selec)


	


if __name__ == '__main__':
    finestra = Tk()
    finestra.title("Cerca Fitxers Redundants")
    app = Interficie(finestra)
    finestra.mainloop()


