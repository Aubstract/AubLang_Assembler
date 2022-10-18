import dictionaries as dict

def debug(code: list):
    """Checks that the instructions are formatted correctly and have valid arguments"""
    for lineNum, line in enumerate(code):

        fields = line.split()

        if len(fields) < 1:
            continue

        if line.startswith("@"):
            if len(fields) != 1:
                invalidArgNum(lineNum, line)

        elif line.startswith("var"):
            if len(fields) != 3:
                invalidArgNum(lineNum, line)
            if fields[2] not in dict.addrDict:
                print("\n#######################################################")
                print("Unrecognized address in line:", lineNum + 1)
                print("line:", line, "\n")
                quit()
        
        elif fields[0] in dict.opDict:

            if fields[0] in {"add","adc","sub","sbc","and","orr","xor","nnd","nor","xnr"}:
                if len(fields) != 5:
                    invalidArgNum(lineNum, line)
                if fields[4] not in {"True", "true", "False", "false"}:
                    invalidControl(lineNum, line)

            elif fields[0] in {"jgt","jet","jlt","jge"}:
                if len(fields) != 5:
                    invalidArgNum(lineNum, line)
                if fields[4] not in {"True", "true", "False", "false"}:
                    invalidControl(lineNum, line)
                if not fields[1].startswith("@"):
                    invalidJmpAddr(lineNum, line)

            elif fields[0] == "jft":
                if len(fields) != 4:
                    invalidArgNum(lineNum, line)
                if not fields[1].startswith("@"):
                    invalidJmpAddr(lineNum, line)
                if not (all(c in '01' for c in fields[2]) and len(fields[2]) == 3):
                    print("\n#######################################################")
                    print("Invalid characters in line:", lineNum + 1)
                    print("line:", line)
                    print("Argument 3 should contain only binary (1s and 0s) and should be 3 digits long", "\n")
                    quit()
                if fields[3] not in {"True", "true", "False", "false"}:
                    invalidControl(lineNum, line)

            elif fields[0] == "lit":
                if len(fields) != 3:
                    invalidArgNum(lineNum, line)
                # If NOT((string has two ' marks AND is in charDict) OR (string has zero ' marks AND is a number between -128 and 256))
                if not (((fields[2].startswith("'") and fields[2].endswith("'") and fields[2].count("'") == 2) and fields[2].strip("'") in dict.charDict) 
                       or (fields[2].count("'") == 0 and fields[2].lstrip("-").isnumeric() and int(fields[2]) <= 255 and int(fields[2]) >= -128)):
                    print("\n#######################################################")
                    print("Invalid literal in line:", lineNum + 1)
                    print("Line:", line, "\n")
                    quit()

            elif fields[0] in {"inc","dec","lsh","lsc"}:
                if len(fields) != 4:
                    invalidArgNum(lineNum, line)
                if fields[3] not in {"True", "true", "False", "false"}:
                    invalidControl(lineNum, line) 

            elif fields[0] == "jmp":
                if len(fields) != 3:
                    invalidArgNum(lineNum, line)
                if not fields[1].startswith("@"):
                    invalidJmpAddr(lineNum, line)
                if fields[2] not in {"True", "true", "False", "false"}:
                    invalidControl(lineNum, line)

            elif fields[0] in {"ret","hlt"}:
                if len(fields) != 1:
                    invalidArgNum(lineNum, line)

            elif fields[0] == "mov":
                if len(fields) != 3:
                    invalidArgNum(lineNum, line)

            elif fields[0] == "nop":
                if len(fields) != 1:
                    invalidArgNum(lineNum, line)

        else:
            print("\n#######################################################")
            print("Unrecognized operation on line:", lineNum + 1)
            print("line:", line, "\n")
            quit()

def debugLiteral(code: list):
    """Checks that the addresses are valid"""
    for lineNum, line in enumerate(code):
        
        fields = line.split()

        if fields[0] in {"add","adc","sub","sbc","and","orr","xor","nnd","nor","xnr"}:
            for n in range(1, len(fields) - 1):
                if not fields[n] in filter(inRegs, dict.addrDict):
                    invalidAddr(code, lineNum)
            
        elif fields[0] in {"jgt","jet","jlt","jge"}:
            if not fields[1] in filter(inJmpAddr, dict.addrDict):
                    invalidAddr(code, lineNum)  
            for n in range(2, len(fields) - 1):
                if not fields[n] in filter(inRegs, dict.addrDict):
                    invalidAddr(code, lineNum)

        elif fields[0] == "jft":
            if not fields[1] in filter(inJmpAddr, dict.addrDict):
                invalidAddr(code, lineNum)

        elif fields[0] == "lit":
            if not fields[1] in filter(inAddrSpace, dict.addrDict):
                invalidAddr(code, lineNum)

        elif fields[0] in {"inc","dec","lsh","lsc"}:
           for n in range(1, len(fields) - 1):
                if not fields[n] in filter(inRegs, dict.addrDict):
                    invalidAddr(code, lineNum)

        elif fields[0] == "jmp":
            if not fields[1] in filter(inJmpAddr, dict.addrDict):
                invalidAddr(code, lineNum)

        elif fields[0] == "mov":
            for n in range(1, len(fields)):
                if not fields[n] in filter(inAddrSpace, dict.addrDict):
                    invalidAddr(code, lineNum)

def inRegs(var: dict) -> bool:
     # disp is there so that operating on a value of 0 is allowed
    registers = {"r0", "r1", "r2", "r3", "disp"}
    if var in registers:
        return True
    else:
        return False

def inJmpAddr(var: dict) -> bool:
    jmpAddresses = {"$0","$1","$2","$3","$4","$5","$6","$7","$8",
                    "$9","$10","$11","$12","$13","$14","$15","$16",
                    "$17","$18","$19","$20","$21","$22","$23","$24",
                    "$25","$26","$27","$28","$29","$30","$31"}
    if var in jmpAddresses:
        return True
    else:
        return False

def inAddrSpace(var: dict) -> bool:
    addressSpace = {"r0","r1","r2","r3","m0","m1","m2","m3","m4",
                    "m5","m6","m7","disp","bcd","plotx","ploty"}
    if var in addressSpace:
        return True
    else:
        return False

def invalidArgNum(lineNum: int, line: str):
    """Prints an error message saying:\n
       Invalid number of arguments on line: ___\n
       Line: ___"""

    print("\n#######################################################")
    print("Invalid number of arguments on line:", lineNum + 1)
    print("Line:", line, "\n")
    quit()

def invalidControl(lineNum: int, line: str):
    """Prints an error message saying:\n
       Unrecognized control character in line: ___\n
       Line: ___"""

    print("\n#######################################################")
    print("Unrecognized control character in line:", lineNum + 1)
    print("Line:", line, "\n")
    quit()

def invalidJmpAddr(lineNum: int, line: str):
    """Prints an error message saying:\n
       Invalid jump address in line: ___\n
       Line: ___"""

    print("\n#######################################################")
    print("Invalid jump address in line:", lineNum + 1)
    print("Line:", line, "\n")
    quit()

def invalidAddr(code: list, lineNum: int):
    """Prints an error message saying:\n
       Invalid literal address in line: ___\n
       Surrounding lines: ___"""

    print("\n#######################################################")
    print("Invalid literal address in line:", code[lineNum])
    print("Surrounding lines:")
    if lineNum > 0:
        print(code[lineNum - 1])
    else:
        print("vvv Start of program vvv")
    print(code[lineNum] + " <")
    if lineNum < len(code) - 1:
        print(code[lineNum + 1] + "\n")
    else:
        print("^^^ Last line of program ^^^")
    quit()