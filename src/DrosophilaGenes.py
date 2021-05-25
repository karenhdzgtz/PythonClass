'''
NOMBRE
	DrosophilaGenes.py
	
VERSION
	1.0
	
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
	
	
DESCRIPCION

	Programa que filtra genes en base al nombre del organismo, contenido de AT, nivel de expression
	y longitud de la secuencia.

USO
	python DrosophilaGenes.py
	
CATEGORIA
	Sequence Analysis
	
DATOS DE ENTRADA Y SALIDA

    Entrada: Archivo data/6-data.csv
    		Formato tabular. Columnas:
		1) Nombre de organismo
		2) secuencia de dna
		3) nombre del gene
		4) valor de expresión
		
		Drosophila melanogaster 	actgtgacgtgtactgtacgactatcgatacgtagtactgatcgctactgtaatgcatccatgctgacgtatctaagt 	jdg766 	185
    
    Salida: 
    		Reporte de totales por cada filtro
		
    	    Genes que pertenecen a Drosophila melanogaster o Drosophila simulans
            Genes de entre 90 y 110 bases de longitud
            Genes cuyo contenido de AT < 0,5 y cuyo nivel de expresión > 200
	    
EJEMPLOS

    Entrada: data/6-data.csv es el archivo de datos a leer
    Salida: Genes que pertenecen a Drosophila melanogaster o Drosophila simulans:
            ['...', '...']
            Genes de entre 90 y 110 bases de longitud:
            ['...', '...']
            Genes cuyo contenido de AT < 0,5 y cuyo nivel de expresión > 200:
            ['...', '...']
	    
LIGAS RELACIONADAS
	    GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/DrosophilaGenes.py
'''

def at_content(seq):
    '''
    Calculates the AT content of dna sequence
    :param int seq : sequence for calculating the AT content
    :return float porcen: AT content
    '''
    sequence_length = len(seq)
    at_content = seq.count("a") + seq.count("t")
    at_porcentage = at_content/sequence_length
    return (at_porcentage)


# Leer todas las lineas del archivo de datos
input_file = open("data/6-data.csv")
all_genes = input_file.readlines()
input_file.close()

# Definir los arreglos donde se guardaran los resultados de los filtros [condicionales]
drosophila_genes_filter = []
size_genes_filter = []
expression_genes_filter = []
name_genes_filter = []

# Analizar cada linea con informacion de los genes
for dgene in all_genes:
	
    # Separar por campos usando la , como separador
    gene_info = dgene.split(",")
    
    ### Aplicar los filtros a los genes ###
	
    # Filtrar los genes cuyo organismo sea melanogaster o simulans
    if gene_info[0] == "Drosophila melanogaster" or gene_info[0] == "Drosophila simulans":
        drosophila_genes_filter.append(gene_info[2])
	
    #Filtrar los genes cuya longitud este entre 90 - 110
    if len(gene_info[1]) >= 90 and len(gene_info[1]) <= 110:
        size_genes_filter.append(gene_info[2])
	
    # Filtrar por contenido de AT < 0.5 y nivel deexpresion > 200
    at_porcentage = at_content(gene_info[1])
    if at_porcentage < 0.5 and int(gene_info[3]) > 200:
        expression_genes_filter.append(gene_info[2])
	
    #Filtrar los genes que comienzan con k o h y no pertenecen a D. melanogaster
    if (gene_info[2].startswith("k") or gene_info[2].startswith("h")) and gene_info[0] != "Drosophila melanogaster":
        name_genes_filter.append(gene_info[2])
	
    #Verificar si el contenido de AT es alto, medio o bajo
    if at_porcentage > 0.65:
        exp_level = "alto"
    elif at_porcentage < 0.45:
        exp_level = "bajo"
    else:
        exp_level = "medio"
	
    #Imprimir como es el % de AT para todos los genes
    print(f"El gen {gene_info[2]} tiene un contenido de AT: {exp_level}")


# Reporte de los totales por filtro
print(f"\nGenes que pertenecen a D. melanogaster o D. simulans:\n{drosophila_genes_filter}")
print(f"Genes de entre 90 y 110 bases de longitud:\n{size_genes_filter}")
print(f"Genes de cuyo contenido de AT sea <0.5 y cuyo nivel de expresión sea >200:\n{expression_genes_filter}")
print(f"Genes que no pertenecen a D. melanogaster y cuyo nombre comience con k o h:\n{name_genes_filter}")
