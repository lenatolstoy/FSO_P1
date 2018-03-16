#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

def eliminarFitxers(directori, fitxers):
	for p_relatiu in fitxers:
		#Unim el path absolut del directori desti amb el path relatiu del fitxer
		path = os.path.join(directori, p_relatiu)
		os.remove(path)	#Eliminem el fitxer

def hardLink(dir_origen, dir_desti, fitxers):
	for p_relatiu in fitxers:
		fitxer = os.path.basename(p_relatiu)
		path_origen = os.path.join(dir_origen, fitxer)	#Unim el path absolut del directori d'origen amb el nom del fitxer
		path_desti = os.path.join(dir_desti, p_relatiu)	#Unim path del directori desti amb el path relatiu del fitxer
		os.remove(path_desti)			#Eliminem el fitxer en el directori destí
		os.link(path_origen, path_desti)	#Creem el hard link


def softLink(dir_origen, dir_desti, fitxers):
	for p_relatiu in fitxers:
		subprocess.call(['./softLink', dir_origen, dir_desti, p_relatiu])



if __name__ == '__main__':
    dir_origen = "/home/lena/Documents/FSO/hola"
    dir_desti = "/home/lena/Documents"
    fitxers = ["FSO/fichero1", "FSO/hola/holi/masficheros"]
    softLink(dir_origen, dir_desti, fitxers)
    
