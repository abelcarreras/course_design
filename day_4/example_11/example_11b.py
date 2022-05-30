import curses
from main import __version__ as version
from main import CoreProgram
from fileio import read_xyz_file


def get_param(screen, prompt_string):
    import textwrap
    screen_width = 80
    prompt_string = textwrap.fill(prompt_string, width=screen_width)

    screen.clear()
    screen.border(0)

    for i, line in enumerate(prompt_string.splitlines()):
        screen.addstr(2+i, 2, line)
    screen.refresh()
    input_data = screen.getstr(10, 10, 60).decode()

    return input_data

screen = curses.initscr()
screen.border(0)
input_file = get_param(screen, "Insert filename:")
symbols, coordinates = read_xyz_file(input_file)
core = CoreProgram(symbols, coordinates)

screen.refresh()
curses.endwin()

while True:
    screen = curses.initscr()
    screen.clear()
    screen.border(0)

    #Option values left screen
    screen.addstr(2, 2, "Please enter option number...")
    screen.addstr(4, 4, "1 - print molecular info")
    screen.addstr(5, 4, "2 - print version number")

    screen.addstr(14, 4, "0 - Exit")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):

        input_file = get_param(screen, "Insert title")
        curses.endwin()
        result = core.print_molecule_info(input_file, spaces=2)
        screen.getch()

    if x == ord('2'):

        screen.clear()
        screen.addstr(5, 7, "Program version {}".format(version))
        screen.getch()

    if x == ord('0'):
        screen.clear()
        screen.refresh()
        break
