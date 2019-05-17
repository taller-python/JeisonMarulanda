"""Taller python"""
def palindromo(palabra):
    """Funcion palindromo"""
    palabra1 = palabra.lower().replace(" ", "")
    palabra2 = ""
    total = len(palabra1)
    for x in palabra1:
        total = total-1
        palabra2 = palabra2 + palabra1[total]
    if palabra1 == palabra2:
        print("Si es palindromo")
    else:
        print("No es palindromo")
print("Ingresa la frase para validar si es palindromo: ")
INP = input()
palindromo(INP)
