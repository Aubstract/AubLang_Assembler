# ------------------FUNCTIONS------------------------
# These are essentially getter functions

def opcode_to_binary(opcode: str) -> str:
    """Converts an opcode mnemonic to binary"""
    return get_binary(OPCODE_DICT[opcode],5)


def address_to_binary(address: str, digits: int) -> str:
    """Converts an address mnemonic to a binary number"""
    return get_binary(ADDRESS_DICT[address],digits)


def literal_to_binary(literal: str) -> str:
    """Converts a literal to binary"""

    literal = literal.strip("'")

    if literal.lstrip("-").isnumeric():
        literal = get_binary(int(literal),8)
    else:
        literal = get_binary(CHAR_DICT[literal],8)

    return literal


def control_char_to_binary(control_char: str) -> str:
    """Converts a control mnemonic into binary"""
    
    if control_char in {"true", "True"}:
        control_char = "1"
    else:
        control_char = "0"

    return control_char


# From: https://stackoverflow.com/questions/12946116/twos-complement-binary-in-python
def get_binary(n: int, bits: int) -> str:
    """Converts 'n' to binary, and fills w/ 0 till the output has 'bits' digits"""
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)



# ---------------------SETS-----------------------------
ARG_SET = {
    "print",
    "file",
    "aub",
    "bin",
    "label",
    "all"
}



# -------------VARIABLE DICTIONARIES--------------------
jump_labels = {}
var_labels = {}


# -------------CONSTANT DICTIONARIES--------------------
OPCODE_DICT = {
    "nop" : 0,
    "add" : 1,
    "adc" : 2,
    "inc" : 3,
    "sub" : 4,
    "sbc" : 5,
    "dec" : 6,
    "and" : 7,
    "orr" : 8,
    "xor" : 9,
    "nnd" : 10,
    "nor" : 11,
    "xnr" : 12,
    "suf" : 13,
    "cuf" : 14,
    "jft" : 15,
    "jgt" : 16,
    "jet" : 17,
    "jlt" : 18,
    "jmp" : 19,
    "ret" : 20,
    "lit" : 21,
    "mov" : 22,
    "hlt" : 23,
    "jge" : 24
}


ADDRESS_DICT = {
    "r0" : 0,
    "r1" : 1,
    "r2" : 2,
    "r3" : 3,
    "m0" : 4,
    "m1" : 5,
    "m2" : 6,
    "m3" : 7,
    "m4" : 8,
    "m5" : 9,
    "m6" : 10,
    "m7" : 11,
    "disp" : 12,
    "bcd" : 13,
    "plotx" : 14,
    "ploty" : 15,
    "$0" : 0,
    "$1" : 1,
    "$2" : 2,
    "$3" : 3,
    "$4" : 4,
    "$5" : 5,
    "$6" : 6,
    "$7" : 7,
    "$8" : 8,
    "$9" : 9,
    "$10" : 10,
    "$11" : 11,
    "$12" : 12,
    "$13" : 13,
    "$14" : 14,
    "$15" : 15,
    "$16" : 16,
    "$17" : 17,
    "$18" : 18,
    "$19" : 19,
    "$20" : 20,
    "$21" : 21,
    "$22" : 22,
    "$23" : 23,
    "$24" : 24,
    "$25" : 25,
    "$26" : 26,
    "$27" : 27,
    "$28" : 28,
    "$29" : 29,
    "$30" : 30,
    "$31" : 31
}


CHAR_DICT = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
    "G" : 16,
    "H" : 17,
    "I" : 18,
    "J" : 19,
    "K" : 20,
    "L" : 21,
    "M" : 22,
    "N" : 23,
    "O" : 24,
    "P" : 25,
    "Q" : 26,
    "R" : 27,
    "S" : 28,
    "T" : 29,
    "U" : 30,
    "V" : 31,
    "W" : 32,
    "X" : 33,
    "Y" : 34,
    "Z" : 35,
    "a" : 36,
    "b" : 37,
    "c" : 38,
    "d" : 39,
    "e" : 40,
    "f" : 41,
    "g" : 42,
    "h" : 43,
    "i" : 44,
    "j" : 45,
    "k" : 46,
    "l" : 47,
    "m" : 48,
    "n" : 49,
    "o" : 50,
    "p" : 51,
    "q" : 52,
    "r" : 53,
    "s" : 54,
    "t" : 55,
    "u" : 56,
    "v" : 57,
    "w" : 58,
    "x" : 59,
    "y" : 60,
    "z" : 61,
    "." : 62,
    "," : 63,
    ":" : 64,
    ";" : 65,
    "!" : 66,
    "?" : 67,
    "+" : 68,
    "-" : 69,
    "*" : 70,
    "/" : 71,
    "=" : 72,
    " " : 73,
    "\m" : 74,
    "\c" : 75,
    "\p" : 76,
    "\s" : 77,
}