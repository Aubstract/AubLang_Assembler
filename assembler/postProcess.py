import dictionaries as dict


def post_process(args: list[str], assembly: list[object], machineCode: list[object]) -> None:
    print("\n~~~~~~~~~~~~~~~~~~~~ successfully assembled ~~~~~~~~~~~~~~~~~~~~\n")
    print("Output file name: output.schem")
    print(f"Program length: {len(machineCode)} lines\n")

    if "print" in args:
        if "label" in args or "all" in args:
            print_labels()
        if "aub" in args or "all" in args:
            print_assembly_code(assembly)
        if "bin" in args or "all" in args:
            print_machine_code(machineCode)
    elif "file" in args:
        if "label" in args or "all" in args:
            pass
        if "aub" in args or "all" in args:
            pass
        if "bin" in args or "all" in args:
            pass
    elif len(args) != 0:
        print("Insufficient arguments, no printing or saving of data executed.")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def print_labels() -> None:
    print("Label Dictionaries: -------------------------------------------------\n")
    print("\t-Jump Labels:")
    for label in dict.jumpLabels:
        print(f"\t\t{label} : {dict.jumpLabels[label]}")
    print("")
    print("\t-Variable Labels:")
    for label in dict.varLabels:
        print(f"\t\t{label} : {dict.varLabels[label]}")
    print("")


def print_assembly_code(assembly: list[object]) -> None:
    print("Assembly Code: ------------------------------------------------------\n")
    for i, line in enumerate(assembly):
        print(f"\t{i+1}\t{line.line}")
    print("")


def print_machine_code(code: list[object]) -> None:
    print("Machine Code: ------------------------------------------------------\n")
    for i, line in enumerate(code):
        print(f"\t{i+1}\t", end="")
        for bit in line.line:
            print(bit, end="")
        print("")