# 2nd version of the AubLang assembler
# By Aubrey Fields
# Start date: 10/16/2022
# End date: 10/26/2022


import copy
import preProcess
import debug
import assemble
import generateSchematic as schem
import postProcess


def main():
    # Get source file (.aub or .txt) and parse it into a list of strings line by line
    source, args = preProcess.getInput()

    # Take the list of strings and translate it into a list of Lines,
    # where a Line object stores the contents of the string, and the
    # line number (the index + 1), this is used later in debugging
    lines = preProcess.constructLines(source)
    
    # Delete comments, empty lines, whitespace, etc
    cleanLines = preProcess.sanitize(lines)

    # debug() looks for syntax errors, valid arguments, etc and
    # prints an error message if an issue comes up
    debug.debug(cleanLines)

    # Replace labels (variables / jump labels) with their literal addresses
    noLabels = assemble.replaceLabels(cleanLines)

    # Check to make sure there arent any arguments left that arent literal addresses
    debug.debugLiteral(noLabels)

    # Create a second list of the assembly code for use in postProcess (printing etc)
    assembly = copy.deepcopy(noLabels)

    # Convert to binary, then make sure the binary is valid
    machineCode = assemble.assemble(noLabels)
    debug.debugMachineCode(machineCode)

    # Use the binary to generate a schematic to paste into Minecraft
    schem.binToSchem(machineCode)

    # Print a report
    postProcess.postProcess(args, assembly, machineCode)


main()