# ----------------CLASSES-------------------------
class Line:
    def __init__(self, line: str, lineNum: int):
        self.line = line
        self.line_num = lineNum


# ----------------FUNCTIONS------------------------
def fileParse(filePath: str) -> list[str]:
    """Reads a text file line by line into a list"""

    if filePath.startswith('"') and filePath.endswith('"'):
        filePath = filePath[1:1]

    file = open(filePath, "r")
    contents = file.readlines()
    file.close()

    return contents


def constructLines(code: list[str]) -> list[object]:
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