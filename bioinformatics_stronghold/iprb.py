import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: iprb.py input.txt")
        sys.exit(1)
        
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        print(lines)
    
if __name__ == "__main__":
    main()