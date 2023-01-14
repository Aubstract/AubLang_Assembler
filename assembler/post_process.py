import dictionaries as dict
from pre_process import Line
import emulator.run as emulator


def post_process(args: list[str], assembly_code: list[Line], machine_code: list[Line]) -> None:
    if "run" in args:
        emulator.run.run(assembly_code)
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~ successfully assembled ~~~~~~~~~~~~~~~~~~~~\n")
        print("Output file name: output.schem")
        print(f"Program length: {len(machine_code)} lines\n")

        if "print" in args:
            if "label" in args or "all" in args:
                print_labels()
            if "aub" in args or "all" in args:
                print_assembly_code(assembly_code)
            if "bin" in args or "all" in args:
                print_machine_code(machine_code)
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
    for label in dict.jump_labels:
        print(f"\t\t{label} : {dict.jump_labels[label]}")
    print("")
    print("\t-Variable Labels:")
    for label in dict.var_labels:
        print(f"\t\t{label} : {dict.var_labels[label]}")
    print("")


def print_assembly_code(assembly: list[object]) -> None:
    print("Assembly Code: ------------------------------------------------------\n")
    for index, line_object in enumerate(assembly):
        print(f"\t{index+1}\t{line_object.line}")
    print("")


def print_machine_code(code: list[object]) -> None:
    print("Machine Code: ------------------------------------------------------\n")
    for index, line_object in enumerate(code):
        print(f"\t{index+1}\t", end="")
        for bit in line_object.line:
            print(bit, end="")
        print("")