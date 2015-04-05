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
import shutil

def saludo_inicial():
	print ("""
		Bienvenido a Pyterpreter.
		Este intérprete fue realizado con fines de aprendizaje.
		Si tienes algunas sugerencia estamos abiertos a cualquier 
		característica interesante que pudieramos agregar.
		De momento solo hay 7 comandos:
			listar
			limpiar
			reubicar
			renm (renombrar)
			eliminar
			mostrar
			salir
	""")

def despedida_final():
	print("""
		Adiós, gracias por venir.		
	""")
	os.system('sleep 1')

def opciones():
	print ("""
Modo de Empleo: pyterpreter [comando] [opción]
	Opciones posibles para usar con el intérprete:
	-h	:	Ayuda (lo que te imprimiría este mensaje).
	-b	:	Mensaje de Bienvenida.
	-v	:	Versión.
	""")


def limpiar():
	os.system('clear')


def listar(direccion):
	archivos = os.listdir(direccion)
	for archivo in archivos:
		print (archivo, end=" ")

def reubicar(direccion):
	os.chdir(direccion)

def inicializacion():
	ruta = os.path.expanduser('~')
	os.chdir(ruta)

def renm(origen,destino):
	os.rename(origen, destino)

def eliminar(ruta):
	os.remove(ruta);

def mostrar(nomArchivo):
	archivo = open(nomArchivo)
	for linea in archivo:
	  print(linea, end='')
	archivo.close()

def copiar():
	pass
