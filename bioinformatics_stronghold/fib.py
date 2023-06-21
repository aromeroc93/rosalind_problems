n = int(input("Months:"))
k = int(input("Litter size:"))


new_rabbits = [1]
old_rabbits = [0]
i = 0

while i < n-1:
    new_rabbits.append(old_rabbits[i] * k)
    old_rabbits.append(old_rabbits[i] + new_rabbits[i])
    i += 1

print("Rabbit pairs:", old_rabbits[i] + new_rabbits[i])