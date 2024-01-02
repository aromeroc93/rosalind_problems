import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: iprb.py input.txt")
        sys.exit(1)
        
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        
    k = int(lines[0][0])
    m = int(lines[0][2])
    n = int(lines[0][4])
    
    total = k+m+n
    
    
if __name__ == "__main__":
    main()