import re#regex replacement eg  load should remain load 
from tables import MNT, MDT

def pass1(lines):
    i = 0
    while i < len(lines):# i is current line number 
        line = lines[i].strip()# remove extra spaces strip is python string function concerts \n to normal 

        if line == "DEFINE":
            i += 1# header is eg  incr(x) this 
            header = lines[i].strip()#move to next line 

            if "(" not in header or ")" not in header:#syntax check 
                print("ERROR: Invalid macro syntax")
                return False

            name = header.split("(")[0].strip()#extract macro name like from incr(x) it extracts incr 

            if name in MNT:
                print(f"ERROR: Duplicate macro '{name}'")
                return False

            params = header[header.find("(")+1:header.find(")")].split(",")#extract parameterss 
            params = [p.strip() for p in params if p.strip() != ""]

            MNT[name] = (len(MDT), len(params))#mnt table  mnt[incr]=(o,1)
            
            i += 1

            while i < len(lines) and lines[i].strip() != "ENDDEF":
                body = lines[i].strip()

                for idx, p in enumerate(params):
                    body = re.sub(rf'\b{p}\b', f"#{idx+1}", body)#X->#1 se rplace kr ra hai 

                MDT.append(body)
                i += 1

            if i >= len(lines):
                print("ERROR: ENDDEF missing")
                return False

        i += 1

    return True