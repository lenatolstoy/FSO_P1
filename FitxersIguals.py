# -*- coding: cp1252 -*-
import os
from os import listdir
from os.path import isfile, join

class fitxersIguals:
        directori_font = ""
        directori_desti = ""
	
	#Constructor
	
        def __init__(self, font, desti):
                self.directori_font = font
                self.directori_desti = desti
		
        def nombrarFont(self, n):
                self.directori_font = n
		
        def nombrarDesti(self, n):
                self.directori_desti = n

        def llistaFitxersOriginals(self):
                llista_font = list()
                if(self.directori_font != ""):  	
                        llista_font = [f for f in listdir(self.directori_font) if isfile(join(self.directori_font, f))]
			
                return llista_font
			
	#devuelve los paths relativos del directorio destino
        def llistaFitxersMateixNom(self):
	
                llista_fitxers = list()
                llista_font = self.llistaFitxersOriginals()
                llista_desti = list()
                
                if(self.directori_font != ""): 
                        for root, dirs, files in os.walk(self.directori_desti):
                            if ('Trash/' not in root) and not(self.directori_font == root):
                                    for nombreArchivo in files:
                                        llista_desti.append(root.replace(self.directori_desti, "") + os.sep + nombreArchivo)
					hola = root.replace(self.directori_desti, "") + os.sep + nombreArchivo
                        
                        for x in range(0, len(llista_font)):
                            for y in range(0, len(llista_desti)):
                                (filepath1, filename1) = os.path.split(llista_font[x])
                                (filepath2, filename2) = os.path.split(llista_desti[y])
                                if (filename1 == filename2):
                                        if not (os.path.islink(self.directori_desti+llista_desti[y])):
                                                llista_fitxers.append(llista_desti[y])
                return llista_fitxers #la lista contiene los paths relativos del directorio fuente
	
	#listaFiles son los ficheros que quiero mirar que tienen iguales (no hay paths relativos)
        #devuelve los paths relativos de los ficheros iguales del directorio destino
        def llistaFitxersIguals(self, listaFiles):
		
                llista_fitxers = self.llistaFitxersMateixNom()
                llista_iguals = list()
                
                if(self.directori_font != ""): 
                        for x in range(0, len(listaFiles)):
                                archivo1 = open(self.directori_font + os.sep + listaFiles[x], 'r')
                                for y in range(0, len(llista_fitxers)):
                                        (filepath, filename) = os.path.split(llista_fitxers[y])
                                        if(filename == listaFiles[x]):
                                                archivo2 = open(self.directori_desti + llista_fitxers[y], 'r')
                                                texto1 = archivo1.read()
                                                texto2 = archivo2.read()
                                                if (texto1 == texto2):
                                                        llista_iguals.append(llista_fitxers[y])
                                
                return llista_iguals

        def llistaFitxersSemblants(self, listaFiles):
		
                llista_fitxers = self.llistaFitxersMateixNom()
                llista_semblants = list()
                if(self.directori_font != ""): 
                        for x in range(0, len(listaFiles)):
                                archivo1 = open(self.directori_font + os.sep + listaFiles[x], 'r')
                                for y in range(0, len(llista_fitxers)):
                                        (filepath, filename) = os.path.split(llista_fitxers[y])
                                        if(filename == listaFiles[x]):
                                                archivo2 = open(self.directori_desti + llista_fitxers[y], 'r')
                                                texto1 = archivo1.read()
                                                texto2 = archivo2.read()
                                                if (texto1 != texto2):
                                                        llista_semblants.append(llista_fitxers[y])
                                
                return llista_semblants
			

