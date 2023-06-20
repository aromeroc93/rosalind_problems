s = input("Input sequence: ")
t = ""
for n in s:
    if n == 'T':
        t += 'U'
    else:
        t += n

print(t)