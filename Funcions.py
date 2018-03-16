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

# Mètode que retorna l'inode del fitxer destí, el path relatiu del fitxer
# destí i el nombre de linies diferents entre el fitxer desti i l'original.
# A més obre el vimdiff per a veure les diferències dels fitxers.
def comparaFitxer(dir_font, dir_desti, p_relatiu):
	fitxer = os.path.basename(p_relatiu)
	path_font = os.path.join(dir_font, fitxer)	#Obtenim el path absolut del fitxer origen
	path_desti = os.path.join(dir_desti, p_relatiu)	#Obtenim el path absolut del fitxer destí
	
	subprocess.call(['./vimdiff', path_font, path_desti])

	#Comptem la quantitat de linies diferents entre els dos fitxers
	dif = 0
	with open(path_font) as f1, open(path_desti) as f2:
		for line1, line2 in zip(f1, f2):
			if line1!=line2:
				dif+=1
	
	#Obtenim l'inode
	inode = os.stat(path_desti).st_ino
	print inode
	return str(inode)+"\t"+path_desti+"\t"+str(dif)


if __name__ == '__main__':
	comparaFitxer("/home/lena/Documents/FSO", "/home/lena/Documents", "FSO/hola/masficheros")

    
