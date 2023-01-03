import dictionaries as dict


MAX_PROGRAM_LEN = 32 # Max number of instructions allowed in the program
INSTRUCTION_WIDTH = 18 # Number of bits per instruction


def debug(code: list[object]):
    """Checks that the instructions are formatted correctly and have valid arguments"""

    for element in code:

        # Unpack the members from the objects to make syntax easier
        line = element.line
        lineNum = element.line_num

        tokens = line.split()

        if line.startswith("@"): 
            if len(tokens) != 1:
                printError(invalidArgNum(lineNum, line))

        elif line.startswith("var"):
            if len(tokens) != 3 or tokens[2] not in dict.addrDict:
                printError(invalidArgNum(lineNum, line))
            if tokens[2] not in dict.addrDict:
                printError(invalidAddr(lineNum, line))
        
        elif tokens[0] in dict.opDict:

            if tokens[0] in {"add","adc","sub","sbc","and","orr","xor","nnd","nor","xnr"}:
                if len(tokens) != 5:
                    printError(invalidArgNum(lineNum, line))
                if tokens[4] not in {"True", "true", "False", "false"}:
                    printError(invalidControl(lineNum, line))

            elif tokens[0] in {"jgt","jet","jlt","jge"}:
                if len(tokens) != 5:
                    printError(invalidArgNum(lineNum, line))
                if tokens[4] not in {"True", "true", "False", "false"}:
                    printError(invalidControl(lineNum, line))
                if not tokens[1].startswith("@"):
                    printError(invalidJmpAddr(lineNum, line))

            elif tokens[0] == "jft":
                if len(tokens) != 4:
                    printError(invalidArgNum(lineNum, line))
                if not tokens[1].startswith("@"):
                    printError(invalidJmpAddr(lineNum, line))
                if not (all(c in '01' for c in tokens[2]) and len(tokens[2]) == 4):
                    printError(invalidBinLit(lineNum, line))
                if tokens[3] not in {"True", "true", "False", "false"}:
                    printError(invalidControl(lineNum, line))

            elif tokens[0] == "lit":
                if len(tokens) != 3:
                    printError(invalidArgNum(lineNum, line))
                # If NOT((string has two ' marks AND is in charDict) OR (string has zero ' marks AND is a number between -128 and 256))
                if not (
                        ((tokens[2].startswith("'") and tokens[2].endswith("'") and tokens[2].count("'") == 2) and tokens[2].strip("'") in dict.charDict) 
                        or (tokens[2].count("'") == 0 and tokens[2].lstrip("-").isnumeric() and int(tokens[2]) <= 255 and int(tokens[2]) >= -128)
                        ):
                    printError(invalidLit(lineNum, line))

            elif tokens[0] in {"inc","dec"}:
                if len(tokens) != 4:
                    printError(invalidArgNum(lineNum, line))
                if tokens[3] not in {"True", "true", "False", "false"}:
                    printError(invalidControl(lineNum, line))

            elif tokens[0] == "jmp":
                if len(tokens) != 3:
                    printError(invalidArgNum(lineNum, line))
                if not tokens[1].startswith("@"):
                    printError(invalidJmpAddr(lineNum, line))
                if tokens[2] not in {"True", "true", "False", "false"}:
                    printError(invalidControl(lineNum, line))

            elif tokens[0] in {"ret","hlt"}:
                if len(tokens) != 1:
                    printError(invalidArgNum(lineNum, line))

            elif tokens[0] == "mov":
                if len(tokens) != 3:
                    printError(invalidArgNum(lineNum, line))

            elif tokens[0] in {"nop","suf","cuf"}:
                if len(tokens) != 1:
                    printError(invalidArgNum(lineNum, line))

        else:
            printError(invalidOp(lineNum, line))


