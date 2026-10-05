def read_input(file):
    with open(file, "r") as f:
        return f.readlines()

def write_output(file, lines):
    with open(file, "w") as f:
        for line in lines:
            f.write(line + "\n")