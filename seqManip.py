#! /usr/bin/env python


#python magic which combines different base combinations with the string of AA characters
#makes a dictionary
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

#function which returns rna equivalent for passed sequence
def rnaEquivalent(sequence):
	sequence=sequence.replace("A","U")
	return sequence

#function which returns reverse complement for passed sequence
def findComplement(sequence):
	#makes a blank string that complementary characters will be added to
	reverseComplement=""
	
	"""loops through sequence from the last position to first
	switch case for each possible base
	adds complementary base to reverseComplement string"""
	for base in sequence[::-1]:
		if base == "A":
			reverseComplement += "T"
		elif base =="C":
			reverseComplement += "G"
		elif base =="G":
			reverseComplement += "C"
		else:
			reverseComplement += "A"
			
	#returns a string representing the reverse complement of the passed sequence
	return reverseComplement
		
#function which returns amino acid equivalent for passed dna sequence
def translate(sequence):
	aaSequence=""
	codonList=[]
	
	for x in range(len(sequence))[::3]:
		codon=sequence[x:x+3]
		if len(codon) == 3:
			aaSequence += codon_table[codon]
			codonList.append(codon)
			
	return aaSequence,codonList
	
	

#define dna sequence, format string
seq="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
seq=seq.strip("\n").upper()

print "seq:\n",seq

print "The length of the stored sequence is", str(len(seq)),"characters"

rnaSeq = rnaEquivalent(seq)

print "rnaSeq:\n",rnaSeq

revCompSeq = findComplement(seq)

print "revCompSeq:\n",revCompSeq

aaSeq,codons = translate(seq)

print "bases in codons 13 and 14:\n", codons[12] + codons[13]

print "total aaSeq:\n", aaSeq


