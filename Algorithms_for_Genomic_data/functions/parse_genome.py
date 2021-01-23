#!/usr/bin/python
# Fastq file has 4 lines for each sequence read
def parse_fastq(filename):
    seqs = []
    quals = []
    with open(filename) as f:
        while True:
            f.readline() # skip name line
            seq = f.readline().rstrip() # read sequence and remove spaces at end
            f.readline() # skip the 3rd line
            qual = f.readline().rstrip()

            if len(seq) == 0:
                break # reached end
                
            seqs.append(seq)
            quals.append(qual)
    
    return seqs, quals

# Fasta file has 2 lines for each sequence read 
def parse_fasta(filename):
    genome = ''
    with open(filename) as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
