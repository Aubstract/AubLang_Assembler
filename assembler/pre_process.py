import dictionaries as dict

# ----------------CLASSES-------------------------
class Line:
    def __init__(self, lineArg: str, lineNumArg: int):
        self.line = lineArg
        self.line_num = lineNumArg


# ----------------FUNCTIONS------------------------
def get_input() -> tuple[list[str],list[str]]:
    """Gets the contents of a source file, and a list of compiler arguments. (in that order)"""
    code = get_source()
    args = get_args()

    return code, args


def get_source() -> list[str]:
    """Gets a  a text file line by line into a list"""

    filePath = get_file_path()

    with open(filePath, "r") as file:
        contents = file.readlines()

    return contents


def get_file_path() -> str:
    """Prompts user for a file path"""

    filePath = input("\nEnter the path to the source file: ")

    if filePath.startswith('"') and filePath.endswith('"'):
        filePath = filePath[1:1]

    return filePath


def get_args() -> list[str]:
    """Gets a list of compiler arguments from user and checks their validity"""
    validArgs = False

    while not validArgs:
        line = input("Enter compiler arguments (blank=default): ")
        args = line.split()

        if len(args) == 0:
            validArgs = True
        else:
            for argument in args:
                if argument not in dict.argSet:
                    validArgs = False
                    print("Invalid arguments, please try again")
                    break
                else:
                    validArgs = True

    return args


def construct_lines(code: list[str]) -> list[object]:
    """Takes a list of strings and creates a list of objects, each with two attributes:\n
       - The line of code (str)\n
       - The line number (int)\n
       This allows the debugger to specify the line number in an error message"""

    for lineNum, line in enumerate(code):
        code[lineNum] = Line(line, lineNum)
    
    return code


def sanitize(code: list[object]) -> list[object]:
    """Eliminates comments, empty lines, tabs, double spaces, etc"""

    for lineNum, lineElement in reversed(list(enumerate(code))):

        line = lineElement.line

        line = line.replace("\t", "")
        line = line.replace("  ", " ")

        if "#" in line:
            line = line[: line.index("#")]
        if line.startswith(" "):
            line = line[1:]
        if "\n" in line:
            line = line[: line.index("\n")]
        
        if len(line) == 0:
            code.pop(lineNum)
        else:
            code[lineNum].line = line

    return code