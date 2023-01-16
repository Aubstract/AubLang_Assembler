# AubLang Assembler

**An assembler for my language AubLang, which outputs a schematic file that can be pasted into Minecraft for use on my Aub CPU.**

How to use the assembler:
- Run the main.py file in the assembler directory
- When the program starts, it will prompt you for a file path to the source file. This can be a .txt or a .aub file containing your AubLang assembly code.
- Next it will prompt you for assembler arguments, these are currently just used to specify secondary outputs. Meaning you can print info to the terminal, or write it to a file (not yet implemented). Or you can choose to run the assembled program on the emulator (WIP).

Here is a list of assembler arguments:
- *print* - the specified outputs will be sent to the terminal.
- *file* - the specified outputs will be sent to a file (not yet implemented).
- *label* - labels are like variable names. There are two types of labels, one stores a memory (register or RAM) address, the other stores a program memory (PROM) address and is used to make jumps in the program. This argument will output the label dictionaries created during runtime which contain the label name, and the associated address.
- *aub* - output the assembly code with literal addresses (instead of labels).
- *bin* - output the machine code (binary).
- *run* - run the assembled program in the emulator.
