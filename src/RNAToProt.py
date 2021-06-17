'''
NOMBRE
	RNAToProt.py
VERSION
	1.0
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
	Repositorio en GitHub: https://github.com/karenhdzgtz/PythonClass/blob/master/src/RNAToProt.py
DESCRIPCION
	Programa que traduce una secuencia de RNA en
	una de proteina usando tripletes y el codigo genetico
CATEGORIA
	Traduccion
DATOS DE ENTRADA Y SALIDA
    Entrada: secuencia de RNA
    Salida: Secuencia de aminoacidos
EJEMPLOS
    Entrada: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
    Salida:  MAMAPRTEINSTRING

'''


#Definimos el diccionario con el codigo genetico
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


#Definimos la string para guardar la proteina
prot = ''

#Pedimos y guardamos la secuencia de RNA convertida a mayusculas
print("Ingresa una cadena de RNA:")
rna = input().upper()

#Como el diccionario tiene T, convertimos las U a T
rna = rna.replace('U', 'T')

#Creamos un loop para verificar los tripletes
for j in range(0,len(rna),3):

    #Sacamos subcadenas de 3 nucelotidos
    trip = rna[j:j+3]

    #Al llegar al codon de paro salimos del ciclo
    #Imrpimimos lo que llevamos traducido
    if gencode[trip] == '_':
        break

    prot = prot + gencode[trip]

print(f'\nLa secuencia de aminoacidos es:{prot}')
