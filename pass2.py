from tables import MNT, MDT

def pass2(lines):
    output = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Skip macro definition
        if line == "DEFINE":
            while i < len(lines) and lines[i].strip() != "ENDDEF":
                i += 1
            i += 1
            continue

        elif "(" in line and ")" in line:
            name = line.split("(")[0].strip()  #extract macro name 

            if name not in MNT:
                print(f"ERROR: Macro '{name}' not defined")
                return None

            args = line[line.find("(")+1:line.find(")")].split(",")
            args = [a.strip() for a in args if a.strip() != ""]

            mdt_index, param_count = MNT[name]

            if len(args) != param_count:  # check param counts 
                print(f"ERROR: Incorrect parameters in '{line}'")
                return None

            # Expand macro
            for j in range(mdt_index, mdt_index + 10):
                if j >= len(MDT):
                    break

                temp = MDT[j]
                for idx, arg in enumerate(args):
                    temp = temp.replace(f"#{idx+1}", arg)  # param replace fetch#1 to fetch A

                output.append(temp)

        else:
            if line != "":
                output.append(line)

        i += 1

    return output