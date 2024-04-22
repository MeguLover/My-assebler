import re

datos_modificados = ['21', 'hola       0']
for i, linea in enumerate(datos_modificados):
    if ' ' in linea:
        palabra, resto = linea.split(maxsplit=1)
        palabra = re.sub(r'\s+', ' ', palabra)
        resto = re.sub(r'(\d)\s+', r'\1', resto)
        datos_modificados[i] = f"{palabra} {resto}"
    else:
        datos_modificados[i] = re.sub(r'(\d)\s+', r'\1', linea)

print(datos_modificados)