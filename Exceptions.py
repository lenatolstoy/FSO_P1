#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkMessageBox

# Exception que salta quan falta un dels directoris a l'hora de cercar o
# els directoris son iguals. A l'executar-se es mostrarà una pantalla que
# indicarà l'error.
class errorCerca(Exception):
	def __init__(self, text):
		self.error = tkMessageBox.showerror("Error al cercar", text)

# Exception que salta quan es prem un botó i no s'ha seleccionat res a la 
# listbox. A l'executar-se es mostrarà una pantalla que indicarà l'error.
class resSeleccionat(Exception):
	def __init__(self):
		self.error = tkMessageBox.showerror("Res seleccionat", "Per a realitzar aquesta acció, s'ha de seleccionar algun element de la llista")


