import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage hamm.py input.txt")
        sys.exit(1)

    with open(sys.argv[1]) as file:
        lines = file.readlines()
        # print(lines)
        
    lines[0].replace('\n', '')
    hamm = 0
    i = 0
    n = list(zip(lines[0], lines[1]))
    # print(n)
    
    for i in n:
        if i[0] != i[1]:
            hamm += 1
    
    print(hamm)
    
        
if __name__ == "__main__":
    main()