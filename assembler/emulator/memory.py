import re

# Specialized registers
program_counter = "$0"

flag_register = [0,0,0,0]

return_register = "$0"

plot_x_register = 0

plot_y_register = 0


# General purpose memory
general_registers = {
    "r0" : 0,
    "r1" : 0,
    "r2" : 0,
    "r3" : 0
}


ram = {
    "m0" : 0,
    "m1" : 0,
    "m2" : 0,
    "m3" : 0,
    "m4" : 0,
    "m5" : 0,
    "m6" : 0,
    "m7" : 0
}


# Program memory (values determined at emulator run time)
prom = []


# Constant value / read-only memory
char_memory = {
    "0" : [[1,1,1],
           [1,0,1],
           [1,0,1],
           [1,0,1],
           [1,1,1]],
    "1" : [[0,1,0],
           [1,1,0],
           [0,1,0],
           [0,1,0],
           [1,1,1]],
    "2" : [[],
           [],
           [],
           [],
           []],
    "3" : [[],
           [],
           [],
           [],
           []],
    "4" : [[],
           [],
           [],
           [],
           []],
    "5" : [[],
           [],
           [],
           [],
           []],
    "6" : [[],
           [],
           [],
           [],
           []],
    "7" : [[],
           [],
           [],
           [],
           []],
    "8" : [[],
           [],
           [],
           [],
           []],
    "9" : [[],
           [],
           [],
           [],
           []],
    "A" : [[],
           [],
           [],
           [],
           []],
    "B" : [[],
           [],
           [],
           [],
           []],
    "C" : [[],
           [],
           [],
           [],
           []],
    "D" : [[],
           [],
           [],
           [],
           []],
    "E" : [[],
           [],
           [],
           [],
           []],
    "E" : [[],
           [],
           [],
           [],
           []],
    "F" : [[],
           [],
           [],
           [],
           []],
    "G" : [[],
           [],
           [],
           [],
           []],
    "H" : [[],
           [],
           [],
           [],
           []],
    "I" : [[],
           [],
           [],
           [],
           []],
    "J" : [[],
           [],
           []],
    "K" : [[],
           [],
           []],
    "L" : [[],
           [],
           []],
    "M" : [[],
           [],
           []],
    "N" : [[],
           [],
           []],
    "O" : [[],
           [],
           []],
    "P" : [[],
           [],
           []],
    "Q" : [[],
           [],
           []],
    "R" : [[],
           [],
           []],
    "S" : [[],
           [],
           []],
    "T" : [[],
           [],
           []],
    "U" : [[],
           [],
           []],
    "V" : [[],
           [],
           []],
    "W" : [[],
           [],
           []],
    "X" : [[],
           [],
           []],
    "Y" : [[],
           [],
           []],
    "Z" : [[],
           [],
           []],
    "a" : [[],
           [],
           []],
    "b" : [[],
           [],
           []],
    "c" : [[],
           [],
           []],
    "d" : [[],
           [],
           []],
    "e" : [[],
           [],
           []],
    "f" : [[],
           [],
           []],
    "g" : [[],
           [],
           []],
    "h" : [[],
           [],
           []],
    "i" : [[],
           [],
           []],
    "j" : [[],
           [],
           []],
    "k" : [[],
           [],
           []],
    "l" : [[],
           [],
           []],
    "m" : [[],
           [],
           []],
    "n" : [[],
           [],
           []],
    "o" : [[],
           [],
           []],
    "p" : [[],
           [],
           []],
    "q" : [[],
           [],
           []],
    "r" : [[],
           [],
           []],
    "s" : [[],
           [],
           []],
    "t" : [[],
           [],
           []],
    "u" : [[],
           [],
           []],
    "v" : [[],
           [],
           []],
    "w" : [[],
           [],
           []],
    "x" : [[],
           [],
           []],
    "y" : [[],
           [],
           []],
    "z" : [[],
           [],
           []],
    "." : [[],
           [],
           []],
    "," : [[],
           [],
           []],
    ":" : [[],
           [],
           []],
    ";" : [[],
           [],
           []],
    "!" : [[],
           [],
           []],
    "?" : [[],
           [],
           []],
    "+" : [[],
           [],
           []],
    "-" : [[],
           [],
           []],
    "*" : [[],
           [],
           []],
    "/" : [[],
           [],
           []],
    "=" : [[],
           [],
           []],
    " " : [[],
           [],
           []],
    "\m" : [[],
            [],
            []],
    "\c" : [[],
            [],
            []],
    "\p" : [[],
            [],
            []],
    "\s" : [[],
            [],
            []]
}


# Getter functions
def get_memory(address: str) -> int:
    if address in {"r0","r1","r2","r3"}:
        return get_general_register(address)
    else:
        return get_ram(address)

def get_program_counter() -> str:
    return program_counter

def get_flag_register(position: int) -> int:
    return flag_register[position]

def get_return_register() -> str:
    return return_register

def get_plot_x_register() -> int:
    return plot_x_register

def get_plot_y_register() -> int:
    return plot_y_register

def get_general_register(address: str) -> int:
    return general_registers[address]

def get_ram(address: str) -> int:
    return ram[address]

def get_instruction() -> str:
    address = get_program_counter()
    numerical_address = int("".join((re.findall("\\$(\\d+)", address))))
    return prom[numerical_address].line

def get_char(code: str) -> list[list[int]]:
    return char_memory[code]


# Setter functions
def set_memory(address: str, value: int) -> None:
    if address in {"r0","r1","r2","r3"}:
        set_general_register(address, value)
    else:
        set_ram(address, value)

def set_program_counter(address: int) -> None:
    global program_counter
    program_counter = address

def set_flag_register(output: int) -> None:
    if output > 255:
        set_flag(0, 1)
    if output == 0:
        set_flag(1, 1)
    if get_binary(output, 8).startswith("1"):
        set_flag(2, 1)

def set_user_flag(value: int) -> None:
    set_flag(3, value)

def set_flag(position: int, value: int) -> None:
    global flag_register
    flag_register[position] = value

def set_return_register(address: str) -> None:
    global return_register
    return_register = address

def set_plot_x_register(value: int) -> None:
    global plot_x_register
    plot_x_register = value

def set_plot_y_register(value: int) -> None:
    global plot_y_register
    plot_y_register = value

def set_general_register(address: str, value: int) -> None:
    global general_registers
    general_registers[address] = value

def set_ram(address: str, value: int) -> None:
    global ram
    ram[address] = value

def set_prom(program: list[object]) -> None:
    global prom
    prom = program

# From: https://stackoverflow.com/questions/12946116/twos-complement-binary-in-python
def get_binary(n: int, bits: int) -> str:
    """Converts 'n' to binary, and fills w/ 0 till the output has 'bits' digits"""
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)