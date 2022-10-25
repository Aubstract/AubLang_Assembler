def cleanLines(code: list) -> list:
    """Eliminates comments, empty lines, tabs, double spaces, etc"""

    for lineNum, lineElement in reversed(list(enumerate(code))):

        line = lineElement.line

        line = line.replace("  ", " ")
        line = line.replace("\t", "")

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