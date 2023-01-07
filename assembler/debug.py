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
                print_error(invalid_num_of_args(lineNum, line))

        elif line.startswith("var"):
            if len(tokens) != 3 or tokens[2] not in dict.addrDict:
                print_error(invalid_num_of_args(lineNum, line))
            if tokens[2] not in dict.addrDict:
                print_error(invalid_address(lineNum, line))
        
        elif tokens[0] in dict.opDict:

            if tokens[0] in {"add","adc","sub","sbc","and",
                             "orr","xor","nnd","nor","xnr"}:
                if len(tokens) != 5:
                    print_error(invalid_num_of_args(lineNum, line))
                if tokens[4] not in {"True", "true", "False", "false"}:
                    print_error(invalid_control_char(lineNum, line))

            elif tokens[0] in {"jgt","jet","jlt","jge"}:
                if len(tokens) != 5:
                    print_error(invalid_num_of_args(lineNum, line))
                if tokens[4] not in {"True", "true", "False", "false"}:
                    print_error(invalid_control_char(lineNum, line))
                if not tokens[1].startswith("@"):
                    print_error(invalid_jump_address(lineNum, line))

            elif tokens[0] == "jft":
                if len(tokens) != 4:
                    print_error(invalid_num_of_args(lineNum, line))
                if not tokens[1].startswith("@"):
                    print_error(invalid_jump_address(lineNum, line))
                if not (all(c in '01' for c in tokens[2]) and len(tokens[2]) == 4):
                    print_error(invalid_binary_literal(lineNum, line))
                if tokens[3] not in {"True", "true", "False", "false"}:
                    print_error(invalid_control_char(lineNum, line))

            elif tokens[0] == "lit":
                literal = tokens[2]
                if len(tokens) != 3:
                    print_error(invalid_num_of_args(lineNum, line))
                # If NOT((string has two ' marks AND is in charDict) 
                # OR (string has zero ' marks AND is a number between -128 and 256))
                if not (((literal.startswith("'") and literal.endswith("'")
                        and literal.count("'") == 2) and literal.strip("'") in dict.charDict)
                        or (literal.count("'") == 0 and literal.lstrip("-").isnumeric()
                        and (int(literal) in range(-128, 256)))):
                    print_error(invalid_literal(lineNum, line))

            elif tokens[0] in {"inc","dec"}:
                if len(tokens) != 4:
                    print_error(invalid_num_of_args(lineNum, line))
                if tokens[3] not in {"True", "true", "False", "false"}:
                    print_error(invalid_control_char(lineNum, line))

            elif tokens[0] == "jmp":
                if len(tokens) != 3:
                    print_error(invalid_num_of_args(lineNum, line))
                if not tokens[1].startswith("@"):
                    print_error(invalid_jump_address(lineNum, line))
                if tokens[2] not in {"True", "true", "False", "false"}:
                    print_error(invalid_control_char(lineNum, line))

            elif tokens[0] in {"ret","hlt"}:
                if len(tokens) != 1:
                    print_error(invalid_num_of_args(lineNum, line))

            elif tokens[0] == "mov":
                if len(tokens) != 3:
                    print_error(invalid_num_of_args(lineNum, line))

            elif tokens[0] in {"nop","suf","cuf"}:
                if len(tokens) != 1:
                    print_error(invalid_num_of_args(lineNum, line))

        else:
            print_error(invalid_operation(lineNum, line))


def debug_literal(code: list[object]):
    """Checks that all literal addresses are valid"""

    if len(code) > MAX_PROGRAM_LEN:
        print_error(invalid_program_len(len(code)))

    for lineElement in code:

        line = lineElement.line
        lineNum = lineElement.line_num
        
        tokens = line.split()

        # filter() info: https://www.geeksforgeeks.org/filter-in-python/

        if tokens[0] in {"add","adc","sub","sbc","and",
                         "orr","xor","nnd","nor","xnr"}:
            for n in range(1, 2):
                if not tokens[n] in filter(in_regs_five_bit, dict.addrDict):
                    print_error(invalid_literal_address(line, lineNum))
            if not tokens[3] in filter(in_regs_two_bit, dict.addrDict):
                print_error(invalid_literal_address(line, lineNum))
            
        elif tokens[0] in {"jgt","jet","jlt","jge"}:
            if not tokens[1] in filter(in_jump_addesses, dict.addrDict):
                    print_error(invalid_literal_address(line, lineNum))
            if not tokens[2] in filter(in_regs_five_bit, dict.addrDict):
                print_error(invalid_literal_address(line, lineNum))
            if not tokens[3] in filter(in_regs_two_bit, dict.addrDict):
                print_error(invalid_literal_address(line, lineNum))

        elif tokens[0] == "jft":
            if not tokens[1] in filter(in_jump_addesses, dict.addrDict):
                print_error(invalid_literal_address(line, lineNum))

        elif tokens[0] == "lit":
            if not tokens[1] in filter(in_addresses, dict.addrDict):
                print_error(invalid_literal_address(line, lineNum))

        elif tokens[0] in {"inc","dec"}:
           for n in range(1, len(tokens) - 1):
                if not tokens[n] in filter(in_regs_five_bit, dict.addrDict):
                    print_error(invalid_literal_address(line, lineNum))

        elif tokens[0] == "jmp":
            if not tokens[1] in filter(in_jump_addesses, dict.addrDict):
                print_error(invalid_literal_address(line, lineNum))

        elif tokens[0] == "mov":
            for n in range(1, len(tokens)):
                if not tokens[n] in filter(in_addresses, dict.addrDict):
                    print_error(invalid_literal_address(line, lineNum))


