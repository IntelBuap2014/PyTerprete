import os

def saludo_inicial():
	print ("""
		Bienvenido a Pyterpreter.
		Este interprete fue realizadon con fines de aprendizaje.
		Si tienes algunas sugerencia estamos abiertos a que cualquier 
		caracteristica interezante que pudieramos agregar.
		De momento solo hay 3 comandos:
			listar
			limpiar
			rehubicar
	""")


def opciones():
	print ("""
Modo de Empleo: pyterpreter [comando] [opcion]
	Opciones posibles para usar con el interprete:
	-h	:	Ayuda (lo que te imprimiria este mensaje).
	-b	:	Mensaje de Bienvenida.
	-v	:	Version.
	""")


def limpiar():
	os.system('clear')


def listar(direccion):
	archivos = os.listdir(direccion)
	for archivo in archivos:
		print (archivo, end=" ")

def rehubicar(direccion):
	os.chdir(direccion)
