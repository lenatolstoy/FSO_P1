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
		#falta comprobar que los directorios existan (mejor mirarlo en la ig)
		#os.path.exists(path)
		
        def nombrarFont(self, n):
                self.directori_font = n
		
        def nombrarDesti(self, n):
                self.directori_desti = n

        def llistaFitxersOriginals(self):
		
                llista_font = list()
			
                llista_font = [f for f in listdir(self.directori_font) if isfile(join(self.directori_font, f))]
			
                return llista_font
			
	#devuelve los paths relativos del directorio destino
        def llistaFitxersMateixNom(self):
	
                llista_fitxers = list()
                llista_font = self.llistaFitxersOriginals()
                llista_desti = list()
		
                for root, dirs, files in os.walk(self.directori_desti):
                    for nombreArchivo in files:
                        llista_desti.append(root.replace(self.directori_desti, "") + os.sep + nombreArchivo)
                        
                for x in range(0, len(llista_font)):
                    for y in range(0, len(llista_desti)):
                        (filepath1, filename1) = os.path.split(llista_font[x])
                        (filepath2, filename2) = os.path.split(llista_desti[y])
                        if (filename1 == filename2):
                            llista_fitxers.append(llista_desti[y])			
                return llista_fitxers #la lista contiene los paths relativos del directorio fuente
	
	#listaFiles son los ficheros que quiero mirar que tienen iguales (no hay paths relativos)
        #devuelve los paths relativos de los ficheros iguales del directorio destino
        def llistaFitxersIguals(self, listaFiles):
		
                llista_fitxers = self.llistaFitxersMateixNom()
                llista_iguals = list()
		
                for x in range(0, len(listaFiles)):
                        archivo1 = open(self.directori_font + os.sep + listaFiles[x], 'r')
                        archivo2 = open(self.directori_desti + os.sep + llista_fitxers[x], 'r')
                        archivo1.read()
                        archivo2.read()
                        if (archivo1 == archivo2):
                                llista_iguals.append(llista_fitxers[x])
			
                return llista_iguals

        def llistaFitxersSemblants(self, listaFiles):
		
                llista_fitxers = self.llistaFitxersOriginals()
                llista_semblants = list()
		
                for x in range(0, len(listaFiles)):
                        archivo1 = open(self.directori_font + os.sep + listaFiles[x], 'r')
                        archivo2 = open(self.directori_desti + os.sep + llista_fitxers[x], 'r')
                        archivo1.read()
                        archivo2.read()
                        if (archivo1 == archivo2):
                                llista_semblants.append(llista_fitxers[x])
			
                return llista_semblants
			
			
			
"""
#cosas que alomejor me van bien:
os.path.samefile(path1, path2)
#(fichero, extension_fichero) = os.path.splitext(text1.get())



font = raw_input("Directori font? ")
desti = raw_input("Directori desti? ")

clase1 = fitxersIguals(font, desti)

print clase1.llistaFitxersOriginals()
"""

