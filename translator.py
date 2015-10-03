gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'q', 'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}


# a function to translate a single codon
def translate_codon(codon):
    return gencode.get(codon.upper(), 'x')
 
# a function to split a sequence into codons
def split_into_codons(dna, frame):
    codons = []
    for i in range(frame - 1, len(dna)-2, 3):
        codon = dna[i:i+3]
        codons.append(codon)
    return codons
 
# a function to translate a dna sequence in a single frame
def translate_dna_single(dna, frame=1):
    codons = split_into_codons(dna, frame)
    amino_acids_seperate = ''
    for codon in codons:
        amino_acids_seperate = amino_acids_seperate +","+ translate_codon(codon)
    amino_acids_whole=amino_acids_seperate.replace(",","")
    return amino_acids_whole+','+amino_acids_seperate
    #return amino_acids_whole
 
# a function to translate a dna sequence in 3 forward frames
def translate_dna_3frame(dna):
    all_translations = []
    for frame in range(1,4):
        all_translations.append(translate_dna_single(dna, frame))
    return all_translations

def reverse_complement(dna):
	baseComplement={'A':"T", 'C':'G', 'T':'A','G':'C','N':'N' }
	return ''.join(baseComplement[base] for base in reversed(dna))		
