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
from funciones import limpiar, rehubicar

if len(sys.argv) == 2:

	if sys.argv[1] == "-h":
		opciones()

	if sys.argv[1] == "-v":
		print ("Version 0.1")

	if sys.argv[1] == "-b":
		saludo_inicial()

limpiar()
saludo_inicial()
while True:
	try:	
		opcion = input("\n@@> ")
		opcion = opcion.lower()  # convertimos la entrada en minisculas
		opcion = opcion.split(sep=" ")  # separamos la cadena por el espacio.
		
		if opcion[0] == "listar":
			listar(opcion[1])
		
		elif opcion[0] == "limpiar":
			limpiar()
		
		elif opcion[0] == "rehubicar":
			rehubicar(opcion[1])
	
		else:
			print ("No es un comando valido")
	except EOFError:
		print ("Error de lectura")
