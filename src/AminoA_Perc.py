'''
NOMBRE
	AminoA_Perc.py
VERSION
	1.0
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
	Repositorio en GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/AminoA_Perc.py
DESCRIPCION
	Dada una secuencia proteica y una lista de aminoacidos introducida
	por el usuario, el programa se encarga de calcular el porcentaje de
	los aminoacidos de la lista en la secuencia.
CATEGORIA
	Secuencia proteica
DATOS DE ENTRADA Y SALIDA
    Entrada: secuencia proteica y lista de aminoacidos
    Salida: porcentaje de aminoacido(s) en la secuencia

    NOTA: El programa toma como default los aminoacidos
          hidrofilicos (A, I, L, M, F, W, Y, V)
          en caso de que no introducirse la lista

EJEMPLOS
    Entrada: "MSRSLLLRFLLFLLLLPPLP", ['M', 'L']
    Salida: 55%
'''

#Funcion para calcular el porcentaje de aminoacidos
def get_aa_percentage(protseq, aalist):
    #Inicializamos la variable donde iremos acumulando el porcentaje a 0
    percen = 0
    # Loop para sacar el porcentaje para cada aa en la lista
    for aa in aalist:
        percen += (protseq.count(aa) * 100) / len(protseq)
    #Regresamos el porcentaje
    return(percen)


#Lista de aminoacidos hidrofilicos default para la funcion
hidrofilic = ['A','I','L','M','F','W','Y','V']

#Almacenar la secuencia proteica
print("Introduce una secuencia proteica:")
prot = input()
prot = prot.upper()

#Almacenar la lista de aminoacidos
print("Introduce los aminoacidos de interes, usa el codigo de una letra y separalos por espacios:")
aminoacids = input()
#Generamos la lista de los aminoacidos a partir de la cadena
#Cambiamos a mayusculas para concordar con la secuencia proteica
aminoacids = aminoacids.upper().split()

#El usuario elige si usar la lista de aminoacidos default o la que el introdujo
print("Si quiere usar la lista default de aminoacidos hidrofilicos escriba 1, si quiere usar su lista ponga 0:")
opt = input()
#Llamamos a la funcion para calcular el porcentaje con su respectiva lista de aminoacidos
if opt == '1':
    result = get_aa_percentage(prot, hidrofilic)
else:
    result = get_aa_percentage(prot, aminoacids)

#Imprimimos el porcentaje
print(str(result) + "%")