def debug_machine_code(code: list[object]):
    """Checks that the machine code is valid"""

    # In the event of a wierd edge case, this is a last check of validity
    for lineElement in code:

        line = lineElement.line
        lineNum = lineElement.line_num

        if len(line) > INSTRUCTION_WIDTH:
            print_error(f"Machine code line {lineNum} is too long \nIt is {len(line)} bits long")
        if not(all(c in '01' for c in line)):
            print_error(f"Machine code line {lineNum} has invalid characters \nLine: {line}")


def print_error(error: str):
    print("\n############################# ERROR #############################\n")
    print(error)
    print("\n#################################################################\n")
    quit()


def in_regs_two_bit(var: dict) -> bool:
    registers = {"r0", "r1", "r2", "r3"}
    if var in registers:
        return True
    else:
        return False

def in_regs_five_bit(var: dict) -> bool:
    # disp is there so that operating on a value of 0 is allowed
    registers = {"r0", "r1", "r2", "r3", "disp"}
    if var in registers:
        return True
    else:
        return False


def in_jump_addesses(var: dict) -> bool:
    jmpAddresses = {"$0","$1","$2","$3","$4","$5","$6","$7","$8",
                    "$9","$10","$11","$12","$13","$14","$15","$16",
                    "$17","$18","$19","$20","$21","$22","$23","$24",
                    "$25","$26","$27","$28","$29","$30","$31"}
    if var in jmpAddresses:
        return True
    else:
        return False

def in_addresses(var: dict) -> bool:
    addressSpace = {"r0","r1","r2","r3","m0","m1","m2","m3","m4",
                    "m5","m6","m7","disp","bcd","plotx","ploty"}
    if var in addressSpace:
        return True
    else:
        return False


def invalid_program_len(length: int):
    """Generates an error message saying:\n
       Program is too long, it must be ___ lines at most"""

    return f"Program is too long, it must be {MAX_PROGRAM_LEN} lines at most\nProgram length: {length}"


def invalid_num_of_args(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid number of arguments on line: ___\n
       Line: ___"""

    return f"Invalid number of arguments on line: {lineNum + 1} \nLine: {line}"


def invalid_control_char(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Unrecognized control character on line: ___\n
       Line: ___"""

    return f"Unrecognized control character on line: {lineNum + 1} \nLine: {line}"


def invalid_jump_address(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid jump address on line: ___\n
       Line: ___"""

    return f"Invalid jump address on line: {lineNum + 1} \nLine: {line}"


def invalid_address(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Unrecognized address on line: ___\n
       Line: ___"""

    return f"Unrecognized address on line: {lineNum + 1} \nLine: {line}"


def invalid_binary_literal(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid characters on line: ___\n
       Line: ___\n
       Argument 3 should contain only binary (1s and 0s) and should be 3 digits long"""

    return f"Invalid characters on line: {lineNum + 1} \nLine: {line} \nArgument 3 should contain only binary (1s and 0s) and should be 3 digits long"


def invalid_literal(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Invalid literal on line: ___\n
       Line: ___"""

    return f"""Invalid literal on line: {lineNum + 1} \nLine: {line}"""


def invalid_operation(lineNum: int, line: str) -> str:
    """Generates an error message saying:\n
       Unrecognized operation on line: ___\n
       Line: ___"""
    
    return f"Unrecognized operation on line: {lineNum + 1} \nLine: {line}"


def invalid_literal_address(line: str, lineNum: int) -> str:
    """Generates an error message saying:\n
       Invalid literal address on line: ___\n
       Line: ___"""

    return f"Invalid literal address on line: {lineNum} \nLine: {line}"