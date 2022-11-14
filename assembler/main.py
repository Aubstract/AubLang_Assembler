# 2nd version of the AubLang assembler
# By Aubrey Fields
# Start date: 10/16/2022
# End date: 10/26/2022


import codeCleaner
import debugger
import assembler
import generateSchematic as schem


def main():
    sourcePath = input("Paste the path to the source file: ")
    code = fileParse(sourcePath)

    code = debugger.constructLines(code)
    
    code = codeCleaner.cleanLines(code)
    debugger.debug(code)

    code = assembler.replaceLabels(code)
    debugger.debugLiteral(code)

    code = assembler.assemble(code)
    debugger.debugMachineCode(code)

    schem.generateSchem(code)

    printSummary(code)


def fileParse(filePath: str) -> list[str]:
    """Reads a file into a list"""

    if filePath.startswith('"'):
        filePath = filePath[1:]
    if filePath.endswith('"'):
        filePath = filePath[:1]

    file = open(filePath, "r")
    contents = file.readlines()
    file.close()

    return contents


def printSummary(code: list[object]):
    """Prints a report on the program once it is assembled"""

    print("\n~~~~~~~~~~~~~~~~~~~~ successfully assembled ~~~~~~~~~~~~~~~~~~~~\n")
    print("Output file name: output.schem\n")
    print(f"Program length: {len(code)} lines")
    print(f"jumpLabel Dictionary:\n{assembler.jumpLabels}")
    print(f"varLabel Dictionary:\n{assembler.varLabels}")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


main()