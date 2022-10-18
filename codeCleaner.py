def cleanCode(code: list) -> list: # Original function, later split into two so that the code could be debugged more easily
    """Removes unwanted characters, comments, empty lines, etc"""

    # Temporarily joins the list into a string, this makes some things easier
    code = ''.join(code)

    # Remove unwanted characters
    while code.find("  ") != -1:
        code = code.replace("  ", " ")
    while code.find("\t") != -1:
        code = code.replace("\t", "")
    while code.find("\n\n") != -1:
        code = code.replace("\n\n", "\n")
    while code.find(" #") != -1:
        code = code.replace(" #", "#")

    code = code.replace("\n ", "\n")

    if code.startswith(" "):
        code = code[1: ]
    if code.endswith(" "):
        code = code[: -1]
    if code.startswith("\n"):
        code = code[1: ]
    if code.endswith("\n"):
        code = code[: -1]

    # Convert code to list
    code = code.split("\n")
    
    # Remove comments (but replaces them with empty strings, which isnt ideal)
    for lineNum, line in enumerate(code):
        if line.startswith("#"):
            line = "" # I tried using code.pop(lineNum), but it removed multiple lines
        if "#" in line:
            line = line[: line.index("#")]
        code[lineNum] = line

    # Removes all empty strings
    while ("" in code):
        code.remove("")

    return code

def cleanLines(code: list) -> list:
    """Only cleans individual lines, it doesnt remove multi-line issues\n
       the reason is to preserve line numbers for the debugger"""
    for lineNum, line in enumerate(code):
        if "#" in line:
            line = line[: line.index("#")] + "\n"
        while line.find("  ") != -1:
            line = line.replace("  ", " ")
        if line.startswith(" "):
            line = line[1:]
        if line.startswith("\n"):
            line = line[1:]
        line = line.replace("\t", "")
        code[lineNum] = line

    return code


def finishClean(code: list) -> list:
    """Finishes cleaning the code"""

    code = ''.join(code)

    # Remove unwanted characters
    while code.find("\n\n") != -1:
        code = code.replace("\n\n", "\n")
    
    code = code.replace("\n ", "\n")
    code = code.replace(" \n", "\n")

    if code.startswith(" "):
        code = code[1: ]
    if code.endswith(" "):
        code = code[: -1]
    if code.startswith("\n"):
        code = code[1: ]
    if code.endswith("\n"):
        code = code[: -1]

    # Convert code to list
    code = code.split("\n")

    while ("" in code):
        code.remove("")

    return code