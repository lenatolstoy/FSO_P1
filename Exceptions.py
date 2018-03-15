#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkMessageBox

class errorCerca(Exception):
	def __init__(self, text):
		self.error = tkMessageBox.showerror("Error al cercar", text)

class resSeleccionat(Exception):
	def __init__(self):
		self.error = tkMessageBox.showerror("Res seleccionat", "Per a realitzar aquesta acció, ha de seleccionar algun element de la llista")


