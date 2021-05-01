'''
NOMBRE
	FastaConv.py
VERSION
	1.0
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
	Repositorio en GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/FastaConv.py
DESCRIPCION
	Dado un archivo con secuencias de DNA, el programa regresa
	las mismas secuencias del archivo original pero en formato
	fasta, con su correspondiente encabezado, la secuencia
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
'''


#El archivo debe estar dentro de carpeta data (cuidado con la ruta del archivo)
file = open("data/4_dna_sequences.txt")
#Extraemos del archivo las lineas, una por una
allseq = file.readlines()
file.close()

#Abrimos en modo escritura el archivo que ccontendra el output
#El archivo fasta resultante se encontrara en la carpeta output
fasta = open("output/dna_sequences.fasta", "w")

#Loop para dar el formato fasta
for seq in allseq:
    #Como la secuencia contiene varios elemento, la dividimos en ellos
    justseq = seq.split(" = ")
    #Convertimos a mayusculas y quitamos las "" y los - a la secuencia
    dna = justseq[1].upper().replace('"', '').replace('-', '')
    #Escribimos en el archivo output la secuencia ya en fasta
    fasta.write(">" + justseq[0] + "\n" + dna)

fasta.close()