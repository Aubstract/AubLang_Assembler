from pre_process import Line

class Tokens:
    def __init__(self, line_num_arg: int) -> None:
        self.line_num = line_num_arg
        self.tokens = {}

    def set_token(self, key: str, value: str) -> None:
        self.tokens[key] = value
    
    def get_token(self, key:str) -> str:
        return self.tokens[key]


def tokenize(code: list[Line]) -> list[Tokens]:
    """Splits a list of Line objects into named tokens"""
    for line_object in code:

        line_num = line_object.line_num
        line = line_object.line
        tokens = line.split()

        line_object = Tokens(line_num)

        if tokens[0] in {"add","adc","sub","sbc","and","orr","xor",
                         "nnd","nor","xnr","jgt","jet","jlt","jge"}:
            line_object.set_token("opcode", tokens[0])
            line_object.set_token("destination", tokens[1])
            line_object.set_token("operand_1", tokens[2])
            line_object.set_token("operand_2", tokens[3])
            line_object.set_token("control_bit", tokens[4])

        elif tokens[0] == "jft":
            line_object.set_token("opcode", tokens[0])
            line_object.set_token("jump_address", tokens[1])
            line_object.set_token("bit_pattern", tokens[2])
            line_object.set_token("control_bit", tokens[3])

        elif tokens[0] == "lit":
            line_object.set_token("opcode", tokens[0])
            line_object.set_token("destination", tokens[1])
            line_object.set_token("literal", tokens[2])

        elif tokens[0] in {"inc","dec"}:
            line_object.set_token("opcode", tokens[0])
            line_object.set_token("destination", tokens[1])
            line_object.set_token("operand_1", tokens[2])
            line_object.set_token("control_bit", tokens[3])

        elif tokens[0] == "jmp":
            line_object.set_token("opcode", tokens[0])
            line_object.set_token("jump_address", tokens[1])
            line_object.set_token("control_bit", tokens[2])

        elif tokens[0] in {"nop","suf","cuf","ret","hlt"}:
            line_object.set_token("opcode", tokens[0])

        elif tokens[0] == "mov":
            line_object.set_token("opcode", tokens[0])
            line_object.set_token("destination", tokens[1])
            line_object.set_token("operand_1", tokens[2])

        elif tokens[0] == "var":
            line_object.set_token("keyword", tokens[0])
            line_object.set_token("var_label", tokens[1])
            line_object.set_token("var_address", tokens[2])

        elif tokens[0].startswith("@"):
            line_object.set_token("jump_label", tokens[0])
    
    return code