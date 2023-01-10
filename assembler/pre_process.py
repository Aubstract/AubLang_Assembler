import dictionaries as dict

# ----------------CLASSES-------------------------
class Line:
    def __init__(self, line_arg: str, line_num_arg: int):
        self.line = line_arg
        self.line_num = line_num_arg


# ----------------FUNCTIONS------------------------
def get_input() -> tuple[list[str],list[str]]:
    """Gets the contents of a source file, and a list of compiler arguments. (in that order)"""
    code = get_source()
    args = get_args()

    return code, args


def get_source() -> list[str]:
    """Gets a  a text file line by line into a list"""

    file_path = get_file_path()

    with open(file_path, "r") as file:
        contents = file.readlines()

    return contents


def get_file_path() -> str:
    """Prompts user for a file path"""

    file_path = input("\nEnter the path to the source file: ")

    if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:1]

    return file_path


def get_args() -> list[str]:
    """Gets a list of compiler arguments from user and checks their validity"""
    valid_args = False

    while not valid_args:
        line = input("Enter compiler arguments (blank=default): ")
        args = line.split()

        if len(args) == 0:
            valid_args = True
        else:
            for argument in args:
                if argument not in dict.ARG_SET:
                    valid_args = False
                    print("Invalid arguments, please try again")
                    break
                else:
                    valid_args = True

    return args


def construct_lines(code: list[str]) -> list[object]:
    """Takes a list of strings and creates a list of objects, each with two attributes:\n
       - The line of code (str)\n
       - The line number (int)\n
       This allows the debugger to specify the line number in an error message"""

    for line_num, line in enumerate(code):
        code[line_num] = Line(line, line_num)
    
    return code


def sanitize(code: list[object]) -> list[object]:
    """Eliminates comments, empty lines, tabs, double spaces, etc"""

    for line_num, line_object in reversed(list(enumerate(code))):

        line = line_object.line

        line = line.replace("\t", "")
        line = line.replace("  ", " ")

        if "#" in line:
            line = line[: line.index("#")]
        if line.startswith(" "):
            line = line[1:]
        if "\n" in line:
            line = line[: line.index("\n")]
        
        if len(line) == 0:
            code.pop(line_num)
        else:
            code[line_num].line = line

    return code