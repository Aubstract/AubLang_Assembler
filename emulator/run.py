# Emulator of Aub CPU
# By Aubrey Fields
# Start date: 1/11/2023
#
# The goal is to verify that the programs I have written work on a logical
# level. Because if the algorithms dont work, and need more memory to
# be fixed, then I might need to change the hardware. And I would rather
# know about that now rather than when I have finished the build.


import time
import alu
import memory
import display
import stats


def run(assembly: list[object]):
    # Initialize everything
    cycles_per_second = 10
    cycle_length = (1/cycles_per_second)

    while True:
        # Start clock cycle
        cycle_start = time.perf_counter()

        # Computation...

        # Stats stuff
        stats.increment_cycle()

        # End clock cycle
        cycle_end = time.perf_counter()

        # Calculate and execute delay
        compute_time = (cycle_end-cycle_start)
        if compute_time < cycle_length:
            time.sleep(cycle_length - compute_time)