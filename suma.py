import random

operaciones = ["suma", "resta"]

class sumaApp:
	def parse(self, peticion, rest):
		try:
			numero = peticion.split()[1][1:]
			tupla = numero.split('/')
		except ValueError:
			return None
		if len(tupla) != 3 or tupla[0] not in operaciones:
			return None
		return tupla

	def process(self, parsedRequest):
		print parsedRequest
		if not parsedRequest:
			return("400 Bad Request", "Go away")
		(operacion, operando1, operando2) = parsedRequest
		try:
			print self.guardado
		except:
			self.guardado = 0
		if operacion == "suma":
			resultado = int(operando1) + int(operando2)
		elif operacion == "resta":
			resultado = int(operando1) - int(operando2)
		
		return("200 OK", "<html>""<body><body><h1>" + str(resultado) + "</body></html>")
		
		
	
