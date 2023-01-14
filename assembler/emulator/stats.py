
TICKS_PER_CYCLE = 36
TICKS_PER_SECOND = 10
cycle_count = 0

# Getter, setter, and modifier functions
def increment_cycle():
    global cycle_count
    cycle_count += 1

def get_cycle_count() -> int:
    return cycle_count

def calculate_runtime() -> int:
    return (cycle_count * TICKS_PER_CYCLE) / TICKS_PER_SECOND
