import stats


def operate(instruction: str):

    # Seperate instruction into tokens
    tokens = instruction.split()

    match tokens[0]:
        case "nop":
            pass
        
    stats.increment_cycle()