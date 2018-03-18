#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import tkMessageBox
import Exceptions

def eliminarFitxers(directori, fitxers):
	""" Mètode que donats un directori i una llista amb els paths
	relatius (respecte al directori) d'una sèrie de fitxers 
	elimina els fitxers.
	"""
	if (not fitxers):
		raise llistaBuida("La llista està buida")
	for p_relatiu in fitxers:
		#Unim el path absolut del directori desti amb el path relatiu del fitxer
		path = directori + p_relatiu
		os.remove(path)	#Eliminem el fitxer

def hardLink(dir_origen, dir_desti, fitxers):
	""" Mètode que donats un directori origen, un destí i una llista
	amb paths relatius (respecte al directori destí) crea un hard
	link dels fitxers originals al directori destí
	"""
	if (not fitxers):
		raise llistaBuida("La llista està buida")
	eliminarFitxers(dir_desti, fitxers) #Eliminem els fitxers destí
	for p_relatiu in fitxers:
		fitxer = os.path.basename(p_relatiu)
		path_origen = os.path.join(dir_origen, fitxer)	#Unim el path absolut del directori d'origen amb el nom del fitxer
		path_desti = dir_desti + p_relatiu	#Unim path del directori desti amb el path relatiu del fitxer
		os.link(path_origen, path_desti)	#Creem el hard link


def softLink(dir_origen, dir_desti, fitxers):
	""" Mètode que donats un directori origen, un destí i una llista
	amb paths relatius (respecte al directori destí) crea un soft
	link dels fitxers originals al directori destí.
	Implementat amb un script, ja que el codi en python hagues sigut 
	pràcticament igual a hardLink.
	"""
	if (not fitxers):
		raise llistaBuida("La llista està buida")
	for p_relatiu in fitxers:
		subprocess.call(['./softLink', dir_origen, dir_desti, p_relatiu])


def renombraFitxer(directori, p_relatiu, nomnou):
	""" Mètode que donat un directori, un path relatiu d'un fitxer i un 
	string amb un nom nou per al fitxer ens retorna el path relatiu del fitxer
	i canvia el nom del fitxer.
	"""
	if (nomnou==""):
		raise ValueError("String buida")
	else:
		dir_relatiu = os.path.dirname(p_relatiu) #Separem el path del nom del fitxer		
		path_nou = os.path.join(dir_relatiu, nomnou) #Obtenim el nou path relatiu
		p_abs_antic = directori + p_relatiu 
		p_abs_nou = directori+path_nou
		os.rename(p_abs_antic, p_abs_nou) #Canviem el nom del fitxer	
	
		return path_nou

def comparaFitxer(dir_font, dir_desti, p_relatiu):
	""" Funció que retorna l'inode del fitxer destí, el path relatiu del fitxer
	destí i el nombre de linies diferents entre el fitxer desti i l'original.
	A més obre el vimdiff per a veure les diferències dels fitxers.
	"""
	fitxer = os.path.basename(p_relatiu)
	path_font = os.path.join(dir_font, fitxer)	#Obtenim el path absolut del fitxer origen
	path_desti = dir_desti + p_relatiu	#Obtenim el path absolut del fitxer destí
	
	#Executem el shell script vimdiff que compara els fitxers original i rèplica
	subprocess.call(['./vimdiff', path_font, path_desti])

	#Comptem la quantitat de linies diferents entre els dos fitxers
	dif = 0
	with open(path_font) as f1, open(path_desti) as f2:
		for line1, line2 in zip(f1, f2):
			if line1!=line2:
				dif+=1
	#Comptem el nombre de linies dels fitxers
	len1 = sum(1 for line in open(path_font))
	print len1
	len2 = sum (1 for line in open(path_desti))
	print len2
	if (len1<len2):
		dif = dif + (len2-len1)
	elif (len1>len2):
		dif = dif + (len1-len2)
	
	#Obtenim l'inode
	inode = os.stat(path_desti).st_ino
	return str(inode)+"\t"+path_desti+"\t"+str(dif)


    
