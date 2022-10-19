import mcschematic

def generateSchem(code: list):
    """Generates a schematic file"""

    schem = mcschematic.MCSchematic()

    totalRows = len(code)

    # Breaks each line into a list of chars
    for lineNum, line in enumerate(code):
        code[lineNum] = [*line]

    # Dimensions of program memory, in relative coords from the corner closest to the paste-location
    DIM_Z = 35
    DIM_X = -15
    DIM_Y = -13

    # The offsets of the schem corner from the player
    X_OFFSET = 0 # -1
    Y_OFFSET = -1
    Z_OFFSET = -1

    # The step size (how many blocks between torches), disregarding direction
    Z_STEP_SIZE = 2
    X_STEP_SIZE = 2
    Y_STEP_SIZE = 4
    
    # Calculate step size and direction, start point, and end point
    if DIM_Z < 0:
        z_step = Z_STEP_SIZE
        z_start = 0 + Z_OFFSET
        z_end = DIM_Z + Z_OFFSET
    else:
        z_step = -1 * Z_STEP_SIZE
        z_start = DIM_Z + Z_OFFSET
        z_end = 0 + Z_OFFSET
    
    if DIM_X < 0:
        x_step = X_STEP_SIZE
        x_start = DIM_X + X_OFFSET
        x_end = 0 + X_OFFSET
    else:
        x_step = -1 * X_STEP_SIZE
        x_start = 0 + X_OFFSET
        x_end = DIM_X + X_OFFSET
    
    if DIM_Y < 0:
        y_step = -1 * Y_STEP_SIZE
        y_start = 0 + Y_OFFSET
        y_end = DIM_Y + Y_OFFSET
    else:
        y_step = Y_STEP_SIZE
        y_start = DIM_Y + Y_OFFSET
        y_end = 0 + Y_OFFSET


    rowCount = 0
    colCount = 0

    for y_coord in range(y_start, y_end, y_step):
        for x_coord in range(x_start, x_end, x_step):
            for z_coord in range(z_start, z_end, z_step):
                if rowCount < totalRows:
                    if code[rowCount][colCount] == '1':
                        schem.setBlock((x_coord, y_coord, z_coord), "minecraft:redstone_wall_torch[facing=west]")
                    else:
                        schem.setBlock((x_coord, y_coord, z_coord), "minecraft:barrier")
                    colCount += 1
                else:
                    break
            colCount = 0
            rowCount += 1
        rowCount += 1
    
    schem.save("C:/Users/Ben/AppData/Roaming/.minecraft/config/worldedit/schematics", "output", mcschematic.Version.JE_1_18_2)

    print("\ndone\n")