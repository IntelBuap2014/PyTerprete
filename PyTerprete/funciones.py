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
