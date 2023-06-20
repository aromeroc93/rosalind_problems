s = input("Input sequence: ")

rc = ""

for n in reversed(s):
    if n == 'A':
        rc += 'T'
    elif n == 'T':
        rc += 'A'
    elif n == 'C':
        rc += 'G'
    elif n == 'G':
        rc += 'C'

print("Reverse complement: ", rc)