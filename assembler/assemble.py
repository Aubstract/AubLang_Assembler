
import dictionaries as dict


def replace_labels(code: list[object]) -> list[object]:
    """Replaces labels with literal values/addresses"""

    # Adds all the variable and jump label names to dictionaries
    line_index = 0
    for line_object in code:

        line = line_object.line
        tokens = line.split()

        try:
            if tokens[0] == "var":
                dict.var_labels[tokens[1]] = tokens[2]
                line_index -= 1
            elif line[0] == "@":
                dict.jump_labels[tokens[0]] = "$" + str(line_index)
                line_index -= 1
        except:
                line_index -= 1
        line_index += 1

    # Pops label declaration lines and replaces labels with literals
    for index, line_object in reversed(list(enumerate(code))):

        line = line_object.line
        
        if line.startswith("var"):
            code.pop(index)
        elif line.startswith("@"):
            code.pop(index)
        else:
            tokens = line.split()

            for index, field in enumerate(tokens):
                if field in dict.var_labels:
                    tokens[index] = dict.var_labels[field]
                elif field in dict.jump_labels:
                    tokens[index] = dict.jump_labels[field]
            line = ' '.join(tokens)
            line = line

    return code


def assemble(code: list[object]) -> list[object]:
    """Converts assembly into machine code"""
    for line_object in code:

        line = line_object.line
        tokens = line.split()

        if tokens[0] in {"add","adc","sub","sbc","and","orr","xor",
                         "nnd","nor","xnr","jgt","jet","jlt","jge"}:
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = dict.address_to_binary(tokens[1], 5)
            operand2 = dict.address_to_binary(tokens[2], 5)
            operand3 = dict.address_to_binary(tokens[3], 2)
            control = dict.control_char_to_binary(tokens[4])
            line = opCode + operand1 + operand2 + operand3 + control

        elif tokens[0] == "jft":
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = dict.address_to_binary(tokens[1], 5)
            operand2 = tokens[2].zfill(5)
            operand3 = "00"
            control = dict.control_char_to_binary(tokens[3])
            line = opCode + operand1 + operand2 + operand3 + control

        elif tokens[0] == "lit":
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = dict.address_to_binary(tokens[1], 5)
            operand2 = dict.literal_to_binary(tokens[2])
            line = opCode + operand1 + operand2

        elif tokens[0] in {"inc","dec"}:
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = dict.address_to_binary(tokens[1], 5)
            operand2 = dict.address_to_binary(tokens[2], 5)
            operand3 = "00"
            control = dict.control_char_to_binary(tokens[3])
            line = opCode + operand1 + operand2 + operand3 + control

        elif tokens[0] == "jmp":
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = dict.address_to_binary(tokens[1], 5)
            operand2 = "00000"
            operand3 = "00"
            control = dict.control_char_to_binary(tokens[2])
            line = opCode + operand1 + operand2 + operand3 + control

        elif tokens[0] in {"ret","hlt"}:
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = "00000"
            operand2 = "00000"
            operand3 = "00"
            control = "0"
            line = opCode + operand1 + operand2 + operand3 + control

        elif tokens[0] == "mov":
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = dict.address_to_binary(tokens[1], 5)
            operand2 = dict.address_to_binary(tokens[2], 5)
            operand3 = "00"
            control = "0"
            line = opCode + operand1 + operand2 + operand3 + control

        elif tokens[0] in {"nop","suf","cuf"}:
            opCode = dict.opcode_to_binary(tokens[0])
            operand1 = "00000"
            operand2 = "00000"
            operand3 = "00"
            control = "0"
            line = opCode + operand1 + operand2 + operand3 + control

    return code