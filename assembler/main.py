# 2nd version of the AubLang assembler
# By Aubrey Fields
# Start date: 10/16/2022
# End date: 10/26/2022


import preCompile
import debug
import assemble
import generateSchematic as schem
import postCompile


def main():
    # Get source file (.aub or .txt) and parse it into a list of strings line by line
    sourcePath = input("Paste the path to the source file: ")
    code = preCompile.fileParse(sourcePath)

    # Take the list of strings and translate it into a list of Lines,
    # where a Line object stores the contents of the string, and the
    # line number (the index + 1), this is used later in debugging
    code = preCompile.constructLines(code)
    
    # Delete comments, empty lines, whitespace, etc
    code = preCompile.sanitize(code)

    # debug() looks for syntax errors, valid arguments, etc and
    # prints an error message if an issue comes up
    debug.debug(code)

    # Replace labels (variables / jump labels) with their literal addresses
    code = assemble.replaceLabels(code)

    # Check to make sure there arent any arguments left that arent literal addresses
    debug.debugLiteral(code)

    # Convert to binary, then make sure the binary is valid
    code = assemble.assemble(code)
    debug.debugMachineCode(code)

    # Use the binary to generate a schematic to paste into Minecraft
    schem.generateSchem(code)

    # Print a report
    postCompile.printSummary(code)


main()