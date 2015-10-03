
Infilename1 = raw_input("Please feed me with input file full name, including extension") or "test.TXT"
Infile1 = open(Infilename1, 'r')

Outfilename1= "allSeq.txt"
Outfile1 = open(Outfilename1, 'w')

Outfilename2= "uniqSeq.txt"
Outfile2 = open(Outfilename2, 'w')

prime5= raw_input("DNA 5prime sequence? ") or "CAGAGCGTT"
prime3= raw_input("DNA 3prime sequence? ") or "GTGAGCAGC"

def truncate(elemDNA):
	prime5.strip("\n")
	prime3.strip("\n")
		
	pos5=elemDNA.find(prime5)
	pos3=elemDNA.find(prime3)+len(prime3) 
	return elemDNA[pos5:pos3]

def unique_DNA(allList):
	uniqList=[]
	for allEntry in allList:
		foundFlag=0
		for uniqEntry in uniqList:
			if allEntry[1]==uniqEntry[2]:
				uniqEntry[0]=str(int(uniqEntry[0])+1)
				foundFlag=1
				break
		if (foundFlag==0):
			tmpList=["1"]
			tmpList.extend(allEntry)
			uniqList.append(tmpList)
	return uniqList


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


def reverse_complement(dna):
        baseComplement={'A':"T", 'C':'G', 'T':'A','G':'C','N':'N' }
        return ''.join(baseComplement[base] for base in reversed(dna))

elemName=''
elemDNA=''
elemList=[]
for line in Infile1:
        line = line.strip('\n')
        if line.strip():
		if (line.startswith(">") ):
			line=line.lstrip('>')
			sense_DNA=truncate(elemDNA)
			if len(sense_DNA)<1:
				sense_DNA=truncate(reverse_complement(elemDNA))
			if elemName:
				output=[elemName,sense_DNA,translator.translate_dna_single(sense_DNA)]
				elemList.append(output)
			#add function to search for patten
			elemName=line
			elemDNA=""
		else:
			elemDNA=elemDNA+line
                 
else:  
	sense_DNA=truncate(elemDNA)
	if len(sense_DNA)<1:
		sense_DNA=truncate(reverse_complement(elemDNA))
	output=[elemName,sense_DNA,translate_dna_single(sense_DNA)]
	elemList.append(output)


Outfile1.write("cloneName,DNA seqeunce, Protein sequence\n")
for allEntry in elemList:
	tmp=",".join(allEntry)+"\n"
	Outfile1.write(tmp)

Outfile2.write("# of duplicates,cloneName,DNA seqeunce, Protein sequence\n")
for uniqSeq in unique_DNA(elemList):
	tmp=",".join(uniqSeq)+"\n"
	Outfile2.write(tmp) 
 

Infile1.close()
Outfile1.close()
Outfile2.close()
