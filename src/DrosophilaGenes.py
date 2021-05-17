'''
NOMBRE
	DrosophilaGenes.py
VERSION
	1.0
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
	Repositorio en GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/DrosophilaGenes.py
DESCRIPCION
    El programa lee y extrae la informacion de los genes de
    Drosophila contenidos en el archivo 6-data.csv. Segun lo
    que se desea verificar respecto a los genes contenidos en
    el archivo, ya sea organismo de procedencia, % de AT, etc.
    es lo que se imprime a pantalla para que el usuario sepa las
    diferentes caracteristicas que poseen los genes del archivo.
CATEGORIA
	Archivo CSV
DATOS DE ENTRADA Y SALIDA
    Entrada: contenido del archivo 6-data.csv
    Salida: Genes que pertenecen a Drosophila melanogaster o Drosophila simulans
            Genes de entre 90 y 110 bases de longitud
            Genes cuyo contenido de AT < 0,5 y cuyo nivel de expresión > 200
EJEMPLOS
    Entrada: **el programa no necesita un input por parte del usuario
    Salida: Genes que pertenecen a Drosophila melanogaster o Drosophila simulans:
            ['...', '...']
            Genes de entre 90 y 110 bases de longitud:
            ['...', '...']
            Genes cuyo contenido de AT < 0,5 y cuyo nivel de expresión > 200:
            ['...', '...']
'''

#Funcion para calcular el % de AT
def AT_Perc(seq):
    total = len(seq)
    at = seq.count("a") + seq.count("t")
    percen = at/total
    return (percen)


#El archivo debe estar dentro de carpeta data (cuidado con la ruta del archivo)
file = open("data/6-data.csv")
#Extraemos del archivo las lineas, una por una
allgenes = file.readlines()
file.close()

#listas donde se guardaran los resultados de las condicionales
genesdros = []
geneslen = []
genesatyexp = []
genesnotmelykh = []

#Loop para revisar las caracteristicas de los diferentes genes en el archivo
for dgene in allgenes:
    #Como la secuencia contiene varios elemento, la dividimos en ellos
    geneinfo = dgene.split(",")
    #Obtener a los genes que pertenecen a melanogaster o simulans
    if geneinfo[0] == "Drosophila melanogaster" or geneinfo[0] == "Drosophila simulans":
        genesdros.append(geneinfo[2])
    #Obtener a los genes de longitud entre 90 y 110
    if len(geneinfo[1]) >= 90 and len(geneinfo[1]) <= 110:
        geneslen.append(geneinfo[2])
    #Sacamos el % de AT
    atper = AT_Perc(geneinfo[1])
    #Obtener los genes con contenido de AT < 0.5 y expresion > 200
    if atper < 0.5 and int(geneinfo[3]) > 200:
        genesatyexp.append(geneinfo[2])
    #Obtener genes que comienzan con k o h y no pertenecen a D. melanogaster
    if (geneinfo[2].startswith("k") or geneinfo[2].startswith("h")) and geneinfo[0] != "Drosophila melanogaster":
        genesnotmelykh.append(geneinfo[2])
    #Verificamos si el contenido de AT es alto, medio o bajo
    if atper > 0.65:
        exlevel = "alto"
    elif atper < 0.45:
        exlevel = "bajo"
    else:
        exlevel = "medio"
    #Imprimimos como es el % de AT para todos los genes
    print(f"El gen {geneinfo[2]} tiene un contenido de AT: {exlevel}")


#Imprimir los resultados de las diferentes condicionales
print(f"\nGenes que pertenecen a D. melanogaster o D. simulans:\n{genesdros}")
print(f"Genes de entre 90 y 110 bases de longitud:\n{geneslen}")
print(f"Genes de cuyo contenido de AT sea <0.5 y cuyo nivel de expresión sea >200:\n{genesatyexp}")
print(f"Genes que no pertenecen a D. melanogaster y cuyo nombre comience con k o h:\n{genesnotmelykh}")