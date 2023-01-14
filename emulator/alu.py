import memory as mem
import display

def operate(instruction: str):
    # Tokenize instruction
    tokens = instruction.split()

    match tokens[0]:
        case "nop":
            pass
        case "add":
            add(tokens)
        case "adc":
            adc(tokens)
        case "inc":
            inc(tokens)
        case "sub":
            sub(tokens)
        case "sbc":
            sbc(tokens)
        case "dec":
            dec(tokens)
        case "and":
            and_(tokens)
        case "orr":
            orr(tokens)
        case "xor":
            xor(tokens)
        case "nnd":
            nnd(tokens)
        case "nor":
            nor(tokens)
        case "xnr":
            xnr(tokens)
        case "suf":
            suf(tokens)
        case "cuf":
            cuf(tokens)
        case "jft":
            jft(tokens)
        case "jgt":
            jgt(tokens)
        case "jet":
            jet(tokens)
        case "jlt":
            jlt(tokens)
        case "jmp":
            jmp(tokens)
        case "ret":
            ret(tokens)
        case "lit":
            lit(tokens)
        case "mov":
            mov(tokens)
        # No hlt() is needed because that is
        # handled in run.run()
        case "jge":
            jge(tokens)
        

def add(tokens: list[str]):
    sum = mem.get_memory(tokens[2]) + mem.get_memory(tokens[3])
    mem.set_memory(tokens[1], sum)
    if tokens[4] == "True":
        mem.set_flag_register(sum)


def adc(tokens: list[str]):
    sum = int(tokens[2]) + int(tokens[3]) + 1
    mem.set_memory(tokens[1], sum)
    if tokens[4] == "True":
        mem.set_flag_register(sum)

def inc(tokens: list[str]):
    sum = int(tokens[2]) + 1
    mem.set_memory(tokens[1], sum)
    if tokens[3] == "True":
        mem.set_flag_register(sum)

def sub(tokens: list[str]):
    pass

def sbc(tokens: list[str]):
    pass

def dec(tokens: list[str]):
    pass

def and_(tokens: list[str]):
    pass

def orr(tokens: list[str]):
    pass

def xor(tokens: list[str]):
    pass

def nnd(tokens: list[str]):
    pass

def nor(tokens: list[str]):
    pass

def xnr(tokens: list[str]):
    pass

def suf(tokens: list[str]):
    pass

def cuf(tokens: list[str]):
    pass

def jft(tokens: list[str]):
    pass

def jgt(tokens: list[str]):
    pass

def jet(tokens: list[str]):
    pass

def jlt(tokens: list[str]):
    pass

def jmp(tokens: list[str]):
    pass

def ret(tokens: list[str]):
    pass

def lit(tokens: list[str]):
    pass

def mov(tokens: list[str]):
    pass

def jge(tokens: list[str]):
    pass