def debugLiteral(code: list[object]):
    """Checks that all literal addresses are valid"""

    if len(code) > MAX_PROGRAM_LEN:
        printError(invalidProgramLen(len(code)))

    for lineElement in code:

        line = lineElement.line
        lineNum = lineElement.line_num
        
        tokens = line.split()

        # filter() info: https://www.geeksforgeeks.org/filter-in-python/

        if tokens[0] in {"add","adc","sub","sbc","and","orr","xor","nnd","nor","xnr"}:
            for n in range(1, 2):
                if not tokens[n] in filter(inRegs5, dict.addrDict):
                    printError(invalidLitAddr(line, lineNum))
            if not tokens[3] in filter(inRegs2, dict.addrDict):
                printError(invalidLitAddr(line, lineNum))
            
        elif tokens[0] in {"jgt","jet","jlt","jge"}:
            if not tokens[1] in filter(inJmpAddr, dict.addrDict):
                    printError(invalidLitAddr(line, lineNum))
            if not tokens[2] in filter(inRegs5, dict.addrDict):
                printError(invalidLitAddr(line, lineNum))
            if not tokens[3] in filter(inRegs2, dict.addrDict):
                printError(invalidLitAddr(line, lineNum))

        elif tokens[0] == "jft":
            if not tokens[1] in filter(inJmpAddr, dict.addrDict):
                printError(invalidLitAddr(line, lineNum))

        elif tokens[0] == "lit":
            if not tokens[1] in filter(inAddrSpace, dict.addrDict):
                printError(invalidLitAddr(line, lineNum))

        elif tokens[0] in {"inc","dec"}:
           for n in range(1, len(tokens) - 1):
                if not tokens[n] in filter(inRegs5, dict.addrDict):
                    printError(invalidLitAddr(line, lineNum))

        elif tokens[0] == "jmp":
            if not tokens[1] in filter(inJmpAddr, dict.addrDict):
                printError(invalidLitAddr(line, lineNum))

        elif tokens[0] == "mov":
            for n in range(1, len(tokens)):
                if not tokens[n] in filter(inAddrSpace, dict.addrDict):
                    printError(invalidLitAddr(line, lineNum))


def debugMachineCode(code: list[object]):
    """Checks that the machine code is valid"""

    # In the event of a wierd edge case, this is a last check of validity
    for lineElement in code:

        line = lineElement.line
        lineNum = lineElement.line_num

        if len(line) > INSTRUCTION_WIDTH:
            printError(f"Machine code line {lineNum} is too long \nIt is {len(line)} bits long")
        if not(all(c in '01' for c in line)):
            printError(f"Machine code line {lineNum} has invalid characters \nLine: {line}")


def printError(error: str):
    print("\n############################# ERROR #############################\n")
    print(error)
    print("\n#################################################################\n")
    quit()


def inRegs2(var: dict) -> bool:
    registers = {"r0", "r1", "r2", "r3"}
    if var in registers:
        return True
    else:
        return False

def inRegs5(var: dict) -> bool:
    registers = {"r0", "r1", "r2", "r3", "disp"} # disp is there so that operating on a value of 0 is allowed
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


def invalidProgramLen(length: int):
    """Generates an error message saying:\n
       Program is too long, it must be ___ lines at most"""

    return f"Program is too long, it must be {MAX_PROGRAM_LEN} lines at most\nProgram length: {length}"


def invalidArgNum(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid number of arguments on line: ___\n
       Line: ___"""

    return f"Invalid number of arguments on line: {lineNum + 1} \nLine: {line}"


def invalidControl(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Unrecognized control character on line: ___\n
       Line: ___"""

    return f"Unrecognized control character on line: {lineNum + 1} \nLine: {line}"


def invalidJmpAddr(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid jump address on line: ___\n
       Line: ___"""

    return f"Invalid jump address on line: {lineNum + 1} \nLine: {line}"


def invalidAddr(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Unrecognized address on line: ___\n
       Line: ___"""

    return f"Unrecognized address on line: {lineNum + 1} \nLine: {line}"


def invalidBinLit(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid characters on line: ___\n
       Line: ___\n
       Argument 3 should contain only binary (1s and 0s) and should be 3 digits long"""

    return f"Invalid characters on line: {lineNum + 1} \nLine: {line} \nArgument 3 should contain only binary (1s and 0s) and should be 3 digits long"


def invalidLit(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid literal on line: ___\n
       Line: ___"""

    return f"""Invalid literal on line: {lineNum + 1} \nLine: {line}"""


def invalidOp(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Unrecognized operation on line: ___\n
       Line: ___"""
    
    return f"Unrecognized operation on line: {lineNum + 1} \nLine: {line}"


def invalidLitAddr(line: str, lineNum: int) -> str:
    """Generates an error message saying:\n
       Invalid literal address on line: ___\n
       Line: ___"""

    return f"Invalid literal address on line: {lineNum} \nLine: {line}"