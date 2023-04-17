#import packages    

import pandas as pd
from Bio import 

Genome_fasta_file_path = input(str("Enter path to genome fasta file :")) # path to genome fasta file
Protein_table_file_path = input(str("Enter path to protein table : "))
genome = SeqIO.read(Genome_fasta_file_path , "fasta") #Fasta
genome_seq = genome.seq
genome_df = pd.read_csv(Protein_table_file_path) #Csv
start_list = list(genome_df["Start"])
stop_list = list(genome_df["Stop"])

# Create a list of sequences of protein coding regions of the genome

mRNA_seq_list = []

for i in range(0,len(genome_df["Start"])):
    mRNA_seq = genome_seq[genome_df["Start"][i]-1:genome_df["Stop"][i]]
    mRNA_seq = mRNA_seq.transcribe() # Convert to RNA
    if genome_df["Strand"][i] == '-':
        mRNA_seq = mRNA_seq.reverse_complement_rna()
    mRNA_seq_list.append(str(mRNA_seq))
    
# Write a file for the above sequences

fasta_file = open("Human\mRNA_fasta" + Chr + "_output.fasta", "w") #Output file
for i in range(0,len(genome_df["Start"])):
    fasta_file.write(">Human|" + Chr[1:] + "|Genome_ID:" + str(genome_df["Accession"][i]) + "|Codes_for:" + str(genome_df["Protein Name"][i])  + "|Locus_tag:" + str(genome_df["Locus tag"][i]))
    fasta_file.write("\n" + mRNA_seq_list[i] + "\n\n")
fasta_file.close()
