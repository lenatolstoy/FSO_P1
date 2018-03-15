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
	
		llista_fitxers = list()
	
		from os import listdir
		from os.path import isfile, join
		llista_font = [f for f in listdir(directori_font) if isfile(join(directori_font, f))] #guarda solo el nombre de los archivos
		llista_desti = [f for f in listdir(directori_desti) if isfile(join(directori_desti, f))]
		
		for x in range(0, llista_font.len):
			for y in range(0, llista_desti.len):
				if ((llista_font[x] == llista_desti[y]):
					llista_fitxers.append(llista.font[x])
					
		return llista_fitxers

	def llistaFitxersIguals(self):
		
		llista_fitxers = llistaFitxersOriginals()
		llista_iguals = list()
		
		for x in llista_fitxers.len:
			archivo1 = open(directori_font + llista_fitxers[x], “r”)
			archivo2 = open(directori_desti + llista_fitxers[x], “r”)
			archivo1.read()
			archivo2.read()
			if archivo1 == archivo2
				llista_iguals.append(llista_fitxers[x])
			
		return llista_iguals

	def llistaFitxersSemblants(self):
		
		llista_fitxers = llistaFitxersOriginals()
		llista_semblants = list()
		
		for x in llista_fitxers.len:
			archivo1 = open(directori_font + llista_fitxers[x], “r”)
			archivo2 = open(directori_desti + llista_fitxers[x], “r”)
			archivo1.read()
			archivo2.read()
			if archivo1 != archivo2
				llista_semblants.append(llista_fitxers[x])
			
		return llista_semblants
			
			
			