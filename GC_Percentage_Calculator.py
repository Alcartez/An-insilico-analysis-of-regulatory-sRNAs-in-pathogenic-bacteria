# Import Packages
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

gc_list = []

df = pd.read_excel("sRNA_Steptococcus.xlsx") # Import metadata

for seq_record in SeqIO.parse("Streptococcus.txt", "fasta"): # Import Fasta
    gc = gc_fraction(seq_record)
    gc_list.append(gc)

df["GC Percentage"] = gc_list # Make new column with GC values

df.to_excel("sRNA_Streptococcus_GC_included.xlsx") # Write
