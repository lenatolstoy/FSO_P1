#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog
import os
import getpass
import Exceptions as ex
import Funcions as funct
from tkSimpleDialog import askstring
#import FitxersIguals

dir_font=None
dir_desti=None


class Interficie(object):
	""" Implementa una interficie grafica que permet comparar fitxers
	de dos directoris diferents	
	"""

	def __init__(self, parent):
		"""Inicialització de la interfície gràfica. S'inicialitzen 4 blocs 
		de manera separada: la primera fila de la IG, la segona fila, les 
		últimes files i la part central on trobem totes les llistes de fitxers.
		"""
		self.finestra = parent
		finestra.resizable(width=False, height=False) #Fem que no es pugui canviar la mida de la finestra
		self._primeraFila()
		self._segonaFila()
		self._ultimesFiles()
		self._llistes()


	'''--------------------------------------------------------------------

	Inicialització, col.locació i assignació d'events de tots els widgets de la IG

	--------------------------------------------------------------------'''
 
	def _primeraFila(self):
		"""Creació de la primera fila que trobem a la IG, on es pot seleccionar el directori font."""

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
		"""Creació de la segona fila de la IG, on es permet a l'usuari
		cercar un directori destí i fer una cerca als dos directoris.
		"""
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
		"""Inicialitzem la part central de la IG, on hi ha les llistes
		de fitxers i els botons de la llista de fitxers iguals i semblants.
		"""
		#Creem un frame per a totes les llistes
		self.centre = Frame(self.finestra)
		self.centre.pack(side=LEFT)

		self._fitxersOriginals()	#Creem la llista de fitxers originals
		
		#Creem un frame per a fitxers iguals i semblants
		self.iguals_semblants = Frame(self.centre)
		self.iguals_semblants.pack(side=LEFT, expand=TRUE, fill=BOTH)
		
		self._fitxersIguals()		#Creem la llista de fitxers iguals
		self._fitxersSemblants()	#Creem la llista de fitxers semblants


	def _fitxersOriginals(self): 
		"""Creem una listbox per als fitxers originals amb la seva scrollbar i un títol a la part superior 
		per a fer saber a l'usuari que conté aquest contenidor.
		"""
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


	def _fitxersIguals(self):
		"""Creem una listbox per als fitxers iguals amb la seva scrollbar i un títol a la part superior per a fer saber
		a l'usuari que conté aquest contenidor. A més creem els botons laterals.
		"""
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

	def _botons_iguals(self):
		"""Inicialitzem els botons que trobem al lateral de la listbox de fitxers iguals."""
		self.iguals_botons = Frame(self.iguals_interior)
		self.iguals_botons.pack(side=RIGHT)

		self.ig_esborra = Button(self.iguals_botons, text='Esborra', command = lambda: self._esborrarFitxers(self.llista_iguals))	#Boto esborra
		self.ig_esborra.pack(side=TOP, anchor="w")

		self.ig_hl = Button(self.iguals_botons, text='Hard Link', command=self._creaHardLink) 	#Boto hard link
		self.ig_hl.pack(side=TOP, anchor="w")

		self.ig_sl = Button(self.iguals_botons, text='Soft Link', command=self._creaSoftLink) 	#Boto soft link
		self.ig_sl.pack(side=TOP, anchor="w")

		self.ig_st = Button(self.iguals_botons, text='Selec Tots') 	#Boto Seleccionar tots
		self.ig_st.bind("<Button-1>", lambda event: self._seleccionarTot(self.llista_iguals))
		self.ig_st.pack(side=TOP, anchor="w")

		self.ig_sc = Button(self.iguals_botons, text='Selec Cap') 	#Boto selecciona cap
		self.ig_sc.pack(side=TOP, anchor="w")
		self.ig_sc.bind("<Button-1>", lambda event: self._seleccionarCap(self.llista_iguals))


	def _fitxersSemblants(self):
		"""Creem una listbox per als fitxers semblants amb la seva scrollbar i un títol 
		a la part superior per a fer saber a l'usuari que conté aquest contenidor. 
		A més creem els botons laterals.
		"""
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

	def _botons_semblants(self):
		""" Inicialitzem els botons que trobem al lateral de la listbox de fitxers semblants."""
		self.semblants_botons = Frame(self.semblants_interior)
		self.semblants_botons.pack(side=RIGHT)

		self.se_compara = Button(self.semblants_botons, text='Compara', command=self._comparaFitxers) 	#Boto compara
		self.se_compara.pack(side=TOP, anchor="w")

		self.se_renombra = Button(self.semblants_botons, text='Renombra', command=self._renombraFixers) 	#Boto renombra
		self.se_renombra.pack(side=TOP, anchor="w")

		self.se_esborra = Button(self.semblants_botons, text='Esborra', command = lambda: self._esborrarFitxers(self.llista_semblants)) 	#Boto esborra
		self.se_esborra.pack(side=TOP, anchor="w")

		self.se_st = Button(self.semblants_botons, text='Selec Tots') 	#Boto Seleccionar tots
		self.se_st.bind("<Button-1>", lambda event: self._seleccionarTot(self.llista_semblants))
		self.se_st.pack(side=TOP, anchor="w")

		self.se_sc = Button(self.semblants_botons, text='Selec Cap') 	#Boto selecciona cap
		self.se_sc.bind("<Button-1>", lambda event: self._seleccionarCap(self.llista_semblants))
		self.se_sc.pack(side=TOP, anchor="w")


	
	def _ultimesFiles(self):
		""" Afegim els botons finals, els de selecciona tots i selecciona
		cap fan referència a la listbox de fitxers originals.
		"""
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
	
	def _obrirDirectoriFont(self):
		"""Al fer clic en el botó d'escollir directori font, obrim
		un tkFileDialog i emmagatzemem el path a dir_font.
		"""
		global dir_font		
		self.dir_font = tkFileDialog.askdirectory(initialdir='/home/%s' %getpass.getuser(), title='Escolliu un directori font')
		if (self.dir_font!=""): #Controlem que l'usuari no hagi cancelat la cerca del directori
			dir_font = self.dir_font
			self.txt_dirfont.config(text=dir_font)

			self._eliminarTotsFitxersLlista(self.llista_orig)		#Si canviem de directori eliminarem la llista 
			self._eliminarTotsFitxersLlista(self.llista_iguals)		# de fitxers que hi havia anteriorment
			self._eliminarTotsFitxersLlista(self.llista_semblants) 	

	def _obrirDirectoriDesti(self):
		"""Al fer clic en el botó d'escollir directori destí, obrim
		un tkFileDialog i emmagatzemem el path a dir_font.
		"""
		global dir_desti		
		self.dir_desti = tkFileDialog.askdirectory(initialdir='/home/%s' %getpass.getuser(), title='Escolliu un directori destí')
		if (self.dir_desti!=""): #Controlem que l'usuari no hagi cancelat la cerca del directori
			dir_desti = self.dir_desti
			self.txt_dirdesti.config(text=dir_desti)

			self._eliminarTotsFitxersLlista(self.llista_orig)		#Si canviem de directori eliminarem la llista 
			self._eliminarTotsFitxersLlista(self.llista_iguals)	# de fitxers que hi havia anteriorment
			self._eliminarTotsFitxersLlista(self.llista_semblants) 	
		
	def _tancarFinestra(self):
		""" Funcionalitat per al botó sortir. """
		self.finestra.destroy()	

	def _cercar(self):
		""" Funció que crida a les funcions llistaFitxersOriginals,
		llistaFitxersIguals i llistaFitxersSemblants del fitxer FitxersIguals.
		També comprova que els directoris tinguin emmagatzemada alguna cosa i 
		que no siguin iguals; en cas de no sigui així fa saltar una exception. 
		"""
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
			self.f_semblants = ['/hola/soy/un/path/fichero','2','3','4']
			self._afegirFitxers(self.llista_semblants, self.f_semblants)

	def _actualitzarSemblantsIguals(self, fitxersorigen):
		""" Mètode que permet donada una llista de fitxers origen, actualitzar les 
		llistes de fitxers iguals i semblants
		"""
		#self.f_iguals = llistaFitxersIguals(dir_desti, fitxersorigen)	
		self.f_iguals = ['a','b']
		self._afegirFitxers(self.llista_iguals, self.f_iguals)

		#self.f_semblants = llistaFitxersSemblants(dir_desti, fitxersorigen)
		self.f_semblants = ['1','3','4']
		self._afegirFitxers(self.llista_semblants, self.f_semblants)
		
	def _afegirFitxers(self, llista, fitxers):
		""" Mètode que rep una listbox i una llista que conté el nom o el path
		relatiu dels fitxers. Afegeix els fitxers a la listbox.
		"""	
		i=0		
		for f in fitxers:
			llista.insert(i, f)
			i+=1
	
	def _eliminarTotsFitxersLlista(self, llista):
		""" Mètode que donada una listbox ens permet esborrar tots els elements que té afegits."""
		llista.delete(0, END)
	
	def _eliminarAlgunsFitxersLlista(self, llista, posicions):
		"""  Mètode que ens permet eliminar una sèrie d'elements d'una listbox
		donada la listbox i la posicio dels elements a eliminar
		"""
		for i in posicions[::-1]:
			llista.delete(i)	

	def _seleccionarTot(self, llista):
		""" Funció per a seleccionar tots els elements de la listbox. A més
		actualitza els elements de la listbox de fitxers semblants i iguals
		si la llista en la que fem la desel.lecció és la listbox d'originals
		"""
		llista.select_set(0,END)

		if (llista is self.llista_orig):
			self._detectarSeleccio()

	def _seleccionarCap(self, llista):
		""" Mètode que deselecciona tots els elements de la listbox. A més
		actualitza els elements de la listbox de fitxers semblants i iguals
		si la llista en la que fem la desel.lecció és la listbox d'originals
		"""
		llista.selection_clear(0,END)

		if (llista is self.llista_orig):
			self._eliminarTotsFitxersLlista(self.llista_iguals)		#Esborrem els elements que hi hagi a la llista de fitxers
			self._eliminarTotsFitxersLlista(self.llista_semblants)	# iguals i de fitxers semblants
			self._actualitzarSemblantsIguals(self.f_origin)


	def _detectarSeleccio(self):
		""" Event de la listbox que conté els fitxers originals. Detecta quins
		elements estan pressionats i actualitza les llistes de fitxers originals """
		self._eliminarTotsFitxersLlista(self.llista_iguals)		#Esborrem els elements que hi hagi a la llista de fitxers
		self._eliminarTotsFitxersLlista(self.llista_semblants)	# iguals i de fitxers semblants
		selec = [self.llista_orig.get(i) for i in self.llista_orig.curselection()] #Obtenim el nom dels fitxers seleccionats
		self._actualitzarSemblantsIguals(selec)

	def _esborrarFitxers(self, llista):
		""" Mètode que permet esborrar els fitxers seleccionats, ja sigui
		a la llista de fitxers iguals o semblants. Si no hi ha cap fitxer
		seleccionat però hi ha elements a la listbox llençarem una exception.
		"""
		#Obtenim l'index dels elements seleccionats		
		selec = llista.curselection()
		#Si hi ha elements, però no s'ha seleccionat cap llencem una exception
		if (llista.size()!=0 and not selec):	
			raise ex.resSeleccionat()
		elif (selec):
			fitxers = [llista.get(i) for i in selec]
			#funct.eliminarFitxers(dir_desti, fitxers)
			self._eliminarAlgunsFitxersLlista(llista, selec)

	def _creaHardLink(self):
		""" Event del botó Hard Link. Permet crear un hard link dels elements
		seleccionats a la Listbox. Si no hi ha cap fitxer seleccionat però hi 
		ha elements a la listbox llençarem una exception.
		"""
		#Obtenim el nom dels elements seleccionats
		selec = [self.llista_iguals.get(i) for i in self.llista_iguals.curselection()]
		#Si hi ha elements, però no s'ha seleccionat cap llencem una exception
		if (self.llista_iguals.size()!=0 and not selec):	
			raise ex.resSeleccionat()
		elif (selec):
			funct.creaHardLink(dir_origen, dir_desti, selec)

	def _creaSoftLink(self):
		""" Event del botó Soft Link. Permet crear un soft link dels elements
		seleccionats a la Listbox. Si no hi ha cap fitxer
		seleccionat però hi ha elements a la listbox llençarem una exception.
		"""
		#Obtenim el nom dels elements seleccionats
		selec = [self.llista_iguals.get(i) for i in self.llista_iguals.curselection()]
		#Si hi ha elements, però no s'ha seleccionat cap llencem una exception
		if (self.llista_iguals.size()!=0 and not selec):	
			raise ex.resSeleccionat()
		elif (selec):
			funct.softLink(dir_origen, dir_desti, selec)

	def _renombraFixers(self):
		""" Event del botó Renombra de la llista de fitxers semblants. Permet renombrar
		els fitxers seleccionats a la listbox. A més actualitza l'element de la
		listbox amb el nou nom. 
		"""
		#Obtenim el nom dels elements seleccionats
		selec = self.llista_semblants.curselection()
		print selec
		#Si hi ha elements, però no s'ha seleccionat cap llencem una exception
		if (self.llista_semblants.size()!=0 and not selec):	
			raise ex.resSeleccionat()
		elif (selec):
			for i in selec:
				#Obtenim l'item de la posicio corresponent
				path = self.llista_semblants.get(i)

				#Demanem a l'usuari el nou nom de fitxer
				nomnou = askstring("Renombrar fitxer","Quin nom vol posar al\nfitxer que es troba a:\n"+path+"?")

				if (nomnou != ""):	#Controlem que l'usuari no hagi premut el boto de cancelar			
					nou_path = funct.renombraFitxer(dir_desti, path, nomnou) #Obtenim el nou path			
					self.llista_semblants.delete(i) #Eliminem l'antic element
					self.llista_semblants.insert(i, nou_path) #Afegim el nou

	def _comparaFitxers(self): 
		""" Funcionalitat del botó compara. Obre una subfinestra amb les dades dels 
		fitxers rèplica i el nombre de linies diferents respecte als fitxers originals.
		A més permet comparar els fitxers. 
		"""
		#Obtenim el nom dels elements seleccionats
		selec = [self.llista_semblants.get(i) for i in self.llista_semblants.curselection()]
		#Si hi ha elements, però no s'ha seleccionat cap llencem una exception
		if (self.llista_semblants.size()!=0 and not selec):	
			raise ex.resSeleccionat()
		elif (selec):
			for i, path in enumerate(selec):
				informacio[i] = funct.comparaFitxer(dir_font, dir_desti, path)
			subfinestra = Subfinestra(self.finestra, informacio)
 
				
class Subfinestra(object):
	""" Finestra filla de Interficie. Mostra la informació dels fitxers 
	rèplica respecte als originals
	"""
	def __init__(self, parent, info):
		self.subfinestra = Toplevel(parent)
		self.subfinestra.title("Comparació fitxers")

		Label(self.subfinestra, text="Inode", relief="groove").grid(row=0, column=0, sticky="nswe")
		Label(self.subfinestra, text=" Path relatiu al directori destí ", relief="groove").grid(row=0, column=1, sticky="nswe")
		Label(self.subfinestra, text=" Número de línies diferents ", relief="groove").grid(row=0, column=2, sticky="nswe")

		for i, fitxer in enumerate(info):
			for j, txt in enumerate(fitxer.split('\t')):
				Label(self.subfinestra, text=txt, anchor='w').grid(row=i+1, column=j, sticky="nswe", padx=7)
		

	
'''--------------------------------------------------------------------

Programa principal

--------------------------------------------------------------------'''

if __name__ == '__main__':
    finestra = Tk()
    finestra.title("Cerca Fitxers Redundants")
    app = Interficie(finestra)
    finestra.mainloop()


