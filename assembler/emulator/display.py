import curses

def init_display():
    global stdscr
    global pixel_on
    global pixel_off
    stdscr = curses.initscr()
    pixel_on = chr(9608) # rectangle symbol
    pixel_off = ' '

def print_char() -> None:
    global stdscr

def print_num() -> None:
    global stdscr

def plot_point() -> None:
    global stdscr

def new_line() -> None:
    global stdscr

def clear_screen() -> None:
    global stdscr

def update_display() -> None:
    global stdscr