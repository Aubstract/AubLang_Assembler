
import dictionaries as dict


jumpLabels = {}
varLabels = {}


def replaceLabels(code: list) -> list:
    """Replaces labels with literal values/addresses"""

    # Adds all the variable and jump label names to dictionaries
    lineIndex = 0
    for line in code:
        dataFields = line.split()
        try:
            if dataFields[0] == "var":
                varLabels[dataFields[1]] = dataFields[2]
                lineIndex -= 1
            elif line[0] == "@":
                jumpLabels[dataFields[0]] = "$" + str(lineIndex)
                lineIndex -= 1
        except:
                lineIndex -= 1
        lineIndex += 1

    # Replaces all the variable declarations and jump labels with empty strings
    for lineNum, line in enumerate(code):
        if line.startswith("var"):
            line = ""
        if line.startswith("@"):
            line = ""
        code[lineNum] = line

    # Removes empty strings
    while ("" in code):
        code.remove("")

    # Replaces the labels with their literal values
    for lineNum, line in enumerate(code):
        lineFields = line.strip().split()
        for index, field in enumerate(lineFields):
            if field in varLabels:
                lineFields[index] = varLabels[field]
            elif field in jumpLabels:
                lineFields[index] = jumpLabels[field]
        line = ' '.join(lineFields)
        code[lineNum] = line

    return code


def assemble(code: list) -> list:
    """Converts assembly into machine code"""
    for lineNum, line in enumerate(code):
        
        fields = line.split()

        if fields[0] in {"add","adc","sub","sbc","and","orr","xor","nnd","nor","xnr","jgt","jet","jlt","jge"}:
            opCode = dict.opToBin(fields[0])
            operand1 = dict.addrToBin(fields[1], 5)
            operand2 = dict.addrToBin(fields[2], 5)
            operand3 = dict.addrToBin(fields[3], 2)
            control = dict.cntrlToBin(fields[4])
            code[lineNum] = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "jft":
            opCode = dict.opToBin(fields[0])
            operand1 = dict.addrToBin(fields[1], 5)
            operand2 = fields[2].zfill(5)
            operand3 = "00"
            control = dict.cntrlToBin(fields[3])
            code[lineNum] = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "lit":
            opCode = dict.opToBin(fields[0])
            operand1 = dict.addrToBin(fields[1], 5)
            operand2 = dict.litToBin(fields[2])
            code[lineNum] = opCode + operand1 + operand2

        elif fields[0] in {"inc","dec","lsh","lsc"}:
            opCode = dict.opToBin(fields[0])
            operand1 = dict.addrToBin(fields[1], 5)
            operand2 = dict.addrToBin(fields[2], 5)
            operand3 = "00"
            control = dict.cntrlToBin(fields[3])
            code[lineNum] = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "jmp":
            opCode = dict.opToBin(fields[0])
            operand1 = dict.addrToBin(fields[1], 5)
            operand2 = "00000"
            operand3 = "00"
            control = dict.cntrlToBin(fields[2])
            code[lineNum] = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] in {"ret","hlt"}:
            opCode = dict.opToBin(fields[0])
            operand1 = "00000"
            operand2 = "00000"
            operand3 = "00"
            control = "0"
            code[lineNum] = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "mov":
            opCode = dict.opToBin(fields[0])
            operand1 = dict.addrToBin(fields[1], 5)
            operand2 = dict.addrToBin(fields[2], 5)
            operand3 = "00"
            control = "0"
            code[lineNum] = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "nop":
            opCode = "00000"
            operand1 = "00000"
            operand2 = "00000"
            operand3 = "00"
            control = "0"
            code[lineNum] = opCode + operand1 + operand2 + operand3 + control

    return code