from Bio import SeqIO
from Bio.SeqUtils import GC

# for record in SeqIO.parse("datasets/rosalind_gc.txt", "fasta"):
#    print(record.id)
    
record_dict = SeqIO.to_dict(SeqIO.parse("datasets/rosalind_gc.txt", "fasta"))
print(record_dict["Rosalind_8155"])  # use any record ID