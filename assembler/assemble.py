
import dictionaries as dict


def replace_labels(code: list[object]) -> list[object]:
    """Replaces labels with literal values/addresses"""

    # Adds all the variable and jump label names to dictionaries
    lineIndex = 0
    for lineElement in code:

        line = lineElement.line
        fields = line.split()

        try:
            if fields[0] == "var":
                dict.varLabels[fields[1]] = fields[2]
                lineIndex -= 1
            elif line[0] == "@":
                dict.jumpLabels[fields[0]] = "$" + str(lineIndex)
                lineIndex -= 1
        except:
                lineIndex -= 1
        lineIndex += 1

    # Pops label declaration lines and replaces labels with literals
    for lineNum, lineElement in reversed(list(enumerate(code))):

        line = lineElement.line
        
        if line.startswith("var"):
            code.pop(lineNum)
        elif line.startswith("@"):
            code.pop(lineNum)
        else:
            fields = line.split()

            for index, field in enumerate(fields):
                if field in dict.varLabels:
                    fields[index] = dict.varLabels[field]
                elif field in dict.jumpLabels:
                    fields[index] = dict.jumpLabels[field]
            line = ' '.join(fields)
            code[lineNum].line = line

    return code


def assemble(code: list[object]) -> list[object]:
    """Converts assembly into machine code"""
    for lineNum, lineElement in enumerate(code):

        line = lineElement.line
        fields = line.split()

        if fields[0] in {"add","adc","sub","sbc","and","orr","xor",
                         "nnd","nor","xnr","jgt","jet","jlt","jge"}:
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = dict.address_to_binary(fields[1], 5)
            operand2 = dict.address_to_binary(fields[2], 5)
            operand3 = dict.address_to_binary(fields[3], 2)
            control = dict.control_char_to_binary(fields[4])
            code[lineNum].line = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "jft":
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = dict.address_to_binary(fields[1], 5)
            operand2 = fields[2].zfill(5)
            operand3 = "00"
            control = dict.control_char_to_binary(fields[3])
            code[lineNum].line = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "lit":
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = dict.address_to_binary(fields[1], 5)
            operand2 = dict.literal_to_binary(fields[2])
            code[lineNum].line = opCode + operand1 + operand2

        elif fields[0] in {"inc","dec"}:
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = dict.address_to_binary(fields[1], 5)
            operand2 = dict.address_to_binary(fields[2], 5)
            operand3 = "00"
            control = dict.control_char_to_binary(fields[3])
            code[lineNum].line = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "jmp":
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = dict.address_to_binary(fields[1], 5)
            operand2 = "00000"
            operand3 = "00"
            control = dict.control_char_to_binary(fields[2])
            code[lineNum].line = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] in {"ret","hlt"}:
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = "00000"
            operand2 = "00000"
            operand3 = "00"
            control = "0"
            code[lineNum].line = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] == "mov":
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = dict.address_to_binary(fields[1], 5)
            operand2 = dict.address_to_binary(fields[2], 5)
            operand3 = "00"
            control = "0"
            code[lineNum].line = opCode + operand1 + operand2 + operand3 + control

        elif fields[0] in {"nop","suf","cuf"}:
            opCode = dict.opcode_to_binary(fields[0])
            operand1 = "00000"
            operand2 = "00000"
            operand3 = "00"
            control = "0"
            code[lineNum].line = opCode + operand1 + operand2 + operand3 + control

    return code