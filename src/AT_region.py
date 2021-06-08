'''
NOMBRE
	Contenido_ATGC.py
VERSION
	1.0
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
	Repositorio en GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/AT_region.py
DESCRIPCION
	Programa que a partir de una secuencia de nucleotidos
	introducida por el usuario, de unicamente contener nucleotidos
	imprime el las regiones ricas en AT, de lo contrario muestra
	los caracteres ambiguos en la secuencia.
CATEGORIA
	Secuencia genomica
DATOS DE ENTRADA Y SALIDA
    Entrada: secuencia de DNA
    Salida: Op1. Letras ambiguas de la secuencia de DNA con su posicion
            Op2. Fragmento de la secuencoa con la region rica en AT
EJEMPLOS
    Entrada: AAGGATGTCGCGCGTTATTAGCCTAA
    Salida:  Op1. Se encontraron las siguientes ambiguedades:
                n en la posicion 25 ...
             Op2. Se encontraron las siguientes regiones ricas en AT:
                ATTATT ...
'''

#Para usar regex
import re

#Funcion para verificar que la secuencia no tenga ambiguedades
def inspect(dna):

    #Estamos condicionando esto solo para las que contengan ATGC
    #Sacar e imprimir las regiones de AT
    if not re.search(r"[^ATGC]", dna):
        at_regs = re.finditer(r"(A|T){5,}", dna)
        print("Se encontraron las siguientes regiones ricas en AT:")
        for at_reg in at_regs:
            print(at_reg.group())

    #Imprimir las bases ambiguas junto con su posicion
    else:
        ambigs = re.finditer(r"[^ATGC]", dna)
        print("Se encontraron las siguientes ambiguedades en la secuencia:")
        for ambig in ambigs:
            base = ambig.group()
            pos = ambig.start()
            print(f"{base} en la posicion {pos}")
        print("Asegurate que tu secuencia solo contenga ATCG e intentalo de nuevo")


#Pedimos la cadena de DNA
print("Inserta la secuencia de DNA que quieres analizar:")
dna_seq = input()

#Llamamos a la funcion que revisa las regiones ricas AT
inspect(dna_seq)


