#!/usr/bin/python3
""" Licencia GPL
PyTerprete

Un simple interprete de ordenes.

Copyright <1 de abril 2015> Adrian Perez Dominguez <adrian<at>aztli.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License	
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""

import sys
from funciones import saludo_inicial
from funciones import opciones
from funciones import listar
from funciones import limpiar
from funciones import reubicar
from funciones import inicializacion
from funciones import renm
from funciones import despedida_final
if len(sys.argv) == 2:

	if sys.argv[1] == "-h":
		opciones()

	if sys.argv[1] == "-v":
		print ("Version 0.1")

	if sys.argv[1] == "-b":
		saludo_inicial()

limpiar()
inicializacion()
saludo_inicial()
while True:
	try:	
		opcion = input("\n@@> ")
		opcion = opcion.lower()  # convertimos la entrada en minisculas
		opcion = opcion.split(sep=" ")  # separamos la cadena por el espacio.
		
		if opcion[0] == "listar":
			try:
				listar(opcion[1])
			except FileNotFoundError:
				print ("\nEl archivo no existe")
		
		elif opcion[0] == "limpiar":
			limpiar()
		
		elif opcion[0] == "reubicar":
			try:
				reubicar(opcion[1])
			except FileNotFoundError:
				print ("No existe el directorio")
			except NotADirectoryError:
				print ("No es un directorio")
		elif opcion[0] == "renm":
			try:
				renm(opcion[1],opcion[2])
			except FileNotFoundError:
				print ("No existe el arhivo o directorio ", opcion[1]);
			except IndexError:
				print ("Número de argumentos incorrecto")	
		elif opcion[0] == "salir":
			limpiar()
			despedida_final()
			limpiar()
			sys.exit()
		else:
			print ("No es un comando valido")
	
	except EOFError:
		print ("\nError de lectura")
