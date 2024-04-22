from iic2343 import Basys3

import sys
import os
import re
#primeros 20 opcode y los ultimos 16 el iteral

def retornar_bytearray(literal: bytearray, opcode:bytearray, opcode_2 = None):
	valor = opcode.pop(0)
	variable = int.from_bytes(literal, byteorder='big', signed=False)
	variable = (variable * 2**4) +  valor
	if opcode_2 is not None:
		opcode_2.pop(0)
		variable_1 =  bytearray(variable.to_bytes(3, "big")) + opcode
		variable_2 =  bytearray(variable.to_bytes(3, "big")) + opcode_2
		return [variable_1, variable_2]
	else:
		return bytearray(variable.to_bytes(3, "big")) + opcode
	

def mov(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x01])
		
	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x02])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x03])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x04])

	if confirmador == 5:
		opcode = bytearray([0x0, 0x00, 0x05])

	if confirmador == 6:
		opcode = bytearray([0x0, 0x00, 0x06])

	if confirmador == 7:
		opcode = bytearray([0x0, 0x00, 0x07])

	if confirmador == 8:
		opcode = bytearray([0x0, 0x00, 0x08])

	if confirmador == 9:
		opcode = bytearray([0x0, 0x00, 0x3f])

	if confirmador == 10:
		opcode = bytearray([0x0, 0x00, 0x40])

	if confirmador == 11:
		opcode = bytearray([0x0, 0x00, 0x41])

	if confirmador == 12:
		opcode = bytearray([0x0, 0x00, 0x42])

	print(f"Se definio un mov con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]

def add(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x09])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x0a])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x0b])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x0c])

	if confirmador == 5:
		opcode = bytearray([0x0, 0x00, 0x0d])

	if confirmador == 6:
		opcode = bytearray([0x0, 0x00, 0x0e])

	if confirmador == 7:
		opcode = bytearray([0x0, 0x00, 0x0f])

	if confirmador == 8:
		opcode = bytearray([0x0, 0x00, 0x043])

	if confirmador == 9:
		opcode = bytearray([0x0, 0x00, 0x44])
	
	print(f"Se definio un add con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]

def sub(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x10])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x11])
		
	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x12])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x13])

	if confirmador == 5:
		opcode = bytearray([0x0, 0x00, 0x14])

	if confirmador == 6:
		opcode = bytearray([0x0, 0x00, 0x15])

	if confirmador == 7:
		opcode = bytearray([0x0, 0x00, 0x16])

	if confirmador == 8:
		opcode = bytearray([0x0, 0x00, 0x45])

	if confirmador == 9:
		opcode = bytearray([0x0, 0x00, 0x46])

	print(f"Se definio un sub con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def f_and(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x17])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x18])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x19])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x1a])

	if confirmador == 5:
		opcode = bytearray([0x0, 0x00, 0x1b])

	if confirmador == 6:
		opcode = bytearray([0x0, 0x00, 0x1c])

	if confirmador == 7:
		opcode = bytearray([0x0, 0x00, 0x1d])

	if confirmador == 8:
		opcode = bytearray([0x0, 0x00, 0x47])

	if confirmador == 9:
		opcode = bytearray([0x0, 0x00, 0x48])
	
	print(f"Se definio un and con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def f_or(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x1e])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x1f])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x20])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x21])

	if confirmador == 5:
		opcode = bytearray([0x0, 0x00, 0x22])

	if confirmador == 6:
		opcode = bytearray([0x0, 0x00, 0x23])

	if confirmador == 7:
		opcode = bytearray([0x0, 0x00, 0x24])

	if confirmador == 8:
		opcode = bytearray([0x0, 0x00, 0x49])

	if confirmador == 9:
		opcode = bytearray([0x0, 0x00, 0x4a])

	print(f"Se definio un or con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def xor(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x25])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x26])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x27])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x28])

	if confirmador == 5:
		opcode = bytearray([0x0, 0x00, 0x29])

	if confirmador == 6:
		opcode = bytearray([0x0, 0x00, 0x2a])

	if confirmador == 7:
		opcode = bytearray([0x0, 0x00, 0x2b])

	if confirmador == 8:
		opcode = bytearray([0x0, 0x00, 0x4b])

	if confirmador == 9:
		opcode = bytearray([0x0, 0x00, 0x4c])

	print(f"Se definio un xor con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def f_not(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x2c])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x2d])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x2e])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x4d])

	print(f"Se definio un not con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def shl(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x2f])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x30])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x31])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x4e])

	print(f"Se definio un shl con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def shr(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x32])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x33])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x34])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x4f])

	print(f"Se definio un shr con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def inc(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x35])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x36])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x37])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x50])

	print(f"Se definio un inc con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def dec(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x38])

	print(f"Se definio un dec con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]

	

def f_cmp(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x39])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x3a])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x3b])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x51])
	
	print(f"Se definio un cmp con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def push(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x57])

	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x58])
	print(f"Se definio un push con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def pop(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode_1 = bytearray([0x0, 0x00, 0x59])
		opcode_2 = bytearray([0x0, 0x00, 0x5a])

	if confirmador == 2:
		opcode_1 = bytearray([0x0, 0x00, 0x5b])
		opcode_2 = bytearray([0x0, 0x00, 0x5c])

	print(f"Se definio un pop con opcode {opcode_1[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	print(f"Se definio un pop con opcode {opcode_2[-1]} en la linea {linea + 1} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode_1, opcode_2)]

def call(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x5d])

	print(f"Se definio un call con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]



def ret(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode_1 = bytearray([0x0, 0x00, 0x5e])
		opcode_2 = bytearray([0x0, 0x00, 0x5f])

	print(f"Se definio un ret con opcode {opcode_1[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	print(f"Se definio un ret con opcode {opcode_2[-1]} en la linea {linea + 1} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode_1, opcode_2)]

def jumps(confirmador, linea, numero):
	confirmador = int(confirmador)
	numero = int(numero)
	literal = bytearray(numero.to_bytes(2,"big"))
	if confirmador == 1:
		opcode = bytearray([0x0, 0x00, 0x3c])
	
	if confirmador == 2:
		opcode = bytearray([0x0, 0x00, 0x3d])

	if confirmador == 3:
		opcode = bytearray([0x0, 0x00, 0x3e])

	if confirmador == 4:
		opcode = bytearray([0x0, 0x00, 0x52])

	if confirmador == 5:
		opcode = bytearray([0x0, 0x00, 0x53])

	if confirmador == 6:
		opcode = bytearray([0x0, 0x00, 0x54])

	if confirmador == 7:
		opcode = bytearray([0x0, 0x00, 0x55])

	if confirmador == 8:
		opcode = bytearray([0x0, 0x00, 0x56])
	
	print(f"Se definio un salto con opcode {opcode[-1]} en la linea {linea} con iteral {numero}")
	print("-------" * 10)
	return [linea, retornar_bytearray(literal, opcode)]


def obtener_posicion_data(lista, nombre):
	for caracter in lista:
		if caracter[0] == nombre:
			valor = caracter[2]
	return int(valor)
	
def obtener_valor_data(lista, nombre):
	for caracter in lista:
		if caracter[0] == nombre:
			valor = caracter[1]
	return int(valor)



contador = 0
contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0
contador_5 = 0
contador_6 = 0
contador_7 = 2
contador_8 = 0
contador_9 = 0
contador_10 = 0
contador_11 = 0
confirmador = False
contador_14 = 0
contador_linea_rom = 0
contador_15 = 0
if len(sys.argv) == 1:
	print("seleccione un .txt")
else:
		#el archivo debe ser un archivo en program_rom, lo que hay que hacer es pasar el archivo, linea por
		#linea usando el program.write

	program_rom = Basys3()
	program_rom.begin()
	archivo = open(sys.argv[1], "r")
	assembler = archivo.read()
	assembler= assembler.split("\n")


	for i in range(4096):
		program_rom.write(i, bytearray([0x00, 0x00, 0x00, 0x00, 0x00]))



	for linea in assembler:
		assembler[contador] = linea.strip()						
		contador += 1


	for linea in assembler:
		if not re.match("CODE:", linea):
			contador_1 += 1
		else:
			datos = assembler[:contador_1]
			codigo = assembler[contador_1:]
			break



	for caracter in datos:
		caracter = re.sub(r"/.+", "", caracter)
		datos[contador_8] = re.sub(r";.+", "", caracter)
		contador_8 += 1


	for caracter in codigo:
		caracter = re.sub(r"/.+", "", caracter)
		codigo[contador_9] = re.sub(r";.+", "", caracter)
		contador_9 += 1

	for linea in codigo:
		codigo[contador_2] = re.sub(' +', '', linea)
		contador_2 += 1


	datos = [caracter for caracter in datos if caracter != '']
	codigo = [caracter for caracter in codigo if caracter != '']

	codigo.pop(0)
	datos.pop(0)



	for i in range(len(datos)):
		if datos[i].endswith(' '):
			datos[i] = datos[i][:-1]

	def reemplazar_hexadecimal_por_decimal(match):
		numero_hexadecimal = match.group()[:-1] 
		numero_decimal = str(int(numero_hexadecimal, 16))  
		return numero_decimal

	def reemplazar_binario_por_decimal(match):
		numero_binario = match.group()[:-1]  
		numero_decimal = str(int(numero_binario, 2))  
		return numero_decimal

	def reemplazar_numeros_por_decimal(match):
		numero = match.group()
		if numero.lower().endswith('d'):
			numero_sin_d = numero[:-1]
			if numero_sin_d.isdigit():
				return numero_sin_d
		return numero

	patron_hexa = re.compile(r'\b[0-9a-fA-F]+h\b')
	patron_binario = re.compile(r'\b[01]+b\b')
	patron_numeros = re.compile(r'\b\d+d\b')

	resultados_modificados = []
	datos_modificados = []

	for caracter in codigo:
		caracter_modificado = caracter
		if re.search(patron_binario, caracter):
			caracter_modificado = re.sub(patron_binario, reemplazar_binario_por_decimal, caracter)
		elif re.search(patron_hexa, caracter):
			caracter_modificado = re.sub(patron_hexa, reemplazar_hexadecimal_por_decimal, caracter)
		elif re.search(patron_numeros, caracter):
			caracter_modificado = re.sub(patron_numeros, reemplazar_numeros_por_decimal, caracter)
		resultados_modificados.append(caracter_modificado)


	for caracter in datos:
		caracter_modificado = caracter
		if re.search(patron_binario, caracter):
			caracter_modificado = re.sub(patron_binario, reemplazar_binario_por_decimal, caracter)
		elif re.search(patron_hexa, caracter):
			caracter_modificado = re.sub(patron_hexa, reemplazar_hexadecimal_por_decimal, caracter)
		elif re.search(patron_numeros, caracter):
			caracter_modificado = re.sub(patron_numeros, reemplazar_numeros_por_decimal, caracter)
		datos_modificados.append(caracter_modificado)

	print(datos_modificados)

	for i, linea in enumerate(datos_modificados):
		if ' ' in linea:
			palabra, resto = linea.split(maxsplit=1)
			palabra = re.sub(r'\s+', ' ', palabra)
			resto = re.sub(r'(\d)\s+', r'\1', resto)
			datos_modificados[i] = f"{palabra} {resto}"
		else:
			datos_modificados[i] = re.sub(r'(\d)\s+', r'\1', linea)



	lista = []
	for linea in datos_modificados:
		
		#listas que van a estar ordenas segun en el orden que se llamaron [[nombre_variable, valor, posicon], [nombre_variable, valor, posicion]]
		#si se crean dos variables con el mismo nombre se considera la ultima
		linea = linea.split(" ")
		if len(linea) == 1:
			lista.append([linea[0], linea[0], contador_3])
		else:
			lista.append([linea[0], linea[-1], contador_3])
		contador_3 += 1

	print("----" * 20)
	print(datos_modificados)
	print("----" * 20)
	print(resultados_modificados)
	print("----" * 20)


	largo_datos = len(datos) * 2
	iterales_jumps = {}
	for caracter in resultados_modificados:
		if caracter[-1] == ":":
			iterales_jumps[caracter[:-1]] = contador_7 + largo_datos + contador_15 - 1
			contador_7 -= 1
		if re.match('pop', caracter, re.I):
			contador_15 += 1
		elif re.match('ret', caracter, re.I):
			contador_15 += 1
		
		contador_7 += 1
	

	print(iterales_jumps)
	print("----" * 20)
	print(lista)
	print("----" * 20)
	for caracter in datos_modificados:
		caracter = caracter.split(" ")
		if len(caracter) == 1:
			escribir = mov(3, contador_linea_rom, caracter[0])
			program_rom.write(escribir[0], escribir[1])
			contador_linea_rom += 1
			escribir = mov(7, contador_linea_rom, contador_14)
			program_rom.write(escribir[0], escribir[1])
		else:
			escribir = mov(3, contador_linea_rom, caracter[1])
			program_rom.write(escribir[0], escribir[1])
			contador_linea_rom += 1
			escribir = mov(7, contador_linea_rom, contador_14)
			program_rom.write(escribir[0], escribir[1])

		contador_14 += 1
		contador_linea_rom += 1
	
	escribir = mov(3, contador_linea_rom, 0)
	program_rom.write(escribir[0], escribir[1])
	contador_linea_rom += 1


	for linea in resultados_modificados:
		if re.match('mov', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")

			if instrucciones[0].upper() == "A":

				if instrucciones[1].upper() == "B":  #--MOV A,B 
					escribir = mov(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"): 
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--MOV A,(B)
						escribir = mov(9, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])
						
					else: #--MOV A, (Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = mov(5, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])

						else:
							escribir = mov(5, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])
						
				else: #--MOV A,Lit
					if instrucciones[1].isdigit(): 
						escribir = mov(3, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])
					else:
						escribir = mov(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])

			


			elif instrucciones[0].upper() == "B":

				if instrucciones[1].upper() == "A": #--MOV B,A
					escribir = mov(2, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--MOV B,(B)
						escribir = mov(10, contador_linea_rom, 0)
						program_rom.write(escribir[0], escribir[1])

					else:
						if instrucciones[1][1:-1].isdigit():
							escribir = mov(6, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])

						else:
							escribir = mov(6, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])
						
				else:
					if instrucciones[1].isdigit():
						escribir = mov(4, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])
					else:
						escribir = mov(4, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])
			

			elif instrucciones[0] == "(B)" or instrucciones[0] == "(b)":
				if instrucciones[1] == "A": #--(B), A
					escribir = mov(11, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				else:  #--(B), Lit
					if instrucciones[1].isdigit():
						escribir = mov(12, contador_linea_rom, instrucciones[1]) 
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = mov(12, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])
			
			else:

				if instrucciones[1] == "A": #--MOV (dir),A
					if instrucciones[0][1:-1].isdigit():
						escribir = mov(7, contador_linea_rom, instrucciones[0][1:-1])
						program_rom.write(escribir[0], escribir[1])
					else:
						escribir = mov(7, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
						program_rom.write(escribir[0], escribir[1])

				else:  #--MOV (Dir), B  
					if instrucciones[0][1:-1].isdigit():
						escribir = mov(8, contador_linea_rom, instrucciones[0][1:-1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = mov(8, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
						program_rom.write(escribir[0], escribir[1])
						

		elif re.match('add', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if len(instrucciones) == 1: #-- ADD (dir)
				if instrucciones[0][1:-1].isdigit():
					escribir = add(7, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])

				else:
					escribir = add(7, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "A":
				if instrucciones[1].upper() == "B": #-- ADD A,B
					escribir = add(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--add A,(B)
						escribir = add(8, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])

					else: #-- ADD A,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = add(5, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])
						else:
							escribir = add(5, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- ADD A, lit
					if instrucciones[1].isdigit():
						escribir = add(3, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = add(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])
						
			elif instrucciones[0].upper() == "B":
				if instrucciones[1].upper() == "A": #-- ADD B,A
					escribir = add(2, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--add B,(B)
						escribir = add(9, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])

					else: #-- ADD B,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = add(6, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])

						else:
							escribir = add(6, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- ADD B, lit
					if instrucciones[1].isdigit():
						escribir = add(4, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])
					else:
						escribir = add(4, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])

		elif re.match('sub', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")

			if len(instrucciones) == 1: #-- sub (dir)
				if instrucciones[0][1:-1].isdigit():
					escribir = sub(7, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])

				else:
					escribir = sub(7, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "A":
				if instrucciones[1].upper() == "B": #-- sub A,B
					escribir = sub(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--sub A,(B)
						escribir = sub(8, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])

					else: #-- sub A,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = sub(5, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])
						else:
							escribir = sub(5, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- sub A, lit
					if instrucciones[1].isdigit():
						escribir = sub(3, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])
					else:
						escribir = sub(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "B":
				if instrucciones[1].upper() == "A": #-- sub B,A
					escribir = sub(2, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--sub B,(B)
						escribir = sub(9, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])

					else: #-- sub B,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = sub(6, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])
						else:
							escribir = sub(6, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- sub B, lit
					if instrucciones[1].isdigit():
						escribir = sub(4, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = sub(4, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])


		elif re.match('and', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if len(instrucciones) == 1: #-- and (dir)
				if instrucciones[0][1:-1].isdigit():
					escribir = f_and(7, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])
				else:		
					escribir = f_and(7, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "A":
				if instrucciones[1].upper() == "B": #-- and A,B
					escribir = f_and(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--and A,(B)
						escribir = f_and(8, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])

					else: #-- and A,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = f_and(5, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])
						else:
							escribir = f_and(5, contador_linea_rom,  obtener_posicion_data(lista,instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- and A, lit
					if instrucciones[1].isdigit():
						escribir = f_and(3, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = f_and(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "B":
				if instrucciones[1].upper() == "A": #-- and B,A
					escribir = f_and(2, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--and B,(B)
						escribir = f_and(9, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])

					else: #-- And B,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = f_and(6, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])
						else:
							escribir = f_and(6, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- And B, lit
					if instrucciones[1].isdigit():
						escribir = f_and(4, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])
					else:
						escribir = f_and(4, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])


		elif re.match('or', linea, re.I):
			linea = linea[2:]
			instrucciones = linea.split(",")
			if len(instrucciones) == 1: #-- or (dir)
				if instrucciones[0][1:-1].isdigit():
					escribir = f_or(7, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])
				else:
					escribir = f_or(7, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "A":
				if instrucciones[1].upper() == "B": #-- or A,B
					escribir = f_or(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--or A,(B)
						escribir = f_or(8, contador_linea_rom, 0)
						program_rom.write(escribir[0], escribir[1])

					else: #-- or A,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = f_or(5, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])
						else:
							escribir = f_or(5, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- or A, lit
					if instrucciones[1].isdigit():
						escribir = f_or(3, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = f_or(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])
						
			elif instrucciones[0].upper() == "B":
				if instrucciones[1].upper() == "A": #-- or B,A
					escribir = f_or(2, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--or B,(B)
						escribir = f_or(9, contador_linea_rom, 0)
						program_rom.write(escribir[0], escribir[1])

					else: #-- or B,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = f_or(6, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])
						else:
							escribir = f_or(6, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- or B, lit
					if instrucciones[1].isdigit():
						escribir = f_or(4, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = f_or(4, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])


		elif re.match('xor', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if len(instrucciones) == 1: #-- xor (dir)
				if instrucciones[0][1:-1].isdigit():
					escribir = xor(7, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])

				else:
					escribir = xor(7, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "A":
				if instrucciones[1].upper() == "B": #-- xor A,B
					escribir = xor(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--xor A,(B)
						escribir = xor(8, contador_linea_rom, 0)
						program_rom.write(escribir[0], escribir[1])

					else: #-- xor A,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = xor(5, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])

						else:
							escribir = xor(5, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- xor A, lit
					if instrucciones[1].isdigit():
						escribir = xor(3, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = xor(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])
						
			elif instrucciones[0].upper() == "B":
				if instrucciones[1].upper() == "A": #-- xor B,A
					escribir = xor(2, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):  
					if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #--add B,(B)
						escribir = xor(9, contador_linea_rom, 0) 
						program_rom.write(escribir[0], escribir[1])

					else: #-- xor B,(Dir)
						if instrucciones[1][1:-1].isdigit():
							escribir = xor(6, contador_linea_rom, instrucciones[1][1:-1])
							program_rom.write(escribir[0], escribir[1])

						else:	
							escribir = xor(6, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
							program_rom.write(escribir[0], escribir[1])

				else: #-- xor B, lit
					if instrucciones[1].isdigit():
						escribir = xor(4, contador_linea_rom, instrucciones[1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = xor(4, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
						program_rom.write(escribir[0], escribir[1])

		elif re.match('not', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if instrucciones[0] == "A":
				if len(instrucciones) == 1:  #-- Not A
					escribir = f_not(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])


			elif instrucciones[0].upper() == "B": #-- Not A, B
				escribir = f_not(2, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0] == "(B)" or instrucciones[0] == "(b)":
				escribir = f_not(4, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			else: #-- Not (Dir), A
				if instrucciones[0][1:-1].isdigit():
					escribir = f_not(3, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])
				else:
					escribir = f_not(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])



		elif re.match('shl', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if instrucciones[0] == "A":
				if len(instrucciones) == 1:  #-- shl A
					escribir = shl(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "B": #-- Shl B
				escribir = shl(2, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0] == "(B)" or instrucciones[0] == "(b)":
				escribir = shl(4, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			else: #-- shl (Dir), A
				if instrucciones[0][1:-1].isdigit():
					escribir = shl(3, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])

				else:
					escribir = shl(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])

		elif re.match('shr', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if instrucciones[0] == "A":
				if len(instrucciones) == 1:  #-- shr A
					escribir = shr(1, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])


			elif instrucciones[0].upper() == "B": #-- shr B
				escribir = shr(2, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])


			elif instrucciones[0] == "(B)" or instrucciones[0] == "(b)":
				escribir = shr(4, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			else: #-- shr (Dir), A
				if instrucciones[0][1:-1].isdigit():
					escribir = shr(3, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])

				else:
					escribir = shr(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])

		elif re.match('inc', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if instrucciones[0].upper() == "A":
				escribir = inc(1, contador_linea_rom, 1)
				program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "B":
				escribir = inc(2, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			elif instrucciones[0].upper() == "(B)":
				escribir = inc(4, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			else:  #-- inc (dir)
				if instrucciones[0][1:-1].isdigit():
					escribir = inc(3, contador_linea_rom, instrucciones[0][1:-1])
					program_rom.write(escribir[0], escribir[1])

				else:
					escribir = inc(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[0][1:-1]))
					program_rom.write(escribir[0], escribir[1])



		elif re.match('dec', linea, re.I):
			linea = linea[3:]
			escribir = dec(1, contador_linea_rom, 1)
			program_rom.write(escribir[0], escribir[1])
 

		elif re.match('cmp', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if instrucciones[1] == "B":       #-- cmp A, B
				escribir = f_cmp(1, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])
			
			elif instrucciones[1].startswith("(") and instrucciones[1].endswith(")"):
				if len(instrucciones[1]) == 3 and (instrucciones[1][1]).upper() == "B": #-- cmp A, (B)
					escribir = f_cmp(4, contador_linea_rom, 0)
					program_rom.write(escribir[0], escribir[1])

				else: #-- cmp A,(dir)
					if instrucciones[1][1:-1].isdigit(): 
						escribir = f_cmp(3, contador_linea_rom, instrucciones[1][1:-1])
						program_rom.write(escribir[0], escribir[1])

					else:
						escribir = f_cmp(3, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1][1:-1]))
						program_rom.write(escribir[0], escribir[1])

			else: #-- cmp A,lit
				if instrucciones[1].isdigit():
					escribir = f_cmp(2, contador_linea_rom, instrucciones[1])
					program_rom.write(escribir[0], escribir[1])

				else:
					escribir = f_cmp(2, contador_linea_rom, obtener_posicion_data(lista, instrucciones[1]))
					program_rom.write(escribir[0], escribir[1])


		elif re.match('push', linea, re.I):
			linea = linea[4:]
			instrucciones = linea.split(",")
			if instrucciones[0].upper() == "A":
				escribir = push(1, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

			else:
				escribir = push(2, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1])

		elif re.match('pop', linea, re.I):
			linea = linea[3:]
			instrucciones = linea.split(",")
			if instrucciones[0].upper() == "A":
				escribir = pop(1, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1][0])
				program_rom.write(escribir[0] + 1, escribir[1][1])

			else:
				escribir = pop(2, contador_linea_rom, 0)
				program_rom.write(escribir[0], escribir[1][0])
				program_rom.write(escribir[0] + 1, escribir[1][1])

			contador_linea_rom += 1
	
		elif re.match('call', linea, re.I):
			linea = linea[4:]
			escribir = call(1, contador_linea_rom, iterales_jumps[linea])
			program_rom.write(escribir[0], escribir[1])

		elif re.match('ret', linea, re.I):
			escribir = ret(1, contador_linea_rom, 0)
			program_rom.write(escribir[0], escribir[1][0])
			program_rom.write(escribir[0] + 1, escribir[1][1])
			contador_linea_rom += 1
			
		
		elif re.match('nop', linea, re.I):
			print(f"Se definio un nop en la linea {contador_linea_rom}")
			print("-------" * 10)
			program_rom.write(contador_linea_rom, bytearray([0x0, 0x00, 0x00, 0x00, 0x00]))


		elif re.match("j", linea, re.I):
			linea = linea[1:]
			if re.match("mp", linea, re.I):
				linea = linea[2:]
				escribir = jumps(1, contador_linea_rom, iterales_jumps[linea])
				program_rom.write(escribir[0], escribir[1])

			elif re.match("eq", linea, re.I):
				linea = linea[2:]
				escribir = jumps(2, contador_linea_rom, iterales_jumps[linea])
				program_rom.write(escribir[0], escribir[1])

			elif re.match("ne", linea, re.I):
				linea = linea[2:]
				escribir = jumps(3, contador_linea_rom, iterales_jumps[linea])
				program_rom.write(escribir[0], escribir[1])

			elif re.match("g", linea, re.I):
				linea = linea[1:]
				if re.match("t", linea, re.I):
					linea = linea[1:]
					escribir = jumps(4, contador_linea_rom, iterales_jumps[linea])
					program_rom.write(escribir[0], escribir[1])

				elif re.match("e", linea, re.I):
					linea = linea[1:]
					escribir = jumps(5, contador_linea_rom, iterales_jumps[linea])
					program_rom.write(escribir[0], escribir[1])

			elif re.match("l", linea, re.I):
				linea = linea[1:]
				if re.match("t", linea, re.I):
					linea = linea[1:]
					escribir = jumps(6, contador_linea_rom, iterales_jumps[linea])
					program_rom.write(escribir[0], escribir[1])

				elif re.match("e", linea, re.I):
					linea = linea[1:]
					escribir = jumps(7, contador_linea_rom, iterales_jumps[linea])
					program_rom.write(escribir[0], escribir[1])

			elif re.match("cr", linea, re.I):
				linea = linea[2:]
				escribir = jumps(8, contador_linea_rom, iterales_jumps[linea])
				program_rom.write(escribir[0], escribir[1])

		elif linea[-1] == ":":
			contador_linea_rom -= 1

		contador_linea_rom += 1
		
	program_rom.end()	
