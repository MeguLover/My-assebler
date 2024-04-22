import re

resultado = ['mova,421d', 'loop:', 'adda,1010b', 'cmpa,10h', 'jneloop', 'cmpa,10h', 'jneend', 'good:', 'movb,AAh', 'jmpend', 'bad:', 'movb,FFh', 'end:']
datos = ['hola 4d', 'var1 11h', 'cueck 01b']

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

for caracter in resultado:
    caracter_modificado = caracter
    if re.search(patron_binario, caracter):
        caracter_modificado = re.sub(patron_binario, reemplazar_binario_por_decimal, caracter)
    elif re.search(patron_hexa, caracter):
        caracter_modificado = re.sub(patron_hexa, reemplazar_hexadecimal_por_decimal, caracter)
    elif re.search(patron_numeros, caracter):
        caracter_modificado = re.sub(patron_numeros, reemplazar_numeros_por_decimal, caracter)
    resultados_modificados.append(caracter_modificado)

print(resultados_modificados)

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
