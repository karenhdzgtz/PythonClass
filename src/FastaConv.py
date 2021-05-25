'''
NOMBRE
	FastaConv.py
	
VERSION
	1.0
	
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>

USO
	python FastaConv.py
	
DESCRIPCION
	Dado un archivo con secuencias de DNA, el programa regresa
	las mismas secuencias del archivo original pero en formato
	fastA, con su correspondiente encabezado, la secuencia
	en mayusculas omitiendo los - que pudiera contener.
	
CATEGORIA
	Archivos fasta
	
DATOS DE ENTRADA Y SALIDA
    Entrada: archivo "4_dna_sequences.txt" con secuencias de DNA
    Salida: archivo "dna_sequences.fasta" con las secuencias en formato fasta
    
EJEMPLOS
    Entrada: seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
    Salida: >seq_1
            ATCGTACGATCGATCGATCGCTAGACGTATCG
	    
LIGAS RELACIONADAS
	GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/FastaConv.py
	
'''


# Leer secuencias del archivo de entrada
file = open("data/4_dna_sequences.txt")
allseq = file.readlines()
file.close()

# Crear archivo de salida para almacenar secuencias en formato fastA
fasta = open("output/dna_sequences.fasta", "w")

# Formatear a fastA cada secuencia del archivo de entrada
for seq in allseq:
	
    # Separar la linea usando el caracter =
    justseq = seq.split(" = ")
	
    #Tomar la secuencia del arreglo y convertirla a mayusculas, quitarle las "" y los - 
    dna = justseq[1].upper().replace('"', '').replace('-', '')
	
    #Escribir en el archivo output la secuencia en formato fastA
    fasta.write(">" + justseq[0] + "\n" + dna)

fasta.close()
