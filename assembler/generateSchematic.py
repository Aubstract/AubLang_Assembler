import os
import mcschematic


def binToSchem(code: list[object]):
    """Generates a schematic file"""

    # Initialize CONSTS and vars -------------------------------------------

    USERNAME = os.getlogin()

    # Direction that the torches face in memory
    TORCH_DIRECTION = "west"

    # Dimensions of program memory, in relative coords (including direction)
    DIM_Z = 34
    DIM_X = -14
    DIM_Y = -12

    # The offsets of the schem corner (0,0,0) from the player
    X_OFFSET = -1
    Y_OFFSET = -1
    Z_OFFSET = 0

    # The step size (how many blocks between torches), including direction
    Z_STEP_SIZE = -2
    X_STEP_SIZE = 2
    Y_STEP_SIZE = -4
    
    # Calculate step size/direction, start point, and end point
    z_step = Z_STEP_SIZE
    z_start = DIM_Z + Z_OFFSET
    z_end = 0 + Z_OFFSET + z_step

    x_step = X_STEP_SIZE
    x_start = DIM_X + X_OFFSET
    x_end = 0 + X_OFFSET + x_step

    y_step = Y_STEP_SIZE
    y_start = 0 + Y_OFFSET
    y_end = DIM_Y + Y_OFFSET + y_step

    # END Initialize CONSTS and vars -------------------------------------------


    schem = mcschematic.MCSchematic()

    # Breaks each line into a list of chars
    for lineNum, lineElement in enumerate(code):
        line = lineElement.line
        code[lineNum].line = [*line]

    totalRows = len(code)
    rowCount = 0
    colCount = 0

    for y_coord in range(y_start, y_end, y_step):
        for x_coord in range(x_start, x_end, x_step):
            for z_coord in range(z_start, z_end, z_step):
                if rowCount < totalRows:
                    line = code[rowCount].line
                    if line[colCount] == '1':
                        schem.setBlock((x_coord, y_coord, z_coord), f"minecraft:redstone_wall_torch[facing={TORCH_DIRECTION}]")
                    else:
                        schem.setBlock((x_coord, y_coord, z_coord), "minecraft:barrier")
                elif rowCount >= totalRows and rowCount < 32:
                    schem.setBlock((x_coord, y_coord, z_coord), "minecraft:barrier")
                else:
                    break
                colCount += 1
            colCount = 0
            rowCount += 1

    schem.save(f"C:/Users/{USERNAME}/AppData/Roaming/.minecraft/config/worldedit/schematics", "output", mcschematic.Version.JE_1_18_2)