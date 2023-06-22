import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: gc.py seq_file.txt")
        sys.exit(1)

    gc = {}
    i = 0
    
    # reading the input file
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        # print(lines)
        seq = read_fasta(lines)
        
    # print(seq)
        
    for item in seq:
        gc[item] = compute_gc(seq[item])
    
    # print(seq)
    # print(gc)
    
    # Finds the key of the dictionary with the highest GC value.
    
    max_gc = max(gc, key=lambda key: gc[key])
    
    # Write output to file
    out = open("gc_out.txt", "w")
    out.write(max_gc + "\n" + str('{0:.6f}'.format(gc[max_gc])))
    out.close()
    
    # print output
    print(max_gc)
    print('{0:.6f}'.format(gc[max_gc]))
    # print(max_gc, gc[max_gc])
    
def read_fasta(lines):
    # Takes the lines of the file and reads fasta sequences into a dictionary. If the line starts with '>' it initialises a key in the dictionary and stores it as "currently reading".
    # Then it keeps reading lines of nucleotides until it finds the start of another sequence, stripping the '\n' at the end of each line.
    seq = {}
    i = 0
    while i < len(lines):
        if lines[i][0] == '>':
            current_seq = lines[i][1:14]
            seq[current_seq] = ""
        else:
            seq[current_seq] = seq[current_seq] + lines[i].replace('\n', '')
        i += 1
    
    return seq

    
def compute_gc(s):
    # Count 'G' and 'C' and divide by the total amount of nucleotides (len(sequence)).
    gc = 0
    for n in s:
        if n == 'C' or n == 'G':
            gc += 1
    return (gc / (len(s))) * 100
    
if __name__ == "__main__":
    main()