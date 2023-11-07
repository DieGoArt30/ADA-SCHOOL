# 1) Crear un nuevo repositorio en tu Github para alamcenar este y sucesivos proyectos del curso.
# 2) Crea un nuevo archivo .py
# 3) Define una variable de cada tipo de primitivo:
texto = "tipo texto,"
numeros_entero = 30
numeros_decimales = 30.30
valores_veradero_falso = True # Variable booleana (verdadero o falso)

#   -Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, 
#       guarda el resultado en una variable.
resultado = texto + " tipo entero, " + str(numeros_entero) + " tipo decimal, " +  str(numeros_decimales) + " tipo booleano, " + str(valores_veradero_falso)
print(resultado)

"""
A - Investigar sobre los límites de los enteros y flotantes en Python.
B - Los enteros en Python no tienen un límite superior en la teoría, pero
     en la práctica están limitados por la memoria disponible.
C - Los flotantes en Python utilizan el estándar IEEE 754 de punto flotante
     de doble precisión y tienen un límite de alrededor de 1.8 × 10^308.
"""
# Aplicar la fórmula de la suma de los primeros n números pares
n = 10  # Puedes cambiar este valor para calcular la suma de los primeros n números pares.
suma_pares = n * (n + 1)  # La fórmula de la suma de los primeros n números pares.

# Imprimir el resultado de la suma de los primeros n números pares
print("La suma de los primeros", n, "números pares es:", suma_pares)



