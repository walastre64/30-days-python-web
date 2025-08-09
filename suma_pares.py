# suma_pares.py
numeros = [3, 4, 7, 10, 13, 18]
suma = 0
indice = 0
while indice < len(numeros):
    if numeros[indice] % 2 == 0:
        suma += numeros[indice]
    indice += 1
print("La suma de los pares es:", suma)