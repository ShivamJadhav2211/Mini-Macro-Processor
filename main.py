from pass1 import pass1
from pass2 import pass2
from utils import read_input, write_output
from tables import MNT, MDT

def main():
    lines = read_input("input.txt")

    print("Running Pass 1...")
    if not pass1(lines):
        return

    print("MNT:", MNT)
    print("MDT:", MDT)

    print("\nRunning Pass 2...")
    result = pass2(lines)

    if result:
        print("\nExpanded Output:")
        for line in result:
            print(line)

        write_output("output.txt", result)

if __name__ == "__main__":
    main()