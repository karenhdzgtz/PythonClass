'''
NOMBRE
	Contenido_ATGC.py
VERSION
	1.0
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
	Repositorio en GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/Contenido_ATGC.py
DESCRIPCION
	Dada una secuencia de DNA introducida por el usuario,
	el programa se encarga de calcular la cantidad de nucleotidos
	A, T, C, G presentes en toda la secuencia
CATEGORIA
	Secuencia genomica
DATOS DE ENTRADA Y SALIDA
    Entrada: secuencia de DNA
    Salida: cantidad de los 4 nucleotidos
EJEMPLOS
    Entrada: AAGGAUGTCGCGCGTTATTAGCCTAA
    Salida: Cantidad de A: 7, Cantidad de C: 5, etc.
'''


#Programa para contar contenido de A,T,C,G de una secuencia
print("Introduce una secuencia de DNA para contar la cantidad de nucelotidos que contiene:")
seq = input()
print('Cantidad de A: ', seq.count('A'))
print('Cantidad de C: ', seq.count('C'))
print('Cantidad de G: ', seq.count('G'))
print('Cantidad de T: ', seq.count('T'))


