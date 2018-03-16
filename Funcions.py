#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import tkMessageBox

# Mètode que donats un directori i una llista amb els paths
# relatius (respecte al directori) d'una sèrie de fitxers 
# elimina els fitxers.
def eliminarFitxers(directori, fitxers):
	for p_relatiu in fitxers:
		#Unim el path absolut del directori desti amb el path relatiu del fitxer
		path = os.path.join(directori, p_relatiu)
		os.remove(path)	#Eliminem el fitxer

# Mètodes que donats un directori origen, un destí i una llista
# amb paths relatius (respecte al directori destí) crea un hard
# link dels fitxers al directori origen al directori destí.
def hardLink(dir_origen, dir_desti, fitxers):
	for p_relatiu in fitxers:
		fitxer = os.path.basename(p_relatiu)
		path_origen = os.path.join(dir_origen, fitxer)	#Unim el path absolut del directori d'origen amb el nom del fitxer
		path_desti = os.path.join(dir_desti, p_relatiu)	#Unim path del directori desti amb el path relatiu del fitxer
		os.remove(path_desti)			#Eliminem el fitxer en el directori destí
		os.link(path_origen, path_desti)	#Creem el hard link


# Mètodes que donats un directori origen, un destí i una llista
# amb paths relatius (respecte al directori destí) crea un soft
# link dels fitxers al directori origen al directori destí.
# Implementat amb un script, ja que el codi en python hagues sigut 
# pràcticament igual.
def softLink(dir_origen, dir_desti, fitxers):
	for p_relatiu in fitxers:
		subprocess.call(['./softLink', dir_origen, dir_desti, p_relatiu])


# Mètode que donat un directori, un path relatiu d'un fitxer i un 
# string amb un nom nou per al fitxer ens retorna el path relatiu del fitxer
# i canvia el nom del fitxer.
def renombraFitxer(directori, p_relatiu, nomnou):
	p_relatiu = os.path.dirname(p_relatiu) #Separem el path del nom del fitxer
	path_nou = os.path.join(p_relatiu, nomnou) #Obtenim el nou path relatiu

	p_abs = os.path.join(directori, p_relatiu) 
	os.rename(p_abs, nomnou) #Canviem el nom del fitxer
	
	return path_nou

    
