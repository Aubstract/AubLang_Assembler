# 2nd iteration of the assembler for AubLang v1
# By Aubrey Fields
# Start date: 10/16/2022

import codeCleaner
import debugger
import assembler
import generateSchematic as schem

def main():

    source = input("Paste the path to the source file: ")

    code = fileParse(source)
    code = codeCleaner.cleanLines(code)

    debugger.debug(code)

    code = codeCleaner.finishClean(code)
    code = assembler.replaceLabels(code)

    debugger.debugLiteral(code)

    code = assembler.assemble(code)

    #print(assembler.jumpLabels)
    #print(assembler.varLabels)

    schem.generateSchem(code)


def fileParse(filePath: str) -> list:
    """Reads a file into a list"""

    filePath = filePath.strip('"')

    file = open(filePath, "r")
    contents = file.readlines()
    file.close()

    return contents

main()