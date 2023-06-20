seq = input("Input sequence:")
a_count = 0
c_count = 0
g_count = 0
t_count = 0
for c in seq:
    if c == 'A':
        a_count += 1
    elif c == 'C':
        c_count += 1
    elif c == 'G':
        g_count += 1
    elif c == 'T':
        t_count += 1

print(a_count, c_count, g_count, t_count)
