import translator

Infilename1 = "test.TXT"
Infile1 = open(Infilename1, 'r')

Outfilename1= "out.txt"
Outfile1 = open(Outfilename1, 'w')

prime5= raw_input("DNA 5prime sequence? ")
prime3= raw_input("3prime sequence? ")

def truncate(elemDNA):
	prime5.strip("\n")
	prime3.strip("\n")
		
	pos5=elemDNA.find(prime5)
	pos3=elemDNA.find(prime3)+len(prime3) 
	return elemDNA[pos5:pos3]


elemName=""
elemDNA=""
for line in Infile1:
        line = line.strip('\n')
        if line.strip():
		if (line.startswith(">") ):
			line=line.lstrip('>')
			elemDNA=truncate(elemDNA)
			if elemName:
				output=elemName+","+elemDNA+","+translator.translate_dna_single(elemDNA)+"\n"
				Outfile1.write(output)
			#add function to search for patten
			elemName=line
			elemDNA=""
		else:
			elemDNA=elemDNA+line
                 
else:  
	elemDNA=truncate(elemDNA)
	output=elemName+","+elemDNA+","+translator.translate_dna_single(elemDNA)+"\n"
	Outfile1.write(output)               

Infile1.close()
Outfile1.close()

