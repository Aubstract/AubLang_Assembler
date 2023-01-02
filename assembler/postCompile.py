import assemble

def printSummary(code: list[object]):
    """Prints a report on the program once it is assembled"""

    print("\n~~~~~~~~~~~~~~~~~~~~ successfully assembled ~~~~~~~~~~~~~~~~~~~~\n")
    print("Output file name: output.schem\n")
    print(f"Program length: {len(code)} lines\n")
    print(f"jumpLabel Dictionary:\n{assemble.jumpLabels}\n")
    print(f"varLabel Dictionary:\n{assemble.varLabels}")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")