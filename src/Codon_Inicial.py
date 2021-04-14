'''
NOMBRE
	Codon_inicial.py
VERSION
	1.0
AUTOR
	Hernandez Gutierrez Ana Karen <karen_hdzgtz@comunidad.unam.mx>
DESCRIPCION
	Dada una secuencia de DNA introducida por el usuario,
	el programa se encarga de encontrar el codon AUG de inicio
	asi como el codon de paro para devolverle al usuario la posicion
	de inicio y termino de la transcripcion asi como el fragmento que
	sera transcrito.
CATEGORIA
	Secuencia genomica
DATOS DE ENTRADA Y SALIDA
    Entrada: secuencia de DNA con codon de inicio y paro
    Salida: posicion del codon de inicio en la secuencia, posicion del
            codon de paro y la secuencia de DNA transcrita
EJEMPLOS
    Entrada: AAGGATGTCGCGCGTTATTAGCCTAA
    Salida: El codon TAC empieza en la posicion  4  y termina en  26
            Fragmento de RNA que será transcrito (en DNA): TACGTCGCGCGTTATTAGCC
'''

print("Programa para obtener las posiciones de los codones de inicio y paro asi como el transcrito de una secuencia de DNA\n")
print("Introduce una secuencia de DNA (debe tener codon de inicio TAC y codon de paro ATT)")
dna = input()
#Para obtener la posicion del codon inicial
start = dna.find('TAC')
print('El codon de inicio, contando desde 0, empieza en la posicion: ', start)
#Para obtener la posicion del codon de paro
end = (dna.find("ATT")) + 2
print('EL codon de paro, contando desde 0, termina en la posicion: ', end)
#Para obtener el transcrito
transdna = dna[start:end - 2]
transrna = transdna.replace("T", "U")
print('Fragmento que sera transcrito (sin codon de paro) version DNA:', transdna)
print('Fragmento que sera transcrito (sin codon de paro) version RNA:', transrna)
