# Specialized registers
instruction_register = 0

flag_ragister = [0,0,0,0]

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


# Read-only memory
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


# Getter/setter functions
def get_instruction_register() -> int:
       return instruction_register

def get_flag_register(position: int) -> int:
       return flag_ragister[position]

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

def get_char(code: str) -> list[list[int]]:
       return char_memory[code]

def set_instruction_register(address: int) -> None:
       global instruction_register
       instruction_register = address

def set_flag_register(position: int, value: int) -> None:
       global flag_ragister
       flag_ragister[position] = value

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